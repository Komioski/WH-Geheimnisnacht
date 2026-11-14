"""Check the mod's modifier files.

    python3 tools/common/check_modifiers.py [--vanilla-loc DIR]

Covers common/event_modifiers, common/opinion_modifiers,
common/triggered_modifiers and common/modifier_definitions. Reports, as ERROR
or WARN:
- a modifier defined twice (in one file or two): the game keeps one and the
  other is silently lost;
- an event modifier that a script adds or checks (add_character_modifier,
  has_province_modifier, add_society_modifier...) but no file defines, and
  the same for opinion modifiers (opinion, reverse_opinion,
  has_opinion_modifier...): adding one does nothing, checking one is always
  false. Static modifiers (common/static_modifiers.txt) count as defined;
- an icon outside the 198 frames of modifier_icons.dds;
- a triggered modifier without potential or trigger;
- a file that is not cp1252/ASCII (UTF-8 breaks names in game);
- commented-out code (git keeps the history).
With --vanilla-loc (the CK2 install's localisation folder) it also warns
about modifiers in use that show in game but have no name in the mod's or
vanilla's localisation, so the player sees the raw key.
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

ICON_FRAMES = 198  # interface/province.gfx, GFX_modifier_icons
FOLDERS = ('event_modifiers', 'opinion_modifiers', 'triggered_modifiers',
           'modifier_definitions')
EVENT_MOD_KEYS = {
    'add_character_modifier', 'remove_character_modifier',
    'has_character_modifier', 'add_province_modifier',
    'remove_province_modifier', 'has_province_modifier',
    'add_holding_modifier', 'remove_holding_modifier', 'has_holding_modifier',
    'add_dynasty_modifier', 'remove_dynasty_modifier', 'has_dynasty_modifier',
    'add_title_modifier', 'remove_title_modifier', 'has_title_modifier',
    'add_society_modifier', 'remove_society_modifier', 'has_society_modifier',
    'has_instances_of_character_modifier',
}
OPINION_KEYS = {
    'opinion', 'reverse_opinion', 'remove_opinion', 'reverse_remove_opinion',
    'has_opinion_modifier', 'reverse_has_opinion_modifier',
}
CODE = re.compile(r'^\s*#\s*[A-Za-z_][A-Za-z0-9_.]*\s*(=|>=|<=)\s*\S')


def read_defs(folder):
    defs = defaultdict(list)
    errors, warns = [], []
    for path in sorted(glob.glob(os.path.join(ROOT, 'common', folder, '*.txt'))):
        rel = os.path.relpath(path, ROOT)
        text, enc = pdx.read(path)
        if enc.startswith('utf-8'):
            errors.append('%s: %s, must be cp1252 or ASCII' % (rel, enc))
        entries, brace = pdx.parse(text)
        if brace:
            errors.append('%s: %d unbalanced braces' % (rel, brace))
        for k, op, v, line in entries:
            if k:
                defs[k].append((rel, line, v))
        for n, raw in enumerate(text.split('\n'), 1):
            if CODE.match(raw):
                warns.append('%s:%d commented-out code: %s' % (rel, n, raw.strip()[:60]))
    return defs, errors, warns


def references():
    ev, op = defaultdict(list), defaultdict(list)
    shown = set()  # event modifiers added at least once without hidden = yes
    roots = ['events', 'decisions', 'common', 'history']
    skip = tuple(os.path.join(ROOT, 'common', f) for f in FOLDERS)
    for r in roots:
        for dirpath, _, files in os.walk(os.path.join(ROOT, r)):
            if dirpath.startswith(skip):
                continue
            for f in files:
                if not f.endswith('.txt'):
                    continue
                path = os.path.join(dirpath, f)
                rel = os.path.relpath(path, ROOT)
                entries, _ = pdx.parse(pdx.read(path)[0])
                for k, o, v, line, d in pdx.walk(entries):
                    if k in EVENT_MOD_KEYS:
                        name = v if isinstance(v, str) else (pdx.get(v, 'name') or pdx.get(v, 'modifier'))
                        if name and not name.startswith('['):
                            ev[name].append('%s:%d' % (rel, line))
                            if k.startswith('add_') and isinstance(v, list) and pdx.get(v, 'hidden') != 'yes':
                                shown.add(name)
                    elif k in OPINION_KEYS and isinstance(v, list):
                        name = pdx.get(v, 'modifier') or pdx.get(v, 'name')
                        if name:
                            op[name].append('%s:%d' % (rel, line))
    return ev, op, shown


def loc_keys(dirs):
    keys = set()
    for d in dirs:
        for path in glob.glob(os.path.join(d, '**', '*.csv'), recursive=True):
            for raw in open(path, encoding='cp1252', errors='replace'):
                k = raw.split(';', 1)[0].strip()
                if k and not k.startswith('#'):
                    keys.add(k)
    return keys


def main():
    vanilla_loc = None
    if '--vanilla-loc' in sys.argv:
        vanilla_loc = sys.argv[sys.argv.index('--vanilla-loc') + 1]
    errors, warns = [], []
    defs = {}
    for f in FOLDERS:
        d, e, w = read_defs(f)
        defs[f] = d
        errors += e
        warns += w
        for k, where in d.items():
            if len(where) > 1:
                errors.append('%s: %s defined %d times (%s)' % (
                    f, k, len(where), ', '.join('%s:%d' % (p, l) for p, l, _ in where)))
    static = set()
    sp = os.path.join(ROOT, 'common', 'static_modifiers.txt')
    if os.path.exists(sp):
        static = {k for k, o, v, l in pdx.parse(pdx.read(sp)[0])[0] if k}
    ev, op, shown = references()
    for name, where in sorted(ev.items()):
        if name not in defs['event_modifiers'] and name not in static:
            errors.append('event modifier %s is used but not defined (%s)' % (name, ', '.join(where[:3])))
    for name, where in sorted(op.items()):
        if name not in defs['opinion_modifiers']:
            errors.append('opinion modifier %s is used but not defined (%s)' % (name, ', '.join(where[:3])))
    for k, where in defs['event_modifiers'].items():
        for p, l, v in where:
            if isinstance(v, list):
                icon = pdx.get(v, 'icon')
                if icon is not None and (not icon.isdigit() or not 1 <= int(icon) <= ICON_FRAMES):
                    errors.append('%s:%d %s: icon %s is not a frame of modifier_icons.dds' % (p, l, k, icon))
    for k, where in defs['triggered_modifiers'].items():
        for p, l, v in where:
            if isinstance(v, list) and (pdx.get(v, 'potential') is None or pdx.get(v, 'trigger') is None):
                errors.append('%s:%d %s: a triggered modifier needs potential and trigger' % (p, l, k))
    if vanilla_loc:
        loc = loc_keys([os.path.join(ROOT, 'localisation'), vanilla_loc])
        for k, where in defs['event_modifiers'].items():
            p, l, v = where[0]
            if k not in shown or k in loc or not isinstance(v, list):
                continue
            vis = pdx.get(v, 'is_visible')
            if isinstance(vis, list) and pdx.get(vis, 'always') == 'no':
                continue
            if pdx.get(v, 'icon') is None:
                continue
            warns.append('%s:%d event modifier %s has no name in localisation' % (p, l, k))
        for k, where in defs['opinion_modifiers'].items():
            p, l, v = where[0]
            if k not in op or k in loc or not isinstance(v, list):
                continue
            if pdx.get(v, 'opinion') in (None, '0'):
                continue  # a zero opinion does not show in the breakdown
            warns.append('%s:%d opinion modifier %s has no name in localisation' % (p, l, k))
    unused_ev = [k for k in defs['event_modifiers'] if k not in ev]
    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN ', w)
    print('modifiers: %d event (%d not used by script), %d opinion, %d triggered, %d definitions; ERROR %d, WARN %d' % (
        len(defs['event_modifiers']), len(unused_ev), len(defs['opinion_modifiers']),
        len(defs['triggered_modifiers']), len(defs['modifier_definitions']), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
