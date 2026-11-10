# Events: database and house style

This folder documents the mod's events.

- `event_database.csv` lists every event: where it lives, what fires it, what it fires, its pre-triggers, its primary faction and a one-line summary. Open it in a spreadsheet or browse it on GitHub.
- The tools in `tools/events/` build the database and check event files. They need Python 3 and nothing else.

```
python3 tools/events/build_event_db.py                 # rebuild event_database.csv and the stats below
python3 tools/events/check_events.py                   # whole-mod summary
python3 tools/events/check_events.py events/X.txt      # every finding for one file
python3 tools/events/pdxfmt.py events/X.txt            # reformat a file in the house style
```

Run both before committing an event change, and commit the regenerated CSV with it.

`pdxfmt.py` only changes layout: tabs, `key = value` spacing, one statement per line with short blocks kept on one line, comments kept where they were. It refuses to write a file if the code or comments would change.

## Database columns

| Column | Meaning |
|---|---|
| `id`, `namespace`, `file`, `line` | Where the event is defined. |
| `type` | character, province, letter, narrative... |
| `fires` | `triggered` (fired by something), `MTTH` (polled by the engine), or `never (orphan)` (triggered-only, but nothing fires it). |
| `hidden` | `yes` for `hide_window` events. |
| `fired_by` | on_actions (with the random list name), decisions, other events, and common/ files such as CB types or job titles. |
| `calls` | Events this one fires. |
| `pre_triggers` | Cheap filters checked before `trigger` (`only_playable`, `religion_group`...). |
| `primary_faction` | From the event's `# Faction:` tag, else the cultures, religions and creature traits its trigger names, else the file's `# Faction:` tag, else its callers. `Generic` when none apply. |
| `faction_source` | Which of those rules decided it: `tag`, `trigger`, `file` or `caller`. |
| `origin` | `vanilla` for Paradox namespaces (HF, WoL, ZE...), otherwise `mod`. |
| `title`, `summary` | From the doc comment. Undocumented events fall back to the old author comment (`summary_source = comment`) or the English description (`loc`). |

The tools only see the mod's own files. Vanilla on_actions that the mod does not override are not counted as callers.

## House style for event files

Refactored files follow these rules. `events/WHG_skaven_events.txt` and `events/WHG_witch_hunter_events.txt` are the reference examples.

**One file per subject, one namespace per file.** Namespaces are short lowercase faction or subject words (`skaven`, `whunter`), 12 characters at most, never author initials.

**Short event numbers.** Number events from 1 and keep them below 1000. Give each section of a file its own block of numbers with room to grow (Skaven: breeding 1-14, old age 20, succession 30-36, warpstone 40, land demands 50-55, Vulkan 60). Loc keys follow the id: `EVTDESC<namespace><number>` and `EVTOPTA<namespace><number>`, `EVTOPTB...` for options in order, with a `b` suffix for a second desc or name variant. **File names.** A finished file is renamed `events/WHG_<subject>_events.txt` so finished files stand out at a glance; the folder stays flat. Small files on the same subject are merged into one (one file may hold several namespaces, each with its own header block). Its loc goes in `localisation/00_WHG_<subject>_events.csv`: the `00_` prefix keeps it loading before the older csvs, because the first definition of a key wins (the Chaos cult boon names override MonksAndMystics.csv this way). The descriptor (`WH-Geheimnisnacht.mod`) has `replace_path = "events"`, so no vanilla event file ever loads: rename or merge freely and delete the old file, no empty placeholder needed.

**File header.** A comment block at the top: what the file covers, the namespace, a `# Faction:` tag, a table of contents by id range, and where the events are fired from.

**Doc comment on every event,** directly above it with no blank line:

```
# skaven.7 Warpstone from the mines
# A ruler whose capital has a warpstone mine gains a step of the warpstone
# modifier. Bigger mines make it more frequent.
# Scope: ROOT is the ruler.
character_event = {
```

The first line is the id and a short title. Then a plain-language summary of what the event does and why, and a `# Scope:` line naming ROOT and FROM. Add `# Faction:` only when the computed faction is wrong.

**Layout.**
- Tabs for indentation, `key = value` with spaces, one block per line unless it is a short one-liner such as `modifier = { factor = 0.5 trait = shy }`.
- Order inside an event: `id`, `desc`, `picture`, `hide_window`, `is_triggered_only` (with a comment naming the on_action), pre-triggers, `trigger`, `mean_time_to_happen` or `weight_multiplier`, `immediate`, options, `after`.
- Label options with a short comment, e.g. `option = { # Refuse`.
- Files are ASCII or cp1252, never UTF-8. CK2 reads cp1252.
- No commented-out code. Git keeps the history. (For now, ask Komi before deleting old commented-out code; mark what is kept with a comment saying why.)

