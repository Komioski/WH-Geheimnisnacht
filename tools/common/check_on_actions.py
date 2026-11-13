"""Check the mod's on_action files (common/on_actions).

    python3 tools/common/check_on_actions.py

Reports, as ERROR or WARN:
- an on_action name the game does not know (typos never fire);
- an event that no event file defines;
- an on_action written in more than one file, or twice in one file (the game
  merges them, but the mod keeps each in one place so one search finds all);
- the same event twice in one list of one on_action;
- a named random_events sub-list with no 0 entry on a pulse (it then fires an
  event on every pulse for everyone who qualifies; usually a mistake);
- commented-out entries (git keeps the history).
Standard library only. Exit code 1 if there are errors.
"""
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'events'))
import pdx  # noqa: E402

# Every on_action in vanilla CK2 3.3.5.1 (common/on_actions/00_on_actions.txt
# and 00_zeus_education.txt). The diplomatic *_ACCEPT_EVENT / *_DECLINE_EVENT
# hooks are on_actions too.
KNOWN = {
    'on_startup', 'on_yearly_pulse', 'on_bi_yearly_pulse',
    'on_five_year_pulse', 'on_decade_pulse', 'on_yearly_childhood_pulse',
    'on_focus_pulse', 'on_combat_pulse', 'on_combat_starting',
    'on_siege_pulse', 'on_battle_won', 'on_major_battle_won',
    'on_battle_won_leader', 'on_major_battle_won_leader',
    'on_battle_won_owner', 'on_battle_lost', 'on_major_battle_lost',
    'on_battle_lost_leader', 'on_major_battle_lost_leader',
    'on_battle_lost_owner', 'on_siege_won_leader', 'on_siege_won_leader_fort',
    'on_siege_won_leader_trade_post', 'on_siege_lost_leader',
    'on_siege_lost_leader_fort', 'on_siege_lost_leader_trade_post',
    'on_siege_over_winner', 'on_siege_over_winner_fort',
    'on_siege_over_winner_trade_post', 'on_siege_over_loc_chars',
    'on_siege_over_loc_chars_fort', 'on_siege_over_loc_chars_trade_post',
    'on_failed_assassination', 'on_failed_assassination_disc',
    'on_assassination', 'on_assassination_disc', 'on_birth', 'on_adulthood',
    'on_adolescence', 'on_post_birth', 'on_post_birth_stillbirth',
    'on_pregnancy', 'on_crusade_creation', 'on_marriage',
    'on_become_imprisoned_any_reason', 'on_avoided_imprison_started_war',
    'on_became_imprisoned', 'on_avoided_imprison_fled_country',
    'on_released_from_prison', 'on_executed', 'on_exiled',
    'on_prepared_invasion_monthly', 'on_prepared_invasion_aborts',
    'on_prepared_invasion_expires', 'on_death', 'on_merc_rampage',
    'on_merc_leave', 'on_merc_turn_coat_from', 'on_merc_turn_coat_to',
    'on_holy_order_leave', 'on_letter_event_message',
    'on_character_event_message', 'on_loot_settlement', 'on_loot_province',
    'DEMAND_RELIGIOUS_CONVERSION_INTERACTION_ACCEPT_EVENT',
    'DEMAND_RELIGIOUS_CONVERSION_INTERACTION_DECLINE_EVENT',
    'REVOKE_TITLE_INTERACTION_ACCEPT_EVENT',
    'REVOKE_TITLE_INTERACTION_DECLINE_EVENT',
    'OFFER_PEACE_INTERACTION_ACCEPT_EVENT',
    'OFFER_PEACE_INTERACTION_DECLINE_EVENT',
    'SEND_GIFT_INTERACTION_ACCEPT_EVENT',
    'SEND_GIFT_INTERACTION_DECLINE_EVENT',
    'ASK_FOR_MONEY_INTERACTION_ACCEPT_EVENT',
    'ASK_FOR_MONEY_INTERACTION_DECLINE_EVENT',
    'ASK_FOR_CLAIM_INTERACTION_ACCEPT_EVENT',
    'ASK_FOR_CLAIM_INTERACTION_DECLINE_EVENT',
    'NOMINATE_BISHOP_TO_POPE_INTERACTION_ACCEPT_EVENT',
    'NOMINATE_BISHOP_TO_POPE_INTERACTION_DECLINE_EVENT',
    'OFFER_VASSALIZATION_INTERACTION_ACCEPT_EVENT',
    'OFFER_VASSALIZATION_INTERACTION_DECLINE_EVENT',
    'ARRANGE_BETROTHAL_INTERACTION_ACCEPT_EVENT',
    'ARRANGE_BETROTHAL_INTERACTION_DECLINE_EVENT',
    'ARRANGE_SUCC_BETROTHAL_INTERACTION_ACCEPT_EVENT',
    'ARRANGE_SUCC_BETROTHAL_INTERACTION_DECLINE_EVENT',
    'OFFER_SUCCESSION_MARRIGE_INTERACTION_ACCEPT_EVENT',
    'OFFER_SUCCESSION_MARRIGE_INTERACTION_DECLINE_EVENT',
    'OFFER_MARRIGE_INTERACTION_ACCEPT_EVENT',
    'OFFER_MARRIGE_INTERACTION_DECLINE_EVENT',
    'RANSOM_CHARACTER_INTERACTION_ACCEPT_EVENT',
    'RANSOM_CHARACTER_INTERACTION_DECLINE_EVENT',
    'EDUCATE_CHARACTER_INTERACTION_ACCEPT_EVENT',
    'EDUCATE_CHARACTER_INTERACTION_DECLINE_EVENT',
    'ABANDON_AMBITION_INTERACTION_ACCEPT_EVENT',
    'ABANDON_AMBITION_INTERACTION_DECLINE_EVENT',
    'STOP_BACKING_AMBITION_INTERACTION_ACCEPT_EVENT',
    'STOP_BACKING_AMBITION_INTERACTION_DECLINE_EVENT',
    'JOIN_AMBITION_INTERACTION_ACCEPT_EVENT',
    'JOIN_AMBITION_INTERACTION_DECLINE_EVENT',
    'GRANT_LANDED_TITLE_INTERACTION_ACCEPT_EVENT',
    'GRANT_LANDED_TITLE_INTERACTION_DECLINE_EVENT',
    'APPOINT_TO_OFFICE_INTERACTION_ACCEPT_EVENT',
    'APPOINT_TO_OFFICE_INTERACTION_DECLINE_EVENT',
    'ASK_FOR_INVASION_INTERACTION_ACCEPT_EVENT',
    'ASK_FOR_INVASION_INTERACTION_DECLINE_EVENT',
    'ASK_FOR_DIVORCE_INTERACTION_ACCEPT_EVENT',
    'ASK_FOR_DIVORCE_INTERACTION_DECLINE_EVENT',
    'ASK_FOR_EXCOMMUNICATION_INTERACTION_ACCEPT_EVENT',
    'ASK_FOR_EXCOMMUNICATION_INTERACTION_DECLINE_EVENT',
    'CALL_ALLY_INTERACTION_ACCEPT_EVENT',
    'CALL_ALLY_INTERACTION_DECLINE_EVENT',
    'DECLARE_WAR_INTERACTION_ACCEPT_EVENT',
    'RETRACT_VASSAL_INTERACTION_ACCEPT_EVENT',
    'RETRACT_VASSAL_INTERACTION_DECLINE_EVENT',
    'INVITE_TO_COURT_INTERACTION_ACCEPT_EVENT',
    'INVITE_TO_COURT_INTERACTION_DECLINE_EVENT',
    'ASK_FOR_VASSALIZATION_INTERACTION_ACCEPT_EVENT',
    'ASK_FOR_VASSALIZATION_INTERACTION_DECLINE_EVENT',
    'ASK_TO_LIFT_EXCOMMUNICATION_INTERACTION_ACCEPT_EVENT',
    'ASK_TO_LIFT_EXCOMMUNICATION_INTERACTION_DECLINE_EVENT',
    'ASK_TO_RANSOM_CHARACTER_INTERACTION_ACCEPT_EVENT',
    'ASK_TO_RANSOM_CHARACTER_INTERACTION_DECLINE_EVENT',
    'SETTLE_ADVENTURER_INTERACTION_ACCEPT_EVENT',
    'SETTLE_ADVENTURER_INTERACTION_DECLINE_EVENT',
    'ASK_TO_JOIN_WAR_INTERACTION_ACCEPT_EVENT',
    'ASK_TO_JOIN_WAR_INTERACTION_DECLINE_EVENT',
    'ASK_TO_EMBARGO_INTERACTION_ACCEPT_EVENT',
    'ASK_TO_EMBARGO_INTERACTION_DECLINE_EVENT',
    'MAKE_CONSORT_INTERACTION_ACCEPT_EVENT',
    'MAKE_CONSORT_INTERACTION_DECLINE_EVENT',
    'ABSORB_CLAN_INTERACTION_ACCEPT_EVENT',
    'ABSORB_CLAN_INTERACTION_DECLINE_EVENT',
    'SPLIT_CLAN_INTERACTION_ACCEPT_EVENT',
    'SPLIT_CLAN_INTERACTION_DECLINE_EVENT',
    'FORM_BLOOD_OATH_INTERACTION_ACCEPT_EVENT',
    'FORM_BLOOD_OATH_INTERACTION_DECLINE_EVENT',
    'SETTLE_FEUD_INTERACTION_ACCEPT_EVENT',
    'SETTLE_FEUD_INTERACTION_DECLINE_EVENT',
    'FORM_ALLIANCE_INTERACTION_ACCEPT_EVENT',
    'FORM_ALLIANCE_INTERACTION_DECLINE_EVENT',
    'DISSOLVE_ALLIANCE_INTERACTION_ACCEPT_EVENT',
    'DISSOLVE_ALLIANCE_INTERACTION_DECLINE_EVENT',
    'BUY_FAVOR_INTERACTION_ACCEPT_EVENT',
    'BUY_FAVOR_INTERACTION_DECLINE_EVENT',
    'REQUEST_SUPPORT_INTERACTION_ACCEPT_EVENT',
    'REQUEST_SUPPORT_INTERACTION_DECLINE_EVENT',
    'FORM_NON_AGGRESSION_PACT_INTERACTION_ACCEPT_EVENT',
    'FORM_NON_AGGRESSION_PACT_INTERACTION_DECLINE_EVENT',
    'ASK_COUNCIL_POSITION_INTERACTION_ACCEPT_EVENT',
    'ASK_COUNCIL_POSITION_INTERACTION_DECLINE_EVENT',
    'ASK_REALM_PEACE_INTERACTION_ACCEPT_EVENT',
    'ASK_REALM_PEACE_INTERACTION_DECLINE_EVENT',
    'FORCE_JOIN_FACTION_INTERACTION_ACCEPT_EVENT',
    'FORCE_JOIN_FACTION_INTERACTION_DECLINE_EVENT',
    'ASK_TO_JOIN_AMBITION_INTERACTION_ACCEPT_EVENT',
    'ASK_TO_JOIN_AMBITION_INTERACTION_DECLINE_EVENT',
    'OFFER_CONSORT_INTERACTION_ACCEPT_EVENT',
    'GIVE_ARTIFACT_INTERACTION_ACCEPT_EVENT', 'on_warleader_death',
    'on_approve_law', 'councilor_on_approve_law', 'on_approve_de_jure_law',
    'on_rebel_revolt', 'on_defect_to_rebels', 'on_defect_from_rebels',
    'on_crusade_success', 'on_crusade_failure', 'on_crusade_invalid',
    'on_forced_consort', 'on_reform_religion', 'on_county_religion_change',
    'on_vassal_accepts_religious_conversion', 'on_heresy_takeover',
    'on_become_doge', 'on_elective_gavelkind_succession', 'on_entering_port',
    'on_rel_elector_chosen', 'on_rel_head_chosen', 'on_settlement_looted',
    'on_navy_returns_with_loot', 'on_create_title', 'on_new_holder',
    'on_new_holder_inheritance', 'on_new_holder_usurpation', 'on_unlanded',
    'on_create_chronicle_if_empty', 'on_chronicle_owner_change',
    'on_chronicle_start', 'on_character_convert_religion',
    'on_character_convert_secret_religion', 'on_character_convert_culture',
    'on_acquire_nickname', 'on_over_vassal_limit_succession',
    'on_war_started', 'on_war_ended_victory', 'on_war_ended_whitepeace',
    'on_war_ended_defeat', 'on_war_ended_invalid', 'on_divorce',
    'on_settlement_construction_start', 'on_trade_post_construction_start',
    'on_fort_construction_start', 'on_hospital_construction_start',
    'on_settlement_construction_completed',
    'on_trade_post_construction_completed', 'on_fort_construction_completed',
    'on_hospital_construction_completed', 'on_holding_building_start',
    'on_feud_started', 'on_feud_ended', 'on_blood_brother_death',
    'on_ai_end_raid', 'on_mercenary_hired', 'on_mercenary_dismissed',
    'on_mercenary_captain_replacement', 'on_enforce_peace',
    'on_enforce_peace_start', 'on_enforce_peace_six_vassals',
    'on_law_vote_passed', 'on_law_vote_failed', 'on_player_mercenary_income',
    'on_outbreak', 'on_province_major_modifier', 'on_society_bi_yearly_pulse',
    'on_character_switch_society_interest', 'on_character_society_rank_up',
    'on_character_society_rank_down', 'on_character_join_society',
    'on_character_leave_society', 'on_character_ask_to_join_society',
    'on_character_kicked_from_society', 'on_character_stop_showing_interest',
    'on_society_created', 'on_society_destroyed', 'on_focus_selected',
    'on_quest_success', 'on_quest_failure',
    'on_society_failed_to_find_new_leader', 'on_artifact_inheritance',
    'on_offmap_policy_changed', 'on_offmap_status_changed',
    'on_offmap_governor_changed', 'on_offmap_ruler_changed',
    'on_offmap_monthly_pulse', 'on_offmap_yearly_pulse',
    'on_eu4_conversion_start', 'on_eu4_conversion_done', 'on_tyranny_gained',
    'on_tyranny_gained_tyrant_only', 'on_revoke_attempted_started_war',
    'on_retract_vassal_attempted_started_war',
    'on_absorb_clan_attempted_started_war',
    'on_split_clan_attempted_started_war', 'on_alternate_start',
    'on_society_progress_zero', 'on_betrothal', 'on_society_progress_full',
    'on_unit_entering_province', 'on_command_unit', 'on_command_sub_unit',
    'on_crusade_preparation_starts', 'on_crusade_launches',
    'on_crusade_canceled', 'on_crusade_monthly', 'on_crusade_target_changes',
    'on_pledge_crusade_participation', 'on_pledge_crusade_defense',
    'on_unpledge_crusade_participation', 'on_unpledge_crusade_defense',
    'on_excommunicate_interaction', 'on_character_renamed',
    'on_title_renamed', 'on_province_renamed', 'on_wonder_renamed',
    'on_artifact_renamed', 'on_bloodline_renamed', 'on_employer_change',
    'on_host_change', 'on_wonder_owner_change',
    'on_wonder_construction_start', 'on_wonder_stage_finish',
    'on_wonder_destroyed', 'on_wonder_upgrade_start',
    'on_wonder_upgrade_finish', 'on_wonder_upgrade_destroyed',
    'on_wonder_loot_start', 'on_wonder_stage_loot_start',
    'on_wonder_stage_loot_finish', 'on_wonder_restore_start',
    'on_wonder_restore_finish', 'on_childhood_pulse', 'on_adolescence_pulse',
}

