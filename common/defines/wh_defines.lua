NDefines.NEconomy.DOGE_SUCC_RANDOM_FACTOR = 100									-- 500 The random Respect factor on actual Doge succession.
NDefines.NEconomy.PATRICIAN_CAMPAIGN_FUND_FACTOR = 2									-- 5 The effect of money in the Campaign Fund on Doge elections (money * factor).
NDefines.NEconomy.PATRICIAN_PRESTIGE_RESPECT_FACTOR = 5									-- 2 The effect of Prestige on the Respect value for Doge elections (prestige * factor).
NDefines.NEconomy.PATRICIAN_AGE_RESPECT_FACTOR = 0.3									-- 1 The effect of Age on the Respect value for Doge elections (age * age * factor).

NDefines.NEconomy.WONDER_STACKING_PENALTY = 0					-- Additional cost for each consecutive wonder construction
NDefines.NEconomy.WONDER_STACKING_PENALTY_SAME_TYPE = 0				-- Extra penalty for construction wonders of the same type

NDefines.NCharacter.FERTILITY_BASE_MULT = 0.30
NDefines.NCharacter.SECONDARY_SPOUSE_FERTILITY_MULT = 0.20
NDefines.NEngine.EVENT_PROCESS_OFFSET = 20
NDefines.NEngine.COURTIER_EVENT_PROCESS_OFFSET = 100

NDefines.NDiplomacy.DEFENSIVE_PACT_THREAT_LIMIT = 0.05							-- The amount of provinces in a realm that is needed for beeing a valid target of a defensive pact
NDefines.NDiplomacy.DEFENSIVE_PACT_SIZE_RATIO = 1.0							-- Relative size requirement is this at 100% threat
NDefines.NDiplomacy.DEFENSIVE_PACT_MAX_RANGE = 200								-- At 100% threat characters are able to join defensive pacts against targets of this distance
NDefines.NDiplomacy.DEFENSIVE_PACT_MAX_RANGE_SAME_GROUP = 100					-- At 100% threat characters are able to join defensive pacts against targets of this distance
NDefines.NDiplomacy.DEFENSIVE_PACT_THREAT_SIZE_START = 0.0						-- Relative size requirement starts from this level of threat
NDefines.NDiplomacy.DEFENSIVE_PACT_BASE_SIZE = 0.0								-- This is the base size requirement at 0% threat
NDefines.NDiplomacy.MAX_INFAMY_GAIN = 15										-- This is the max infamy gained from a single source
NDefines.NDiplomacy.EVERY_DEFENSIVE_PACT_JOIN_THREAT = 100 				-- If threat is this high, members of all defensive pacts against a target will join
NDefines.NDiplomacy.EVERY_DEFENSIVE_PACT_EXCEPT_HEADS_JOIN_THREAT = 100	-- If threat is this high, members of all defensive pacts against a target will join, except religious heads that only joins when their own group is attacked
NDefines.NDiplomacy.OTHER_DEFENSIVE_PACT_JOIN_THREAT = 100					-- If threat is this high, other religious groups band together when attacked, if it's lower every defensive pact acts on it's own

NDefines.NDiplomacy.SHORT_REIGN_YEARS_END = 8
NDefines.NDiplomacy.LONG_REIGN_YEARS_START = 9
NDefines.NDiplomacy.MAX_LONG_REIGN_BONUS = 50
NDefines.NDiplomacy.SHORT_REIGN_OPINION_MULT = 1.5
NDefines.NDiplomacy.LONG_REIGN_PENALTY = -2
NDefines.NDiplomacy.LONG_REIGN_OPINION_MULT = 0.4
NDefines.NDiplomacy.PRESTIGE_OPINION_DIV = 100
NDefines.NDiplomacy.PRESTIGE_OPINION_MAX = 20
NDefines.NDiplomacy.PIETY_OPINION_DIV = 25
NDefines.NDiplomacy.PIETY_OPINION_MAX = 20