**Performance.**
- Every MTTH or pulse event starts with cheap pre-triggers: `only_playable`, `only_rulers`, `religion_group`, `culture_group`, `has_character_flag` or `ai`. The engine checks these before the trigger A `min_age` of 40 or more also counts, since few characters live that long. Events on `on_adolescence` (once a lifetime) and `on_startup` (once a load) don't need one.
- Prefer on_action `random_events` lists to MTTH. A `weight_multiplier` only works for events in a `random_events` list.
  - Use the slowest pulse that fits, so the yearly pulse stays light: `on_bi_yearly_pulse`, `on_five_year_pulse` or `on_decade_pulse` for anything rarer than every few years, and a one-off on_action (`on_adolescence`, `on_death`...) for anything tied to a moment in life. Keep `on_yearly_pulse` for events that must react within a year.
  - To convert an MTTH event, put it in its own named sub-list next to a `0` option, so its odds do not change the other events. With `my_list = { 100 = 0  w = ns.5 }` the chance per pulse is w / (100 + w): for MTTH 10 years on the five-year pulse, w = 100 (1 in 2 per five years). Turn the MTTH modifiers into `weight_multiplier` factors by inverting them (0.5 becomes 2).
  - MTTH is still right when the event depends on where a character is or what they are doing right now (for example an army marching through a region). Give it a strong pre-trigger.
  - For a state that lasts a while (a witch hunt, a quest), set a character flag when it starts and use `has_character_flag` as the pre-trigger of its MTTH events.
- Job action events stay MTTH and must be listed in the action's `events = { }` in `common/job_actions`. The game then only checks them for characters doing that action.
- Avoid `any_character`, `random_character` and other world-wide loops in triggers and pulses. Use event targets, flags or a narrower scope.
- Repeated trigger blocks become scripted triggers (`common/scripted_triggers/wh_<subject>_triggers.txt`).

**Races and gender.**
- Keep DLC fallbacks. Every DLC is recommended, but some players will miss one. Never drop a `has_dlc` / `lacks_dlc` check or a `NOT = { has_dlc = ... }` branch as dead. A DLC branch that has a fallback keeps it, and new content that leans on a DLC feature (hospitals, epidemics, societies, bloodlines, the Cathay offmap, focuses, council votes) gets a `has_dlc` check or a plain fallback. `add_symptom_effect` and the Reaper's Due `give_*_effect`s already fall back to `ill` on their own.
- Never test `is_female = yes` for a woman's role (daughter, wife, mother, sister, lover, lady of the court) or a gendered text variant. Use `is_woman_trigger = yes` / `= no` (`common/scripted_triggers/wh_scripted_triggers.txt`). Orcs, goblins, lizardmen, Skaven, Fimir and Tomb Kings have no women as vanilla shows them; their engine-female characters are snotlings, breeders, Saurus or the Maergh, and `is_no_females_race` is the one place that lists them. Romance partners also need `is_no_females_race = no`, and every `add_lover` sits behind that check for both lovers. Snotlings, Saurus and Skaven breeders carry `cannot_marry`. Keep raw `is_female` only for race mechanics (racial traits, breeders, `set_gender`).
- Faith and culture changes go through `faith_fits_race_of_prev_trigger` and `culture_fits_race_of_prev_trigger` (`WHG_race_triggers.txt`).

**Modern syntax.**
- `if` / `else_if` / `else` instead of chains of `if` with `break = yes`.
- `death = { death_reason = ... }`, never `death = yes`.
- `NOT = { health = 6 }` rather than `health < 6` for triggers that do not document comparison operators.

**Renaming a namespace** changes every event id. Update on_actions, decisions, other events and common/ in the same commit. `check_events.py` reports calls to missing events. Events already scheduled in a running save under the old id are lost, so a renamed namespace breaks saves in progress for that content.

## Stats

Generated by `build_event_db.py`.

<!-- stats:start -->
| Faction | Events | Mod-written | Vanilla | Player-visible | Documented |
|---|---:|---:|---:|---:|---:|
| Generic | 7603 | 3678 | 3925 | 6363 | 2159 |
| Chaos | 1069 | 1054 | 15 | 809 | 920 |
| Old World faiths | 819 | 567 | 252 | 680 | 313 |
| Araby & Southlands | 554 | 480 | 74 | 516 | 230 |
| Diplomacy & realms | 542 | 542 | 0 | 456 | 192 |
| Vampires | 491 | 491 | 0 | 447 | 392 |
| Family & bloodlines | 456 | 455 | 1 | 410 | 21 |
| Lizardmen & Amazons | 412 | 411 | 1 | 365 | 403 |
| Dwarfs | 371 | 371 | 0 | 302 | 252 |
| Warrior societies | 340 | 340 | 0 | 275 | 260 |
| Kislev | 297 | 292 | 5 | 253 | 277 |
| Empire | 262 | 247 | 15 | 202 | 190 |
| Faiths & doctrines | 248 | 247 | 1 | 215 | 0 |
| Beastmen | 161 | 131 | 30 | 128 | 99 |
| Dark Elves | 149 | 149 | 0 | 134 | 78 |
| High Elves | 143 | 143 | 0 | 115 | 72 |
| Greenskins | 114 | 114 | 0 | 92 | 100 |
| Norsca | 97 | 79 | 18 | 84 | 46 |
| Wood Elves | 72 | 72 | 0 | 63 | 42 |
| Bretonnia | 63 | 58 | 5 | 42 | 41 |
| Tomb Kings | 56 | 56 | 0 | 50 | 2 |
| Chaos Dwarfs | 39 | 39 | 0 | 36 | 35 |
| Skaven | 32 | 32 | 0 | 24 | 27 |
| Tilea, Estalia & Sartosa | 31 | 14 | 17 | 26 | 4 |
| Cathay & the East | 29 | 29 | 0 | 24 | 13 |
| Ogres | 7 | 7 | 0 | 6 | 1 |
| Albion & Fimir | 1 | 1 | 0 | 1 | 0 |

14458 events in 260 files. MTTH: 502, triggered: 13640, never fired: 316.
<!-- stats:end -->
