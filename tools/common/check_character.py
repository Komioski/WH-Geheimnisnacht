"""Check the mod's character files.

    python3 tools/common/check_character.py [--vanilla-loc DIR]

Covers common/traits, common/nicknames, common/death, common/death_text,
common/heir_text, common/execution_methods and common/disease. Reports, as
ERROR or WARN:
- a trait, nickname, death reason, death or heir text or disease defined
  twice: the game keeps one and the other is silently lost;
- a trait, nickname, death reason or disease that a script uses (trait =,
  add_trait =, give_nickname =, death_reason =, spawn_disease =...) but no
  file defines: the effect does nothing and the check is always false;
- a trait opposite, a disease trait or an execution death that is not
  defined;
- a faith or culture in these folders that common/religions or
  common/cultures does not define;
- a disease with "rip = no": the game only uses it without The Reaper's Due;
- a file that is not cp1252/ASCII, unbalanced braces, commented-out code.
With --vanilla-loc (the CK2 install's localisation folder) it also warns
about visible traits, nicknames and death reasons with no text in the mod's
or vanilla's localisation, so the player sees the raw key.
Standard library only. Exit code 1 if there are errors.
"""
import glob
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'events'))
import pdx  # noqa: E402

FOLDERS = ('traits', 'nicknames', 'death', 'death_text', 'heir_text',
           'execution_methods', 'disease')
REPEATED = {'execution_method'}  # one key per entry by design
CODE = re.compile(r'^\s*#\s*[A-Za-z_][A-Za-z0-9_.]*\s*(=|>=|<=)\s*\S')
SCOPES = {'yes', 'no', 'ROOT', 'THIS', 'liege', 'top_liege', 'father',
          'mother', 'real_father', 'spouse', 'employer', 'host', 'killer',
          'owner', 'controller', 'holder', 'location', 'capital_scope'}
USES = {
    'traits': re.compile(r'\b(?:trait|add_trait|remove_trait)\s*=\s*([A-Za-z_][\w-]*)'),
    'nicknames': re.compile(r'\b(?:give_nickname|has_nickname)\s*=\s*([A-Za-z_]\w*)'),
    'death': re.compile(r'\b(?:death_reason|death)\s*=\s*(death_\w+)'),
    'disease': re.compile(r'\b(?:disease|spawn_disease|has_disease)\s*=\s*([A-Za-z_]\w*)'),
}
FAITH = re.compile(r'\b(religion|true_religion|secret_religion|religion_group|'
                   r'true_religion_group|culture|culture_group)\s*=\s*([A-Za-z_]\w*)')


def read_loc(folder):
    keys = set()
    for path in glob.glob(os.path.join(folder, '**', '*.csv'), recursive=True):
        raw = open(path, 'rb').read()
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            text = raw.decode('cp1252', errors='replace')
        for line in text.split('\n'):
            if ';' in line and not line.startswith('#'):
                keys.add(line.split(';', 1)[0].strip())
    return keys


def stripped(path):
    return '\n'.join(l.split('#', 1)[0] for l in pdx.read(path)[0].split('\n'))


def faiths_and_cultures():
    rel, relg, cul, culg = set(), set(), set(), set()
    for path in glob.glob(os.path.join(ROOT, 'common', 'religions', '*.txt')):
        for k, op, v, line in pdx.parse(pdx.read(path)[0])[0]:
            if isinstance(v, list):
                relg.add(k)
                for kk, oo, vv, ll in v:
                    if isinstance(vv, list) and pdx.get(vv, 'icon') is not None:
                        rel.add(kk)
    for path in glob.glob(os.path.join(ROOT, 'common', 'cultures', '*.txt')):
        for k, op, v, line in pdx.parse(pdx.read(path)[0])[0]:
            if isinstance(v, list):
                culg.add(k)
                cul |= {kk for kk, oo, vv, ll in v if isinstance(vv, list)}
    return {'religion': rel, 'true_religion': rel, 'secret_religion': rel,
            'religion_group': relg, 'true_religion_group': relg,
            'culture': cul, 'culture_group': culg}


