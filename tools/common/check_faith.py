"""Check the mod's faith files.

    python3 tools/common/check_faith.py [--vanilla-loc DIR]

Covers common/religions, common/religious_titles, common/religion_features
and common/religion_modifiers. Reports, as ERROR or WARN:
- a religion group, religion, religious title, feature or authority modifier
  defined twice: the game keeps one and the other is silently lost;
- a religion's parent, reformed version or intermarry target that is not a
  religion, and intermarry across groups written on one side only (WARN;
  within a group marriage is allowed anyway);
- two religions with the same icon or the same colour (WARN: the map and
  the faith screen cannot tell them apart), unless one is the other's
  heresy (parent) or reformed version, as in vanilla;
- a graphical_culture that common/graphicalculturetypes does not define;
- a religious title of an undefined religion;
- a religion, religion group, religion feature or authority modifier that a
  script anywhere in the mod uses (religion =, has_religion_feature =,
  religion_authority = { modifier = }...) but nothing defines: the check is
  always false or the effect does nothing;
- a file that is not cp1252/ASCII, unbalanced braces, commented-out code.
With --vanilla-loc (the CK2 install's localisation folder) it also warns
about religions and groups with no name or description, and god names,
scriptures, priest titles and crusade names with no text.
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

CODE = re.compile(r'^\s*#\s*[A-Za-z_][A-Za-z0-9_.]*\s*(=|>=|<=)\s*\S')
SKIP = {'yes', 'no', 'ROOT', 'THIS', 'PREV', 'FROM', 'liege', 'top_liege', 'father', 'mother',
        'real_father', 'spouse', 'employer', 'host', 'killer', 'owner', 'controller', 'holder',
        'location', 'capital_scope', 'event_target', 'religion_head', 'rightful_religious_head_scope',
        'root', 'from', 'prev', 'this', 'random', 'historical', 'full_random'}
USE = re.compile(r'\b(religion|true_religion|secret_religion|religion_group|true_religion_group|secret_religion_group|'
                 r'has_religion_feature|has_selected_religion_feature)\s*=\s*([A-Za-z_]\w*)')
AUTH = re.compile(r'religion_authority\s*=\s*\{[^{}]*?\bmodifier\s*=\s*([A-Za-z_]\w*)', re.S)
# common/ folders not refactored yet: their vanilla leftovers are warnings
# until their own pass.
LATER = ('alternate_start', 'cb_types', 'wonders', 'wonder_upgrades', 'succession_voting',
         'government_flavor', 'governments', 'laws', 'minor_titles', 'cultures', 'buildings',
         'artifacts', 'bloodlines', 'objectives', 'societies', 'landed_titles', 'offmap_powers',
         'job_actions', 'council_positions', 'council_voting', 'mercenaries', 'retinue_subunits',
         'special_troops', 'combat_tactics', 'tributary_types', 'trade_routes', 'stories',
         'holding_types', 'bookmarks', 'dynasties', 'minor_titles')
LOC_FIELDS = ('high_god_name', 'scripture_name', 'priest_title', 'crusade_name', 'piety_name')


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


def load(folder, errors, warns):
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'common', folder, '*.txt'))):
        rel = os.path.relpath(path, ROOT)
        text, enc = pdx.read(path)
        if enc.startswith('utf-8'):
            errors.append('%s: %s, must be cp1252 or ASCII' % (rel, enc))
        entries, brace = pdx.parse(text)
        if brace:
            errors.append('%s: %d unbalanced braces' % (rel, brace))
        for n, raw in enumerate(text.split('\n'), 1):
            if CODE.match(raw):
                warns.append('%s:%d commented-out code: %s' % (rel, n, raw.strip()[:60]))
        out.append((rel, entries))
    return out


def dupes(items, what, errors):
    seen = defaultdict(list)
    for k, where in items:
        seen[k].append(where)
    for k, w in sorted(seen.items()):
        if len(w) > 1:
            errors.append('%s %s defined %d times (%s)' % (what, k, len(w), ', '.join(w)))


def main():
    errors, warns = [], []
    # religions
    groups, rels = {}, {}
    gitems, ritems = [], []
    for rel, entries in load('religions', errors, warns):
        for k, op, v, line in entries:
            if not isinstance(v, list) or k == 'secret_religion_visibility_trigger':
                continue
            groups[k] = (rel, line, v)
            gitems.append((k, '%s:%d' % (rel, line)))
            for kk, oo, vv, ll in v:
                if isinstance(vv, list) and pdx.get(vv, 'icon') is not None:
                    rels[kk] = (rel, ll, vv, k)
                    ritems.append((kk, '%s:%d' % (rel, ll)))
    dupes(gitems + ritems, 'religion or group', errors)
    gfx = set()
    for path in glob.glob(os.path.join(ROOT, 'common', 'graphicalculturetypes', '*.txt')):
        gfx |= {k for k, o, v, l in pdx.parse(pdx.read(path)[0])[0] if k}
    icons, colors = defaultdict(list), defaultdict(list)
    for r, (rel, line, v, g) in sorted(rels.items()):
        icons[pdx.get(v, 'icon')].append(r)
        c = pdx.get(v, 'color')
        if isinstance(c, list):
            colors[tuple(x[2] for x in c)].append(r)
        for key in ('parent', 'reformed'):
            x = pdx.get(v, key)
            if x and x not in rels:
                errors.append('%s:%d %s: %s %s is not a religion' % (rel, line, r, key, x))
        for x in pdx.getall(v, 'intermarry'):
            if x in groups:
                continue
            if x not in rels:
                errors.append('%s:%d %s: intermarry %s is not a religion' % (rel, line, r, x))
            elif rels[x][3] != g and r not in pdx.getall(rels[x][2], 'intermarry') \
                    and g not in pdx.getall(rels[x][2], 'intermarry'):
                warns.append('%s:%d %s intermarries with %s, but not the other way round' % (rel, line, r, x))
    for r, (rel, line, v, g) in sorted(rels.items()):
        x = pdx.get(v, 'graphical_culture') or pdx.get(groups[g][2], 'graphical_culture')
        if x and x not in gfx:
            errors.append('%s:%d %s: graphical_culture %s is not defined' % (rel, line, r, x))
    def kin(a):
        v = rels[a][2]
        return {a, pdx.get(v, 'parent'), pdx.get(v, 'reformed')} | {
            r for r, x in rels.items() if a in (pdx.get(x[2], 'parent'), pdx.get(x[2], 'reformed'))}
    for what, table in (('icon', icons), ('colour', colors)):
        for i, rs in table.items():
            rest = [r for r in rs if not any(r in kin(o) for o in rs if o != r)]
            if len(rest) > 1:
                warns.append('%s %s shared by %s' % (what, ' '.join(i) if isinstance(i, tuple) else i,
                                                     ', '.join(rest)))
    # religious titles
    titems = []
    for rel, entries in load('religious_titles', errors, warns):
        for k, op, v, line in entries:
            if isinstance(v, list):
                titems.append((k, '%s:%d' % (rel, line)))
                x = pdx.get(v, 'religion')
                if x and x not in rels:
                    errors.append('%s:%d title %s: religion %s is not defined' % (rel, line, k, x))
    dupes(titems, 'religious title', errors)
    # features
    feats, fitems = set(), []
    for rel, entries in load('religion_features', errors, warns):
        for k, op, v, line in entries:
            if isinstance(v, list):
                for kk, oo, vv, ll in v:
                    if isinstance(vv, list) and kk != 'buttons':
                        feats.add(kk)
                        fitems.append((kk, '%s:%d' % (rel, ll)))
    dupes(fitems, 'religion feature', errors)
    # authority modifiers
    mods, mitems = set(), []
    for rel, entries in load('religion_modifiers', errors, warns):
        for k, op, v, line in entries:
            if isinstance(v, list):
                mods.add(k)
                mitems.append((k, '%s:%d' % (rel, line)))
    dupes(mitems, 'authority modifier', errors)
    # uses across the mod
    known = {'religion': rels, 'true_religion': rels, 'secret_religion': rels,
             'religion_group': groups, 'true_religion_group': groups, 'secret_religion_group': groups,
             'has_religion_feature': feats, 'has_selected_religion_feature': feats}
    for r in ('events', 'decisions', 'common', 'history'):
        for dirpath, _, files in os.walk(os.path.join(ROOT, r)):
            for name in files:
                if not name.endswith('.txt'):
                    continue
                path = os.path.join(dirpath, name)
                rel = os.path.relpath(path, ROOT)
                text = '\n'.join(l.split('#', 1)[0] for l in pdx.read(path)[0].split('\n'))
                for n, line in enumerate(text.split('\n'), 1):
                    for m in USE.finditer(line):
                        k, x = m.groups()
                        if x in SKIP or x.isupper() or x.startswith(('FROM', 'PREV', 'event_target')):
                            continue
                        if x not in known[k]:
                            later = rel.startswith(tuple('common/' + f for f in LATER)) or rel == 'decisions/wonder_decisions.txt'
                            (warns if later else errors).append('%s:%d %s %s is not defined%s' % (
                                rel, n, k, x, ' (fix with that folder)' if later else ''))
                for m in AUTH.finditer(text):
                    if m.group(1) not in mods:
                        n = text.count('\n', 0, m.start()) + 1
                        errors.append('%s:%d authority modifier %s is not defined' % (rel, n, m.group(1)))
    if '--vanilla-loc' in sys.argv:
        loc = read_loc(os.path.join(ROOT, 'localisation'))
        loc |= read_loc(sys.argv[sys.argv.index('--vanilla-loc') + 1])
        for g, (rel, line, v) in sorted(groups.items()):
            if g not in loc:
                warns.append('%s:%d religion group %s has no name' % (rel, line, g))
        for r, (rel, line, v, g) in sorted(rels.items()):
            for key in (r, r + '_DESC'):
                if key not in loc:
                    warns.append('%s:%d religion %s has no text %s' % (rel, line, r, key))
            names = [pdx.get(v, f) for f in LOC_FIELDS]
            for f in ('god_names', 'evil_god_names'):
                for x in pdx.getall(v, f):
                    names += [vv for kk, oo, vv, ll in x] if isinstance(x, list) else []
            for x in filter(None, names):
                if x not in loc:
                    warns.append('%s:%d religion %s: %s has no text' % (rel, line, r, x))
    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN ', w)
    print('faith: %d groups, %d religions, %d religious titles, %d features, %d authority modifiers; '
          'ERROR %d, WARN %d' % (len(groups), len(rels), len(titems), len(feats), len(mods),
                                 len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
