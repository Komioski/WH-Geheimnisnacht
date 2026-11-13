# common/: house style and refactor progress

The `common/` folder is being refactored one sub-folder at a time, after the
events refactor (see `docs/events/README.md`, whose rules on races, gender,
DLC fallbacks and performance apply here too).

## Rules for every refactored folder

**File names.** A finished file is named `WHG_<subject>_<folder>.txt`
(`WHG_pulse_on_actions.txt`, `WHG_race_triggers.txt`), so finished work stands
out at a glance. Small files on one subject are merged.

**Vanilla file names.** In folders without `replace_path` in
`WH-Geheimnisnacht.mod`, a mod file with the same name as a vanilla file
replaces it, and every other vanilla file still loads. Such a file keeps its
vanilla name even when the content moves to `WHG_` files; it then holds only a
header saying why it exists and an index of the folder
(`common/on_actions/00_on_actions.txt`, `common/societies/00_societies.txt`).
Vanilla copies are never deleted, even when identical to vanilla.

**File header.** A comment block at the top: what the file covers, how the
game reads this kind of file when that is not obvious, and a list of what is
in it.

**Comments.** Every entry that points at an event, effect or trigger says what
it is in a few words, and the file it lives in. No commented-out code: git
keeps the history. Real-world names (Pope, Jihad, Zoroastrian...) are replaced
by their Warhammer counterparts, except engine keys that cannot change
(`NOMINATE_BISHOP_TO_POPE_INTERACTION_ACCEPT_EVENT`).

**Encoding.** cp1252 or plain ASCII, never UTF-8; tabs for indentation.

**Checks.** Each folder gets a checker in `tools/common/` when the game would
fail silently on a mistake there.

## Progress

| Folder | Status | Files |
|---|---|---|
| on_actions | done | 15 files merged into 9 `WHG_*_on_actions.txt` by subject; `00_on_actions.txt` and `00_zeus_education.txt` are vanilla-name overrides with the index |

## on_actions

- Every on_action is written exactly once in the mod, in the `WHG_` file for
  its subject: startup, pulse, character, realm, diplomacy, war, faith,
  building, society. The game would merge several copies, but one place per
  hook makes the load of each pulse visible and one search finds every
  caller.
- Above each on_action sit vanilla's scope notes (who is ROOT, FROM...).
- Each event line: `ns.12 # Title from the event's doc comment (WHG_x_events)`.
- New events go in an existing on_action block. Converted MTTH events get their
  own named `random_events` sub-list with a `0` entry (see the events README,
  Performance).
- `python3 tools/common/check_on_actions.py` reports unknown on_action names,
  missing events, an on_action written twice, duplicate entries, pulse
  sub-lists without a `0` entry and commented-out entries. Run it with
  `tools/events/check_events.py` before committing.
