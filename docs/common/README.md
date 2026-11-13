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
| modifiers | done | event_modifiers (57 files to 21), opinion_modifiers (22 to 21), triggered_modifiers (1 to 3), modifier_definitions (2 to 3), all `WHG_<subject>_<folder>.txt`; the vanilla names are overrides with the index |
| scripted triggers, effects, score values | done | 326 files merged into 23 `WHG_<subject>_triggers.txt`, 23 `WHG_<subject>_effects.txt` and 2 `WHG_*_score_values.txt`; the 24 vanilla names are overrides (the 00_ files hold the index) |

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

## Modifiers (event, opinion, triggered, definitions)

- One file per subject in each folder, with the same subjects everywhere
  (character, court, realm, war, faith, society, magic, chaos, undead,
  greenskin, dwarf, elves, empire, bretonnia, kislev, south, east, sea,
  legend): `WHG_kislev_event_modifiers.txt`,
  `WHG_kislev_opinion_modifiers.txt`. A modifier goes in the subject of the
  scripts that use it most.
- `WHG_engine_*` holds what the game applies itself (prison, truce breaking,
  bankruptcy, and vanilla's "hard" opinion modifiers): never rename those.
  `WHG_vanilla_*` holds vanilla modifiers that nothing in the mod uses, kept
  for salvage; move one to its subject file when you bring it back.
- Each entry starts with a comment: its name in game and the files that use
  it. Modifiers nothing uses yet go at the end of their file under "Not used
  by any script yet".
- Every modifier a player can see needs a name and a `_desc` in
  localisation (`localisation/00_WHG_modifiers.csv` for ones without a home
  file). Opinion modifiers at 0 need none (they do not show).
- Triggered modifiers are checked for every character all the time: put
  cheap, rare checks (a title, a trait, a flag) in `potential` and the rest
  in `trigger`, which need not repeat `potential`.
- `python3 tools/common/check_modifiers.py` reports modifiers defined twice,
  modifiers used but not defined (adding one does nothing, checking one is
  always false), bad icons, triggered modifiers missing a block, UTF-8 files
  and commented-out code. With `--vanilla-loc <CK2>/localisation` it also
  reports visible modifiers with no name.

## Scripted triggers, effects and score values

- One file per subject, the same subjects as the modifiers plus `race`
  (racial traits, which faiths and cultures fit a race, races without women)
  and `game_rule`: `WHG_kislev_triggers.txt`, `WHG_kislev_effects.txt`.
  Score values are few: the mod's are in `WHG_ai_score_values.txt`.
- A definition goes in the subject of its name (`add_trait_wroth_effect` is
  character, `warp_realm_at_war_trigger` is chaos) or of the file it was
  written for; helpers with no clear subject go where they are used most.
- `WHG_engine_*` holds what the game calls by name: vanilla's hard-coded
  triggers and effects (interactions, the crusade buttons, exile, leading
  troops) and the portrait triggers read by `interface/portraits` and
  `portrait_properties`. Never rename those.
  `WHG_vanilla_*` holds vanilla definitions nothing in the mod reaches,
  kept for salvage; move one to its subject file when content uses it.
- Inside a file: "Shared" (used by three or more files) first, then a section
  per file that uses four or more of them, then "Other helpers", then what no
  live script reaches yet. Every entry has a `# Used by:` line naming the
  files that call it.
- Names are global across the three folders and the load order does not
  matter: a definition may use one written later or in another file.
- Scripted triggers take conditions only. Branch with `trigger_if` /
  `trigger_else_if` / `trigger_else` (with `limit`), never `if`.
- Put cheap checks first in an OR or AND: a flag, a trait, a game rule or a
  scope comparison before a loop over friends, the court or the world.
  `hidden_trait`, `visible_trait` and the religion variants run for every
  trait on every portrait, so their loops come last.
- `python3 tools/common/check_scripted.py` reports names defined twice,
  `*_trigger`/`*_effect`/`*_score` calls that nothing defines, effect
  commands in a trigger, missing `Used by` lines, UTF-8 files and
  commented-out code. `--unused` lists what no live script reaches.