NDefines.NDiplomacy.MAX_PREP_INV_TARGET_HOLDINGS = 100
NDefines.NDiplomacy.MAX_PREP_INV_ATTACKER_HOLDINGS = 100
NDefines.NDiplomacy.JAIN_LIEGE_OPINION_BONUS = 30
NDefines.NDiplomacy.MAX_DIPLO_DISTANCE = 1000
NDefines.NDiplomacy.IMPRISON_CHARACTER_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.IMPRISON_CHARACTER_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.EXECUTE_IMPRISONED_INTERACTION_ENABLED = 10
NDefines.NDiplomacy.RETIRE_TO_MONASTERY_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.RETIRE_TO_MONASTERY_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.DEMAND_RELIGIOUS_CONVERSION_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.DEMAND_RELIGIOUS_CONVERSION_INTERACTION_THRESHOLD_FOR_YES =  10
NDefines.NDiplomacy.DEMAND_RELIGIOUS_CONVERSION_INTERACTION_ENABLED = 0
NDefines.NDiplomacy.INVITE_TO_COURT_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.INVITE_TO_COURT_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.OFFER_VASSALIZATION_INTERACTION_THRESHOLD_FOR_NO = 20
NDefines.NDiplomacy.OFFER_VASSALIZATION_INTERACTION_THRESHOLD_FOR_YES = 20
NDefines.NDiplomacy.ASK_FOR_VASSALIZATION_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.ASK_FOR_VASSALIZATION_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.ARRANGE_BETROTHAL_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.ARRANGE_BETROTHAL_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.OFFER_SUCCESSION_MARRIGE_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.OFFER_SUCCESSION_MARRIGE_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.OFFER_MARRIGE_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.OFFER_MARRIGE_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.RANSOM_CHARACTER_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.RANSOM_CHARACTER_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.EDUCATE_CHARACTER_INTERACTION_THRESHOLD_FOR_NO = 0
NDefines.NDiplomacy.EDUCATE_CHARACTER_INTERACTION_THRESHOLD_FOR_YES = 0
NDefines.NDiplomacy.ABANDON_AMBITION_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.ABANDON_AMBITION_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.JOIN_AMBITION_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.JOIN_AMBITION_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.SETTLE_ADVENTURER_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.SETTLE_ADVENTURER_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.DIVORCE_INTERACTION_THRESHOLD_FOR_NO = 35
NDefines.NDiplomacy.DIVORCE_INTERACTION_THRESHOLD_FOR_YES = 75
NDefines.NDiplomacy.ASK_TO_RANSOM_CHARACTER_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.ASK_TO_RANSOM_CHARACTER_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.ASK_TO_JOIN_WAR_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.ASK_TO_JOIN_WAR_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.ASK_TO_EMBARGO_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.ASK_TO_EMBARGO_INTERACTION_THRESHOLD_FOR_YES = 10
NDefines.NDiplomacy.MAKE_CONSORT_INTERACTION_THRESHOLD_FOR_NO = 10
NDefines.NDiplomacy.MAKE_CONSORT_INTERACTION_THRESHOLD_FOR_YES = 10

NDefines.NCharacter.MAX_CHILD_BIRTH_AGE = 3000
NDefines.NCharacter.MALE_ATTRACTION_CUTOFF = 10000
NDefines.NCharacter.FEMALE_ATTRACTION_CUTOFF = 10000

NDefines.NTitle.DE_JURE_ASSIMILATION_YEARS = 750
NDefines.NTitle.EMPIRE_DE_JURE_ASSIMILATION_YEARS = 750

NDefines.NReligion.ELECTOR_TITLE_AGE_FACTOR = 0.5

NDefines.NEconomy.PATRICIAN_AGE_RESPECT_FACTOR = 0				-- The effect of Age on the Respect value for Doge elections (age * age * factor)
NDefines.NNomad.ALWAYS_GENERATE_NOMADS = 1

