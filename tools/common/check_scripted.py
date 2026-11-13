"""Check the mod's scripted triggers, effects and score values.

    python3 tools/common/check_scripted.py [--unused]

Covers common/scripted_triggers, common/scripted_effects and
common/scripted_score_values. Reports, as ERROR or WARN:
- a name defined twice (in one file or two, or in two of the folders): the
  game keeps one and the other is silently lost;
- a scripted trigger, effect or score value called as "name = yes/no" that no
  file defines (names ending in _trigger, _effect or _score): the game logs an
  error and the call does nothing, so a condition built on it never holds;
- effect commands (if, else, limit at the top, set_*_flag, add_trait...) in a
  scripted trigger, where they do nothing (use trigger_if / trigger_else);
- a file that is not cp1252/ASCII (UTF-8 breaks names in game), unbalanced
  braces, commented-out code (git keeps the history);
- a WHG_ file whose "Used by" lines are missing (each entry says who uses it).
With --unused it also lists the definitions no live script reaches: nothing
calls them, or only other unused definitions do. Those are kept on purpose
(vanilla ones in the WHG_vanilla_ files, the mod's own at the end of each
subject file) and are not an error.
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

FOLDERS = ('scripted_triggers', 'scripted_effects', 'scripted_score_values')
CODE = re.compile(r'^\s*#\s*[A-Za-z_][A-Za-z0-9_.]*\s*(=|>=|<=)\s*\S')
CALL = re.compile(r'\b([A-Za-z_][A-Za-z0-9_]*_(?:trigger|effect|score))\s*=\s*(yes|no)\b')
EFFECTS_IN_TRIGGER = {
    'if', 'else', 'else_if', 'set_character_flag', 'clr_character_flag',
    'set_global_flag', 'add_trait', 'remove_trait', 'set_variable',
    'change_variable', 'add_character_modifier', 'character_event',
    'hidden_effect', 'random_list',
}
# Engine parameters that end like a scripted name (add_law = { opinion_effect = no })
PARAMS = {'opinion_effect'}
# The game calls these by name: they count as used.
ENGINE = {
    'will_add_kinslayer', 'assassination_interaction_trigger',
    'pagan_baptism_trigger', 'needs_coronation_trigger',
    'can_rename_character_trigger', 'pledge_crusade_trigger',
    'unpledge_crusade_trigger', 'defender_pledge_crusade_trigger',
    'defender_unpledge_crusade_trigger', 'select_crusade_receiver_stance_trigger',
    'contribute_to_crusade_pot_trigger', 'fit_to_lead_troops',
    'valid_exile_court_trigger', 'reset_religion_features_effect',
    'rename_character_effect', 'randomize_religion_names_effect',
    'pledge_crusade_effect', 'unpledge_crusade_effect',
    'defender_pledge_crusade_effect', 'defender_unpledge_crusade_effect',
    'contribute_to_crusade_pot_effect', 'crusade_give_artifact_effect',
    'select_crusade_receiver_stance_effect',
}


def definitions():
    defs = defaultdict(list)  # name -> [(folder, rel, line, block)]
    errors, warns = [], []
    for f in FOLDERS:
        for path in sorted(glob.glob(os.path.join(ROOT, 'common', f, '*.txt'))):
            rel = os.path.relpath(path, ROOT)
            text, enc = pdx.read(path)
            if enc.startswith('utf-8'):
                errors.append('%s: %s, must be cp1252 or ASCII' % (rel, enc))
            entries, brace = pdx.parse(text)
            if brace:
                errors.append('%s: %d unbalanced braces' % (rel, brace))
            lines = text.split('\n')
            for k, op, v, line in entries:
                if not k:
                    continue
                defs[k].append((f, rel, line, v))
                if os.path.basename(path).startswith('WHG_'):
                    above = lines[max(0, line - 6):line - 1]
                    if not any(l.startswith('# Used by: ') for l in above) and \
                            not _in_unused_section(lines, line):
                        warns.append('%s:%d %s has no "Used by" line' % (rel, line, k))
            for n, raw in enumerate(lines, 1):
                if CODE.match(raw):
                    warns.append('%s:%d commented-out code: %s' % (rel, n, raw.strip()[:60]))
    return defs, errors, warns


def _in_unused_section(lines, line):
    for raw in reversed(lines[:line - 1]):
        if raw.startswith('# Not used by any live script'):
            return True
        if raw.startswith('# Shared:') or raw.startswith('# Used by ') or \
                raw.startswith('# Other helpers') or raw.startswith('# Building blocks'):
            return False
    return False


def calls():
    """name -> [(rel, line, owner)] for every 'name = yes/no' in script."""
    out = defaultdict(list)
    for r in ('events', 'decisions', 'common', 'history'):
        for dirpath, _, files in os.walk(os.path.join(ROOT, r)):
            for f in files:
                if not f.endswith('.txt'):
                    continue
                path = os.path.join(dirpath, f)
                rel = os.path.relpath(path, ROOT)
                owner = None
                scripted = rel.startswith(tuple('common/' + x for x in FOLDERS))
                for n, raw in enumerate(pdx.read(path)[0].split('\n'), 1):
                    code = raw.split('#', 1)[0]
                    if scripted:
                        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=', code)
                        if m:
                            owner = m.group(1)
                    for m in re.finditer(r'\b([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(yes|no)\b', code):
                        out[m.group(1)].append((rel, n, owner if scripted else None))
    return out


def main():
    defs, errors, warns = definitions()
    for k, where in sorted(defs.items()):
        if len(where) > 1:
            errors.append('%s defined %d times (%s)' % (
                k, len(where), ', '.join('%s:%d' % (r, l) for _, r, l, _ in where)))
        f, rel, line, v = where[0]
        if f == 'scripted_triggers' and isinstance(v, list):
            bad = sorted({kk for kk, o, vv, ll, d in pdx.walk(v) if kk in EFFECTS_IN_TRIGGER}
                         | {kk for kk, o, vv, ll in v if kk == 'limit'})
            if bad:
                errors.append('%s:%d %s: effect commands in a trigger: %s' % (rel, line, k, ', '.join(bad)))
    used = calls()
    for name, where in sorted(used.items()):
        if name in defs or name in PARAMS or not CALL.match(name + ' = yes'):
            continue
        errors.append('%s is called but not defined (%s)' % (
            name, ', '.join('%s:%d' % (r, l) for r, l, _ in where[:3])))
    # live set: called from outside the scripted folders, by the game, or by
    # a live definition
    callers = defaultdict(set)
    live = set(ENGINE) & set(defs)
    for name, where in used.items():
        if name not in defs:
            continue
        for r, l, owner in where:
            if owner is None:
                live.add(name)
            elif owner != name:
                callers[name].add(owner)
    # Named elsewhere than as "name = yes": interface/portraits and
    # portrait_properties read portrait triggers, off-map powers read their
    # likes and dislikes by name, score values sit in weight blocks.
    names = set(defs)
    for r in ('events', 'decisions', 'common', 'history', 'interface'):
        for dirpath, _, files in os.walk(os.path.join(ROOT, r)):
            if os.path.relpath(dirpath, ROOT).startswith(tuple('common/' + x for x in FOLDERS)):
                continue
            for f in files:
                if f.endswith(('.txt', '.gfx', '.gui')):
                    text = '\n'.join(l.split('#', 1)[0] for l in pdx.read(os.path.join(dirpath, f))[0].split('\n'))
                    live |= set(re.findall(r'[A-Za-z_][A-Za-z0-9_]*', text)) & names
    changed = True
    while changed:
        changed = False
        for name in set(defs) - live:
            if callers[name] & live:
                live.add(name)
                changed = True
    dead = sorted(set(defs) - live)
    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN ', w)
    if '--unused' in sys.argv:
        for k in dead:
            print('UNUSED', k, '(%s)' % defs[k][0][1])
    n = {f: sum(1 for w in defs.values() if w[0][0] == f) for f in FOLDERS}
    print('scripted: %d triggers, %d effects, %d score values; %d not reached by any live script; ERROR %d, WARN %d' % (
        n['scripted_triggers'], n['scripted_effects'], n['scripted_score_values'],
        len(dead), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
