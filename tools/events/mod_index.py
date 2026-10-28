"""Loads the mod's events and everything that fires them.

Index(root) reads events/, decisions/, common/on_actions/, the rest of
common/ (cb_types, job titles, scripted effects...), cultures, religions and
English localisation. build_event_db.py and check_events.py both use it.
"""
import os
import re
from collections import Counter, defaultdict

import pdx
from factions import factions_of, VANILLA_NAMESPACES

EVENT_TYPES = ('character_event', 'province_event', 'letter_event', 'narrative_event',
               'long_character_event', 'diploresponse_event', 'society_quest_event',
               'unit_event')
DECISION_BLOCKS = ('decisions', 'targetted_decisions', 'title_decisions', 'plot_decisions',
                   'offmap_decisions', 'fort_decisions', 'hospital_decisions',
                   'trade_post_decisions', 'settlement_decisions', 'unit_decisions')
# Keys allowed before `trigger`; the engine checks them cheaply before the trigger.
PRE_TRIGGERS = set('''only_playable only_rulers only_independent only_men only_women
    only_capable capable_only min_age max_age prisoner religion religion_group culture
    culture_group has_dlc is_part_of_plot war is_married is_female ai has_character_flag
    has_global_flag is_patrician is_in_society has_job_title friends rivals lacks_dlc
    is_sick is_pregnant age has_flag is_night'''.split())
STRONG_PRE = set('''only_playable only_rulers only_independent religion religion_group is_sick
    culture culture_group has_character_flag has_global_flag ai is_patrician
    is_in_society has_job_title has_flag'''.split())
PULSES = set('''on_yearly_pulse on_bi_yearly_pulse on_five_year_pulse on_decade_pulse
    on_yearly_childhood_pulse on_adolescence on_startup on_new_holder'''.split())
TAG = re.compile(r'^\s*#+\s*(Faction|Scope|Fired by|Calls|Notes?)\s*:\s*(.*)$', re.I)


class Event:
    def __init__(self, eid, etype, body, path, line):
        self.id = eid
        self.type = etype
        self.body = body
        self.path = path
        self.line = line
        self.namespace = eid.split('.')[0] if '.' in eid else ''
        self.triggered_only = pdx.get(body, 'is_triggered_only') == 'yes'
        self.hidden = pdx.get(body, 'hide_window') == 'yes'
        self.has_mtth = pdx.get(body, 'mean_time_to_happen') is not None
        self.has_weight = pdx.get(body, 'weight_multiplier') is not None
        self.pre = [k for k, op, v, l in body if k in PRE_TRIGGERS]
        self.calls = pdx.event_calls(body)
        self.doc_title = ''
        self.doc_summary = ''
        self.doc_faction = ''
        self.legacy_comment = ''

    @property
    def origin(self):
        if self.namespace in VANILLA_NAMESPACES or self.id.isdigit():
            return 'vanilla'
        return 'mod'

    def loc_keys(self):
        """(kind, key) pairs for desc, title and option names."""
        out = []
        for key in ('desc', 'title'):
            for v in pdx.getall(self.body, key):
                if isinstance(v, str):
                    out.append((key, v))
                elif isinstance(v, list) and pdx.get(v, 'text'):
                    out.append((key, pdx.get(v, 'text')))
        for opt in pdx.getall(self.body, 'option'):
            if not isinstance(opt, list):
                continue
            for v in pdx.getall(opt, 'name'):
                if isinstance(v, str):
                    out.append(('option', v))
                elif isinstance(v, list) and pdx.get(v, 'text'):
                    out.append(('option', pdx.get(v, 'text')))
        return out


