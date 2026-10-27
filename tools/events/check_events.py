#!/usr/bin/env python3
"""Check event files for errors and performance problems.

Usage (from the mod root):
    python3 tools/events/check_events.py                 # summary for the whole mod
    python3 tools/events/check_events.py events/X.txt    # every finding for these files

Exit code is 1 when a checked file has an ERROR.

ERROR  brace mismatch, duplicate id, undeclared namespace,
       call to an event that does not exist
WARN   missing localisation (mod events only), non-cp1252-safe encoding,
       MTTH or pulse event without a cheap pre-trigger, weight_multiplier on an
       event that is never in a random_events list (the weights do nothing),
       on_action listing an event that does not exist
STYLE  space-indented lines, `break = yes` (use else_if), commented-out code,
       event numbers of 1000+ or namespaces longer than 12 characters (mod files)
"""
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdx  # noqa: E402
from mod_index import Index, STRONG_PRE, PULSES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LOC_KEY = re.compile(r'^[A-Za-z0-9_.\-]+$')
CODE_COMMENT = re.compile(r'^\s*#\s*[a-z_]+\s*=\s*[{\w]')


def check(idx, only=None):
    """Return list of (level, file, line, message)."""
    out = []
    known = set(idx.events)
    declared = {ns for info in idx.file_info.values() for ns in info['namespaces']}

    def want(path):
        return only is None or path in only

    for path, info in idx.file_info.items():
        if not want(path):
            continue
        if info['brace_errors']:
            out.append(('ERROR', path, 0, '%d unbalanced brace(s)' % info['brace_errors']))
        if info['encoding'].startswith('utf-8'):
            out.append(('WARN', path, 0, 'file is %s; CK2 reads cp1252' % info['encoding']))
    for eid, path, line in idx.duplicates:
        if want(path):
            out.append(('ERROR', path, line, 'duplicate event id %s' % eid))
    for ev in idx.events.values():
        if not want(ev.path):
            continue
        spaces = idx.file_info[ev.path]['namespaces']
        if ev.namespace and ev.namespace not in declared:
            out.append(('ERROR', ev.path, ev.line, 'namespace %s is never declared' % ev.namespace))
        elif ev.namespace and ev.namespace not in spaces and ev.origin == 'mod':
            out.append(('STYLE', ev.path, ev.line, '%s uses a namespace declared in another file' % ev.id))
        if only is not None and ev.origin == 'mod':
            num = ev.id.split('.')[-1]
            if num.isdigit() and int(num) >= 1000:
                out.append(('STYLE', ev.path, ev.line, '%s: keep event numbers below 1000' % ev.id))
            if len(ev.namespace) > 12:
                out.append(('STYLE', ev.path, ev.line, 'namespace %s is long; keep it under 12 characters' % ev.namespace))
        for callee in sorted(set(ev.calls)):
            if callee not in known:
                out.append(('ERROR', ev.path, ev.line, '%s fires missing event %s' % (ev.id, callee)))
        if ev.origin == 'mod' and not ev.hidden:
            for kind, key in ev.loc_keys():
                if LOC_KEY.match(key) and key not in idx.loc and key not in ('OK',):
                    out.append(('WARN', ev.path, ev.line, '%s: no localisation for %s %s' % (ev.id, kind, key)))
        strong = set(ev.pre) & STRONG_PRE
        if not ev.triggered_only and ev.has_mtth and not strong:
            out.append(('WARN', ev.path, ev.line, '%s: MTTH event with no cheap pre-trigger '
                        '(only_playable, only_rulers, religion_group, has_character_flag...)' % ev.id))
        pulses = idx.pulse_listed.get(ev.id, set()) & PULSES
        if pulses and not strong:
            out.append(('WARN', ev.path, ev.line, '%s: runs on %s for every character; add a '
                        'pre-trigger' % (ev.id, ', '.join(sorted(pulses)))))
        if (ev.has_weight and ev.triggered_only and ev.origin == 'mod'
                and ev.id not in idx.random_listed):
            out.append(('WARN', ev.path, ev.line, '%s: weight_multiplier is ignored; the event is '
                        'not in any random_events list' % ev.id))
    for src, eid in idx.external_calls:
        if eid not in known and want(src):
            out.append(('ERROR', src, 0, 'fires missing event %s' % eid))
    for eid, sources in idx.fired_by.items():
        if eid in known:
            continue
        for src in sources:
            if src.startswith('on_action:') and only is None:
                out.append(('WARN', 'common/on_actions', 0, '%s lists missing event %s' % (src, eid)))
    if only:
        for path in only:
            out.extend(style(path))
    return out


def style(path):
    out = []
    full = os.path.join(ROOT, path)
    if not os.path.exists(full) or not path.startswith('events/'):
        return out
    text, _ = pdx.read(full)
    for n, row in enumerate(text.split('\n'), 1):
        if row.startswith('    '):
            out.append(('STYLE', path, n, 'indented with spaces; use tabs'))
        if re.search(r'\bbreak\s*=\s*yes', row.split('#')[0]):
            out.append(('STYLE', path, n, '`break = yes`; prefer if / else_if / else'))
        if CODE_COMMENT.match(row):
            out.append(('STYLE', path, n, 'commented-out code; delete it (git keeps history)'))
    return out


def main(argv):
    targets = [a.replace(os.sep, '/') for a in argv[1:]]
    idx = Index(ROOT)
    findings = check(idx, set(targets) if targets else None)
    if targets:
        for level, path, line, msg in sorted(findings, key=lambda f: (f[1], f[2])):
            print('%-5s %s:%d  %s' % (level, path, line, msg))
    else:
        by_level = Counter(f[0] for f in findings)
        by_file = defaultdict(Counter)
        for level, path, line, msg in findings:
            by_file[path][level] += 1
        print('Whole mod: %s' % ', '.join('%s %d' % kv for kv in sorted(by_level.items())))
        worst = sorted(by_file.items(), key=lambda kv: (-kv[1]['ERROR'], -kv[1]['WARN']))[:25]
        for path, c in worst:
            print('  %-50s ERROR %3d  WARN %4d' % (path, c['ERROR'], c['WARN']))
        for level, path, line, msg in findings:
            if level == 'ERROR':
                print('%-5s %s:%d  %s' % (level, path, line, msg))
    return 1 if any(f[0] == 'ERROR' for f in findings) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
