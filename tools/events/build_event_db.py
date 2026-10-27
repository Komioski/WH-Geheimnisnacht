#!/usr/bin/env python3
"""Build the event database: docs/events/event_database.csv and docs/events/README.md stats.

Usage (from the mod root):  python3 tools/events/build_event_db.py

One row per event. Most columns are computed from the script, so they never
drift. `title` and `summary` come from the event's doc comment (see
docs/events/README.md); events not yet documented fall back to the old
author comment or the English text of their description.
"""
import csv
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mod_index import Index, STRONG_PRE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT_DIR = os.path.join(ROOT, 'docs', 'events')
LOC_CLEAN = re.compile(r'\[[^\]]*\]|\$[^$]*\$|§.|\\n')


def short(text, limit=160):
    text = LOC_CLEAN.sub('', text).replace('  ', ' ').strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(' ', 1)[0]
    return cut + '...'


def how_it_fires(ev, idx):
    if not ev.triggered_only:
        return 'MTTH' if ev.has_mtth else 'auto'
    return 'triggered' if idx.fired_by.get(ev.id) else 'never (orphan)'


def main():
    idx = Index(ROOT)
    primary, source = idx.attribute()
    os.makedirs(OUT_DIR, exist_ok=True)
    rows = []
    for ev in sorted(idx.events.values(), key=lambda e: (e.path, e.line)):
        title, summary, summary_src = ev.doc_title, ev.doc_summary, 'doc'
        if not title:
            summary_src = ''
            for kind, key in ev.loc_keys():
                if kind == 'title' and idx.loc.get(key):
                    title = short(idx.loc[key], 80)
                    break
        if not summary:
            if ev.legacy_comment:
                summary, summary_src = short(ev.legacy_comment), 'comment'
            else:
                for kind, key in ev.loc_keys():
                    if kind == 'desc' and idx.loc.get(key):
                        summary, summary_src = short(idx.loc[key]), 'loc'
                        break
        callers = sorted(set(idx.fired_by.get(ev.id, ())))
        rows.append({
            'id': ev.id,
            'namespace': ev.namespace,
            'file': ev.path,
            'line': ev.line,
            'type': ev.type.replace('_event', ''),
            'fires': how_it_fires(ev, idx),
            'hidden': 'yes' if ev.hidden else '',
            'fired_by': '; '.join(callers),
            'calls': '; '.join(sorted(set(ev.calls))),
            'pre_triggers': ' '.join(ev.pre),
            'primary_faction': primary.get(ev.id, 'Generic'),
            'faction_source': source.get(ev.id, ''),
            'origin': ev.origin,
            'title': title,
            'summary': summary,
            'summary_source': summary_src,
        })
    path = os.path.join(OUT_DIR, 'event_database.csv')
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    write_stats(rows, idx)
    print('wrote %d events to %s' % (len(rows), os.path.relpath(path, ROOT)))


def write_stats(rows, idx):
    """Replace the generated stats section of docs/events/README.md."""
    by_faction = defaultdict(Counter)
    for r in rows:
        f = by_faction[r['primary_faction']]
        f['events'] += 1
        f[r['origin']] += 1
        if not r['hidden']:
            f['visible'] += 1
        if r['summary_source'] == 'doc':
            f['documented'] += 1
    lines = ['| Faction | Events | Mod-written | Vanilla | Player-visible | Documented |',
             '|---|---:|---:|---:|---:|---:|']
    for name, c in sorted(by_faction.items(), key=lambda kv: -kv[1]['events']):
        lines.append('| %s | %d | %d | %d | %d | %d |' % (
            name, c['events'], c['mod'], c['vanilla'], c['visible'], c['documented']))
    total = Counter(r['fires'] for r in rows)
    lines.append('')
    lines.append('%d events in %d files. MTTH: %d, triggered: %d, never fired: %d.' % (
        len(rows), len(idx.file_info), total['MTTH'], total['triggered'], total['never (orphan)']))
    readme = os.path.join(OUT_DIR, 'README.md')
    if not os.path.exists(readme):
        return
    text = open(readme, encoding='utf-8').read()
    start, end = '<!-- stats:start -->', '<!-- stats:end -->'
    if start in text and end in text:
        head, rest = text.split(start, 1)
        tail = rest.split(end, 1)[1]
        text = head + start + '\n' + '\n'.join(lines) + '\n' + end + tail
        open(readme, 'w', encoding='utf-8').write(text)


if __name__ == '__main__':
    main()