def main():
    errors, warns = [], []
    defs = {}
    for f in FOLDERS:
        d = defaultdict(list)
        for path in sorted(glob.glob(os.path.join(ROOT, 'common', f, '*.txt'))):
            rel = os.path.relpath(path, ROOT)
            text, enc = pdx.read(path)
            if enc.startswith('utf-8'):
                errors.append('%s: %s, must be cp1252 or ASCII' % (rel, enc))
            entries, brace = pdx.parse(text)
            if brace:
                errors.append('%s: %d unbalanced braces' % (rel, brace))
            for k, op, v, line in entries:
                if k:
                    d[k].append((rel, line, v))
            for n, raw in enumerate(text.split('\n'), 1):
                if CODE.match(raw):
                    warns.append('%s:%d commented-out code: %s' % (rel, n, raw.strip()[:60]))
        for k, where in sorted(d.items()):
            if f == 'disease' and sorted(pdx.get(v, 'rip') or '' for _, _, v in where) == ['no', 'yes']:
                continue  # one copy for each version of the game (rip = yes / no)
            if len(where) > 1 and k not in REPEATED:
                errors.append('%s defined %d times (%s)' % (
                    k, len(where), ', '.join('%s:%d' % (r, l) for r, l, _ in where)))
        defs[f] = d
    traits, deaths = defs['traits'], defs['death']

    for k, where in sorted(traits.items()):
        rel, line, v = where[0]
        for o in pdx.getall(v, 'opposites'):
            for kk, oo, vv, ll in (o if isinstance(o, list) else []):
                if kk is None and vv not in traits:
                    errors.append('%s:%d %s: opposite %s is not a trait' % (rel, ll, k, vv))
    for k, where in sorted(defs['disease'].items()):
        rel, line, v = where[0]
        t = pdx.get(v, 'trait')
        if t and t not in traits:
            errors.append('%s:%d disease %s: trait %s is not defined' % (rel, line, k, t))
        if pdx.get(v, 'rip') == 'no':
            warns.append('%s:%d disease %s has rip = no: only used without The Reaper\'s Due' % (rel, line, k))
    for rel, line, v in defs['execution_methods'].get('execution_method', []):
        d = pdx.get(v, 'death')
        if d and d not in deaths:
            errors.append('%s:%d execution_method: death %s is not defined' % (rel, line, d))

    # uses across the mod
    known = {'traits': traits, 'nicknames': defs['nicknames'], 'death': deaths,
             'disease': defs['disease']}
    fc = faiths_and_cultures()
    for r in ('events', 'decisions', 'common', 'history'):
        for dirpath, _, files in os.walk(os.path.join(ROOT, r)):
            for name in files:
                if not name.endswith('.txt'):
                    continue
                path = os.path.join(dirpath, name)
                rel = os.path.relpath(path, ROOT)
                ours = rel.startswith(tuple('common/' + f for f in FOLDERS))
                for n, line in enumerate(stripped(path).split('\n'), 1):
                    for kind, pat in USES.items():
                        for m in pat.finditer(line):
                            x = m.group(1)
                            if x in SCOPES or x.isupper() or x.startswith(('FROM', 'PREV', 'event_target')):
                                continue
                            if kind == 'disease' and rel.startswith('common/disease'):
                                continue
                            if x not in known[kind]:
                                errors.append('%s:%d %s %s is not defined' % (rel, n, kind.rstrip('s'), x))
                    if ours:
                        for m in FAITH.finditer(line):
                            k, x = m.groups()
                            if x in SCOPES or x.isupper() or x.startswith(('FROM', 'PREV', 'event_target')):
                                continue
                            if x not in fc[k]:
                                errors.append('%s:%d %s %s is not defined' % (rel, n, k, x))

    if '--vanilla-loc' in sys.argv:
        loc = read_loc(os.path.join(ROOT, 'localisation'))
        loc |= read_loc(sys.argv[sys.argv.index('--vanilla-loc') + 1])
        for k, where in sorted(traits.items()):
            rel, line, v = where[0]
            if pdx.get(v, 'hidden') == 'yes':
                continue
            for key in (k, k + '_desc'):
                if key not in loc:
                    warns.append('%s:%d trait %s has no text %s' % (rel, line, k, key))
        for k, where in sorted(defs['nicknames'].items()):
            if k not in loc:
                warns.append('%s:%d nickname %s has no text' % (where[0][0], where[0][1], k))
        for k, where in sorted(deaths.items()):
            rel, line, v = where[0]
            desc = pdx.get(v, 'long_desc')
            for key in filter(None, (desc, pdx.get(v, 'death_date_desc'))):
                if key not in loc:
                    warns.append('%s:%d death %s has no text %s' % (rel, line, k, key))
        for f in ('death_text', 'heir_text'):
            for k, where in sorted(defs[f].items()):
                if k not in loc:
                    warns.append('%s:%d %s has no text' % (where[0][0], where[0][1], k))

    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN ', w)
    print('character: %d traits, %d nicknames, %d death reasons, %d death texts, %d heir texts, '
          '%d execution methods, %d diseases; ERROR %d, WARN %d' % (
              len(traits), len(defs['nicknames']), len(deaths), len(defs['death_text']),
              len(defs['heir_text']), len(defs['execution_methods'].get('execution_method', [])),
              len(defs['disease']), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
