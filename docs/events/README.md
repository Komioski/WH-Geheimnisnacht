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

Refactored files follow these rules. `events/S_skaven_events.txt` and `events/S_witch_hunters_events.txt` are the reference examples.

**One file per subject, one namespace per file.** Namespaces are short lowercase faction or subject words (`skaven`, `whunter`), 12 characters at most, never author initials.

**Short event numbers.** Number events from 1 and keep them below 1000. Give each section of a file its own block of numbers with room to grow (Skaven: breeding 1-14, old age 20, succession 30-36, warpstone 40, land demands 50-55, Vulkan 60). Loc keys follow the id: `EVTDESC<namespace><number>` and `EVTOPTA<namespace><number>`, `EVTOPTB...` for options in order, with a `b` suffix for a second desc or name variant. File names keep their prefix for now so diffs stay readable; the folder stays flat.

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
- Every MTTH or pulse event starts with cheap pre-triggers: `only_playable`, `only_rulers`, `religion_group`, `culture_group`, `has_character_flag` or `ai`. The engine checks these before the trigger.
- Prefer on_action `random_events` lists to MTTH. A `weight_multiplier` only works for events in a `random_events` list.
- Avoid `any_character`, `random_character` and other world-wide loops in triggers and pulses. Use event targets, flags or a narrower scope.
- Repeated trigger blocks become scripted triggers (`common/scripted_triggers/wh_<subject>_triggers.txt`).

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
| Generic | 11996 | 3356 | 8640 | 9907 | 41 |
| Old World faiths | 557 | 61 | 496 | 478 | 14 |
| Lizardmen & Amazons | 314 | 307 | 7 | 279 | 0 |
| Araby & Southlands | 298 | 43 | 255 | 268 | 0 |
| Empire | 285 | 157 | 128 | 198 | 106 |
| High Elves | 226 | 226 | 0 | 198 | 0 |
| Chaos | 222 | 128 | 94 | 191 | 4 |
| Norsca | 191 | 13 | 178 | 166 | 0 |
| Dwarfs | 110 | 110 | 0 | 95 | 0 |
| Tilea, Estalia & Sartosa | 93 | 10 | 83 | 55 | 0 |
| Greenskins | 92 | 92 | 0 | 77 | 0 |
| Beastmen | 87 | 43 | 44 | 76 | 0 |
| Dark Elves | 85 | 85 | 0 | 78 | 0 |
| Kislev | 69 | 17 | 52 | 54 | 0 |
| Tomb Kings | 54 | 54 | 0 | 49 | 0 |
| Chaos Dwarfs | 45 | 45 | 0 | 39 | 0 |
| Vampires | 41 | 41 | 0 | 39 | 0 |
| Wood Elves | 40 | 40 | 0 | 33 | 1 |
| Bretonnia | 39 | 17 | 22 | 23 | 0 |
| Skaven | 32 | 32 | 0 | 24 | 27 |
| Nagash | 13 | 13 | 0 | 13 | 0 |
| Cathay & the East | 9 | 2 | 7 | 7 | 0 |
| Ogres | 7 | 6 | 1 | 6 | 0 |
| Albion & Fimir | 1 | 1 | 0 | 1 | 0 |

14906 events in 361 files. MTTH: 859, triggered: 13534, never fired: 513.
<!-- stats:end -->