class Index:
    def __init__(self, root):
        self.root = root
        self.events = {}            # id -> Event
        self.duplicates = []        # (id, path, line)
        self.file_info = {}         # rel path -> dict(namespaces, encoding, brace_errors, faction, header)
        self.fired_by = defaultdict(list)   # id -> [source strings]
        self.random_listed = set()  # ids that appear in on_action random_events
        self.job_listed = set()  # ids listed in common/job_actions events lists
        self.pulse_listed = defaultdict(set)  # id -> on_action names (events = { } lists)
        self.external_calls = []    # (source, id) from non-event files
        self.scripted_triggers = {}
        self.scripted_effects = {}
        self.decisions = {}
        self.culture_group = {}
        self.religion_group = {}
        self.loc = {}
        self._load_groups()
        self._load_scripted()
        self._load_loc()
        self._load_events()
        self._load_on_actions()
        self._load_decisions()
        self._load_common()

    def rel(self, path):
        return os.path.relpath(path, self.root).replace(os.sep, '/')

    # --- reference data -------------------------------------------------
    def _load_groups(self):
        for path in pdx.files(self.root, 'common/cultures'):
            block, _ = pdx.parse(pdx.read(path)[0])
            for group, op, v, l in block:
                if not isinstance(v, list):
                    continue
                for culture, op2, v2, l2 in v:
                    if isinstance(v2, list) and (pdx.get(v2, 'color') is not None
                                                 or pdx.get(v2, 'male_names') is not None):
                        self.culture_group[culture] = group
        for path in pdx.files(self.root, 'common/religions'):
            block, _ = pdx.parse(pdx.read(path)[0])
            for group, op, v, l in block:
                if not isinstance(v, list):
                    continue
                for religion, op2, v2, l2 in v:
                    if isinstance(v2, list) and religion != 'color' and (
                            pdx.get(v2, 'icon') is not None or pdx.get(v2, 'god_names') is not None):
                        self.religion_group[religion] = group

    def _load_scripted(self):
        for sub, target in (('common/scripted_triggers', self.scripted_triggers),
                            ('common/scripted_effects', self.scripted_effects)):
            for path in pdx.files(self.root, sub):
                block, _ = pdx.parse(pdx.read(path)[0])
                for k, op, v, l in block:
                    if isinstance(v, list):
                        target[k] = v

    def _load_loc(self):
        for path in pdx.files(self.root, 'localisation', '.csv'):
            text = open(path, 'rb').read().decode('cp1252', errors='replace')
            for row in text.split('\n'):
                if not row or row.startswith('#'):
                    continue
                parts = row.split(';')
                key = parts[0].strip()
                if key and key not in self.loc:
                    self.loc[key] = parts[1].strip() if len(parts) > 1 else ''

    # --- events -----------------------------------------------------------
    def _load_events(self):
        for path in pdx.files(self.root, 'events'):
            text, enc = pdx.read(path)
            lines = text.split('\n')
            block, errors = pdx.parse(text)
            rel = self.rel(path)
            namespaces = [v for k, op, v, l in block if k == 'namespace']
            info = dict(namespaces=namespaces, encoding=enc, brace_errors=errors,
                        faction='', header='', events=[])
            info['header'], info['faction'] = self._file_header(lines)
            self.file_info[rel] = info
            for k, op, v, line in block:
                if k not in EVENT_TYPES or not isinstance(v, list):
                    continue
                eid = pdx.get(v, 'id')
                if not eid:
                    continue
                ev = Event(eid, k, v, rel, line)
                self._read_doc_comment(ev, lines)
                info['events'].append(eid)
                if eid in self.events:
                    self.duplicates.append((eid, rel, line))
                    continue
                self.events[eid] = ev
        for ev in self.events.values():
            for callee in ev.calls:
                self.fired_by[callee].append('event:' + ev.id)

    @staticmethod
    def _file_header(lines):
        """Leading comment block of a file, and its `# Faction:` tag."""
        header, faction = [], ''
        for row in lines:
            s = row.strip()
            if not s.startswith('#'):
                if s.startswith('namespace') or not s:
                    continue
                break
            m = TAG.match(s)
            if m and m.group(1).lower() == 'faction':
                faction = m.group(2).strip()
            text = s.lstrip('#').strip()
            if text:
                header.append(text)
        return ' '.join(header), faction

    @staticmethod
    def _read_doc_comment(ev, lines):
        """Comment lines directly above an event (no blank line in between).

        Convention:  # <event id> <title>
                     # One or more summary lines.
                     # Faction: <name>          (optional override)
        """
        i = ev.line - 2
        block = []
        while i >= 0 and lines[i].strip().startswith('#'):
            block.insert(0, lines[i].strip())
            i -= 1
        if not block:
            return
        summary = []
        for row in block:
            m = TAG.match(row)
            if m:
                if m.group(1).lower() == 'faction':
                    ev.doc_faction = m.group(2).strip()
                continue
            text = row.lstrip('#').strip()
            if not text or set(text) <= set('#=-'):
                continue
            if text.startswith(ev.id + ' ') or text == ev.id:
                ev.doc_title = text[len(ev.id):].strip(' -:')
                continue
            summary.append(text)
        if ev.doc_title:
            ev.doc_summary = ' '.join(summary)
        else:
            ev.legacy_comment = ' '.join(summary)

    # --- callers ------------------------------------------------------------
    def _load_on_actions(self):
        for path in pdx.files(self.root, 'common/on_actions'):
            block, _ = pdx.parse(pdx.read(path)[0])
            for name, op, v, l in block:
                if not isinstance(v, list):
                    continue
                for k2, op2, v2, l2 in v:
                    if k2 == 'events' and isinstance(v2, list):
                        for k3, op3, eid, l3 in v2:
                            if k3 is None and isinstance(eid, str):
                                self.fired_by[eid].append('on_action:' + name)
                                self.pulse_listed[eid].add(name)
                    elif k2 == 'random_events' and isinstance(v2, list):
                        self._random_list(name, v2)
                    elif k2 == 'effect' and isinstance(v2, list):
                        for eid in pdx.event_calls(v2):
                            self.fired_by[eid].append('on_action:%s (effect)' % name)

    def _random_list(self, name, block, sub=''):
        for k, op, v, l in block:
            if isinstance(v, list):
                if k == 'delay':
                    continue
                self._random_list(name, v, k)
            elif k and k.isdigit() and v != '0':
                label = 'on_action:%s (random%s)' % (name, ': ' + sub if sub else '')
                self.fired_by[v].append(label)
                self.random_listed.add(v)

    def _load_decisions(self):
        for path in pdx.files(self.root, 'decisions'):
            block, _ = pdx.parse(pdx.read(path)[0])
            for k, op, v, l in block:
                if k not in DECISION_BLOCKS or not isinstance(v, list):
                    continue
                for name, op2, body, l2 in v:
                    if not isinstance(body, list):
                        continue
                    self.decisions[name] = body
                    for eid in pdx.event_calls(body):
                        self.fired_by[eid].append('decision:' + name)

    def _load_common(self):
        skip = ('common/on_actions', 'common/scripted_triggers', 'common/cultures',
                'common/religions')
        for path in pdx.files(self.root, 'common'):
            rel = self.rel(path)
            if rel.startswith(skip):
                continue
            block, _ = pdx.parse(pdx.read(path)[0])
            label = rel[len('common/'):]
            if rel.startswith('common/job_actions'):
                # Job actions list their MTTH events by id; the game only checks
                # them for characters doing that action.
                for name, op, body, l in block:
                    if not isinstance(body, list):
                        continue
                    for k, op2, v, l2 in body:
                        if k == 'events' and isinstance(v, list):
                            for item in v:
                                eid = item[2] if item[0] is None else item[0]
                                if isinstance(eid, str):
                                    self.fired_by[eid].append('job_action:' + name)
                                    self.job_listed.add(eid)
            for eid in pdx.event_calls(block):
                self.fired_by[eid].append(label)
                self.external_calls.append((rel, eid))

    # --- attribution --------------------------------------------------------
    def refs(self, block, out=None, neg=False, depth=0, seen=None):
        """Positive references to cultures, religions, their groups and creature traits."""
        if out is None:
            out = Counter()
        if seen is None:
            seen = set()
        for k, op, v, l in block:
            if k is None:
                continue
            n = neg or k in ('NOT', 'NOR')
            if isinstance(v, list):
                self.refs(v, out, n, depth, seen)
                continue
            if n:
                continue
            if k == 'culture' and v in self.culture_group:
                out['cg:' + self.culture_group[v]] += 1
            elif k == 'culture_group':
                out['cg:' + v] += 1
            elif k == 'religion' and v in self.religion_group:
                out['r:' + v] += 1
                out['rg:' + self.religion_group[v]] += 1
            elif k == 'religion_group':
                out['rg:' + v] += 1
            elif k == 'trait' and v.startswith('creature_'):
                out['tr:' + v] += 1
            elif v == 'yes' and k in self.scripted_triggers and depth < 3 and k not in seen:
                seen.add(k)
                self.refs(self.scripted_triggers[k], out, False, depth + 1, seen)
        return out

    def own_factions(self, ev):
        block = [e for e in ev.body if e[0] in PRE_TRIGGERS]
        trig = pdx.get(ev.body, 'trigger')
        if isinstance(trig, list):
            block = block + trig
        return factions_of(self.refs(block))

    def attribute(self):
        """Primary faction per event: doc tag, file tag, own refs, then callers."""
        primary, source = {}, {}
        for ev in self.events.values():
            if ev.doc_faction:
                primary[ev.id], source[ev.id] = ev.doc_faction, 'tag'
                continue
            own = self.own_factions(ev)
            if 1 <= len(own) <= 3:
                primary[ev.id], source[ev.id] = own.most_common(1)[0][0], 'trigger'
            elif self.file_info[ev.path]['faction']:
                primary[ev.id], source[ev.id] = self.file_info[ev.path]['faction'], 'file'
        dec_faction = {}
        for name, body in self.decisions.items():
            pot = pdx.get(body, 'potential')
            fs = factions_of(self.refs(pot)) if isinstance(pot, list) else Counter()
            if 1 <= len(fs) <= 3:
                dec_faction[name] = fs.most_common(1)[0][0]
        for _ in range(12):
            changed = False
            for ev in self.events.values():
                if ev.id in primary:
                    continue
                votes = Counter()
                ok = bool(self.fired_by.get(ev.id))
                for src in self.fired_by.get(ev.id, ()):
                    if src.startswith('event:') and src[6:] in primary:
                        votes[primary[src[6:]]] += 1
                    elif src.startswith('decision:') and src[9:] in dec_faction:
                        votes[dec_faction[src[9:]]] += 1
                    else:
                        ok = False
                        break
                if ok and votes:
                    primary[ev.id], source[ev.id] = votes.most_common(1)[0][0], 'caller'
                    changed = True
            if not changed:
                break
        return primary, source