PULSES = {'on_yearly_pulse', 'on_bi_yearly_pulse', 'on_five_year_pulse', 'on_decade_pulse',
          'on_focus_pulse', 'on_yearly_childhood_pulse', 'on_childhood_pulse',
          'on_adolescence_pulse', 'on_society_bi_yearly_pulse'}
DEAD = re.compile(r'^\s*#\s*(\d+\s*=\s*)?([A-Za-z_]+\.\d+|\d{3,})\s*(#.*)?$')


def defined_events():
    ids = set()
    for path in pdx.files(ROOT, 'events'):
        text, _ = pdx.read(path)
        ns = re.findall(r'^\s*namespace\s*=\s*(\S+)', text, re.M)
        for m in re.finditer(r'^\s*id\s*=\s*([A-Za-z_]+\.\d+|\d+)', text, re.M):
            ids.add(m.group(1))
    return ids


def main():
    events = defined_events()
    errors, warns = [], []
    where = defaultdict(list)
    for path in pdx.files(ROOT, 'common/on_actions'):
        rel = os.path.relpath(path, ROOT)
        text, enc = pdx.read(path)
        if enc.startswith('utf-8'):
            errors.append('%s: saved as %s, CK2 reads cp1252' % (rel, enc))
        for n, line in enumerate(text.split('\n'), 1):
            if DEAD.match(line):
                warns.append('%s:%d commented-out entry: %s' % (rel, n, line.strip()))
        entries, braces = pdx.parse(text)
        if braces:
            errors.append('%s: %d unbalanced braces' % (rel, braces))
        for name, op, block, line in entries:
            if not isinstance(block, list):
                continue
            where[name].append('%s:%d' % (rel, line))
            if name not in KNOWN:
                errors.append('%s:%d unknown on_action %s' % (rel, line, name))
            for key, _, lst, l2 in block:
                if key == 'events' and isinstance(lst, list):
                    ids = [v for k, o, v, l in lst]
                    for eid, c in Counter(ids).items():
                        if c > 1:
                            warns.append('%s:%d %s lists %s %d times' % (rel, l2, name, eid, c))
                    for k, o, v, l in lst:
                        if v not in events:
                            errors.append('%s:%d %s fires missing event %s' % (rel, l, name, v))
                elif key == 'random_events' and isinstance(lst, list):
                    top = []
                    for k, o, v, l in lst:
                        if isinstance(v, list):
                            sub = [(kk, vv, ll) for kk, oo, vv, ll in v if kk != 'delay']
                            if name in PULSES and not any(vv == '0' for kk, vv, ll in sub):
                                warns.append('%s:%d %s sub-list %s has no 0 entry' % (rel, l, name, k))
                            for kk, vv, ll in sub:
                                if vv != '0' and vv not in events:
                                    errors.append('%s:%d %s fires missing event %s' % (rel, ll, name, vv))
                            for eid, c in Counter(vv for kk, vv, ll in sub if vv != '0').items():
                                if c > 1:
                                    warns.append('%s:%d %s sub-list %s lists %s %d times' % (rel, l, name, k, eid, c))
                        else:
                            top.append(v)
                            if v != '0' and v not in events:
                                errors.append('%s:%d %s fires missing event %s' % (rel, l, name, v))
                    for eid, c in Counter(v for v in top if v != '0').items():
                        if c > 1:
                            warns.append('%s:%d %s random_events lists %s %d times' % (rel, l2, name, eid, c))
    for name, places in sorted(where.items()):
        if len(places) > 1:
            warns.append('%s is written %d times: %s' % (name, len(places), ', '.join(places)))
    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN ', w)
    print('on_actions: %d in use, ERROR %d, WARN %d' % (len(where), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
