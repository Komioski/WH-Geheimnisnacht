"""Faction map used to attribute events to a primary faction.

Each faction lists the culture groups (cg:), religions (r:), religion groups
(rg:) and creature traits (tr:) that identify it. An event that references
1-3 factions in its pre-triggers or trigger is attributed to the most
referenced one. Edit this file when cultures or religions are added.
"""

FACTIONS = {
    'Empire': ['cg:imperial_group', 'r:sigmarite', 'r:ulrican', 'r:taalite',
               'tr:creature_halfling', 'cg:halfling_old_world', 'rg:halfling_gods_group'],
    'Bretonnia': ['cg:bretonnian_group', 'r:grail', 'r:false_grail'],
    'Kislev': ['cg:kislevite_group', 'r:kislev_gods'],
    'Tilea, Estalia & Sartosa': ['cg:tilean_group', 'cg:estalian_group', 'cg:sartosan_group',
                                 'r:myrmidian', 'rg:stromfels_group', 'r:manannite'],
    'Old World faiths': ['rg:old_world_group', 'r:shallyan', 'r:morrian', 'r:old_faith',
                         'r:old_faith_reformed', 'r:northern_gods', 'r:northern_gods_reformed'],
    'Albion & Fimir': ['cg:albion_group', 'cg:fimir_group', 'tr:creature_fimir'],
    'Dwarfs': ['cg:dwarf_group', 'rg:dwarf_gods_group', 'tr:creature_dwarf'],
    'High Elves': ['cg:asur_group', 'r:cadai'],
    'Wood Elves': ['cg:asrai_group', 'cg:forest_group', 'r:asrai_cadai',
                   'tr:creature_forestspirit', 'tr:creature_treekin'],
    'Dark Elves': ['cg:druchii_group', 'rg:cytharai_group', 'r:cult_of_pleasure'],
    'Lizardmen & Amazons': ['cg:lizardman_group', 'cg:amazon_group', 'cg:halfling_lustrian',
                            'rg:old_ones_group', 'tr:creature_skink', 'tr:creature_saurus',
                            'tr:creature_slann', 'tr:creature_amazon'],
    'Greenskins': ['cg:orc_group', 'cg:goblin_group', 'rg:greenskin_gods_group', 'tr:creature_orc',
                   'tr:creature_goblin', 'tr:creature_hobgoblin', 'tr:creature_snotling'],
    'Ogres': ['cg:ogre_group', 'rg:great_maw_group', 'tr:creature_ogre'],
    'Araby & Southlands': ['cg:arabyan_group', 'cg:southlander_group', 'rg:ormazd_gods_group'],
    'Cathay & the East': ['cg:oriental_group', 'rg:oriental_gods_group'],
    'Vampires': ['cg:vampire_group', 'cg:lahmian_group', 'cg:strigany_group', 'r:vampiric',
                 'r:drachen', 'rg:necromantic_group'],
    'Tomb Kings': ['cg:nehekharan_group', 'rg:nehekharan_gods_group', 'tr:creature_nehekharan'],
    'Nagash': ['r:nagashi'],
    'Chaos': ['r:chaos', 'r:khorne', 'r:nurgle', 'r:tzeentch', 'r:slaanesh', 'cg:daemonic_group',
              'cg:kurgan_group', 'cg:hung_group', 'tr:creature_chaosspawn', 'rg:chaos_gods_group'],
    'Norsca': ['cg:norscan_group', 'r:norscan_gods', 'r:norscan_gods_reformed'],
    'Chaos Dwarfs': ['cg:dwarf_chaos_group', 'r:hashut', 'tr:creature_chaos_dwarf'],
    'Beastmen': ['cg:beastman_group', 'tr:creature_beastman'],
    'Skaven': ['cg:skaven_group', 'rg:horned_rat_god_group', 'tr:creature_skaven'],
}

# Paradox (vanilla) namespaces. Files using them are kept close to vanilla.
VANILLA_NAMESPACES = set(
    'CM HF HFP HL JD LT LoR MNM REP RIP RoI SSI SoA TOG WoL ZE COM diploresponse'.split())

KEY_TO_FACTIONS = {}
for _name, _keys in FACTIONS.items():
    for _key in _keys:
        KEY_TO_FACTIONS.setdefault(_key, set()).add(_name)
KEY_TO_FACTIONS['rg:cadai_group'] = {'High Elves', 'Wood Elves'}


def factions_of(refs):
    """refs: Counter of keys like 'cg:skaven_group'. Returns Counter faction -> weight."""
    from collections import Counter
    out = Counter()
    for key, count in refs.items():
        for name in KEY_TO_FACTIONS.get(key, ()):
            out[name] += count
    return out