NDefines.NMilitary.LEVY_MAINTENANCE_FACTOR = 1.0
NDefines.NMilitary.PAGAN_HOME_SUPPLY_MOD = 0.25					-- Non Pagans suffer extreme attrition in some Pagan homelands (based on province religion)
NDefines.NMilitary.COMMAND_MODIFIER_MARTIAL_MULTIPLIER = 0.02	  -- How much positive command modifiers are increased, and negative modifiers decreased (capped to 100% for negative), per point of martial
NDefines.NMilitary.TERRAIN_SPEC_BONUS = 0.1						-- Bonus to fighting in this terrain if you have that terrain as your

NDefines.NTechnology.PAGAN_HOME_ATTRITION_REMOVAL_LEVEL = 7.0
NDefines.NTechnology.DONT_EXECUTE_TECH_BEFORE = 2000
NDefines.NTechnology.IDEAL_YEAR_LEVEL_0 = 2000
NDefines.NTechnology.IDEAL_YEAR_LEVEL_1 = 2050
NDefines.NTechnology.IDEAL_YEAR_LEVEL_2 = 2100
NDefines.NTechnology.IDEAL_YEAR_LEVEL_3 = 2200
NDefines.NTechnology.IDEAL_YEAR_LEVEL_4 = 2250
NDefines.NTechnology.IDEAL_YEAR_LEVEL_5 = 2300
NDefines.NTechnology.IDEAL_YEAR_LEVEL_6 = 2400
NDefines.NTechnology.IDEAL_YEAR_LEVEL_7 = 2450
NDefines.NTechnology.IDEAL_YEAR_LEVEL_8 = 2500
NDefines.NTechnology.IDEAL_YEAR_AHEAD_PENALTY_INVEST = 0.35

NDefines.NEngine.MISSING_SCRIPTED_SUCCESSOR_ERROR_CUTOFF_YEAR = 2010
NDefines.NEngine.MISSING_SCRIPTED_SUCCESSOR_ERROR_CUTOFF_MONTH = 1
NDefines.NEngine.MISSING_SCRIPTED_SUCCESSOR_ERROR_CUTOFF_DAY = 1

NDefines.NAI.AI_EMPEROR_CREATES_KINGDOMS = 1

NDefines.NAI.RAID_AGGRESSION = 12

NDefines.NFrontend.CAMERA_LOOKAT_X = 2200.0
NDefines.NFrontend.CAMERA_START_X = 2200.0
NDefines.NFrontend.CAMERA_END_X = 2200.0
NDefines.NFrontend.FRONTEND_POS_X = 2200.0
NDefines.NFrontend.FRONTEND_POS_Y = 1000.0
NDefines.NFrontend.FRONTEND_POS_Z = 200.0
NDefines.NFrontend.FRONTEND_LOOK_X = 2200.0
NDefines.NFrontend.SETTINGS_POS_X = 2200.0
NDefines.NFrontend.MP_OPTIONS_POS_X = 1360.0
NDefines.NFrontend.MP_OPTIONS_LOOK_X = 1490.0
NDefines.NFrontend.TUTORIAL_POS_X = 1600

NDefines.NEndGame.DYN1_ID = 10047
NDefines.NEndGame.DYN2_ID = 19000
NDefines.NEndGame.DYN3_ID = 23001
NDefines.NEndGame.DYN4_ID = 11000
NDefines.NEndGame.DYN5_ID = 31005
NDefines.NEndGame.DYN6_ID = 13003
NDefines.NEndGame.DYN7_ID = 16000
NDefines.NEndGame.DYN8_ID = 10000
NDefines.NEndGame.DYN9_ID = 12000
NDefines.NEndGame.DYN10_ID = 23006
NDefines.NEndGame.DYN11_ID = 14003
NDefines.NEndGame.DYN12_ID = 20082
NDefines.NEndGame.DYN13_ID = 19003
NDefines.NEndGame.DYN14_ID = 79085
NDefines.NEndGame.DYN15_ID = 14018

NDefines.NRulerDesigner.MAX_AGE = 500
