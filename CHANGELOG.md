------------------------------------------------------

                WH: Geheminisnacht
                    CHANGELOG

------------------------------------------------------
CURRENT CHECKSUM
------------------------------------------------------
    ||  PUBLIC RELEASE = HLCN ||
------------------------------------------------------
TABLE OF CONTENTS
------------------------------------------------------
> CURRENT CHECKSUM
> TABLE OF CONTENTS
> CHANGELOG HISTORY
    - v1.4.1    - [PLANNED] Pirates, Adventurers, Colonies
    - v1.4.0    - [PLANNED] Performance Rebuild
    - v1.3.7    >> CURRENT
    - v1.3.6
    - v1.3.51
    - v1.3.5    - A Cold Tyrant
    - v1.3.42
    - v1.3.41
    - v1.3.4    - Winds of Magic
    - v1.3.3
    - v1.3.2
    - v1.3.1
    - v1.3.0    - Chaos In The Old World
    - v1.2.9
    - v1.2.8
    - v1.2.7
    - v1.2.6
    - v1.2.5
    - v1.2.4
    - v1.2.3
    - v1.2.2    - Ruinous Powers
    - v1.1.6
    - v1.1.5
    - v1.1.3    - Vampire Wars
    - v1.0.1
    - v1.0.0    - Legacy Release
> RELEVANT CHANGES BEFORE LEGACY
------------------------------------------------------
v1.3.7:   <<< CURRENT RELEASE
------------------------------------------------------
- Changed some on_action events to be in custom random lists to ensure factions are recieving relevant events
- Reworked Ulthuan depopulation to be a simpler system and less taxing on the engine
- Tweaked learning magic as an Asur apprentice at Hoeth
- Changed some MTTH asur events to on_actions
- removed extra namespaces for asur events
- Documented/optimized wh_asur_events
- Removed duplicate pregnancy event chains, these were added in vanilla
- Cleaned up learning magic somewhat
- Cleaned up teaching yourself magic somewhat
- Fixed antideath effect for Chaos Dawi Sorcerors
- Updated the borrow/donate money to holy order decisions
- Fixed the Shallya Self Sacrifice society power
- Lowered the cost of the Shallya self sacrifice to 8000
- Wearing armor (Artifact) now lowers your battle magic pool unless it has the armored caster flag
- Made some adjustments to Witch Hunter decisions
- Witch Hunters check to denounce liege doubled from 2 years to 4
- Made adjustments and cleanup to the mount market and training mounts
- Changes to Ekrund under Karak Ankor
- Added ambition for Skaven to become a Grey Lord
- Refined the Become Chaos Dawi Sorcerer ambition
- Fixed Loot Province Society Mission
- Adjusted papal AI behavior to account for Witch Hunters and Templars
- Fixed Hobgoblin/Goblin Localisation
- Ulthuan will no longer view Athel Loren as a Colony but you can still aid them in their wars (player only)
- Small changes to Antoch start up war events
- Fixed the Antoch war firing again when loading a save and meeting the requirements
- Cleaned a stray pixel off the 4th Dawi government icon
- Added the icon GFX for the new Dawi government
- Localized Shadow Warriors
- Should now ONLY be able to turn humans into vampires
- Fixed Ekrund History Typo
- Fixed vampire_hunter trait
- Buffed vampire_hunter trait
- The death of the Everchosen should now reset the Doom Counter
- Shallya Self Sacrifice now resets doom counter instead of just lowering it
- Slight changes to DOOM effects and scaling
- Fixed Stegadon animation file names
- event CC.10030: picture = GFX_evt_Comet changed to GFX_evt_comet (lowercase)
- Defined Stromfels group opinion modifier
- Added or fixed event pictures for many, many events
- Event druchii.2 now uses MTTH instead of weight_multiplier
- Fixed a serious event duplication issue between the hashishin and mariner societies
- Fixed many event duplications
- Commented out certain non-existant events from on_actions
- Fixed some incorrect bloodline modifiers
- First pass through HF_warrior_lodge_feast_events.txt
- Doom should now properly be reset to when winning against black crusades
- More event GFX fixes
- Localization additions
- Lizardmen spiritual jobs reference events 164900 and 164902 which dont exist, so I commented them out
- Fixed some bloodline modifiers
- Commented out more non-existent events from on_actions
- Drachen religion has now been given holy-sites (not having enough or having too many holy sites can cause crashes)
- Fixed inconsistencies with Geg of Wainfleet, the peasant Knight dynasty (now its properly none)
- Waldo is now sigmarite (sorry, lol, the games not happy about him not having a religion)
- Generated empty history files for all of the wasteland province
- Fixed unborn title holders so that they would at least be 0 years old upon inhereting titles
- Removed non-existant title holders from title history
- Changed some lore thing that DeadliestIncome asked for, relating to Gardevoir Galand
- Changed these files who where on UTF-8 to ANSI(Windows-1252)
    > nb_naval_events.csv
    > beastmen_nomad.csv
    > offmap_powers.csv
    > ulricanadditions.csv
    > wh_ToS_localisation.csv
    > 000_breto_mer_name.csv
    > 00_cultural_titles.csv
    > 00_marriage_correction.csv
    > 00_religious_titles.csv
    > wh_ToS_localisation.csv
- moved the contents of 00_comanders.csv to 00_cultural titles
- Removed warpstone health malus for now due to skaven mass dying from it
- Added kharan_the_blighted_bloodline for Kharan who invaded Bretonnia
- Created a dynasty for kharan
- Added nickname for Kharan "the Blight"
- Changes to consorts in amazonia
- rework of the pet consort trait
- DR_Pirate_events should now be correct
- Added a bit of piety to the elector counts
- fixed missing namespace for darkelfmagic events
- Fixed the one legged, eyed, one handed for DR_pirate_events.txt
- Removed monthly wealth for peasant traits.
- Buffed holy orders a bit
- Witch Hunters were supposed to get 4 ducats a month, but only got like 0.2. Since apparently monthly_income transferred to yearly income on titles just because. Fixed.
- hobgoblin_nomadic vassals are now callable
- Added peasant "Gen Waifield" as an knight
- You can no longer dejure claim and tribute cbs on the witch hunters without expelling them first.
- Fixed wrong scripted trigger for warrior lodges
- Limited Grail Shrines to characters with the Grail religion or Top Liege with the Grail religion
- Changed Olricstaad building location from "b_kirkja_hiti" to "b_olricfjord"
- Added Skaven city buildings "Warpstone Generator" and "Laboratory"
- Changed several Norscan Dynasty names to match lore
- Added government flavour entries for many of the new governments including 3 tiers for the Eonir government and 2 tiers for the myrmidian governments
- Fixed the Hobgoblin charframe switrching bug
- Added cultural name swaps for titles in the southlands for cathayan and jade vampire cultures
- Made several changes to landed titles set up history at start
- Added a few titular titles "d_skulltakers" "c_skulltakers" and "e_realm_horned_one"
- Eldership succession unlocked for tilea/estalia/myrmidia governments
- Skulltakers added to military elective succession
- Added the groundwork for the Horned Rat offmap power
- offmap_currency for the Skaven offmap labled "monthly_warpstone_tokens" or "warpstone_tokens"
- Cleaned up on_Action entry for ARMS.2 # Standard Found event
- Delayed the stillborn birth fix by 1 day to allow racial traits to correct themselves
- Fixed RETTYPE_CUL_EONIR2 active block and modifier
- Some Skaven traits now apply "monthly_warpstone_tokens"
- Added a "Royal Trading Hall" wonder upgrade for Marienburg
- First draft of new Norscan wonder added "wonder_norse_heorot"
- Added a trigger_if block and made some minor changes to the "claim_high_kingship" decision for dawi
- Cleaned up references to vanilla in "culture_conversion_events"
- Lots of clean-up and some rewrites to the dwarf reunification events and voting system
- Simplified council job calculation code based on skill to use set triggers "job_event_mtth_modifier_diplomacy_score" etc.
- Some clean up and expansion to the alliance scripts for The Empire
- Small fixes to region code in the hunting events file
- Province 1914 is no longer a major river #Halkildfjord
- Added 3 new provinces for a total of 2445
- Renamed "Halkildfjord" to "IceDrake Fjord"
- Updated regions in the map files to reflect recent additions and changes to Norsca and the Underempire
- Province border changes in Norsca
- Lots of History changes for characters in Norsca
- fixed all cases of "ï¿½" in the localisation files after the correction of files to ANSI
- Added artifacts.info containing all insformation for balancing and creating new artifacts
- Reworked "03_artifacts_druchii" - added a manifest, organized and balanced
- Adjusted artifact spawns for druchii
- Created system to allocate artifact amounts based on tier (see artifact_spawns.info)
- Split artifact spawns between generic and magic categories for granularity
- Moved all mounts to a separate file in the artifact section unless they are character unique
- Reworked "20_artifacts_mounts" - added a manifest, organized and balanced
- All mounts now have stacking = no checks
- Fixed some artifacts not applying to slots
- Some mounts will also get a combat rating matching the artifact tier, alternatively they may get days_of_supply for pack animals
- All mounts should now be integrated into the AI check system that forces them to switch to the best mount in their treasury
- Added a new slot for artifacts, limiting the number of familiars equipped to 2 at a time
- All Dwarfs can now use runes and master runes not just runesmiths and runelords, the latter two types of dwarf are the only ones who can create runes however
- The great book of grudges is now a tome slot not a library slot
- Added a trinket slot to limit the modifier creep from random artifacts in your treasury
- Merged Kislev, Bretonnia, Empire artifacts into "20_artifacts_mortal_realms" - added a manifest, organized and balanced
- Reworked "11_artifacts_dwarfs" - added a manifest, organized and balanced
- Merged event "aicleanup.033" which destroys cursed artifacts on death into event "55520" which destroys no_inherit artifacts on death
- Reworked "09_artifacts_lizardmen" - added a manifest, organized and balanced
- Reformatted history/technology
- Reformatted half of history/titles (need to do duchy, count, empire files)
- Added names to the offmap powers missing them in history/offmap_powers
- Reformatted history/characters/1000_albion added a manifest, re-ID characters from 1000 range to 100 range
- Reformatted history/characters/2000_halfling_mootlander added a manifest, re-ID characters from 2000 ( was 5200 for some reason ) range to 200 range
- Reformatted history/characters/3000_halfling_miyan added a manifest, re-ID characters from 3000 ( was 5100 for some reason ) range to 300 range
- Shifted character age and name on the GUI so they dont overlap in extreme cases
- Reformatted history/characters/4000_amazon added a manifest, re-ID characters from 4000 range to 400 range
- Landed more Amazon rulers amongst the existing holdings, added some consorts and magic users to a few courts
- Reformatted history/characters/ruinous_powers added a manifest, cleaned up character code
- Added add_twenty_five_duel_experience_modifier to allow history files to quickly power characters without using a lot of the add_ten_duel_experience_modifier
- Allowed Slaan to be commanders
- Reworked title_commander "allowed_to_hold" for readability and allowed ogres to be commanders for other races
- Reformatted history/characters/5000_ogres added a manifest, re-ID characters from 5000 range to 500 range
- Added 15 Ogre mercenaries to various courts in the old world and beyond
- Restored "Sha'shala" as the ruler of the Lustrian Cathayan enclave
- Moved and made some minor adjustments to the easter egg character that replaced her
- Reformatted history/characters/5400_oriental added a manifest, re-ID characters from 5400 range to 600 range
- Lowered the cost of becoming chosen, champion and prince for AI
- Marriage system tweaks to fix bugs and performance
- Sylvanian oldage pointing to wrong gfx fixed
- A fix for Ruler Designer crashes when selecting certain cultures
- Fix for unlanded Patrician offmap chaos interactions
- Interracial marriage now works if turned on
- Introduced beastmen interspecies marriage pruning to slow them breeding out the chaos wastes
- Added some piety requiremets for the anti-magic war
- Fixed stacking of opinion_spared_witch
- Magic law fixes
- pleasure_twist disabled for use on the everqueen and everqueen heir
- Added has_impious_trait_trigger to make it a bit more limited in its usage
- Igor should no longer go negative in prestige
- Kraka hyfol now has the right culture
- Fixed Dustpaq positions
- Deleted some old code related to stealing and gifting artifacts as they were ancient and redundant
- stromfels_group allowed access to the slavery system
- Fixed numerous instances of "old_gods_group" which should actually reference "northern_gods"
- Allowed "stromfels_group" to purchase armaments from the Dawi Zharr
- Extra scripting added to norscan events and enabled some old events for northern god conversion after updating code
- Restructured the slavery system, streamlined the variables. Retained some depth and while promoting balance
- Deployed slaves now raises local revolt risk
- Deployed slaves no longer lower build time (costs less not faster)
- The bonus to vassal_opinion for "succ_bretonnia_elective" changed to feudal_opinion
- Nurgle now likes the trusting trait
- Slightly reworked "Duel_effect" as part of Everchosen quest fix
- Reworked opinion_modifiers for the "knights_of_brettonia" society (Was 45+ now closer to 15+)
- Impaler, Wroth, and Cruel are now negative instead of positive traits for the "knights_of_brettonia" society
- Fixed the bug where you could invite members to you cult who had already joined
- Added some easter egg code for the "Egg of Quango"
- Ice witches removed from mage ward teaching system for now as its handled through the society
- Added easter egg code for the Winter Equinox for norscan_gods
- AI excluded from some warrior lodge missions
- Bloodthirsty Gods: The Mass Sacrifice re-enabled for Khornate followers
- Event CC.1 added to properly clear known cultist flags
- Fixed the Everchosen event chain
- Fixed Harskamp start culture and religion
- magic_power modifiers removed from Magic Offmap GUI trigger as they are mostly redundant and can cause some bugs
- Repaired Isabella von Carstein generic vampire bug
- Expanded the remove_race_trait_effect to include goblin and orc size traits
- create_[daemon]_effect changed slightly to use remove_race_trait_effect to eradicate edge cases
- Feudal dawi bug fixed
- Should have fixed the society grandmaster power to summon disciples
- Added beastman_government to has_tribal_or_nomadic_government_trigger
- Champion decisions on the undivided offmap have all been fixed
- Fixed localisation error for the mark of tzeentch for undivided
- Undivided offmap favour now resets upon death
- Conversion to vampire triggers now properly clear chaos offmap favour
- Removed potential blocks from bloodthirsty gods traits so they should no longer reset when you reload the game
- Reworked the Cleanse Greenskin decision to show no upfront cost since its scaled wealth based on location, and removed pretige cost to back out from the decision
- Slightly reworked success chance and cost calculation for cleanse greenskin decision
- Overhauled Druchii Building Lists, Each culture gets a unique version of a building tree, Tribals got some love with expanded lists, exceptions made for the easter egg Tzeentch Druchii
    Special Units
    > Castles - War Beasts
    > Cities - Chariots
    > Temples - Magic Spells
- Changed just a few tribal cultures for the druchii
- Modified how cold ones vs dark riders potential for druchii
- Adjusted math for norsca.1-5 events, moved them to a decade pulse and limited them slightly
- Adjusted math for norsca.1 and moved to a longer pulse
- Adjusted the weak heir collapse in Norsca to only fire for demense sizes larger than 2
- Adjusted math for norsca.1-5 events to only fire for norscan_gods
- Norscan Tribal Gov now only gives +1 concubine instead of +5
- Grail society fixed to allow all members as long as they are
    > religion = grail
    > trait = noble
    > is_adult = yes
    > is_female = no
- Fixed Bretonnian Trebuchet stats
- Fixed commander requirements for orcs and goblins
- Updated family palace requirements to create a slaver post
- Excluded creature goblins from the marriage system
- small fixes to characters using the anti death system
- exterminating greenskins in world_troll_region now changes culture to ropsmann instead of kislevite
- Fixed bug: gaining stats when hiring goblin courtiers
- Chaos court can now call vassals to arms.
- Becoming daemon prince of khorne now requires the correct offmap value.
- You can no longer become a daemon prince of chaos when you are already a daemon prince
- Becoming a champion/chosen/prince of a specific god will now give you their respective religion
- Created few dark elf characers.
- Druchii Sorceresses under malekith should no longer be thrown to agnatic
- Allowed dreuchii to use the court mage mechanics.
 > Male mages living under malekith are of course outlawed.
 > Elves have lower requirement to pass.
 > Elves can become apprentice even when adult. Minimum of 15 learning required when adult.
- Added sisters of twilight icon and trait
- Added sisters of twilight to the anti death engine
- Added some new hair colors to asrai, asur, druchhii chaos dwarves, kurgans, tileans, estalians and the amazons
- Changed the culture modifier of the asrai to me more distinct from the asur
- DNA changes to the sisters of twilight so that their appearance is closer to lore
- Added some modifiers to the Oak of Ages
- Fixed Ogre trait localisation
- Added Orion and Ariel to the immortal engine
- Adjusted static modifiers, added forest and jungle terrain modifier
- Adjusted asrai retinues
- Added a truce to Bretonnia at game start
- Greenskin extermination ai weight changes
- Nomadic governmant changes
    > Severe crash fixes:
        - game does not support changing nomadic governments (order to chaos and vice verca)
        - If an heir is in a different religion group than the father it chanegs the heir to the rulers religion
- Trading decisions issue fixed
- Fixed Replublics so they are playable again
- Seperated world_troll_country from kislev and norsca regions, since it causes ai to gain -100 IQ (on top of their zero IQ) and destory their armies marching in to Norsca
- Added a cb to kill skaven surface realms
- Buffed imperial wonders a bit since ai is still struggeling against local threats until we can implement overhaul
- Temporarily removed the wonder from the oak of ages
- Cleaned up the tooltip for the unique Herdstone buildings for beastmen
- Overhauled the custom map mode module, the third section is now entirely dedicated to warhammer specific map modes as intended:
    > Places of Power are tied to the corresponding gameplay element, this allows you to see them and their respective game states visually
    > Ulthuan Depopulation is tied to the corresponding province variables allowing you to visualize their impact (especially useful when planning invasions as the Druchii)
    > Corruption allows you to track the location of warpdust traces, warpstone meteors, and warpstone veins. As well as visualize the impact of vampiric corruption as necromancers cast spells and raise the dead
    > Lustrian Jungle is tied to the corresponding province variables allowing you to visualize their impact (especially useful when planning invasions as a colony or defending the temples as Lizardmen)
    > Beastmen Presence shows you the location of herdstones, scattered beastmen, beastmen unrest, and the various levels of beastmen scourging
    > Greenskin Presence shows you the location of scattered greenskins, and the various levels of greenskin population
- Added the first pass of one of our more important game systems: Places of Power
    These represent the leylines, ogham stones, cruxes, and all other symbolic or magically connected places across the world.
    These locations passively affect the Doom Counter and should tie into players mid/long term goals
    For now only the core regions of the Old World have been implemented as well as some of the Wastes as we work to dial in the math and the performance impact of locations
    There are several stages for places of power: Active, Inactive, Corrupt, Drained
    > Active places of power drain points directly from the doom counter
    > Inactive places of power have no effect
    > Corrupt places of power contribute points directly to the doom counter
    > Drained places of power have been rendered temporarily inactive for an alternative effect
    Places of power can be corrupted or restored as long as you meet several qualifications and the location is under your control
    For now the ability to drain them has been disabled until the next round of events are added and we add the Lizardmen Places of Power
    (meditate_pop_order, meditate_pop_corrupt)
- Merged aicleanup.013 which sets dwarfs old age GFX with aicleanup.007 which distributes old age traits
- All characters given the old age trait will now get the infertile trait
- Cleaned up localization for the Doom level notifier so it fits in the message box
- Added missing terrain types to prosperity engine
- Changed fatandira to be of Arabyan origin
- Changed fatandira to be of shallyan religion
- First pass adding shallyan retinues
- Border princes have much more flexibility when it comes to succession laws
- Added a morrian ruler to the border princes
- Increased AI weight for daemon prince clickers.
- Some minor changes to Doom Counter math and events
- Doom notifier is now a decade pulse instead of every 5 years
- Overhaul of several maintenance and set up events including:
    > aiclean.1			# Event changes religion of nomadic heirs if they are from a different religion group on_death
    > aiclean.2			# On Succession event - if holder of Samur's Witch Hunter chapter is not a Witch Hunter, the title disappears.
    > aiclean.3			# on_death to pass Avelorn to the next Everqueen
    > aiclean.4			# Inheritance of Everqueen ping from aiclean.3
    > aiclean.5			# Everqueen/Phoenix King trait lost, bi-yearly pulse
    > aiclean.6			# On_birth, dwarf children should not be old already
    > aiclean.7			# Distribute Old age traits
    > aiclean.8			# Demand Vassal Conversion rework (ROOT is the demander, FROM is the vassal)
    > aiclean.9			# Demand Vassal Conversion rework ping (ROOT is the vassal, FROM is the demander)
    > aiclean.10		# Spell failed event (null event)
    > aiclean.11		# Remove woodwalking event (fired on timer)
    > aiclean.12		# Greenskin Government maintanance
    > aiclean.13		# on_death of Master, free all mage apprentices
    > aiclean.14		# Give the proper age traits to dwarves at start up (perhaps change to long term on action)
    > aiclean.15 		# Special Titles break on the character's death
    > aiclean.16 		# on_death Big Akghan succession, creates a new character and pings aiclean.2 to give titles
    > aiclean.17		# on_death Big Akghan succession or The holder of the university of Martek is always a scholar, creates a new character and pings aiclean.17 to give titles
    > aiclean.18 		# on_adolescence, elves receive the youngling trait, preventing them from wasting themselves in lowborn marriages.
    > aiclean.19 		# After 45, elves lose their youngling traits and can be married off.
    > aiclean.20 		# Court cleansing for Khemri Servants and Skaven Breeders on_ten_years pulse (Bad AI, stop spawning useless stuff - remove when root cause in spawn decisions are fixed)
    > aiclean.21 		# To Check for Mining outpost getting deleted. Fired from 'on_siege_over_winner'. Owner of the winning unit is ROOT. The taken Holding title is in FROM.
    > aiclean.22 		# Ping event from aiclean.21 to Check for Mining outpost getting deleted.
    > aiclean.23 		# Upon title holder change clears crown_law_change title flag triggered by on_new_holder, on_new_holder_inheritance, on_new_holder_usurpation
    > aiclean.24		# Forces bloodline on the same dynasty member, if the bloodline is flagged
    > aiclean.25		# Places of Power Initialization and Mists of Albion
    > aiclean.26		# on_action Event Generates priestess fired from on_new_holder, on_new_holder_inheritance, on_new_holder_usurpation, on_chronicle_start, on_startup
    > aiclean.27		# ping event to set Slaan as Mage Priests on_chronicle_start, on_create_title, on_startup, on_bi_yearly_pulse
    > aiclean.28		# ping event to set Special Corsair Titles on_chronicle_start, on_create_title, on_startup, on_bi_yearly_pulse
    > aiclean.29		# Xen-Huong the dragon emperor of cathay. Grant special titles and cool nickname (fired from character history)
    > aiclean.30 		# Blanket on_chronicle_start Maintenance to Set surface tunnel modifiers for Skaven, Set Religions for secret cults, and Kill male rulers of female held titles
    > aiclean.31 		# Checks for no character trait and applies one if necessary, on_startup, on_employer_change
    > aiclean.32		# Event to rectify religion switchs, with a built in failsafe and log entry (tied to rulerdesigner system)
    > aiclean.33		# Player choice event if human for religion group page 1
    > aiclean.34		# Player choice event if human for religion group page 2
    > aiclean.35		# Specific God choice after religion group choice
    > aiclean.36		# Choose your Vampiric Lineage page 1
    > aiclean.37		# Choose your Vampiric Lineage page 2
    > aiclean.38		# Choose your Vampiric Lineage page 3
    > aiclean.39		# Choose your magic power
    > aiclean.40		# Choose your magic potential
    > aiclean.41		# Random Lore event for player created untrained mages
    > aiclean.42		# on_adulthood Immortal age GFX fix ping
    > aiclean.43		# on_adulthood Immortal age GFX fix effect
    > aiclean.44		# Red Duke's bloodline allocated properly on_chronicle_start
    > aiclean.45		# Apply burnt by flames bloodline
    > aiclean.46		# Apply redeemed by flames bloodline
- Removed the ai racial correction decisions, we may need the redundancy but with testing the blanket event may be enough to keep things in line
- Overhauled, optimized, and documented wh_amazon_events
- Changed code so that only old women get the infertile trait while old age men get a flat fertility malus
- Ice witches dont get the old age trait or infertility (all handled by society)
- Some minor performance changes to amazon events
- Adjusted mutation effects and chances in order to lower mutation frequency
- Primary mutation event based on location changed from a MTTH event to a random on_bi_yearly_pulse event
- Merged the chaos spawn and forsaken on_bi_yearly_pulse events into the primary mutation event
- Removed the chaos gods limitation for Invisible_friend artifact since its tied to the lunacy system
- Overhauled, optimized, and documented wh_mutation_events
- Moved several Lunacy and Mutant Events to on_actions instead of MTTH
- is_fat and is_malnourished now apply -1 health
- added a new death_reason - death_starvation
- Amazon government updated for female only consorts
- Overhauled, optimized, and documented dooming and star sign events then merged into wh_star_signs_event
- Restored pinky and the brain easter egg
- Reformatted history/characters/6000_skaven added a manifest, re-ID characters from 6000 range to 700 range
- bloodline and history fixes for fatandira
- females will not kicked out of the grail society, they still cant join but if they somehow manage to enter they will not get kicked out
- warhammer marriage correction rule removed
- orc county conquest creates more threat
- chaos raid ends inconclusively if the ruler is no longer of chaos religion
- limited the county conquest cb on old world
- halo of maidenly wrath no longer has the requirement you have to be in the grail knight societiy
- removed has global marriage correction options
- Mutation ping event set to five year pulse
- Places of Power balancing
- Fixed pagan_conquest CB
- Added a cost to ulthuan colonisation CB
- history name changes
- Granted Louis his bloodline again
- Fixed goblin/hobgoblin localization swap for creature_trait
- Fixed the immortal suspicions event to only fire for specific religion groups
- Attempt made to correct interspecies breeding loophole using twins
- Bloodlines created when becoming a daemon prince now give general opinion to all members of the chaos gods group instead of solely slaanesh
- Removed permanent winds of albion game rule option
- Game rule options labeled as default to show intended gameplay
- punishment_release_prisoner game rule set to off as default
- diplo_range game rule set to restricted by default
- Fixed the display trigger for the magic system so that it only shows for characters that can actually cast spells
- Some siege events for ormazd and old world group interaction ported from vanilla
- Game rules modified slightly (preparations made to adapt 4th crusade and shephards crusade systems)
- Expanded on the Beastmen custom map mode
- rising_tomb_king modifier changed from a wildly unbalanced 1,000,000% to a much more natural 200%
- snehekharan.2 now also immediately refills nehekharan holding levies when it fires to account for the intention of the original modifier
- Small changes to snehekharan.10 and set it to on_new_holder, on_new_holder_inheritance, on_new_holder_usurpation to restore the malus for non tomb kings
- Minor rebalance to Khemri special buildings, this will be revisited in the Great Works refactor
- Fix Skaven Laboratory building upgrade chain
- Minor bug fixes to some event chains
- crafting_magic_item trait added back for now, its used by the old commissioned crafting system that wasnt ported with the refactored crafting that was a part of the magic system
- Amazons excluded from the "Present Noble" courtier spawning decision
- LOTS of localisation fixes and improvements
- Small changes to snehekharan.10 to fire through the any_realm_province scope. It now fires correctly to give the "Cursed Sands" modifier
- Small balance changes to nehekharan_curse modifier
- Added a "Solomon Kane" easter egg
- Moved Morrian holy site from Bechafen to Carlsbruck
- Changed Essen to a morrian holder as its a stronghold of the knights of morr
- Essen is now a vassal of Lord Voss of Siegfriedhof
- Carlsbruck granted to a new character
- Moved Morrian holy site from Tobaro to Nucca/Monte Negro
- Nucca/Monte Negro changed to morrian religion
- Added a Temple to Nucca/Monte Negro
- Spomanti split to a direct vassal of Remas
- Expanded on the Cult of Morr
    > Split the Knights of Morr and the Order of the Raven
    > The Knights of Morr are stationed in Monte Negro (County of Nucca) and hold the Raven Theatre in Luccini
    > They remain vassals of Remas (may change in the future)
    > The Order of the Raven remains in Siegfriedhof and holds the chapterhouse in Essen
    > They remain independent
    > Technically the Knights of Morr would not use the vampire hunting society as it was designed for The Order of the Raven
    > In the interest of gameplay experience both orders will utilize the society
- Title changes made, The Order of the Raven is now a Playable Holy Order
- Effect added when gaining the title of the Order of the Raven
- Special building added to Monte Negro
- Allowed cathayans to use the Cupbearer minor title
- Set Novazong as "Sha'shala The Grand Generals" Cupbearer and gave him the blood chalice artifact intended for him
- Repaired the Bloodline and Sword "Sha'shala The Grand General" is supposed to start with
- Warp Tear special building adjusted slightly
- removed health malus from malnourished and fat traits
- lowered offmap costs for ai across the board by about 50% since they dont game the system like a Player does
- Kislevites can now restore places of power without any magic laws being active
- Removed training spidermount decision the correct decision is in the mount market now
- Minor CB fixes
- Cost added to elven colonization CB
- Kislev no longer worries about magic laws
- Added checks for the other congenital intelligence traits across the filebase or relied on is_smart_trigger
- Fixed missing is_lunatic_trigger which was causing numerous errors across the game
- Removed a typo from society_clothes.gfx
- Hunt artifact scripted trigger fixed
- Some balancing done on the druchii
    > Lowered culture tech
    > Gave minimum centralisation
    > Lowered demense bonus of the Witch Kingdom government
    > Lowered vassal bonus of the Witch Kingdom government
- Loads more localisation fixes
- Added some more missing localisations in tooltips
- Expanded the vanilla generate families system on game start to work for merchant republics and women!
    > Since our files predate this system warhammer has more female rulers than usual to allow for marriages and because lore
    > This should give their dynasties more longevity and allow merchant families to survive longer than one generation from start
- Cleaned up and merged artifact localisations
- add_warband_champion_trait_effect changed from a trigger to add champion traits for society members
- Scrubbed all references to event RoI.30121
- Empress Magritta admitted to The Morrian Society as according to lore she supported for the order during this time period (temporary measure will expand on this in the near future)
- First pass at overhauling Dawi buildings (Castle and City done just missing Temples)
- Bloodline localisation merges and fixes, and removed references to muslims in the holy war CB
- reinforce_your_company decision for the Brass legion should now properly cost 500 prestige and detract the amount
- Selling Warpstone is now worth 300 gold down fron 400
- Adjusted third party score math to prevent negative costs when selling a mount
- Modified mutation chances (Heavy Nerf)
- Fixed namespace of few mutation events
- More grammar fixes in events
- Merged building localisations into one file
- More misc localisation fixes for tooltips, and removed more vanilla references
- Fixed dawi building localisation
- Removed chance for rulers to be female when spawned as part of the border gore cleanup rule to remove edge cases
- new_character_effect now applies star sign/dooming immediately instead of with a 5 day delay
- Generated family members now fire aiclean.31 which applies character traits, star signs, magic, dooming, and so on immediately
- Adjusted the position of age on the character view gui
- Extended the position of names on the character view gui
- Moved the position of the rename button for children on the character view gui
- All rampaging beasts in lustria should be set to proper portraitGFX and have a creature trait
- Repaired Fimir events to properly allocate class and to apply creature_fimir
- Green knight will now always be a brilliant strategist and is given the creature_human trait
- Replaced all "warrior" traits in tournament events with martial education counterparts which should fix calculations and events
- Adapted Jeanne dArc events ID SoA.5350-SoA.5399 to instead spawn an "avatar of myrmida" since we already have a parallel to real life Jeanne dArc in Brettonia
    > These are not optimized or test and localization is probably off
- Condensed Tooltips for declaring black crusade for legibility
- Fixed trait allocation for fimir intermarriage clean up events
- Made some fixes to the chess with death event
- All 1400 instances of new_character now properly apply creature traits or fire event aiclean.31 which fires new_character_effect
    > Undoubtably a performance loss, as the same effect was fired by on_employer_change on_action already
    > However this should sort some edge cases and the on_action becomes a net for exceptions instead of the primary action
    > The event will only fire if they dont have a creature trait so overall shouldnt be a big difference in performance
- Many minor errors with spawned characters corrected alongside this
- new_character_effect now only has a 5% chance to fire magicpotential.1 and an 8% chance to fire wh_magic_law.40 which determine magic sensitive characters
- Added clear_favour_effect to reset offmap favour
- Zar Tat-Ugek now starts with 1000 nurgle favour
- Azalaïs now starts with 800 tzeentch favour
- Should have finally replaced all instances of the old favour system for chaos
- Final pieces of old doom system converted over
- Settra is now a level 1 wizard and has acess to the lore of nehekhara spells
- Landed Khatep and granted him the Grand Hierophant nickname
- Added a check in the send_strigany_caravan decision and the events themselves to delay the ping a few years if you turn them away
- Khateps start province changed to his culture and religion and changed from tribal to castle
- establish_greenskin_tribe now costs nothing for ai and can be taken during a war. This should help stop empty holding shenanigans with greenskins
- grant_landed_title_waagh can no longer be used on empty holdings to prevent shenanigans, first a tribe must be established
- focus_ch_heritage can now only be taken if your liege is the same religion (intended for culture swaps not religion this is just one change of many coming to this system to close loopholes)
- witch_hunter_rapier artifact no longer locked to just witch hunters for use
- Employed priests, witch hunters, and physicians now apply both ai_flag_refuse_concubinage / ai_flag_refuse_marriage flags to prevent edge cases
- Should have fixed the cost of corrupting places of power
- Added a custom tooltip for owning a dark crystal to the cathayan jade dragon decisions (it seems artifacts cause same tooltip fuckery as scripted triggers etc.)
- Small position changes (still plan to hit entire map these are just smaller bugs)
- All places of power decisions should now detract piety from decision taker not province holder
- Added terrain = impassable_mountains to wonder_dawi_karak build potential
- healing_effect used in spells and potions now heals blinded and eunuch traits
- Throgg is now infertile
- Warhammer star signs now use { has_religion_feature = religion_astrology } allowing reformed religions access to them as well
- has_any_astrology_trait_trigger now uses warhammer star signs instead of zodiac
- Allowed witch hunters to use the employ chancellor decision
- Fixed all existing errors in trait validation
- Fixed all existing errors in retinue validation
- Empire/Sudenburg artillery/gunpowder retinues will upgrade automatically at higher tech levels
- Replaced Vanilla City Fortifications building with a Sartosan equivalent
- beastman_herdstone_offering is now useable if you have the herdstone modifier OR building
- Loosened the offmap brayherd requirements so you no longer have to be in diplo range to use them
- Allowed non-zealous atruhayid player characters to join the has_assassins_prerequisites trigger
- Removed all remaining references to the gender game rule
- Allowed the several minor titles from jade dragon to be used by members of the draconite religion (cathayan/jade vamps)
- Added 11 Ogre Mercenary Companies, bringing the count at game start to 16 since they can be hired across the old world
- Adjusted Ogre Mercenary sizes
- Varied Ogre mercenaries to use all 3 primary cultures firegut, irongut, and ogre main
- Enabled and converted event chain JD.1000 a five year pulse event finding Ormazd Adventurers to target Estalia/Tilea
    > This should interact with the converted reconquista system allowing for some more back and forth between the three world regions
- Added a missing check for magic_law_3 in the has_magic_law_1_or_above_trigger scripted trigger
- Removed potential from berserker, reaver, ravager, seaking, sea_queen and pirate
- Some cb bug fixes
- Removed defensive attrition from spider gobbos
- Should have fixed the scaled wealth costs of restoring a place of power
- Changed Varangian Guard references to Kreml guard
- More localisation flavor and fixes
- donate_money_to_witch_hunters can now be clicked at 300 gold
- Added in several breaks that should stop marriage loops
- Disabled marriage for beastmen and Fimir.
- Beastmen should use the split clan decision to give away titles.
- Added in a decision for Fimir to give away titles
- Added wh_marriage_exlusion_trigger instead of pasting the traits in the file.
- Replaced ai interval with ai = no for give_province_amazon_2 decision. Ai uses a different decision
- Created a decision for AI fimir to grant titles
- Replaced Blood Keep Vampire Knights special troop with retinuesize_perc up to 35%
- Overhauled balanced and documented skaven artifacts
- Overhauled balanced and documented banner artifacts
- Overhauled balanced and documented magic artifacts
- Overhauled balanced and documented Ogre artifacts
- Overhauled balanced and documented Tombking artifacts
- Overhauled balanced and documented Greenskin artifacts
- Overhauled balanced and documented Beastmen artifacts
- Overhauled balanced and documented Asrai artifacts
- Overhauled balanced and documented Cathay artifacts
- Updated Steam Icon
- Replaced all remaining references to warrior traits and replaced with martial learning traits
- Overhauled balanced and documented vampire artifacts
- Slight rework of wh_magic_laws_scripted_triggers
- Slight rework of wh_battle_magic_triggers
- Weapon artifact restrictions loosened to allow factions to use various weapons
- Reforming the empire is now easier for both players and AI
- Added dwarf_commander_age_tt tooltip
- Removed the skaven prototype offmap for now
- Fixed invalid reference for brayherd offmap power
- Brass Legion title should now properly set chaos undivided champion trait using on_gain_effect
- Removed code reference to capitol holding for the Brass Legion
- k_direholm capitol changed to be within its de jure lands
- d_fezzir capitol changed to be within its de jure lands
- d_karak_karlnir capitol changed to be within its de jure lands
- d_zifilibar capitol changed to be within its de jure lands
- Set a de jure capitol for e_the_empire since the engine requires one
- b_biberhof granted to character 79068
- Removed lots of characters unused in our start date in characters/79000_stirlander
- Fixed all validator issues with title history
- Tweaked technology history for k_paraskiros
- References to add_building = no_elephant_camp_2-8 removed from code for now for tech set up
- TECH_RECRUITMENT now provides retinue size bonuses
- TECH_FORTIFICATIONS_CONSTRUCTION now provides 10% siege_defense
- Minor clean up to the technology files to clear validator errors, will cause some balance issues until another pass is taken closer to 2.0
- Deleted unused title files in history
- Fixed title scope in the effects for d_siegfriedhof
- Cleaned up references to future vampire societies in 02_scripted_triggers_warrior_lodges
- Changed references to d_chinon in wh_mercenaries to c_chinon
- Repaired the effect that hides magic from witch hunters, it was looking for character modifiers but we use flags
- Removed Adventure Society prototypes from files
- Removed all references to vanilla zodiac signs
- Fixed weight modifier for voting for any heirs to the current ruler of Bretonnia
- Fixed all validator errors involving societies
- Repaired Ariel of Athel Loren bookmark entry
- Fixed Fatandira start culture
- Terrain layout changed for the Kitadal
- Some more terrain blockers added across the map
- Switched almost all mountain and no_character provinces to Impassible Terrain
  > Cons:
  - Lose the unique names on most mountain ranges etc.
  - Terrain is greyed out in realm view mode (most used mode) so less pretty
  - Surrounding the provinces in question will no longer fill it in your color so minor addition to border gore in large regional empires
  > Pros:
  - Legibility, at a glance players have the important information on movement paths and bottlenecks
  - AI, we have strongly suspected its at least somewhat to cause for ai breakdowns while impassable terrain is a hardcoded pathfinding calculation
  - Legibility, the large names across big swathes of land could easily get in the way (think the giant chaos wastes word across the top)
  - Legibility/bug fix, this removes the floating letters on the map as the skaven tunnels name stretched across the old world funny and ended up jumbled
  - Since each one uses a province to define it, removing them frees up something like 50 provinces for use anywhere you want
  > Removed Provinces-
    > Aguidi Mountains
    > Southlands
    > Abasko Mountains
    > Adhrar Mountains
    > Worlds Edge Mountains
    > Worlds Edge Mountains 2
    > Worlds Edge Mountains 3
    > Apucinni Mountains
    > The Vaults
    > Devils Backbone Mountains
    > Pale Sisters
    > Forest of Arden
    > Grey Mountains
    > Athel Loren
    > Black Mountains
    > Anulii Mountains
    > Anulii Mountains 2
    > Beast Peaks
    > Vanaheim Mountains
    > Mountains of Thjazi
    > Mountains of Naglfari
    > Mountains of Hel
    > Ulfwerenar Mountains
    > Trollheim Mountains
    > Gianthome Mountains
    > Goromadny Mountains
    > Mountains of Mourn
    > Azgorh
    > Blackspine Mountains
    > Spiteful Peaks
    > Black Forest
    > Grey Guardians
    > Drakwald
    > Middle Mountains
    > The Under Empire
    > Skaven Tunnels
    > The Blighted Marshes
    > Spine of Sotek
    > Great Jungle
    > Icewind Mountains
    > Beastblood Mountains
    > Jagged Spine
    > The Frostbites
    > Pillars of the Gods
    > Plateau of Zorn Uzkul
    > Massif Orcal
    > Sahra Desert
- Added some missing description entries for triggered_gain used in society currencies
- Fixed all validator errors involving province history
- Repaired several bookmark characters for the custom bookmarks
  > Lone Sentinel
  > Greenskin Menace
  > Old World Forests
- Igor the Terrible now starts with the berserker trait and 25 duel skill experience
- Removed duplicate on_action reference to WB.11999 which caused bugs with the legendary journey progress
- Disabled references to numerous on_action events not currently used though I will rework and reenable them later
- Reworked Doom.0 to be a character event
- Reworked lustria.9 where a random building is lost to the jungle
- Reworked schaos.2 where a Building gets eaten by mouth in the ground
- Daemon culture group is now immune to schaos.2
- Reworked schaos.5 where gravity is reversed in a province
- Daemon culture group is now immune to schaos.5
- Reworked schaos.6 where a hellgate opens in your capital
- Fixed schaos.11 to be a character event
- Fixed lustria.2 to be a character event
- Fixed on_Action reference to mutate.12
- Reenabled and reworked event orcs.14-19 the ork gardening events and set them on a decade pulse for orks with high stewardship and not in command
- Fixed asur.61 to be a character event
- Fixed snehekharan.10 to be a character event
- Fixed snehekharan.10005 to be a character event
- Fixed DR_greenskins.151 to be a character event
- Fixed DR_greenskins.182 to be a character event
- Fixed all validator errors involving on_actions history
- All instances of cathayan_imperial_government changed to celestial_empire_government need TODO fix confucian_bureaucracy
- Fixed a vanilla bug where bloodline_less_factions flag wasnt properly applying
- Fixed a vanilla bug with the monumental bloodline counter
- Fixed all validator errors involving factions objectives and plots
- Fixed all validator errors involving nicknames
- Fixed a few mounts not applying defensive modifiers
- adjusted Ai difficulty levels
- adjusted doom effects on manpower, population, and levy size for chaos
- Fixed all validator errors involving the map
- Fixed all validator errors involving modifiers
- Fixed Gor-Rok bookmark portrait
- Fixed an issue with the allow block in law: tribal_organization_4
- Fixed numerous issues with scopes related to magic laws
- The Fay Enchantress no longer allows random traits and some appropriate traits added
- Converted the greek intrigue bonus for sucession voting to apply to vampire culture group
- Converted the roman diplomacy bonus for sucession voting to apply to imperial culture group
- Fixed some mutation triggers
- Fixed portrait properties for a few of our special Arabyan characters
- Fixed loads of errors and vanilla references with portrait properties
- Fixed all validator errors with the interface
- Fixed all validator errors with artifacts
- Converted the byzantine disfigurment bonus for sucession voting to apply to norscan culture group
------------------------------------------------------
v1.3.6:
------------------------------------------------------
- Norscan Gods given the offensive religion unit modifier
- Dun and Eux returned to Bretonnian ownership at game start
- Triers moved to the Gisoreux Duchy to match lore
- Beastmen mutations now conform with the visible traits game rule
- Reworked the Arden forest in Bretonnia
- Added loreistic Wood Elves to the Arden Forest
- Gave the Duke of Aquitaine a wife and son to stop the red duke from inheriting the title right away
- Switched the Red Dukedom and Aquitane Dynasty flags
- Lowered holding count of Arden Forest from 5 > 4
- Added Moonclaw as a Beastman easter egg character
- Added "Learn Lore of Chaos" for undivided offmap
- Scattered Norscan Strongholds across Norsca
- Reworked the Norscan initial set-up
- Sprinkled some chaos religions across Norsca
- Added holdings to Mount Hellspire, and a temple since its a holy site for chaos undivided
- Minor tech changes in Norsca
- Split Harskamp from the freebootah goblins and returned it to Westerland
- Split Wouduin from the forest goblins of the Drakwald and gave it to the beastmen to help with balance
- Split Middenmoor from the forest goblins of the Drakwald and gave it to the beastmen to help with balance
- Added an Old Imperial easter egg character to Norsca representing the "forest of knives"
- Norscan Stronghold Ambition should now properly convert your capital holding to a castle
- Westerlanders can now have beards
- Changed greenskins extermination to factor 2. Should help ai priortize them a bit more compared to other CB
- Added more pre-triggers to Bretonnia events
- Fixed mercenary decision
- Created a new government for Hobgoblins under the Dawi Zharr call "Hobgoblin Satrapy"
- Created a new, extremely harsh permanent tributary type for hobgoblins under the Dawi Zharr
- Disabled "release from tributary" decision for Dawi Zharr when its Hobgoblins
- Increased the age of the ruler of Dukhyls
- Reworked kislev, ungols, dukhyls forest, ropsmann, ostrosk, and troll county set-up at start
- Subfeudal no longer applies to independent Bretonnian lords
- Made balance changes to sub_feudafication Laws
- Localized sub_feudafication laws
- Added "drink potion" missing decision GFX
- Excluded chaos and norscan buildings from the dawi zharr
- Made the "buy from order dawi" and "buy from chaos dawi" mutually exclusive so they dont stack
- Excluded asrai_cadai from the seduction focus
- Allowed SOME state troops for nonvampire Sylvanians
- Special Road Warden and Huntsmen versions of traditional state troops for Sylvania
- Nomads no longer build temples, was a waste of money. Hardoded, dont know why it was on in the government file
- Minor tech change in Norsca
- Added Fimir holding GFX
- More nomads in northern Kislev
- Fixed Bookmark typo
- GetReligiousPerson quick fix, need to overhaul the custom localization eventually
- Typo fixes
- Removed extra modifier from wildwood rangers
- Fixed typo in castle version of sudfreecorps_4
- Fixed Fatandira CoA
- MP lobby chat text is now black instead of white
- Added the missing player list slot to MP lobbies
- Fixed missing Gov Flavor for norscan stronghold and congregation gov
- Changed the ruler of Ostermark to match lore
- Fixed vanilla introduce heir event chain
- Made changes to the imperial government and elector count governments
- Restricted "Hold Blot" to Norscan Gods
- Hid WAAGH.19 tombola event
- Added decision GFX for "train a mammoth"
- Allowed norscan gods to worship the ancestors
- Removed the levy bonus from the ulfsland special buidling until it can become a wonder
- Added a Norscan Society, unique from the other warbands as it focuses entirely on the norscan way of life.
    > 5 unique missions
    > 3 new powers
    > New lifestyle stuff preparing for
        - Search/Create Norscan relics
        - Raiding Quests
        - Mythical Creature Quests
        - Quests to obtain Viking Traits
        - Forging Quests
        - Relic Quests
- Built a city in Galiti
- Added a trade node to Galiti
- Added a trade node to Sartosa
- Built a trade post at start in Luccini
- Built a trade post at start for Cittafinistre
- Added a new trade branch to Monte Castello
- Added a new trade branch to Miragliano
- Added a new trade branch to Myrmidens
- Added a city and increased holding count of Gwingui in the southlands
- Added a new trade branch from Gwingui to Sudenburg
- Made some map/province changes to southern araby
- Fixed custom localisation for Jizya Tax
- Ulfsland changed to norscan stronghold and slightly nerfed
- Gave the county of Tintannil to the Royarch of Bretonnia
- Minor History changes
- Blooddragons can now wear eye patches
- Luthar Harkon is now missing an eye
- Drekla his first mate is now missing a hand
- 2 new vampirates added to the Vampire Coast
- Fixed a few modifiers not a part of the visible traits game rule
- New Vampire Pirate Retinues
- Pirate history changes across the map
- Pirate building overhaul with unique branches for the three culture types
- Special building for forts added for pirates
- Ormazd and Kitabid religions can now join chaos cults again
- Stromfels religion can no longer join chaos cults
- The ai = yes limitation for startup population of all societies removed except chaos warbands
- NOT = { prisoner = yes } added to all focuses, before prisoners could only take seduction, learning, and theology
- NOT = { prisoner = yes } added to all childhood focuses, before child prisoners could still be given any focus
- Mount decisions and events both reflect proper costs now
- Removed curse flag from mount artifacts
- Chaos and norscans can now build chariots
- Can no longer purchase a another mount until your done training the first one
- Nerfed Marcheur culture modifier
- Gave Tasselone back to Bretonnia at game start
- Added flags for hobgoblin realms
- Warp Tear can now only be built in the primary holding of the capital
- Slight Buff to warp tear
- Akendorf now uses feudal elective to match lore
- Completely reworked the start set up for the Border Princes
- Added both lore friendly Confederations at start
- Eagle and North Border Confederacy now use feudal elective to match lore
- Fixed wrong scope for offmap decisions to switch from undivided to mono-god
- Magic laws should no longer revert back to base level after forming the colleges of magic
- Seduction changes:
    > Vampires, Slaanesh: No same sex scandal
    > Slaanesh, Lahhmian: Allow same sex seduction without Homosexual trait.
    > Slaanesh. No Incest scandal risk, No priest scandal and No age scandal.
- Westerland is now a valid elector to form the empire
- Excluded fimir from marriage correction, should fix bugs
- Some performance pre-trigger changes
- Added necromancy to Isabella and made Vlad older
- Minor bloodline changes
- Obregon counties now touch to create a contiguous border
- rumours_events religion changes
- Expanded the exclude list for the the marriage event
- Added 5 new mercenary companies to Norsca at start
- Added an Ogre Tribe in the Border Princes and in Norsca
- Changed the various Old World Faith Intermarriage Rules
- Small changes to history in Nordland
- Minor Gui fixes
- Added trade posts for Halflings in the Moot
- Re-adjusted the halfing merchant families
- Reduced the size of trade post models on the map by 60%
- Reduced the size of trade port models on the map by 25%
- Reduced the size of trade flags on the map by 25%
- Rebalanced the cost of Kislevite Retinues
- Performance enhancements for the Von Carstein events
- Fix for the Duplicate witch hunter societies clashing, Merged
- Reforming the Empire will now bring religious peace and restore the Intermarriage between the empire faiths
- If a Black Crusade threatens the Empire or the Von Carsteins grow too powerful, religious peace will be gained and the empire will seek alliances with others for aid
- Fixed undivided chosen having access to becoming champion decision
- Changed the timing on The Everchosen chain to fix it failing without warning
- Canceling the decision to craft a magic item will now refund the winds of magic spent
- Munzig can now build a trade post to utilize the gold mine
- Added a trade post to munzig at game start
- Fixed missing localization for the "Perilous Beasts" Bookmark
- Fixed a positions issue in norsca causing ships to go on land
- Greenskin mounts now locked to that religion group
- Lizardmen mounts now locked to that religion group
- Changed the "Perilous Beasts" Lizardmen start to Hexoatl
- The pocket of defenders event will no longer kill you if you let them go
- Minor adjustments to history at start up around the world
- Fixed the vampire wars not firing correctly
- Minor adjustments to Reunification of the imperial religions
- Disabled the getting into shape war focus line for Ogres
- Add in Thorgrim as a child at the start date, as the grandchild of Alrik
- Eating prisoners as Ogres/Huge Orcs can make you fat
- You now gain duel exp for hunting vampires personally
- Added Fort level to Altdorf and Marienburg until they can become wonders
- Added Flavour events but left them disable for now until they can be polished
- Strengthened each religion that allows for reformation
- First Pass at Reformable Religions. I expect several iterations will be required for polish
    > Atruhayid
    > Old Faith
    > Norscan Gods
    > Northern Gods
- Added character flags for one eyed/one handed/one legged. to drekla, luthor harkon, and the crimson king of numas as well as allowances in the auto healing system for those flags
- Fixed Ruler Designer crash for sartosans
- Minor fixes
- Fixed Crash with reformation window
- Fixed Doom notifications
- Fixed missing Government flavour and GFX for all the new governments
- Added a new Dawi Government called "Thanehold"
- Ottilian family line fixed. Which was causing a broken familiy tree and missing bloodline
- Finished several Flavour events and enabled them
    > Valka the Serpent in Norsca
    > Each of the Imperial Claimants
- Added a small boost to AI Valka
- Changed the magic laws for Westerland since wizards there were giving protection by Magritta in 1993. Still Illigal for the vassals Nordland and Stirland.
------------------------------------------------------
v1.3.51:
------------------------------------------------------
- Modified WOL events since cheating isnt a crime in all religions
- Small nerf to the Red duke
- Gave Louis The Young piety to hire holy orders
- The entire world should no longer join the Black Crusades
- Engineering event should no longer fire randomly
- Minor performance improvements
- Removed a battle disfigured event in favor of a vanilla variant
- Localisation for undivided boons
- Theology focus can now remove addict trait
- Disabled engineers guild until its finished
- Minor adjustments to MP lobby layout
- Repaired the Assassins society for Araby
- Properly excluded AI from 2 events in on_action_events.txt
- Rewrote the description for the Subfeudal government to be more clear
- Rewrote the description for the Tzardom government to be more clear
- Disabled the new coastal colonisation CB until it can be tied to the new colony mechanics
- Added GFX for the drink elixir decision
- Fixed frame switch bug, will finalize and update custom frames for the new governments in a later patch
- Fixed the Maelstrom government, should now be pirate fleet at start
- Repaired the Elixirs to properly increase stats
- Limited elixirs from being used if your stat is too high, instead of wasting them and doing nothing
- Repaired the 2 missing spells from the lore of shadows
- Changed the starting religion for vulture mountain and its ruler to shadowmen instead of vampiric
- Fixed Conquistador retinue calling null unit type
- Fixed Ostland Ogre retinue calling null unit type
- Fixed the "enfeeble foe" spell for lore of shadows
- Fixed layout of special interest characters in the outliner
- Repaired several other spells where the event target was set after the event was fired
- Lowered the brightness on the "hills" terrain GFX
- Added GFX for the "Impassable Mountains" terrain
- Updated GFX for "Urban Area" terrain
- Over 20 provinces in the empire changed to the "Urban Area" terrain type
- Updated both of the volume 2 music tracks
- Chaos rulers will no longer claw their eyes out on a daily basis
    > Repaired 4 events tied to seiges in the chaos wastes, everything should fire correctly
- Excluded Necrarch vampires from the "Cleanse Beastmen" CB
- Lowered disease rates for immortal races for things like cancer
- Reworked fertility debuff for fimir to be a reduction of 25%
- Reworked chaos traits so you no longer retain multiple tiers of one trait
- Allowed tribal holdings for the Strigoi government
- Repaired Santa Magritta
- Repaired positions.txt for offmap trade node
- Repaired Lizardmen Tablet recovery wars
- Lowered The effect of age on the Respect value for Doge elections
- Repaired Trade Routes and Nodes
- Removed piety from red duke
- Fixed some bugs with ogre buildings
- Added a game rule to disable the malus for plots across factions
- Excluded lahmians from the malus when plotting against Humans
- Added missing Localisation
------------------------------------------------------
v1.3.5:
------------------------------------------------------
- Added pre-flag triggers to on_action_events.txt > potential CTD fix on weaker systems
- Removed mentions of doomengine.1 from on_actions. Was duplicating the repeating event inflating the doom rising
- Fixed the Voting for Witch Hunters
- Fixed Undivided Daemons in all applicable triggers
- Can no longer ask Witch Hunters to leave your court if they are there on a witch hunt
- Performance Fixes for some Nehekharan MTTH events
- Becoming a Daemon Prince now creates a bloodline and summons some daemon event troops
    > Nonreinforcing for players, reinforcing for AI
- Some more favour changes for S_chaos_events
- Changed Nehekharan Province Events to yearly pulse instead of 5 day MTTH
- Fixed one of the Ice Spells being locked to lore of fire
- Reworked s_chaos_events
    > Converted much of the MTTH events to on_actions
    > Reenabled possession events
    > Removed event causing locked saves
- Reworked Chaos undivided offmap power
- Added a way for players to properly shift from undivided to a specific god
- Made the Red Duke older than King Louis
- Cleaned up beastmen decisions
- Removed the purge decision from lustria (we now have "cleanse provinces" that replaced it)
- Added flavour event to becoming a daemon prince
- Pre-triggers added a few nehekharan events
- Republic government changes
- Vampires should be able to create Merchant republics
- Skaven cant build trade posts any more
- Vampire Government fixes on new Ruler designed character
- Some reworks on some Bretonnian history so it would be closer to lore
- Fixed Fatandira bloodline
- Fixed all the issues of the female temple holder of myrmidia by simply denying male temple holders in their religion (Should also lighten up the engine a bit)
- Pig and Toad traits now give proper negative modifiers
- Buffed Empire holy orders
- Made trait opinions make a bit more sense
- removed cannot wear stuff from chaos artifacts. The armor you receive from chaos bends around you, fitting around your mutations
- Map changes to cut off red eye horde from kislev
- Created decision to reorganize the kremlin guard.
- Added in the Ice court holy order, to defend the magic in Kislev
- Enabled a few varangian guard events for the kremlin guard
- Added a special government for Strigoi Ghoul Kings
- Added a special government for Pygmy Halflings
- Added a special government for Amazons
- Added a special government for Ogre Tribes
- Added a special government for Cathayans
- Added a special government for Tilean/Estalians
- Changed the name of the norscan feudal/tribal government hybrid from "tribal baronys" to "Norscan Stronghold"
- witchhunter.8 no longer targets characters of the wrong religion/culture. But instead looks for anyone outside the religion group/with mutations
- Buffs to Bretonnian Retinues
- New GFX for Bretonnian Noble, Clergy, and Peasant traits
- Reverted Gor-Rok to the upgraded lizardmen gov
- Created a new government for the pygmies of lustria
- Created a new government for the amazons of lustria
- Reworked some government icons and the map colors for governments
- Recompressed all DDS files without mipmaps, decreasing overall mod size
- Artifact updates
- Some CB updates
- Society Fixes
- Some nerfs to the mutation system
- New GFX for all new mutations
- New GFX for creature_chaosspawn
- New GFX for different race/religion/culture character interfaces
- Greek Fire events enabled for myken culture
- Finally added special halfling government
- Halflings are now a republic featuring 5 lore accurate families
 > Thorncobble
 > Brandysnap
 > Tumbleberry
 > Merribuck
 > Rumster
- Choosing "nevermind" when crafting magic items now properly clears the crafting flag
- New "Jade Court" government added for jade vampires
- Reworked all government GFX
- Reworked all government map mode colors
- Fixed outremer (bretonnia - lyonesse) port bug with raised ships (positions.txt issue)
- Extended the Doom counter to slow progression
- Slowed movement speed on the oceans
- Reworked all terrain types movement, defense, and supply values
- Nerfed Mercenary company sizes
- Updated Red duke trait GFX
- Updated Drachenfels trait GFX
- Losing a Black Crusade as chaos now resets the Doom counter to 0
- Adjusted Beastmen migration to use modifiers instead of character flags to be more clear to the player
- Repaired the distribute Runefang Decision
- Excluded Chaos and Greenskins from "renouncing the throne"
- Colleges of magic can now only be formed by independent rulers
- Added ambition to become a Daemonsmith for Chaos Dawi
- Cleaned up all ambition GFX, added one for Daemonsmith
- Cleaned up automatic battle magic code a bit
- Lots of Pretrigger checks added and some minor performance enhancements to code
- Changed the trade route color on map to be a bit easier to see and understand whats going on
- Changed the acheivement event to an on_action
- Repaired some AI Cleanup Events
- Repaired the mists of Albion
- Reenabled the zun_pagan torture of releasing prisoners into the desert for nomadic ormazdians
- Removed acheivement events from on_actions
- Fixed Dawi Reunification Decision voting
- Updated Slayer events
- Combed through on_action lists for performance
- Properly setup all traits and character modifiers to interact with the hidden traits game rule properly.
    > If we missed any let us know!
- Added Madcap Mushrooms and Scarlet Elf Caps as artifacts
- Allowed Greenskins to consume both mushroom types similar to consuming warpstone
    > This will be polished and expanded later, for now basic functionality and two mushroom types
- Lizardmen are now allowed to use the Purge Greenskins CB
- Added checks for Fimir and Hobgoblins across the filebase
- A bit of spring cleaning
- Buffed kislev building chain troop values
- Added artifacts to various kislev leaders from the lore
- Fixed a bug in duels preventing warrior lodge members from recieving protection from death
- Removed Kislevites from joining nightly orders of the old world
 > will replace with Boyarin or winged hussar society
- Removed a few same race opinion bonuses
- Updated Kislev start position further
- Added tyranny gain to the erengrad event
- Updated history and added the Romanoffs as a distant relation to the ruling family in kislev
- repaired a map adjacency in norsca
- Norscans can now convert tribal baronies to Castles or Cities
- Fixed the CTD when you hover over "potential target of Antoch decision"
- Added Sons of Ursa as a holy order to replace the ice guard holy order
- Added Throgg to norsca and made some minor changes to the map
- Enabled destruction of indestructible artifacts on character death
- Changed the weights of cursed chaos artifacts
- Made all forgeable bloodlines patrilineal
- Lowered the unit maintanance of magic archers due ai bankrupting themself in piety
- Adjusted the spawn rates of Fimir Fimm and Shearls
- Allowed fort ostrosk in kislev to build trade posts
- Adjusted bonuses from the Fimir Maergh trait
- Removed the "cannot marry" limitation from Fimir
    > they wont do it anyway and it allows them to finally grant landed titles without elaborate workarounds
- Added some flavor and fallback events incase fimir do "marry"
- Added the Maelstrom
- Added Galleons Graveyard
- Added the Hobgoblin Khanate
 >These 3 require more polish but we are getting close to a final map
- Nerfed Tschad of the brass legion slightly
- Cleaned up the province borders on the Khuitan Shelf
- Excluded Hobgoblins from the cleanse greenskin decision
- Allowed Hobgoblins to use the make land green decision
- Overhauled the message window
- Overhauled the outliner and created custom gfx for the different UI themes
- Repaired the Elective League decision
- Overhauled the game start UI
- Overhauled the bookmark UI
- Overhauled the multiplayer UI (!*REQUIRES MORE TESTING WITH OVER 10 PLAYERS)
- Repaired missing music tracks (sound still crackles will fix in a future update)
- Fixed Succession Voting
- Added Hobgoblin Dynasties
- Repaired Red Duke Special Elective
- Added Flags for the maelstrom and dreadfleet
- Repaired the Ice witch society startup population and joining requirements
- Finished the new province interface
    5 Separate versions for:
    > Muslim
    > Indian
    > Pagan
    > Republics
    > Base
- Update the holding strip GFX for trade posts, land trade posts, and forts for:
    > Arabyans
    > Asrai
    > Asur
    > Beastmen
    > Bretonnians
    > Cathayans
    > Chaos Dwarfs
    > Greenskins
    > Halflings
    > Kislev
    > Kurgans
    > Lahmians
    > Lizardmen
    > Nehekharan
    > Ogres
    > Reiklanders
    > Sartosans
    > Skaven
    > Strigany
    > Sylvanian
    > Tileans
    > Wasai
- Changed the Ostland Ogre Retinue to use the new maneater special troops
- Changed the Mootland Ogre building to use the new maneater special troops
- Repaired the Arabyan Trade Route
- Repaired the Brettonnian Trade Routes
- Repaired the Skull Road
- Extended the khyprian road to Luccini
- Changed Jakob, the ruler of the Galat to Neueslander Culture and changed the homosexual trait to romantic
- Restored an offmap trade anchor that was overwritten with the hobgoblin changes
- Updated Hobgoblin GFX to be somewhat unique - More portrait stuff planned in the future
- Shallyans can sacrifice themselves to lower the doom counter at the highest tier of their society
- Freebootas can now build new holdings
- Freebootas can now build Forts
- Waaaagh! Government can no longer build forts
- Regular Greenskins can now build forts
- Hobgoblin Khanate nomadic government added
- Minor Terrain Fixes
- Fixed the Positions.txt for the changes made for the hobgoblin provinces
- Changed the "Form Kremlin Guard Decision" so that you no longer HAVE to control Erengrad. Its just much cheaper if you do
- Removed the single letter names from the seagit name lists
- Hobgoblins can build forts
- Limited Antoch crusades to only be useable by the Grail religion
- Added checks to summoning Daemons inside prisoners to remove the characters dynasty:
    > dynasty = none
    > recalc_succession = yes
- Also added to the chaos spawn effect
- Fixed the localization for brewing potions
- Added the localization for brewing elixirs
- Artifacts changed back to a 1-5 scale instead of 1-10. Hardcoded AI limitation
- Repaired the Empire Achievment Event
- Lizardmen cannot start a tablet search expedition while the Jade staff war is happening
- When a Slaan is awakend and takes over titles the abdicated ruler will now return to the same court after a day instead of a nearby realm
    > This allows Gor-Rok to be used by a commander during the Staff of Jade Reclaimation war
    > Also allows you to keep track of your actual character while not under your control
- Skaven and Lizardmen ship decisions now have a reduced prestige cost, tightened checks for performance, and zero maintenance
    > They also now grant a variable amount of ships depending on your tier, so everyone isnt floating around on 100 ship fleeps when they only need 25
- Added mastermind_theologian trait to all Slaan
- Rewrote Staff of Jade war with Antoch to fire at Game Start
- Allowed other lizardmen rulers to join the war against Antoch
- The War with Antoch now wakens a Slaan to lead, plans to switch to mazdamundi to follow lore are planned. For now its the resident Slaan of Itza
- Fixed some minor positions in domestic_court.gui for the council tab
- The event to awaken a Slaan now sets the proper Government
- Fixed wh_magic_law.23, typo "independent"
- Replaced Gor-Rok with Gorro in the lizardmen name lists to avoid confusion
- Lizardmen are no longer killed by thier own traps. Lost Gor-Rok when my slaan awakened since it counted as a change of court
- Disabled the Skaven ships decision for AI, waste of performance
- Lowered tech requirements and raised income for lizardmen as a temporary income fix until I get to the overhaul
- Added a decision to enact the ritual for the Staff of Jade, instead of relying on an on_action
- Changed the Altar of Ultimate Darkness to static map item instead of a wonder
- Moved the Corpse Tree to Arguun
- Made Arguun the holy site for nurgle
- Moved the Daemon prince of nurgle to Arguun
- Fixed a stray pixel for a chaos waste province
- Returned Cold Mire to a "wasteland" Province
- lowered negative base score for brief non-aggression pacts
- Raised max battle score for Vlads Subjugation from 25 to 50
- Modified the Black market to allow access to a broader range of characters
- Tweaked buying and selling on the black market
- Added localization for the Throgg trait
- Added unique GFX for the Throgg trait
- Cleaned up the borders of the eonir forest
- Fixed unitpanel location for sieging armies
- Fixed some customizable loc errors
- Fixed DR_pirates.107
- Changed the is_smart_trigger in the colleges of magic societies to use triggered_gain
- Removed duplicate HF.501 - HF.506 events in HF_warband_flavor_events
- Fixed piety gain for the Baba minor title
- Removed designated_heir = yes in the designated_heir title. Invalid command
- Fixed the reference to "heavy_cavalry" in svampires.16 now properly references "knights"
- Localized over 200 barony titles added in the past few patches
- Repaired 00_customizable_localisation_armoury
- DR_pirates.106 - DR_pirates.107 added as bi-annual pulses for pirate modifier maintanance
- Fixed duplicate events 50005, 50006, 50020. The duplicates changed to 55555, 55556, 55520
- Moved wh_mutation.101 and 80 = wh_mutation.102 to yearly random on actions instead of MTTH
- Removed History Command 'set_graphical_culture'  for Character history/characters/18000_special.txt at Line 1487
- Fixed Duplicate Historical Character ID:42052 >> 42053
- fixed references to undefined traits in the history files
- Fixed "d'Gisoreux" missing dynasty
- fixed the Waldo easter egg character religion = noreligion to religion = none
- Added "de Alaca" dynasty  for Cadavo
- Repaired Magical inheritance for magic power level 4
- Fixed some Provinces that were supposed to be impassable mountains
- Added an ambition to become a norscan stronghold if your a norscan tribe
- Added GFX for the norscan Stronghold ambition
- Repaired costs of converting settlements and added a few checks for lustria
- Repaired the Chaos Dwarf armament bug where you could sell to as many people as youd like at one time as long as you didnt click on the event options
- Added a counterpart decision to buy armaments from the regular dwarfs for non-chaos rulers
- Repaired some Witch Hunter events
- Split up the Kreml guard event
    > AI now forms the kreml guard in a maintanance event. Player still uses the decision
- Fixed parse error
- Localized undivided offmap
- Reenabled event 60504 Landless status clean-up for everchosen in the on_action list
- Added DR_chaosundivided.10 to spawn AI everchosens to a decade pulse
- The DOOM notifier GUI should now properly reveal the existence of the everchosen
- Got the Everchosen quest to a workable state
- Removed only_playable = yes from sell_stuff_chaos_dwarfs since ai = no is enough to block all AI
- Fixed namespace of buying chaos armaments. Namespaces are capital sensitive
- Fixed undivided off map decisions not working
- Removed uses_piety_for_law_change = yes from some laws
- Repaired some magic laws
- Added tooltips to the new norscan stronghold ambition
- repaired "can_grant_title_witch_hunter" scripted trigger
- Excluded Grey Seers from becoming Eshin Assassins
- Fixed the new "Buy Armaments" decision
- Added a new check to the duel system to make them less deadly
- Adapted some duel stuff for berserkers
- Adapted some duel events centered around the nile and scripted them for Nehekhara, Araby, and Lustria
- Repaired some warrior lodge events
- Repaired some empire events
- Fixed the province GUI holding modifier icons
- Changed the province GUI to make room for the longer titles
- Added a 3 point flat health boost to the nurgle religion to help offset the diseased courts
- Added modifiers for the Places of Power system
- Slightly nerfed the chaos dawi and dawi armaments modifiers
- Fixed a bit of localization
------------------------------------------------------
Legacy_v1.3.42:
------------------------------------------------------
- Repaired Damage and Heal Spells from casusing CTD
- Damage and Heal Spells now work on a percentage instead of a set amount to prevent negatives *REQUIRES TESTING
- S_chaos_events changed to use offmap currency instead of old favour system
- Confined all instances of mutation_toughness_test_effect to a custom tooltip to prevent CTD
- Fixed CTD for summoning Treekin.
- Applied the archer modifiers to Magic Archers.
- Summoned Treekin added to moddifiers for forests and jungle
- Fixed wrong goverment in kislev
- Disabled invalid triggers of all visable trait mechanics
- Corrected "Impassable Mountain" stats
- Moved erengrad dilemma to on_actions event on start up
- Repaired Kislev and Ungol AI.
    > This was a MAJOR issue and who knows how long its been latent, recommend not playing any patch before this one.
- Changed stats for war engines (trebuchets) and artillery
------------------------------------------------------
Legacy_v1.3.41:
------------------------------------------------------
- Changed namespace of magic system events. Performance fix
- Reverted the Defines that alter court Pruning. Performance Fix
- Added a check to damage spells to prevent negative units numbers. REQUIRES TESTING
- Repaired CTD from channeling
- Changed Woodelf Retinue units to use new treekin unit type
- Buffed Nuln Artillery Regiments
- Demanding erengrad bribe makes then a tributary of kislev
- Changed bloodline fatandira_blood from matrilineal to patrilineal
- Optimized and fixed Dooming events
- Missing cult societies decision file restored
- Special Building changes
- General Bug fixes
- Building changes
- Removed extra 0 from dwarf slave buildings
- Small building changes
- Limited absolute law from norscan tribes
- Society fixes (Order of the bleeding heart shallya)
- Gave neferata some zombie retinues
- Mercenary: Mananns Blades of Marienburg Created
- Mercenary: Red Talons of Marienburg Created
- Mercenary: Mordland Seahawks of Nordland Created
- Added limitations to Imperial Reconquest
- Transfered the mercenary company winged lancers to kislev
- Added custom flag for the winged lancers.
- Character changes
- Disabled incomplete societies
- Removed "cannot marry" from the everchild trait
- Gave Neferata the lores she had in 8th edition lore
------------------------------------------------------
Legacy_v1.3.4:
------------------------------------------------------
- New Wonder: fortress for Araby
- New Wonder (VINEYARD) *FIX GFX
- Fixes for mutations and pseudo daemonhood
- Nerfed Greenskin Culture Modifiers
- Fixed the Verena Missions and updated the files
- Fix Greenskin CB
- Fix Lost Dawi Holds Tech
- Combined Decision files
- Fixes for history files
- nerfed greenskin building chains
- allowed pirates access to county conquest CB
- Norse Dawi get a unique culture modifier
- Lowered the modifier bonus from martial in defines to stop steamrolling high martial characters
- Changes to icewitch society
- Some wonder changes for the shrine of asuryan
- Clean up for Asur Events
- History Fixes
- New prototype GFX for the Druchii Raiding society
- New prototype GFX for the Adventuring society
- Merged Crafting Decisions to the magic offmap
- Merged Potion Brewing Decisions to the offmap
- Added artifacts for the unique potions
- Changed the decisions to drink potions
- Finalized some new spell effects
- Finalized necromancy spellbook
- update offmap magic GUI and localization
- Fixed Kislev ai pathing. Single pixel was wrong in provinces.bmp
- Small improvements to kislevite culture_conversion_events.txt
- Gave kingdom of nordland to salz to help westerland survive
- Created a betrothal between the two for stability
- Gave margritta prestige so that she starts on equal footing of other electors
- Made Silver Pinacle a small bit better, to help neferata not get eaten by gobbos
- Began Custom naming wonders to help performance, need to do this for karaks and switch to just generic wonders
- Fix to Black Crusade defenders not joining properly
- Added the elixirs to the brewing decision panel
- Added 4 new elixir Artifacts
- Updated potion GFX to be unique for each
- Update special_unitstrip GFX for new treekin unit
- Added a new Summoned Treekin special unit
- Updated magic modifiers
- Updated magic effects for the magic system
- Repaired missing effect required for teaching yourself magic
- SPELLBOOK :
    > NECROMACY
        - invocation_of_nehek
            # Unnatural Aura, Combat rating, Martial and 20% undead horde defense/offense boost
        - gaze_of_nagash
            # Plot Protection, Reveals Plots
        - curse_of_years
            # Ages and harms target, Heals caster
        - undead_summoning
            # Summons undead horde
    > LORE OF DEATH
        - aspect_of_the_dreadknight
            # Aura, Combat rating, Morale and 25% global revolt risk reduction
        - soulblight_spell
            # Applies Province Tainted modifier and lowers prosperity
        - purple_sun_of_xereus
            # Damage units at the current location
        - spirit_leech
            # Ages and harms target, Heals caster and friendly units at location
    > LORE OF LIFE
        - shield_of_thorns
            # Aura, Defense Modifier and personal combat skill
        - regrowth_spell
            # Heal units at current location removes tainted province modifier
        - the_dwellers_below
            # Damage units at the current location
        - awakening_of_the_wood
            # Summon Treekin event troops
    > LORE OF LIGHT
        - bironas_timewarp
            # Aura, Movement Speed bonus, Land Organisation
        - light_of_battle
            # Aura, Defense Modifier and personal combat skill
        - shems_burning_gaze
            # Damage units at the current location
        - banishment
            # dispels undead horde and demons
    > LORE OF FIRE
        - cascading_fire_cloak
            # Aura, Defense Modifier and personal combat skill
        - flame_storm
            # Damage units at the current location
        - flaming_sword_of_ruin
            # Aura, Strength bonus, Land Organisation
        - the_burning_head
            # Extreme Damage units at the current location
    > LORE OF METAL
        - glittering_robe
            # Aura, Defense Modifier and personal combat skill
        - gehennas_golden_hounds
            # Damage units at the current location
        - transmutation_of_lead
            # Grants scaled wealth, half your yearly income, min 100 max 500, money REMOVED later
        - searing_doom
            # Extreme Damage units at the current location
    > LORE OF HEAVENS
        - fantastic_foresight
            # Plot Protection, Reveals Plots
        - chain_lightning
            # Damage units at the current location
        - harmonic_convergence
            # Enhances Province Prosperity
        - comet_of_casandora
            # Extreme Damage units at the current location
    > LORE OF BEASTS
        - panns_impenetrable_pelt
            # Aura, Defense Modifier and personal combat skill
        - flock_of_doom
            # Damage units at the current location
        - beast_master
            # Summons, random animal commander for a limited amount of time
        - wyssans_wildform
            # Transforms Target Prisoner into a pig toad or other beast
    > LORE OF THE WILD
        - devolve
            # Lowers Prosperity of current location
        - bray_scream
            # Damage units at the current location
        - beast_made_well
            # Heal units at current location and applies a strength aura
        - viletide
            # Extreme Damage units at the current location
    > LORE OF SHADOWS
        - enfeebling_foe
            # Influences target opinion of caster
        - the_withering
            # Damage units at the current location
        - okkams_mindrazor
            # Aura, Strength bonus, Land Organisation
        - pit_of_shades
            # Extreme Damage units at the current location
    > LORE OF HIGH MAGIC
        - soul_quench
            # Morale Damage units at the current location and drains commanders of magic and spellpower
        - apotheosis_spell
            # Heal units at current location removes tainted province modifier
        - fiery_convocation
            # Extreme Damage units at the current location
        - hand_of_glory
            # Enhances Province Prosperity and adds strength and speed auras
    > LORE OF DARK MAGIC
        - doombolt
            # Damage units at the current location
        - word_of_pain
            # Morale Damage units at the current location and drains commanders of magic and spellpower
        - blade_wind
            # Extreme Damage units at the current location
        - soul_stealer
            # Ages and harms target, Heals caster and friendly units at location
    > LORE OF CHAOS
        - boon_of_chaos
            # Aura, Strength bonus, Land Organisation
        - burning_blood
            # Damage units at the current location
        - lure_of_Chaos
            # Influences target opinion of caster
        - veil_of_corruption
            # Extreme Damage units at the current location
    > LORE OF NURGLE
        - plague_wind
            # Applies Province Tainted modifier and lowers prosperity
        - rotbomb
            # Damage units at the current location
        - nurgles_boon
            # Heal units at current location removes tainted province modifier and reduces disease
        - sumptuous_pestilence
            # Spawns Disease at current location and adds morale and combat auras
    > LORE OF TZEENTCH
        - flames_of_fate
            # Plot Protection, Reveals Plots
        - treason_of_tzeentch
            # Morale Damage units at the current location and drains commanders of magic and spellpower
        - infernal_gateway
            # Damage units at the current location
        - mindfire
            # Influences target opinion of caster
        - tzeentchs_blessing
            # Potentially Mutates and harms target, Heals caster and friendly units at location
        - daemonfire_vortex
            # Extreme Damage units at the current location
    > LORE OF SLAANESH
        - luxurious_torment
            # Damage units at the current location
        - song_of_seduction
            # Influences target opinion of caster and adds morale and combat auras
        - slothful_stupor_spell
            # Applies Slothful Stupor modifier and lowers prosperity
        - pavane_of_slaanesh
            # Extreme Damage units at the current location
    > LORE OF HASHUT
        - ash_storm
            # Damage units at the current location
        - breath_of_hatred
            # Aura, Strength bonus, Land Organisation
        - dark_subjugation
            # Enhances Province Prosperity
        - flames_of_azgorh
            # Extreme Damage units at the current location
    > LORE OF NEHEKHARA
        - incantation_of_protection
            # Aura, Defense Modifier and personal combat skill
        - incantation_of_desert_wind
            # Applies Desert Wind modifier and lowers prosperity
        - incantation_of_urgency
            # Aura, Movement Speed bonus, Land Organisation
        - incantation_of_vengeance
            # Damage units at the current location
    > LORE OF THE BIG WAAAAGH
        - brain_bursta
            # Damage units at the current location
        - ard_as_nails
            # Aura, Strength bonus, Land Organisation
        - the_evil_sun
            # Extreme Damage units at the current location
    > LORE OF THE LITTLE WAAAAGH
        - great_green_spite
            # Lowers Prosperity of current location
        - gift_of_the_spider_god
            # Aura, Movement Speed bonus, Land Organisation
        - curse_of_da_bad_moon
            # Morale Damage units at the current location and drains commanders of magic and spellpower
    > ICE MAGIC
        - chill_voice
            # Aura, Charisma and Diplomacy boost
        - hawks_of_miska
            # Damage units at the current location
        - blizzard
            # Applies Blizzard modifier
        - ice_maidens_kiss
            # Extreme Damage units at the current location
    > ICE HAG MAGIC
        - fortune_told
            # Plot Protection, Reveals Plots
        - resist_chaos
            # Aura, Defense Modifier and personal combat skill
        - cleanse_soul
            # Heal units at current location removes tainted province modifier and reduces disease
        - witchs_curse
            # Morale Damage units at the current location and drains commanders of magic and spellpower
    > GUT MAGIC
        - spinemarrow
            # Aura, Strength bonus, Land Organisation
        - bonecrusher
            # Damage units at the current location
        - trollguts
            # Heal units at current location removes tainted province modifier and reduces disease
        - the_maw
            # Extreme Damage units at the current location
    > GENERIC SPELLS
        - mystic_shield
            # Aura, Defense Modifier and personal combat skill
        - arcane_blast
            # Damage units at the current location
        - twilight_pathway
            # Heal units at current location removes tainted province modifier and reduces disease
    > LORE OF THE DEEP
        #IN PROGRESS
    > LORE OF VERMIN
        #IN PROGRESS
- increased the become_chaos_spawn_trigger count to 7
- increased the become_forsaken_trigger count to 5
- excluded beastmen despoilers and the everchosen from the mutation effect
- Changed KA.2 and KA.4 to be on_actions. Perfomance Fix
- Changed bretonnia.5 through bretonnia.10 to be on_actions. Perfomance Fix
- Those voted to become King of Bretonnia, if already a part of the society become a grail knight
- Repaired the Green Knight Despawning Properly
- Repaired the Green Knight Spawning To aid as a commander if you lose a battle
- Fixed a CTD caused by restless Slaan who would end every war at once across the world
- Repaired Nehekhara outside Conquest CB
- Added a few new dynasties to the forests of the old world
- Manpower and Population buff to the beastmen government to stop them disbanding starting herds
- Added a Port Royale easter egg
- Mordheim Tributaries can no longer infight
- Created the Colony Tributary Type
- The Ice Witch Society is no longer secret
- Updated some on_actions for Lizardmen
- Adjustment to society code and joining societies
- Cleaned up Lizardmen event pretriggers. Performance Fix
- Added GFX for Phoenix Guard wonder upgrade
- Laid the Groundwork for the new adventure societies
- Added the Druchii Corsair Society
- Added Pirate Society
- Added the southern realms adventure society
- All GFX is in Prototype stage
- Most events/ Missions for them are in prototype stage
- Reworked the title set up for the lustrian coastline to prepare for new colony mechanics
- Added system to protect AI female rulers from marriage issues
- Made the following Define Changes for performance. Requires testing.
    > FERTILITY_BASE_MULT = 0.4
    (Slightly lower base fertility to balance character count)
    > SECONDARY_SPOUSE_FERTILITY_MULT = 0.25
    (Significantly lower concubine/second wife fertility to prevent children spamm by tribals and muslims, when they have 10+ children every time)
    > EVENT_PROCESS_OFFSET = 100
    (Increased the delay between event loops for provinces and characters)
    > COURTIER_EVENT_PROCESS_OFFSET = 255
    (Increased the delay between event loops for courtiers)
    > COURT_PRUNE_SIZE = 1
    (Every court is checked for pruning)
    > PRUNE_MINIMAL_AGE = 1
    (Every "unimportant" character is pruned at any age)
------------------------------------------------------
Legacy_v1.3.3:
------------------------------------------------------
- Lots of Bug Fixes
- More Araby and Underempire Changes
- Building fixes
- Repaired society Clothes
- Updated all Tributary CBs to exclude Greenskins
- Excluded Necromancers from the holy war CB
- Minor Updates to several files
- Lowered tech for the greenskins in bretonnia and empire
- Reunited drakwald
- wonder and building fixes
- Removed arbitrary limitations of some artifacts
- Phoenix King will now wear his proper crown
- Nerfed banners
- Landed Titles Fixes
- Began using the is_vampire_trigger and is_vampire_visible_trigger to clean up conditions
- Created New Scripted Effects for the Magic Engine
- Began converting the necromancer decisions to the spell book
- Necromancy now has a unique version of magic
- Changed how consuming warpstone works and removed the decay from necromantic power
------------------------------------------------------
Legacy_v1.3.2:
------------------------------------------------------
- Nerfed a few of the mounts
- Adjusted dwarven_reconquest CB
- Adjusted the Dwarven High Kingdom Decision to now use a weighted voting system
- Changed "diplomatic_range" of the Lady to be "society_member_of = knights_of_bretonnia"
- Changed chaos offmap powers to "true_religion" to better scope to secret religion
- Added Custom Characters for our Patreons and Supporters
- All custom character now has "disallow_random_traits = yes " and "easter_egg = yes" so we know not to delete them
- Hippogryph Knights were non-patrician, so patricians now have one
- Players will only be given one apprentice at a time and can reject the choices given to them. AI will also be preferred as a teacher for new students
- Chaos Cults and Cult of Pleasure where missing check on Rank 1 being full, could lead to performance issues especially with Cult of Pleasure membership becoming ridiculously high
- Added new rank 5 power for colleges, lets you add a single building to your demense that gives minor benefits and fixed a few localisation errors in the colleges UI
- Added new Equipment Requisition for colleges at rank 2, lets you buy some artefacts using society currency that aid in spell casting
- Fixed a few text errors and a bug with teaching starting twice for colleges
- Fixed Vrodjik having 2 education traits
- Added Official-Submods.zip to the SVN
- Added notification event when getting a mutation
- Changed hedge wizard combat rating(cr) to +1, hedge witch cr to +5 and warlock to cr +10
- Made colleges a bit easier to create if being created by a magic using ruler
- Reduced chances of characters joining a newly formed college as an apprentice
- Added a chance a new college will be named after your dynasty
- Characters from realms without legal magic will not join a magic college founded in another realm
- Fixed cathayan_kow_tow_pilgrimage decision popping up for chaos
- Fixed Chaos bug with convert_to_feudalism_vassal, and Remove SoA event trigger on birth
- Fixed a bug where the Norscan government became theocracies, I had to make a 2nd government for norsca that was "Feudal" but its tribal in all ways, Its called Tribal Baronys
- Fixed Gork and Mork traits
- Fixed some validator errors with broken file parsing
- Added extra descriptions to black crusade to explain hardcoded restrictions on land distribution
- Made most common CBs invalidate if the target is the defender of a black crusade,
    > This is due to the fact the join war commands are extremely limited and will only join the first war in the list for the defender
    > By invalidating all other wars when the crusade starts we ensure others who join the defence from other order religions will always join the correct war
- Added the Mutation Overhaul
    > Adds 400 new traits removing the old mutation in the process
    > Adds a ton of new scripted_triggers the most interesting being the mutation counter which check to see if your mutations equals your health
    > Adds a ton new scripted_effects including a mutation table in general and one for the 4 gods of chaos, a toughness test to see if you get a mutation, and a script for chaos spawn
    > All mutation events were either removed or reworked including adding a new event to become a chaos spawn and become a forsaken which is mutually exclusive depending on if you are a champion/chosen of chaos or not
- Moved the Under-Empire
- Resized Araby
- Artifacts now only spawn at game start for characters with less than 2 artifacts
- Some fixes to cathay events
- Nerf to artifacts and they now tier 1-10
- Witchhunter Court Issues resolved
- Localization Fixes
- Changed Alith Anar and his shadow warriors to a landed title with a special succession
- Added in the Witchhunter society!
------------------------------------------------------
Legacy_v1.3.1:
------------------------------------------------------
- Khalida can no longer take off her mask.
- Restored the magic power lvl up system
- Renumbered the Mootlanders
- Gave the Red Dukedom the same military succession as brass legion/antoch
- Lots of Greenskin changes and fixes
- Refined the AI acceptance for the alliance system with a standard opinion calc, diplo calc and if either character can use a claim/dejure claim on the other
- Added an icon for Subfeudalism
- Fixed Marche Orcale title creation requirements
- Removed 2 unmentioned events from on_actions by codename DAWI
- Made it so you cant send more courtiers to holy order if they are above 50 courtiers from ai courts (and generaly made ai prefer actually bit militaristic people to send)
- Adjusted the setup to randomize magic power
- Satan child event chain conversion from vanilla cults to Warhammer cults,
- Removed rank up block from the lodge/warbands
- Forced recruitment event adjusted to include the Runesmiths
- Fixed Red Dukes 3 spacebar name into 2 space bar name
- Blackstone event localization
- Mounts event fixes
- Assigned ssildra to a geographical region
- WAAAAGH edits
- Added Sympathy checker for vampiric influence and the Ogre vs Chaos dawi to the alliance system
- Refined some of the new Undivided System for Chaos
- Added unique art for the orc/goblin wonder upgrades
- Repaired the Fatandira Bloodline
- Repaired and updated the Cathay offmap power with new interactions
    > can now request unique courtiers that when combined can be used to create terracotta retinues
    > Cathay interaction is now dependent on the status of the coiled covenant and the Dragon Isle
- New "Employ Courtier" Decisions for the orcs to replace the vanilla options
- New "Awaken Ancestor" Decision for the tomb kings allowing you to awaken long lost/dead members of your dynasty to aid you in ruling your realms
- Added the Frosthoime Lodge
- Overhauled the Ice witches and Ice Hags
- Finished the Ice Witch society
- Restored the Western Oblast and the Roppsman kingdom
- Added the Kreml wonder upgrade to the Ice Palace
- Reworked the kislev hidden event
- Reworked Learning Ice Magic
- Overhauled the Kislevite melting pot events it now spreads dynamically from kislev
------------------------------------------------------
Legacy_v1.3.0:
------------------------------------------------------
- AI now much more likely to build forts within their own lands
- Custom Smoke GFX added on the world map
- New Interface Overhaul!
    > New Formatting of main screen and custom buttons for nudge and gameinfo
    > Game Rules at game start now show a list of 8 instead of 6
    > Custom Character interface focusing on information flow and accessability
        - Pagan, Muslim, Indian, Vanilla interfaces complete. Custom ones can be done later for unique races like orcs/chaos
- Ruler of Antoch made older, to match his traits
- Daemonic Incursion and Everchosen Invasion marked holy_war. limited attacker battle warscore to 25.
- Fix for diplo icons showing bugged in interface diplo popups
- Got rid of Combat Rating from Magic Potential so you cant tell who has it and who doesnt.
- Fix for black crusade bug, removed fail_trigger_effect and now religion head titles cleanup when the original black crusade caller was overthrown or died is simply done on a yearly pulse
- AI Everchosen appeared far too early. Moved it to an on action event, after 150 years and doom requirement at highest. with this the everhcosen apearing is more "fixed timeline"
- Cursed Artifacts are now destroyed on death instead of forever cursing your Dynasty
- Slight change to the cursed artifact bleeding hands (defense debuff instead of damage)
- Fix slaanesh artifact absurd tax modifier
- convert_to_morrian_power_desc will now display the text correctly
- Cleansing undead will no longer tell you unknown location
- Necromantic religion can no longer purge the undead in their land now
- Fixes Dooming and Star Signs and adds Quickening which is the ritual of a child becoming an adult in the Empire
- Expanded the triggers for quickening
- You can no longer get all 5 marks of chaos at once
- Fixed Crafting an Ice Sword giving you money
- Nehekkans now use Lahmian portraits. (Nehekkans were still using vanilla portraits, temporary fix)
- Fixed Banner of Avelorn GFX
- Small fix for make_pet_consort - It will now go away after theyre a concubine
- Will now lose incapacitated_tomb_king if conquered by a non incapacitated_tomb_king Tomb King 1 month later instead of 5
- You can no longer curse someone who has no land to prevent you from cursing their liege
- Fixed vanilla demand religious conversion which was mistakenly reenabled sometime in the last few patches due to an error when changing the ai acceptance defines
- Added "Knights of Bretonnia" as a Society replacing the old system of Grail Knighthood
- Added a "Blessings of the Lady" offmap power for Grail Knights
- Added a new Bretonnian election system in which only Grail Knights can be elected to Rule Bretonnia
- Added a Caste System to Bretonnia
- Added the Virtue of Chivalry, 14 Virtues of Knighthood, Virtue of the Quest, and Virtues of the Grail
- The Green Knight will now come to your aid if your the king of Bretonnia
- Reworked the Green Knight combat, its no longer based off your Personal Combat Skill and is now based off whether you are a good or bad Knight
- New version of skaven reproduction event that only counts living children
- Dynasty changes for Hochland and Ostermark
- Reworked all Societies (not events tied to them just the primary society code)
- Restored the Cult of Verena Society
- Created an Ice Witch Society for Kislev (Currently just the framework)
- Rebalanced Starting Retinues of the 3 Emperors so Otillia is more militarised and Reikland is weaker
- Repaired the voting system for The Empire
- Adjusted Technology Balance in Bretonnia
- Overhauled Brettonnian Buildings for Castles, Cities, and Temples
- Overhauled Brettonnian Retinues
- Overhauled Tilean Buildings for Castles, Cities, and Temples
- Overhauled Estalian Buildings for Castles, Cities, and Temples
- Overhauled Myken Buildings for Castles, Cities, and Temples
- Overhauled Tilean/Estalian/Myken Retinues
- Added a Generic Cannon retinue for imperial factions
- Artillery Retinues now have light infantry crews to protect them and provide some more survivabilty in combat
- Buffed The Red Duke a bit to compensate for the Bretonnia overhaul
- Added a Chapter of the "Knights of Morr" to Luccini. they now hold the Raven Theatre
- Overhauled the Mount System
    > Mount Upkeep
    > Province Modifiers such as grazing land or races etc.
    > Breeding and Death
    > New Mounts w/ GFX
- Made changes to Bretonnia History at game start
- Made changes to Nehekhara History at game start
- Chaos Offmap Sacrifices now only work on people in your own dungeons
- Balance Fixes to Chaos Retinues
- Some additions and reworking of chaos retinues
- Added The Ability to Become a chaos chosen of Undivided
- Added The Ability to ascend to daemonhood as Undivided, Though it is far more difficult
- Lowered Some of our highest Char-ids in an initial test of an upcoming performance overhaul. **Fun Code Snippet** 666 - Devil Child Highest Character ID formerly 7902205 DO Not Change ID (Deadliest Income)
- Reworked some of lustria to make it more interesting to play there especially along the coasts
- Map changes in Bretonnia
- Map changes in Mountains of Mourn
- Map changes in Lustria
- Map changes in the Empire
- Added a **REDACTED** society. but we dont talk about it
- Added more dynamic Titles in Bretonnia and a slight government rework
- Reworked the Drakwald
- Added the Eonir Woodelves
- Reworked the Easy / Normal / Hard / and Very Hard AI
    > easy_ai -
        attrition = -0.25
    > normal_ai -
	   max_population=1000
	   max_manpower=500 #To Avoid Disbandings
	   retinue_maintenence_cost=-0.1
	   horde_maintenence_cost=-0.1
    > hard_ai -
	   max_population=1500
	   max_manpower=500
	   land_morale = 0.25
	   retinue_maintenence_cost=-0.2
	   horde_maintenence_cost=-0.2
	   global_tax_modifier = 0.1
	   levy_reinforce_rate = 0.5
    > very_hard_ai -
	   max_population=2000
	   max_manpower=500
	   retinue_maintenence_cost=-0.3
	   horde_maintenence_cost=-0.3
	   land_morale = 0.5
	   global_tax_modifier = 0.2
	   levy_reinforce_rate = 1.0
- Added Separate Culture Modifiers depending on your Bretonnian Culture
- Added negative Supply Limit to Chaos and Norscan Culture Modifiers
- Added winter supply to Kislev and norscan Culture Modifiers
- Expanded on Orc Culture Modifiers
- Expanded on Goblin Culture Modifiers
- Expanded on Ogre Culture Modifiers
- Added many more custom bookmarks
- Added Slave Mines and Such for Trade posts for Chaos Factions
- Added buildings for Forest Goblins
- Added The Phoenix Guard with a unique building(May become wonder instead) and more!
- Orcs can no longer use the beastmen cleanse CB
- Made CB changes for pagan conquests
- Made CB changes for county conquests
- Made CB changes for freebootas
- Lords Bordering Elves can declare war to take pieces of forest
- Added two new Dawi cultures to the dwarf culture group
    > Southron dawi
    > Grey dawi
- Added two new ogre cultures to the ogre culture group
    > Irongut ogres
    > Firegut ogres
- Added iron orcs to the orc culture group
- Added hill goblins to the goblin culture group
- Changed AI Raid aggression
- Enabled Execution of imprisoned characters for all AI
- Overhauled Orc, Eonir, and Forest of the Old world Dynasties. Including many new easter eggs
- Nerfed plot power against characters outside your "faction" by 25%
- Added alot of Flavour for the Brass Legion
- Reworked Dawi Guild Governments
- Added a new special unit type - Critters
- New WAAAAAAAGHHH!! system
- Myrmidia is now a Pentarchy
- Created a new Military elective system for the south realms
- Applied new military elective system to the knights of antoch and the brass legion
- Created command modifiers for Impassible Mountains
- Removed martial from berzerker trait as  its meant to summon daemons as a "spellcaster type"
- Added martial to all daemon traits, not just khorne
- Added AI greed to the human trait
- Added negative opinion of Greenskins to the dwarf trait to ensure they hate them no matter what
- Added positive opinion of is_fat to ogre trait, lore of course
- Added Different Orc & Goblin Boss traits
- Added Lore of the Maw
- Added Firemouth Ogres as special Ogre Mages
- Added Ogre Slaughter Master
- Reworked Ogre Maneaters
- Reworked Vampire and Tomb King Opinion modifiers
- Ropsmann can now use the eldership succession law
- Added more Dawi Karaks
- Added The Shrine of Asuryan as a wonder
- Added Tor Lithanel - The Silver City
- Added Orc Wonders
    > Massif Orcal
    > Iron Stronghold
    > Arachnid Lair
    > Greenskin Stronghold
- Creating the De Jure Drakwald is now far more difficult
- Stromfels followers can now also recieve strigany caravans
- Pirates/Corsairs/Norscans can now Pillage a Holding
- More Tech changes in the History Files
- Added a Daemonsmith society for Hashut and the Chaos Dawi
- Added 2 Greenskin societies
- Added Droyaska minor title to kislevites
- Overhauled Ungol Buildings for Castles, Cities, and Temples
- Overhauled Ropsmann Buildings for Castles, Cities, and Temples
- Overhauled Gospodar Buildings for Castles, Cities, and Temples
- Overhauled Kislevite Buildings for Castles, Cities, and Temples
- Overhauled Norscan Buildings for Castles, Cities, and Temples
- Minor changes to Ungol/Ropsmann/Gospodar/Kislevite Retinues
- Added the song "Dread Cargo" from the new soundtrack
- Made some minor changes to AI weights for Character Focus
- Reworked AI weights for childhood focus and the education focus will then be chosen based primarily on the traits the child has developed. Mostly based on RP:
    > Pride: used for rulers, heirs, and close family members of rulers. Used less often for girls in agnatic realms and boys in enatic realms
    > Humility: used mostly for lowborn children and bastards
    > Etiquette: used mostly for children of a noble dynasty in feudal, republican, and theocratic courts. Used less often for girls in agnatic realms and boys in enatic realms
    > Duty: can be used for any child in a feudal or republican realm
    > Thrift: used mostly for children in republican realms and in realms ruled by a scholarly liege
    > Struggle: used mostly for nomads, tribals, bastards, and lowborns
    > Faith: used on infidel children or if liege is theocratic
    > Heritage: used to educate children who have either different culture or different religion than their liege
- Added a few new congenital traits
    > Fluent
    > Melodious
    > Resilient
    > Frugal
- Added a few new hidden traits
    > Psycopath
    > Romantic
- Limited the new JD tributary CB a bit like the original
- Fixed the special events tied to the "Organist of Praag"
- Set up the "Winds of Magic" or "Mana" generation for magic users, it refreshes yearly and can vary depending on your level of magic potential as well as the strength of the Winds of Chaos
- "Channeling" has also been implemented using this variable system, in case you need a few extra spell points
    > careful though, there is a small chance of a miscast or even devolving into a chaos spawn when doing so
- Overhauled the history at game start for the kislev region of the old world
- Battle magic for the lore of ice now varies in strength depending on the weather of the province
- Brightened the elven castle GFX
- Beauty inheritance event was scoped to the recognized father rather than the biological father this has been fixed
- ruinous_standard.dds - Missing - Replaced with tattered_banner.dss for now, was using nothing before
- Remove chalay.dds and chalay_small.dss and add chayal.dds and chayal_small.dds
- skaven_warpbomb.dds - Missing - Replaced with skaven_smokebomb.dds for now, was using slayer_of_kings.dds before
- deathmaster_sigil.dds - Missing - Replaced with nightlord_sigil.dds for now, was using slayer_of_kings.dds before
- wand_kharaidon_morathi.dds - Missing - Replaced with GFX_heartrender_darksword_morathi.dds for now, was using nothing before
- amber_amulet_morathi.dds - Missing - Replaced with dark_fire_amulet_hellebron.dds for now, was using nothing before
- GFX_war_bear_mount > GFX_war_bear
- Spite artefact added
- Text changed and added for numerous artefacts
- Stopped vampires joining magic colleges and made it so you need magic already legal to create a dynamic college
- Reworked province borders for the new wastlenad province in the kislev region - crags of shargun
- Fixed ork COAs
- Added the new track for Nehekhara
- Fixed Trade Routes
- Updated Skaven events related to requesting land. Should make it much less annoying
- Added a unique bloodline and history for Fatandira in the borderlands as an easter egg reference to Warhammer Fantasy RPG 2nd ED -- Lure of the Liche Lord
- Updated a few Bretonnian CoA
- Now when youre more than a Marquis in Bretonnia, you can hire Knight Errants, the king of Bretonia can hire all Knight Errants and when you have Marcheur culture, you can always hire the Marcheur Knight errants
- Created Black Grail Knights Under the Red Duke
- Society membership and Minor trait gain changes
- Integrated the Naval Combat Module. Allowing fleets with embarked armies to clash with enemy fleets, Some factions can even attack neutral ships!
    >simple ping event fires to set targets
    >then naval battle commences
    >chance to get an admiral and leadership trait
    >as well as pirate/viking if you plunder
    >druchii, pirate gov, freebootah gov, norscans can all plunder even neutral ships
    >Plans to expand with duels and black arks etc.
- And much much more!
------------------------------------------------------
Legacy_v1.2.9:
------------------------------------------------------
- aicleanup.023 Cleared out Slayer King Trait, Also this event breaks the New Mechanic with Warriors/veteran Dwarf warrior training, added blocks if they already have those traits
- Finally added mass Sacrifice of Prisoners (For Lowered  Offmap power points) took a moment to fix it actually counting prisoners
- Removed knightly order/dawi Access to sacrifice Button If the captured Person is Neither: Orc, Skaven or Goblin (IE Creature Beyond Redemption)
- Adjusted martial Req. for Ulricans
- Removed The Reaver Bonuses From Dawi and the Knight Orders as they are illogical, gave them some extra power to capture lords
- Replaced FROM.FROM Localisation scopings to FROMFROM. so it actually tells the settlement name
- Fixed minor clan uprising, earmarked to disband the Event troops and give a few to replace them
- Allow Champions to be hired by daemon princes as well
- Some Favour bonuses from completing the blood tournament and winning, (500) and removed mentions of the old khorne favor system
- Adjusted the Commander Limit the bigger Horde you have, also doubled the cost to build the primary building chain
- Similiar thing done for Beastmen, tied to bloodgrounds for now
- Fixed the siege defense modifier which does not work to begin with by replacing it with flat fort level
- Lowered some Init tech requirements so the areas with 0 Tech are not completly empty for beastmen
- Added a new minor title for Kurgans
- Completely balanced the chaos traits from marks > champion > chosen > princes
- Removed Access to Chaos Knight trait as a Demon of any kind
- Added some Slaneeshi special female math to capture men in sieges over women
- Fixed The Legends Events
- Fixed call to glory
- Fixed Courtiers having multiple Minor Deity dedications
- Allow impaler warrior lodge commanders to swap out
- Changed modifiers from Owner to Local effects (Similiar to watch towers) for Karaks & Chaos Fortresses as they are not Per-say Unique
- Small changes to the Zanbaijan wonder
- Fixed greenskin item purchases
- Fixed make land green decision
- Enabled Black orc Culture heirs ONLY IF YOU ARE ALLREADY BLACK ORC CULTURE! So you cant go swapping as normal orc to black orc
- Modified the code so the Chaos Waste nomads Wont ever Raze Tribes/Castles of their own Culture/Religion for the AI, player can still do what they want
- Now vassal occupied territory is counted towards expansion
- Added a "Settle Tribe" decision similar to the "Become Nomad" decision
- Stopped newly independent realms occasionally going negative in prestige/piety for setting default magic laws
- Fixed loc of gender swapping creatures
- Overhauled the chaos razing events to stop the crashes
- Allowed Beastmen to join which ever society they want, provided they follow chaos undivided, and access a decision to use the society to convert religion
- Warband general Member score & point generation tweaks
- Hindered early expansion for daemons, Limited the range of Nomad Subjugation as well
- Removed Execution Death type as countable towards murder bloodline
- Pirate Ports now apply a negative to global trade value
- Karak Dum now accessable by land
- Fate of Karak Dum flavour events added
- Added both Beastmen & Chaos Horde Retinue Events to help the ai handle army comp
- Delyan-Graf River adjency added
- Adjusted Special unit maintenence values
- Added a small bit of tax income to norscan buildings until I can get to the overhaul
- Tweaked Artifact modifiers
- Fixed Tlaqua, Under-Tlaqua, & Uzkulak history files
- Fixed for chaos_host_government to call in their vassals
- Fixed midnight_aristocracy from directly raising troops from the elector counts
- Added more generic chaos artifacts to chaos off map lists
- Other chaos cults should no longer get khorne only missions
- Removed the command moddifiers from carsteins ring
- Gave vlad_subjugation cb the holy war flag and limited warscore of battles to 25%. Due to making a holy war flag the defenders have a +40 opinion of defending against infidels
- Changed kemperbad to a merchant republic
- Added starting retinues to several Merchant Republics across the old world
- To Throw off the Witch hunters & Vampire hunters looking for cultits we hid several modifiers and traits from everyone except friends and yourself
- Added a way to decide wether to contain yourself as a cultist or to act freely
- Disabled Imperial reconquest CB against races that would result in vassalization/have Better CB to use against (IE Beastmen or Greenskins)
- Added active despoilment while under despoiler invasion
- Created a subsection in decisions similar to hiring courtiers. This contains QoL decisions to hide racial traits and star signs as well as the info event for the star signs if youd like to learn more
- Added in some pirate stuff including a minor title to designate your heir
- Localisation fixes
------------------------------------------------------
Legacy_v1.2.8:
------------------------------------------------------
- Druchii watchtower bonuses modified
- Druchii court size bonuses removed
- Fixed sound effect for warriors of ulric. It had satanist sound effect before
- Allowed Atruhayid (Ormazdic) pirates to exist and practice piracy
- Added lores to the Tzeentch and Nurgle princes. Fixes a magic power reset bug
- The Chaos Destrier now uses GFX_dorghar
- Chaos Dwarfs who worship Chaos Gods other than Hashut will now correctly use Chaos Court
- You can now take any courtier as your apprentice, disabled the decision or the ai
- Moved special building for lothern to the top barony
- Artifact quality tiers quickly rebalanced to be 1-5 as the ai seems to treat 5+ artifacts as quality 1
- Gave a form of diplomatic immunity for mage family members of rulers in realms with legal magic going abroad
    so you can marry your kids off to foreign realms or send them to university without them getting executed
    This also has the benefit of making other realms more tolerant to magic once they have a spouse with magic
- Universities will also never care about mages in their court
- The global flag triggering on magic being legal for 50 years will now correctly display the event saying so to the player
- Mercenaries and the Witch Hunters will become tolerant of magic after the above global flag is set
- Added a cb for realms to force magic laws back to the Traditional on other realms, this can also be used by the Witch Hunters until the above global flag is set
- New realms and vassals who gain independence will get magic laws set sometime correctly sometime within the year by a maintenance event
    the game may sometime ignore default selection for laws you cant have as a vassal becoming available on gaining independence
- The random chance to become a mage for new character will wait a few days so traits are fully assigned by characters created by event
    this will prevent mage witch hunters and multiple lore traits
- Added an event when your court mage dies or retires, assigning a new court mage will also make them pick up any leftover apprentices from an old mage dying
- The court mage and mages with apprentices gain magic xp every year
- Mage commanders will stop casting when their flank starts retreating
- Everchosen_exists flag no longer is set on game start, this will allow an Everchosen ai appear
- Events also tweaked so killing an ai everchosen will not make another appear for some decades
- AI will join warriors of ulric correctly
- High Elves can now use the county and duchy colonisation cbs against Dark Elves
- Ai joining chaos cults will have secret religion set correctly
- Corrected trade post in border princes to be in Kypur rather than the county next to it
- Ai will take the chaos artefact and army boon 100% of the time if they have over 5000 favour
- Duels will no longer consider fighting 50 years + immortal races dishonourable, fighting beardlings and elven scions/maidens is now considered dishonourable
- Removed "Gunnery school" building appearing in kislev culture group holdings
- Added the ice lore to the magic mutation exclusion,  Ice magic does not carry the same risks of mutation
- Added in Henri le Mastiff to Repanse in northern Brettonia with his own dynasty
- Some triggered_gain scopes werent properly functioning for the new Ulric warrior lodge
- Fixed the Lack of saurian commander access for saurian rulers (Gor-rok)
- Added magic_archers special unit type to the game similar in power to gunpowder units
- Ice guard retinues added to kislev
- Sisters of Avarlorn retinues added to Ulthuan
- Converted the wonder flavour events
- Adjusted our custom defines slightly
- Added Ogre Artifacts
- Wiki link added for Henri le Massif and Tzy'y
- Tzy'y now has elusive_shadow instead of intricate_webweaver to match with the other daemon princes
- GFX for Henri le Massifs artifacts added
- Chaos can demand close relatives who are courtiers to convert to chaos, otherwise chaos uprising tend to die out if they survive after the first generation
- Adjusted black crusade declaration to encourage more to be declared by the ai champions and chosen
- You can no longer pledge to the black crusade multiple times during the prep stage
- Due to limitations in join_defender_wars only ever joining one war, a temporary alliance is created between the defender and all realms who pledge to help
    An opinion modifier is added to allow them to be called in for the war
- Added a triggered modifier for all landed followers of chaos when doom is at high or very high levels providing a boost to levy/population/manpower
- The Everchosen will no longer get rid of their mark of chaos by taking one of the lesser 4 marks
- Troops boon for offmaps is checked more frequently and will check if they are primary attackers or defender or part of a crusade
- AI everchosen dying will prevent another spawning for 100 years
- Fixed issue with characters passing mage training despite having no magic potential
- Fixed issue where training could continue forever after becoming a mage, leading to near 100+ learning
- Added a backup event for magic laws when the civil war fails to fire due to nobody hating magic in the realm/being willing to start a civil law over it
    This will have the same effect as winning the civil war with a slightly different description
- Magic legal bloodline no longer gives prestige so the effects dont overflow the ui
- Grudge wars now correctly give piety when won against racial enemies, the ai will also not declare them against those holding land in de jure Karak Ankor or Drak Ankor
- Removed ability to view offmap cathay for chaos relgions, as otherwise chaos undivided in Araby cant access all four offmap chaos gods
- Peasant and religious fanatic revolts will apply the recent uprising modifier to the province correctly
- Monster hunting plot and events now use holy fury duel engine for the actual confrontation with your target
    Assassination and fighting through to your target still depend on traits though combat rating is taken into account now
- Coronation events now work for cult of Morr and getting crowned will no longer check investiture laws for non sigmarites
- religious head asking for a title to be given to a holy order will now only ask for a county and never the capital
- Daemon Princes can now hold temple holdings
- Adjusted the Holy Sites for the Chaos Religions
- Adjusted chaos cults to no longer allow morrians or arabyans
- Split Mousillon from Bretonnia at game start
- Added black orcs to the Irrana Mountains as a nod to the old lore of "iron orcs" rumored to be living there
- Added portrait to who is getting married to who with the elven courting events
- Merged the armoury project
    this adds "hire smith" equivalent events for several key races such as Greenskins and Aelves
    as well as one of our most requested features. **Runesmiths!**
    there are now several runesmiths seeded into a few courts as well as several lore friendly playable rulers
    this also includes a runesmith society and a host of new artifacts! (just as we had GFX for all of the new ones we add more)
- Added a maintenence event for the slayer king trait to be inherited
- Added a few more fimir to face the norse dawi
- Made changes to norse dawi history files to be more friendly
- Fixed potential crash in crusade sieging events
- Fixed issue with sometimes not being able to target certain rulers with crusade cb
- Doom Reduction from losing a Black Crusade tripled, from playtesting once doom hit max otherwise it would just stay at max forever
- Creating Morr religion head will now give them a holy site to ensure they are a theocracy and make them a vassal if you are empire tier
- Random Greenskin attacks will no longer attack your capital instead preferring to aim for fringe provinces
    usually in terrain such as wasteland/mountains/forest and that are bordering other realms
- Allowed prestigious Chaos rulers without a mark to convert to Chaos Undivided
- Quick fix for Druchii Hydra making it unbearable to play around the Naggaroth (will hopefully repair the hydra model in the future)
- AI building of hospitals adjusted to be much more likely when the ai has a few thousand gold sitting around
    should act as a money sink for dwarfs and single county rulers who have trade posts, etc. over a long game
- Fixed the Pilgrimage for beastmen to remove the travelling trait properly
- Completely reworked positions.txt for the Chaos Wastes
- Rebuilt the chaos wastes from the ground up
    >Moved holy sites
    >Shattered Realms to add approx 3x as many chaos lords
    >Diversity in characters created
    >Many new easter eggs and unique warlords
    >Diversity in Government types used
    >Reworked character history to fix half the chaos characters being in dynasty 0
- Limited doomings, and converted to an on_action 5 year pulse
- Limited religious conversion demands for fuedal governments
- Fixed a few Government bugs from the rewrite
- Added a Temple holding to the Ragged Maze since it is now a holy site for tzeentch
- Mercenaries can no longer buy/sell from the chaos dwarfs
- Strigany_strife should no longer stack
- Changed Gor-Rok from morale offence to defence
- Removed the Beastmen capital refill decision as it was ai only anyway and they seem fine balance-wise currently
- Duelling vampires over the age of 50 is no longer considered dishonourable
- Fixed Invite Child to Warrior Lodge/Warband Decision
- Fixed missed entry for Cancer Age calculation, adjusted it
- ai everchosen now gets the mark of chaos
- Everchosen trait gets same health boost as chosen
- Beastman can end up as vassals of other govs when a beastman child of a human chaos follower inherits, which could cause weird bugs
    added an emergency backup decision to make them independent if this happens
- Added a chance of become a chaos spawn from using offmap boons. Chance is reduced by being a chosen/champion and full eliminated by being a prince/everchosen
- Modified the retire with harem event to add in uncouth instead of content
- Fixed river not connecting properly in Bretonnia
- Greenskin Culture Conversion Adjustment for Black orcs (Through the Make Green Decision)
- Disabled Mass Conversion into Black Orcs
- Adjusted the "Make Green" decision to finally stop being able to reconvert yourself as a Black Orc and allowed Black Orcs to convert other sub cultures with the decision
- Allowed Black Orcs to construct black orc buildings
- Limited Dawi from teaching themselves magic
- Daemon Princes no longer have acess to the conquest CB as they use the chaos incursion CB
- Updated trees.bmp
- Rebalanced technology levels across the old world
- Limited the tributary and holy war CB
- Empire minor titles "Reiksmarshal" and "Champion" now grant the proper runefangs to the title holder and not the Emperor
- Disabled Armoury Great Work Events as an option for Invite Smith for now
- Added A warrior society for the Dawi
- Added the Knightly Brotherhoods society for the empire to help offset the warbands of chaos
- You can now become a chaos knight once you at least rank 2 in any chaos warband, using a targetted decision
- Decadence events should no longer fire for just the ormazd religion group
- Fixed gift timers for the offmap powers
- Localization fixes
------------------------------------------------------
Legacy_v1.2.7:
------------------------------------------------------
- Fixed chaos artifacts to be useable for norscans etc.
- Completely overhauled government files to be less rigid and allow for more fluid gov transitions
- Files cleanup
    > Did a profile on events running over 2011-2017 using debug_events and debug_dumpevents
        - Moved worse offenders of MTTH events that were firing tens of thousands of times, to on_actions.
        - Made triggers better so they wont fire when not needed
    > While most of these events where very simple and it doesnt seem to have any performance benefit at game start. (at least on my pc, which is overkill for CK2, lower end ones may differ)
    it may be more useful as the game goes as on and more characters are generated due to the benchmark showing 467407 events firing vs 775780 during the testing period.
- Changed a lot of NOT = { trait = incapable } to is_incapable = no, as now any trait can make you incapable
- Chaos cultists sneaking across borders to a non-chaos realm now also effect ormazdic
- The event will also use existing unimportant courtiers in the chaos realm rather than generating now ones
- Chaos cultists will have suspicion modifiers removed when starting an uprising
- Black Crusades vs the Norse-Dwarf holds will have defenders much less likely to join unless they hold land in the Kislev or Norsca Regions, Norse Dwarfs are also guaranteed to help each other
- Lustria Jungle 2 modifier no longer gives more revolt risk that Jungle 4
- Lizardmen now access "settle tribes" action to allow them to spread thier culture and religion
- Dark Crystal event now correctly more likely to fire when you have the necessary criteria rather than less likely
- Star sign events are now fired on the racial trait assignment effect
- Fixed Fimir born after a parent died having human portraits.
- Holy Fury fat/thin events can trigger for characters over 55
- Dwarfs and Elves now have a temporary fertility modifier applied after having child
- Magic lores give a minor bit of health
- Chaos Champions, Chosen, and Princes will no longer become incapable for decades due to health boost
- Adjusted the Unjust Conquest CB
- Changed warband mechanics to allow other warrior lodges as well
- Added Ulric Martial society/Warrior Lodge
- Orc and Beastmen uprisings no longer cancel the "see the realm prosper" ambition, same as basegame rebel wars
- Fixed error with racial fertility system not working
- If the top liege of a realm is a mage (even if its technically illegal) the witch hunters will no longer be able to seize your vassals and courtiers and burn them
    you still get massive opinion penalties for letting your kids live so its still basically mandatory to get the laws passed
    Letting people with magic potential live when its legal will also no longer make people suspect you are a chaos cultist
- Added Morr as a major religion. with its own holy orders and society
- Added a dooming mechanic
- Fixed beastmen despoiler trait
- Beastmen Brayherd Mutation Boon now properly checks current mutations
- Added population bonus to Mourkhain Wonder
- Added "add_beastman_artifact_effect" for the Pilgrimage
- Added a scaling "defensive_plot_power_modifier" to beastman horn traits
- If a chaos nomad uses the claim horse decision they will get a chaos steed artifact
- Mage learning will stop when the variable magic learning reaches 20
    - Added in a 50% chance to have the mage events happen in 200 days, with a random chance of adding 75 days ( other 50% is 250 days adding in at random of 125 days per event tick
    - You also can gain extra magicxp with event choices, Currently linked to the most rare changes
    - You will not graduate if you are a minor (if you reach magic teaching 20 you will get events that give you a small chance of getting xp until 16 years old)
    - At 16 Then the event will fire to test you.
    - If you somehow started later, learning magic will force you to stop at the age of 25 and force it to test. Lets hope you can pass
    > Pass chances:
        trait/flag = magic_potential_1 pass value: learning 18 or magicxp 20
        trait/flag = magic_potential_2 pass value: learning 15 or magicxp 17
        trait/flag = magic_potential_3 pass value: learning 12 or magicxp 15
        trait/flag = magic_potential_4 pass value: learning 10 or magicxp 13
    - altered the age limit a bit.
- You can take childeren up to age of 25 as mage apprentice
- Almost all artifact GFX should be complete
------------------------------------------------------
Legacy_v1.2.6:
------------------------------------------------------
- Fixed Pillage Beastman Decision
- Slightly buffed beastmen buildings
- Fixed Beast Paths localization
- Adjusted Beastmen CBs
- Added Despoiler trait and bloodline for beastmen
- Removed Duplicate Akendorf
- Slightly lowered beastman commander limit
- Fixed Gor-Rok turning Feudal on game start
- Blocked Beastmen from traditional Chaos Raid CB
- Overhauled Beastmen event pics
- Polished the Beastmen Pilgrimage
- Fixed Gui error (damn hardcoded GUI had to recreate the tribal interface)
------------------------------------------------------
Legacy_v1.2.5:
------------------------------------------------------
- Must be a Chosen in order to summon a champion from the offmap powers
- Kislev Retinues have been overhauled to bring them in line with the nearby factions:
    - Zastyvshiy Warriors, archers and light infantry with a 40% offensive and 20% defensive/morale bonus
    - Kossars, light infantry and archers with a 20% offensive/defensive and morale bonus
    - Kremlin Guard, Heavy infantry and Pikemen with a 20% offensive/defensive and morale bonus
    - Svistyashchiy Cavalry, light cavalry and horse archers with a 20% offensive/defensive and morale bonus
    - Pochtennyy Warbears, heavy cavalry and war beasts with a 80% offensive and 20% defensive/morale bonus
    - Slavnyy Winged Lancers, light cavaly and heavy cavalry with a 100% offensive and 20% defensive/morale bonus
    - Urugan Cannons, artillery with 100% offensive/defensive bonus
- Added "Exalted Hero" minor title for all Chaos and Norscan Rulers
- Added the Bokha Palace wonder for Kislev
- Added the Praag Opera House for the ungols/kislev <-- This is going to be fun
- Tribal Shipyards require lower tech levels to build
- Removed 1 of the castle baronies from Antoch
- Beastmen trait fertility bonus lowered from 50% to 20%
- Adjusted chaos retinues
- Allowed a few more commanders for beastmen
- Nerfed Herdstone Building
- Restored the on_action witchunter event to hunt down lahmian brothels
- Dark Crystal Ambition event converted to a decade pulse on_action
- Malekith and Fay Enchantress can no longer join the Cult of Pleasure
- Fixed the reclaim the staff of jade cb
- Changed Jozans concubines to be chaos undivided instead of Slaaneshi and Tzeentch
- Stopped The building option for non-owned provinces for warpstone meteors
- Fixed Warband Nicknames
- Adjusted the Duel Calculations
- Made kislev absolute cognatic
- No more female inheritance for kurgans
- Norscan religion is now feminist
- Made kislev have full status of women law
- Made fearfrost compatible with our current tiers of weapons
    - Also added a female requirement in as of the lore
- Gave the Kislev Queen higher magic potential
- Also gave her current heir magic potential
- Made vampires visible in the Ruler Designer
- All Artifacts that had GFXs should now have all their sprites added (Any missing ones is just missing GFX)
- Cold One Mount finally has localization
- "Train a Cold One" can now only be used if you dont own a Cold One
- "Train a War Bear" can now only be used if you dont own a War Bear
- Armour of Fortune now has its localization
- Visible and Hidden Vampire traits are now removed from the RD
- Assigned all of the special traits to their characters
- Custom Rank Icons for Chaos Warbands and Cults added
- Removed the Immortal Trait from the RD
- Added court mage title, the court mage will attempt to teach children in the court magic, can only be assigned if magic is legal generally, or for a certain gender
- Ai will grant this title and the witchhunter title via decision as the ai apparently doesnt hand out minor titles on its own
- Magic inheritance event now checks true_father_even_if_dead, so hidden bastards will get the correct genetics
- The bloodline of Miska the first ice witch makes women much more likely to have magic potential if they are of the correct dynasty and born in kislev
- Removed misplaced is_ruler check from learn magic decision as the intention was to allow courtiers to take it, also edited potential so Araby men can take the decision when vassals
- Magic power modifier now gives combat rating
- Made magic potential much harder to pass on to a child in general
- Lore of ice will no longer spawn on randomly generated mages, its not a wind of magic like the other but a specific practice of magic tied to the land of Kislev
- Magic potential is no longer a genetic trait, we already had an event giving hidden magic potential
- Adult characters who are generated with magic will also have their magic manifest
- Beastmen have a small chance of being born or generated as a bray shaman
- Random elf mages now can spawn as either casters of high magic, dark magic, light lore or shadow lore to match learning events
    - Asur cant get shadow magic or dark magic and vice versa for Druchii
- Rewrote siege magic as siege pulse on action only triggers if there is a commander on the centre flank of a siege, now works of individual mages entering the province
- Changed magical devastation to be a stacking modifier, so longer a siege goes on the more damage is caused by the mages
- Fixed levelling up magic power not setting the cl variable correctly, this is used in the siege magic events
- Amazon males now get fully handled by the racial system and are given the traits to prevent marriage and holding land
    if they spawn in a non amazon court human, e.g. the jade vampire general they will switch culture and religion
- Removed all male amazons landed under a Miyan Halfling liege, the amazon mechanics just dont work with male rulers
- All rebel leaders of amazon religion are now female and tribal government
- Flower wars give much more decadence reduction
- All male amazons in the history files are setup correctly as disinherited
- Amazons can no longer take consorts, as all men are incapable in the culture and incapable men cant get someone pregnant outside of events
- Amazon city holding art changed to be the same as lizardmen, as the non looted amazon one was the same as the looted one and always on fire
- Elven and dwarf fertility is no longer a 50 chance of becoming infertile with every child, the chance scales with number of children and the overall fertility of the mother
    - However even not becoming infertile will take a small amount of fertility away permanently
- Grail knights are now immune to random mutations
- Fixed an issue where witch hunters could go after ice witches
- Temple vassals outside of old world religions will correctly use open elective rather than gavelkind
- You can only duel other members of your race over strong claims
- Chaos rulers can duel each other for strong claims even when not tribal
- Chaos fortresses slightly increase the max population for Nomads
- Gave Prince Fandranrion, one of the main High Elf colony rulers a claim on the other de jure duchy of Arnheim
    - his father was the previous ruler and he has a claim on the non-existent kingdom
- Fixed slaanesh artefact boon making undivided go to negative favour
- All champion and chosen trait have 15 health minimum
- Skulls taken in battle can now be given to Khorne
- Support has been re added for humans having portraits outside their cultures default
    -Certain cultures e.g. Amazon and Albion are exluded due to war paint and tattoos being part of the portrait itself
- Nurgles blessing when you have diseases now also counteracts the combat rating reduction
- Summon Daemon decision removed for those who have access to daemons through offmap powers
- Female orcs and goblins are now given the snotling trait again rather than orc or goblin
- The marriage events now also check for snotling, goblin and orc traits as a few cases of ruler marrying snotlings has been seen
- The Fimir 99% chance to change to male will no longer happen if there are none in the lieges court. This stops the game continuously spawning in new women to be married
- Repaired some artifacts missing slots
- Join Defence Against Black Crusade decision now works
- Lowered combat_rating bonuses across all traits
- Added "beastmen_capital_refill" settlement decision to help Migratory Herds former lands survive
- Fixed some vampire bloodlines
- Added a unique "building" for Daemon Princes
- Fixed Beastman gov Flavour
- Soul Suck decision as a daemon prince now gives 50 prestige
- Added an xp route to becoming a mage
    - if you do not have enough learning you get will need 15xp to pass
    - This ensures if you start training young enough, you could pass
    - But when older your forced to be relied on your learning
    - This is only when you are being taught by a mage. Self teaching has not been changed
    - If you start training too late you have to rely on the riskier experiments to gain high learning
    **WARNING** you could have incredibly bad luck. Thats warhammer for you
- Removed the beastman_baron_cleaning decision and replaced it with the traditional nomad pillage_settlement
- shared offmap decision "claim_chaos_undivided" available for warherds if chaos undivided beastman
- Added negative global_revolt_risk to bretonnian and imperial culture modifiers
- Increased province count in Obo valley
- Overhauled Beastmen CBs
- Placed Herdstones in lore-friendly locations
- Balanced Kislev and Praag unique castle buildings
- Balanced Bretonnian unique castle buildings
- Balanced Norscan unique castle buildings
- Border Princes Confederations are no longer feudal only
- Court Council background GUI now supports 5 council jobs
- Fixed "Guardian of the Deep" minor title
- Brief non-aggression pact now requires only +50 opinion to make alliances easier
- Adjusted Tech Values across the world
- Slightly nerfed the Dawi settlement fort values
- Added the "Dawi Karak" wonder and began adding them to lore friendly locations, still missing **many** though
- Added seige events for chaos ( separate chains for beastmen and traditional chaos )
- Rulers who pledge to defend against a Black Crusade and then convert to chaos afterwards will no longer join the defender
- Made a few edits so siege magic doesnt start till you have been sieging a province for a month, stops you leaving a line of siege modifiers wherever you walk in enemy territory
- Fixed a bug where Black Crusades could sometime not clear down the religion head title after a crusade ended until the current ruler died or 10 years after the initial decision was taken
- Added starting forces for the two landed daemon princes at game start
- Increased learning to 15 for tetyana so that she can teach her childeren. removed magic_potential from an incorrect character
- Matrilineal inheritance is kinda broken, so its now changed to patrinial with our own override
- Balanced Unique Border Prince Buildings
- Fixed missing Brayherd "journey to the dark heart"
- Balanced Erengrad
- Fixed Gor Rok portrait
- Added a "Holy Ziggurat" wonder to Itza, the first of several wonders for the lizardmen
- No holy wars vs dwarfs
- Made chaos less likely to use the chaos raid cb when they have a ton of favour already
- Made the ai willing to use county conquest vs beastmen
- Offmap Favour now resets on death
- Stopped the high elves electing the everqueen or everqueen heir
- All special Dawi buildings are now wonders
- Overhauled beastmen buildings and balanced them
- Herdstones are now unique buildings tied to specific locations
------------------------------------------------------
Legacy_v1.2.4:
------------------------------------------------------
- Added the missing government flavor for the tzardom gov
- Daemons of any type can no longer join Warbands
- Made the Everqueen an Asur Mage with the appropriate Lore
- No Everqueen or Everchild shall join the Cult of Pleasure
- Modified Favour gain amounts to slow progress, this should allow us to avoid cooldown timers but still stop characters abusing the system
- Daemon princes in a warband can now complete their change focus mission
- Asrai will no longer join the Cult of Pleasure if they are exposed to it
- Childrens crusade localisation and bloodline is no longer identical to the base game
- Childrens crusade leader set to chaos court gov if they are a nomad culture so they dont become raiding adventurers, raid someone, get beaten and lose their title
- If a friend of a mage apprentice dies it will check the friend is actually the person teaching them magic before removing the mage apprentice trait
- Mage apprentices can now marry normally
- Ice Witches no longer have a fertility penalty
- The defender of the ulthuan_invasion cb will have direct duke and king vassals who the same culture group and religion join them in the defence, looks to stop Malekith winning every time
- The cheating death mechanic increments a variable on the character so we can see how often they die
- declare_black_crusade logs to a global variable each type of crusade declared through the game
- Fimir caste trait assignment fixed for random fimir
- Fixed Morgrim of c_kholim to properly set historical_nomad = yes to prevent him from going landless
- Believe I have fixed the Daemon Princes culture and province culture at game start
- Created a "become warherd" fallback decision to automatically convert the ai beastmen if needed, and for players to choose to convert to warherd if they have no other way to do so
- Added customizable localization to add you health and fertility value to the character tooltip (shown when you hover with your curser above a portrait)
    The scales go from
    0-30.0 health / 0%-300% fertility in 0.5 or 5% increments.
    Any values below the minimum value be shown as a 0
    Any values above the maximumvalue  will be shown as 30.0 / 300%
    (these max caps shouldnt be reachable in a normal game anyway)
    If a value isnt divisable by 5 it will be shown as the next lower value
    (ie. health of 5.8 will be shown as 5.5)
- Defensive Pact Localization should be fixed to no longer show a variable of 10000
- Adjusted Beastmen CB, Doesnt steal kingdoms anymore and sticks to the Dejure borders, capturing your opponent is no longer auto victory
- Dire Wolves retinue now gets proper modifier
- Adjusted the Antideath trait to fit more than just tomb kings
- The Fay Enchantress now has a modified version of the antideath effect
- Made absolutely sure only skinks can get the defective trait
- Tzeentchian Sacrifice should now kill the prisoner
- Added the ability for players to shift to chaos undivided as long as they dont have a mark of chaos and have enough prestige
- Summoning Daemons inside prisoner difficulty now scales with your chaos rank
    Regular - 50/50
    Cultist - 55/45
    Champion - 75/50
    Chosen - 85/15
    Daemon Prince - 100/0
    Everchosen - 100/0
- Capturing the Phoenix King no longer auto wins the war for Ulthuan
- Summon Tomb King Decision Added Back
- Gor-Rok Nickname Added
- Baragor Nickname Fixed
- Nagashizzar potential Religion check Fixed
- Fimir Building Localizations Fixed
- Event Titles For Battle & Siege Magic tutorial events
- Hopefully Cultist event chains have been fixed
- Updated all government checks to check for the new chaos governments
- Added everything required for the city looting/razing events for chaos but deactivated for now as we still get CTDs
------------------------------------------------------
Legacy_v1.2.3:
------------------------------------------------------
- Everyone in the necromantic religion group can activate/use the Nagashizzar wonder
- Fixed beastmen_artifact_stonecrusher_mace
- Fixed d_glanborielle the beastman would become a landless independent. Moved the date of the title way earlier so that the vassalize date is after the liege geting the title. Also removed the law rules
- You will no longer get ask to spill blood if your not a Khorne worshiper and the ai should not ask you to join a cult if your already seeking one this should fix a lot of the issues with cults
- Using potion of healing now removes symptom traits
- Removed DLC lock on offmap powers, except brayherd, as that uses Jade Dragon events
- Fixed Artifacts able to be sent back to the offmaps for more favour
- Allowed norcscans who follow chaos to use the artifacts given
- Fixed player being able to take boons they shouldnt have while a cultist
- Deleted mean time to happen events to become Champion/Chosen/Prince that didnt check trait properly and would set princes and chosen back down to Champion
- Champion/Chosen/Prince boons require you actually have the favour needed before letting you choose them
- Chaos Undivided Champion no longer requires you have 4x as much favour as the other Champion boons
- The Everchosen cant take the Champion/Chosen/Prince boons, as it would make them stop being the Everchosen
- Favour gain from donating artifacts nerfed heavily, now scales from 50 to 1000 for quality 3-10 artifacts
- Beastmen get favour with the Brayherds when winning a chaos raid
- Proper trigger in the offmap decisions from_from_potential added as the ai bypasses the display trigger and can use decisions regardless without strict checks
- Crusade interface fixed
- Fixed a few invalid modifiers from misspellings in artifacts
- Search for smith decision now works
- Some cult scripted effects moved from 00_scripted_effects to wh_scripted_effects
- Dwarfs cannot appoint elder title to people under 150
- Chaos Cults had misspelling in event giving duelist trait, preventing you from getting the trait
- Sleeping Slann event now only triggers for lizardmen
- Orcs trying to make goblin provinces orcish and vice versa now works
- Coronations wont spawn people with the chaos crusader trait
- daemonic_subjugation cb now costs scaling amount of favour
    500 at medium doom, 250 at high and no cost at very high
- Doom tracker UI now updates to let you know if daemon invasions and black crusades are possible or not
- Fixed Seagit and Freeboota to let thim hold citys and castles
- Fixed the Ancestor Worship decision for dwarfs
- Fixed Brayherd Artifacts
- Fixed Beastman Pilgrimage to the Dark Heart
- Added Beastman Jabberslythe Hunt
- Updated Chaos God Traits with the values of +2/+3/+5/+2 monthly grace for Chosen/Champion/Prince/Lore
- Adjusted some retinue cost to stop chariots spam for Beastmen, and lower gunner spam in the Empire
- Adjusted the Blood axe Tribe in the Southlands
- Moved Erengrad Under the Translynsk Kingdom instead of Kislev, and made it the capitol of said kingdom
- Lowered the Brief Non-Aggression Pact opinion requirement from +75 to +50
- Should have fixed the insane Beastman Warherd sizes
- Integrated upgraded version "WH-More-Imperial-Claimant" sub-mod. it adds:
    tons of new Kingdom and Empire tier titles for "The Empire"
    3 game rules so you can turn them on for just the Empires or for both the Kingdoms and Empires; off is the default
    two decisions to restore Solland and Drakwald and reobtain their Runefangs, until the proper quest can be written
    they have the Imperial Reconquest and you need two kingdom titles and cannot already be an emperor
    theres also a ton of new flags
- Added the missing government flavor for the new chaos govs, everqueen gov, norscan gov, and freeboota gov
- Fixed the Oak of Ages
------------------------------------------------------
Legacy_v1.2.2:
------------------------------------------------------
- Restructered Changelog
- Added the "Dammaz Kron" an event/decision logging tool for error reporting
- Began reworking Buildings to refer to the locations culture and not its rulers. This should stop buildings dissapearing and will completed in the first hotfix
- Added "the voice of Tzeentch" modifiers
- Reworked the Childrens Crusade to fire for tzeentchian children under 16. They will traverse the chaos wastes seeking support before assaulting Kislev
- Added a Daemon Prince of Tzeentch in the chaos wastes, he rules over "The Ragged Maze". NOTE: Since Chaos CBs will now be tied to the winds of magic it will be a boring start
- Moved the "Inevitable City" Wonder to "The Ragged Maze"
- Added a Daemon Prince of Nurgle in the chaos wastes, he rules over "Cold Mire"
- Added the Gallows Tree wonder and placed it in "Cold Mire"
- Fixed The minimap, you can now click again!
- Reworked the Minimap Art
- Added the initial version of the "Renounce Imperial Throne" decision. Right now its players only in case you dont wish to be Emperor
- Edited the DNA of Valka the Serpent when she becomes a daemon prince she will now have a better potrait
- Added religion icons for Mapmode and topbar for the following religions:
    Dwarf
    Cadai
    Cytharai
    Skaven
    Maw
    Celestial
    Halfling
    Nehekharan
- Updated the vampire piety icon and topbar religion buttons
- pet_consort trait purged from the gamefiles
- old_ones_group religion group (amazons and old ones) now use indian interface
- Changed all native Orcs in Lustria to the Savage culture
- Added three Freeboota and three Seagit characters
    My favorite Freeboota is in lustria, a dangerous buccaneer who relishes hunting the native savage orcs for a good Krumpin
- House Fingerpori fixed
- Irminsul Tree buildings made available for both beastmen and Norscans
- Great Pillars fixed
- Fixed The Chaos offering Decision to not show for religions it doesnt handle
- Enabled freckles system for some human, elf and dwarf cultures
- Fixed weight_multiplier on DR_cults.60001 to DR_cults.60000
- Fix to where counties hold by the Phoenix King werent given away to the new ruler
- Updated worship_morr trait GFX
- Summon Throngs decision limited to a single use every year
- Added only_playable and other pretriggers to decisions to continue performance optimisation
- Added The Druchii Watchtower Wonder and placed one in all 11 canon provinces as a buffer to the chaos wastes
- Added the Ghrond wonder for Morathi
- Added The Black Tower wonder for Malekith
- Modified positions.txt so each of the Druchii Towers are at the center of each city
- Adeed a magic law system allowing you to legalize magic, This has a high chance of causing unrest or rebellions
- Added a Bloodline for legalizing magic (Will most likely be merged later with the bloodline for forming the empire when the decision to form the colleges of magic is completed)
- Fixed The Ramaccan portraits
- Allowed Ungors in Ruler Designer
- Allowed Blood Dragons in Ruler Designer
- Allowed Forest Spirits in Ruler Designer
- Added a whole bunch of Opinion Modifiers
- Cleaned up all traits available in ruler designer to make for a friendlier experience
- You can now have more than one apprentice at a time
- Reworked Magic Learning and inheritance
- Fixed the Cultist society missions firing twice
- Magic casting as part of a battle is now completely automated, all Mage commanders in a battle will summon special spell units every 5 days of combat, these units disappear after the battle ends. Mages only have a limited amount of times they can summon these units depending primarily on their magic potential tier and to a lesser extent magic power skill level
- Cleaned up Vlad Von Carstein event spawned troops (Still split retinues though)
- Added an extra step to the VAMPIRE WARS game rule, it now progresses: DEFAULT > DANGEROUS > DEADLY > OFF
- Fix for Karond Kars unique building not showing
- Adjusted history files with artifacts given out to Asur characters, and added in the Phoenix Crown.
- Gave Caledor Dragontamer his nickname
- Increased Teclis Magic Power in the history files
- Overhaul of High Elf Colony system
- Fixed a bunch of colony buildings being mistakenly scoped to the location of the holder, so if they ever went to ulthuan as a commander a bunch of buildings would explode
- Added a decision for the phoenix king that lets you make all land you may somehow own outside of Ulthuan into a colony. The player is given a choice of three lords in an event from the most powerful members of the colony
- Added a new culture for High Elf colonists, ai lords will embrace this culture if landed outside Ulthuan and switch back out of it if they somehow end up landed back in Ulthuan, the culture has +2 marital, opinion bonuses with interventionist elves and opinion maluses with isolationist elves to match the interventionist trait.
- Removed 40 buildings and added 4. Previously every High elf culture had two full building chains for cultural buildings one for inside and one outside Ulthuan. Now there is a single cultural building chain used outside of Ulthuan for all High Elf cultures that gives some of every troop type + chariot special troops.
- Added two new Bloodline for High Elves.
    -The first is given to any Pheonix King who is burned crossing the flame, replacing the old trait, this bloodline is only active for Cadai religion characters of the founders dynasty, give large maluses to opinion with Cadai followers though the new colonial culture is more tolerant.
        This bloodline can be deactivated by the second bloodline. As long as this bloodline is active, unlanded member non-heirs of your dynasty may decide to leave Ulthuan to any High Elf Colonies or become adventurers.
    -The second is given when a member of the first bloodline manages to cross the flame successfully and is crowned Phoenix King, this bloodline is given to all members of your dynasty who have the first bloodline not just your direct descendants.
- Began reworking positions.txt across the map in preparation for the map overhaul
- Allow Norscans with patron traits to access some chaos events and decisions.
- Added a bunch of new scripted triggers to check which chaos god characters worship
- Offmap decisions are setup for undivided if needed
- Edited ai chance to stop hidden cultist outing themselves using the boons
- Summon Reinforcements from the warp wait time lowered from 2400 days to 1200 days
- Repaired the Norscan Warlord/Reaver traits and event chains
- Allowed Chaos Raid CB for all followers of chaos no matter their culture or government
- Allowed chaos rulers with ambitious trait to use county conquest CB
- Update to the artifact events from smiths etc.
- Applied fix to cure tomb kings, vampires, kdaai, demons(except nurgle demons) of disease related modifiers and disease related symptoms.
- Reiksmarshal Minor Title should now grant the Grudge Settler Runefang and removing the Title should remove it
- Added a small QOL improvement to the employment decisions.
    You activate one decision to make them all appear, and another decision to make them all disappear from the intrigue menu.
- Added the Invite Witchhunter decision to allow you to request a witch hunter to join your court if there is none
- Added a Witchhunter Minor Title to protect your witchhunter from court exodus if you are over your court limit (will add more events tied to this in time)
- Repaired the employment decisions to show the name of the employed character
- Daemon Princes are hidden during character selection, you will have to know where they are to play them
- Crazy Cannibal fixed for Ogres
- Fixed the ability to spam the Chaos Dwarf selling armaments decision which could lead to players having unlimited money
- Gave Konrad von Carstein the county of Waldenhof
- Gave Mannfred von Carstein the county of Templehof
- Fixed a few event frames
- Made the ruler of Luccini of the "Lupo" Dynasty
- Gave Malekith the "Disinherited" trait to stop any inheritance loopholes
- Changed traits undernourished to is_malnourished and fat to is_fat to match vanilla traits. removed the original warhammer health traits
- Modified the provinces around the gulf of medes to fit Antoch, the Brettonnian Crusader Fortress-City
- Added unique building - Antoch which provides commander limit, tax income, light cavalry, and knights
- Added the knights of Antoch, a holy order from Brettonia who wages war in the southern desert in the name of the lady
- Fixed the CB_icon_strip
- Increased orc tax income
- Removed duplicate Sea Temple building
- Gromnil mine changed to Gromril
- Regular Tomb Kings county cb restricted to inside e_nehekhara, prestige requirement raised to 250 prestige. A separate version for outside e_nehekhara costs 2500 prestige however the cost goes down to 1500 if you control either the whole western or eastern region of Nehekhara, if you have e_nehekhara the cost goes down further to 250
- Added onto the Chaos Cults system
- Doom Engine + Magic Laws/Battle Magic Edits
    -Doom Scale change from 1-100 to 1-1000 and changed to global variable from a province variable.
    -All changes to the counter changed from directly changing the value to scripted effects e.g.
        add_doom_progress_tiny_effect,
        reduce_doom_progress_major_effect etc.
    (There are some still some old ones in the files, but these are in unused events and pending a purge when testing version is out)
    -Every single war declared by chaos rulers + norcan follower of chaos and all wars declared against them will add or remove 1 doom depending on the result. Wars vs other chaos rulers, Skaven, norscans are excluded.
    -Chaos specific cbs add or remove more.
    -All baronys fully looted by chaos rulers give 1 doom if held by non-chaos rulers.
    -daemonic_subjugation cb needs higher than 250 doom to use
    -The passive removal of doom every year by the vortex is around 5-20.
    -All randomly spawned in adult courtiers have a very small chance being mages for Humans with legal magic, Amazons, Chaos Dwarfs, Elves, Skinks, Skaven and Beastman.
        The chance is heavily influenced by the characters traits and the doom counter.
    -Daemon summoning in the new battle magic has a higher chance of summoning more daemons when doom is higher.
- Humans become more accepting of legal magic when a realm manages to keep it legal for over 50 years
- If a peasant leader spawns as a mage and wins they get a bloodline and get the magic legal law added to their new realm.
- Added debug event HH_Debug.1 to make a character a mage, you need to use this rather than the console to setup magic power modifiers, xp levelling etc.
    Will give appropriate lore trait for race/culture/religion. Only use with, Humans/Amazons/Vampires, Chaos Dwarfs, Elves, Skinks, Skaven and Beastmen
- Repaired wonders for dwarves and other races
- Disabled the Dwarf Mason trait requirement for the Royal Clan Halls until we implement the societies
- Hid the Mordheim Notification in case a player somehow manages to take it before the warpstone runs out
- Added The Arena of Zanbaijin wonder
- Added a generic Chaos Fortress wonder to mirror the traditional Grand Fortress Available to order races
- Placed a few chaos fortresses throughout the chaos wastes
- Added Skavenblight as a wonder
- Allowed Underground City for Beastmen and Goblins
- 250+ new artifacts, though about half still need GFX
- Armour and Magic interaction created
    Added flag armoured_caster to artifacts for characters that cast magic in armour without penalty.
    Added in the necessary scripted scope values and modifier definitions for the armour artifacts to provide their duel buff
- Assigned the following artifacts to Dwarf characters-
    -Dimrond Angrun received:
        Gromril Armour
        Clan Angrund Hammer
        Defiance Shield
    -Slayer King Garagrim received:
        Gromril Armour
        Axe of Dargo
        Slayer Crown
    -Alrik Deathdealer received:
        Axe of Grimnir
        Armour of Skaldour
        Dragon Crown
        Great Book of Grudges
        Throne of Power
- Adds in decisions to buy a black dragon egg, hatch it and eat it.
- Added in missing black dragon hatchling artifact so that Black Dragon events function.
- Malekiths armour is now cursed so he cannot remove it
- Malekith no longer spawns with a Wyvern.
- Added in an offmap system for each of the four chaos gods, this is fully featured and is how you recieve boons from the gods! Im not going to go into detail here as I want you to explore the system for yourselves
- Added in an Warband(Warrior Lodge) system for each of the four chaos gods and undivided, this is fully featured and is another way to recieve boons from the gods! Im not going to go into detail here as I want you to explore the system for yourselves
- Fix Empire unification bloodline
- Remove/fix references to the elixir_of_youth trait, its an artifact now
- Allow pillaging provinces with only 1 settlement
- Minor QoL on establish_lahmian_presence decision
- Updated fimir shearl to be unable to inherit or hold titles
- Females that follow slaanesh no longer have the option to go celibate
- Allowed Southlanders  to tell a story (african flavor from HF)
- Allowed decision "hold a grand hunt" for cadai and cythari elves group, and allowed females
- Humans are more likely to support magic when doom is high and less likely when its low
- Expelling the witch Hunters will make magic de facto legal and will make witches and hedge wizards start appearing in the realm
- Realms ruled by peasant leaders and by those who have expelled the Witch Hunters will have a much higher chance of spawning mages if magic is not legal elsewhere in the old world
- Split magic laws out into their own triggers and effects files
- Doom counter can no longer go negative or over 1000 and should start properly.
    (Now triggers off Malekith on game start and then is set as a repeating event on province 1 every year)
- Doom can now passively increase per the amount of Champions, Chosen and Princes active in the world as well as if the Everchosen is active
    This is a random chance and is lower if they only hold land in the chaos wastes and massively lower if they are not landed
    Higher traits have a higher base chance of adding doom.
    However the doom loss on death has been extended to champions as well, though at a much lower level
- Higher Doom makes mages much more likely to appear randomly (even higher for chaos mages) and also allows easier summoning of Demons
- Magic System
    Moved all triggers and scripted effects used in the new casting system to new appropriately named files, everything outside these files is currently deprecated except for magic crafting and learning events
    Rewrote magic xp system to make sense (Why the hell was it using three xp variables rather a single xp variable?)
- Magic xp is gained during casting in battle and passively through a random event
- Higher Magic potential traits make it easier for you to level up your magic power level
- Added a bunch of tooltips to magic triggers
- Liche priests and tomb kings get a 1 and 2 magic pool boost respectively, otherwise they might not be able to cast with a low magic power. Liche priests are incapable of levelling up magic xp anyway so not that overpowered
- Wearing armour as a mage can reduce battle magic pool if not using specific mage equipment
- Gave orcs and goblins a chance to spawn with magic
- Also made non historical characters on game start have a chance to be mages not just those generated as the game continues to make each game different
    Average of about 6 High Elf mages, 2-3 dark elf mages, 5 chaos mages etc.
- Changed time for expelled_strigany modifier to expire after 10 years
- Magic system extended to sieges
    On a siege starting it will check all attacking commanders in the army and apply a scaling province modifier that reduces fort level, garrison size and levy reinforce rate depending on the total magic power present in the attacking force.
    A tutorial event will pop up first time it happens for the player same as battle magic
- Added Star Sign mechanic to the Civilized Humans of the Old World. They are traits with small modifiers, and they also affect the AI personality
- Added the Court of the Everqueen government
- Added the Norscan Tribes government with unique charframe rings
- Gave Dwarfs the mountain_ambush_tactic Combat Tactic
- Added special combat tactics for the chaos warbands when experiencing a call to glory
- Fixed the ai Everchosen spawn events
- Added Black Crusades
    -Black Crusades can be started by the Everchosen, or an undivided ruler with enough prestige and piety can start one by decision if no Everchosen exists and there is a moderate level of doom
    -Other chaos religions (except chaos dwarfs) and Norscans with a dark patron can join in after the war starts for a chance at artefacts and favour if chaos wins
    -However they will not receive any land or war chest rewards due to hardcoded limitations in the crusade system.
    -Otherwise functions mostly the same as base game crusades with events, bloodline, traits, and GFX made more suited to chaos
- Broad priority for targeting is
    > Kislev (Volkova then Kislev Kingdom)/ the Watchtowers
    > Empire Coastal
    > Empire interior/ other parts of Naggaroth/Norse dwarfs
    > Brettonia/Ulthuan/Estalia
    > Tilea
    > Border Princes
    > Main Dwarf Holds/Araby
    > Southlands
    > Tomb Kings/Lustria
- Ropsmannia removed and its land given to the Kislev kingdom for purposes of making Black Crusade targeting only take 2 wars to get through the Kislev empire and move on to The Empire.
- Ropsmannia is now a cultural name for e_kislev and k_kislev
- Added a few extra debug events HH_Debug.2 and HH_Debug.3 to add or reduce doom
- Fixed save bricking crash with old amazon event causing wh_setup.7 to keep trying to fix a character religion in an infinite loop.
- Using magic_physical_healing can now remove eunuch trait AND blinded trait
- State Troops moved again, this time to Obligation Laws. Overall this should help balance as Merchant Republics no longer get access since they get a bonus per tradepost
- All Culture Modifiers restored and balanced
- Added a Unique Building for Mordheim
- Added The Asur Mountain gates Phoenix, Eagle, Griffon, Etc. as Wonders
- Added special Asur Wonder Upgrades for the Gates
- Changed Castle Drakenhof to a wonder
- Added Mourkhain as a damaged wonder to the Badlands
- Added Nagashizzar as a wonder
- Adjusted the amount of chaos undivided rulers at game start
- Added the "Herdstone" building for beastmen, its easy to build and contains several modifiers to give them a bit of a chance
- Overhauled Beastmen Retinues
    -Ungor Raiders, light infantry and archers with a 20% offensive/defensive bonus for both
    -Gor Raiders, archers and heavy infantry with a 30% offensive/defensive bonus for both
    -Bestigor Raiders, heavy infantry with a 50% offensive/defensive bonus and a 20% morale boost
    -Centigor Raiders, light cavalry and horse archers with a 30% offensive/defensive bonus for both
    -Razorgor Chariots, chariots with a 50% offensive bonus and a 20% morale boost
    -Harpies, war beasts with a 80% offensive and 50% defensive boost
    -Minotaur Pack, war beasts with 100% offensive bonus and 100% morale boost
- Overhauled Chaos/Norscan Retinues
    >Religion Specific
        -Plague Champions, heavy infantry with a 80% defensive bonus and 20% morale boost
        -Khorne Berserkers, heavy infantry with a 80% offensive bonus and 20% morale boost
        -Exalted Ones, heavy infantry with a 20% offensive bonus and 80% morale boost
        -Brood Lords, heavy infantry with a 40% offensive bonus 30% defensive bonus and 40% morale boost
    >General
        -Chaos Marauders, Light infantry and archers with a 20% offensive bonus and 20% morale boost
        -Chaos Marauder Champions, pikemen and heavy infantry with a 40% offensive bonus and 50% morale boost
        -Chaos Warriors, heavy infantry and pikemen with 50% offensive bonus and 80% morale boost
        -Marauder Horsemen, horse archers and light cavalry, with a 50% offensive bonus and 20% morale boost
        -Chaos Knights, heavy cavalry, with a 50% offensive bonus and 80% morale boost
        -Gorebeast Chariots, chariots with 50% offensive bonus and 20% morale boost
        -Trolls, War Beasts with 50% offensive bonus and 80% morale boost
        -Giants, War Beasts with 100% offensive bonus and 30% morale boost
    >Norscan only
        -Skin Wolves, War Beasts with 80% offensive bonus and morale boost
        -War Mammoth, war elephants with 50% offensive/defensive bonus
    >Nomad only
        -Dragon Ogres, war beasts for chaos chosen, 200% offensive bonus and 100% defensive bonus
        -Dragon Ogre Shaggoths, war beasts for daemon princes, 400% offensive bonus and 200% defensive bonus
    >Piety Retinues
        -Forsaken, daemonic host with 100% offensive bonus and 50% morale bonus
        -Chaos Spawn, daemonic host with 100% offensive bonus and 100% morale bonus
        -Fimir Raiders, light infantry and heavy infantry, 100% offensive bonus and 50% morale boost to both
- Nerfed the Green Knights combat bonus so he wins less
- Beastmen do not have access to offmap powers, they will get a separate "Brayherd" mechanic
- Removed the culture requirements from unholy_raid cb. Now every chaos follower can use that cb
- Von Carstein Vampire War Events should now check held titles before firing
- Beastmen Duels for rulership are now deadly
- Added a offmap boon to become a chaos undivided champion as undivided could not become the other champion types
    and the only other way was through the warbands
- Ai will now use all boons, and request them in a more intelligent way e.g. will only summon one daemon familiar of each type, wont claim more than 1 steed etc.
- Made it so when the ai event to make them join a Warband fires it will prioritize rulers joining, basic daemons, bloodletters, plague lords are now forbidden from joining. As well as rulers e.g. mercs who dont hold actual land
- Warband ai memebership limit upped to 60
- No more independent barons seagits/norcans turning into nomads
- Norscan Gov wont turn to republic gov when holding just castles
- Fixed landless nomad witch hunters chapters
- Added blood dragon culture check to racial triat assignment system
- The chaos ruler in Mordheim is no longer the Everchosen
- Gave the mark and champion traits a bit of piety gain
- Fixes some scoping issues on the modifiers that were meant to stop chaos waste nomads wasting time making each other tributarys
- Every daemon in the world has a miniscule chance of adding doom
- Once you have a mark of a chaos god or are a champion of that god as undivided you are able to convert to that god
- The Chaos Offering Decision no longer Fires Twice
- Black Crusades can now be called at low doom once per century per religion, medium or higher doom is still every 30 years per religion
- If any kingdom in the Chaos Wastes or Norsca (except Fjellsende, The Goromadny and the Isles) are held by a non chaos ruler then the once per century restriction is lifted, Chaos will focus on the Chaos Wastes then Norsca
- Adjusted technology in the Chaos Wastes
- Added the Mark of Chaos for the Everchosen
- AI will no longer take their husband as a consort
- Fixed a few instances where chaos nomad govs might not be setting correctly in nomad agitation and minor clan uprising events
- You cannot send mounts gained from the offmaps back to them for more Favour
- Artifacts with a higher quality level than 5 now no longer give the same favour as a quality level 3 artefact
- Added scripted effects to give or take varying levels of favour appriate to the offmap a character has access to. Changed chaos cbs to use these effects
- You can no longer learn lores through boons multiple times or become a berserker if you a mage and vice versa
- Chaos Undivided can use the steeds from the offmaps
- Made the ai even more sensible with boons
    e.g they wont recruit champions if they are not one themselves, they wont always summon an army unless they are at war to allow them to save up for higher tier boons etc.
- Fixed issue with Fimir born from human mothers not getting Fimir portraits
- Slavery menu now works for selling slaves
- Magic revolts will no longer pick an imprisoned person to be the leader
- Black Crusade game rule is switched around and the default is everyone has access
    ultimately the ai is stupid and we need undivided chaos rulers to have the potential to call them if we dont want to just have an event for them to fire
- Zanbaijin holdings and chaos holy sites will no longer be destroyed when a chaos ruler in the wastes converts to a nomad
- The Lizardmen War to reclaim the staff of jade has been added, the empire of lustria has to be formed first, and then Mazdamundi will awaken to lead the lizardmen against the Bretonnian Crusade City of Antoch
    If you succeed he will enact the ritual to reset the doom counter to 0
- The secret Kislev event will now make you an ice-witch if you succeed as a fallback route to keep the magic alive until the overhaul
- Converted the Oak of Ages to a wonder
- Fimir will now get blinded instead of one eyed
- Adjusted Disease outbreak start dates
- Returned access to specific offmap gods for beastmen that worship them, but increased the boon cost similar to Chaos Undivided
- Added the Breyherd offmap Power for the Beastmen, this is unique from the other chaos gods with its own set of mutations and effects for beastmen
- Fix to edge case of spell units not spawning in correct province, and fix to prevent commanders getting kicked when casting starts. Had to turn off auto army merging due to hardcoded bug with commanders being kicked when merging
- Placed a Beastman ruler in Morgheim surrounded by orcs on all sides but determined to hold the ruin
- Merged the "old world only - Elf Enclaves" submod with "old world only", since the doom engine fires on malekith on game start.
- And many many general bugfixes and localization fixes
------------------------------------------------------
Legacy_v1.1.6:
------------------------------------------------------
- Added vampire religion icon for Mapmode and topbar
- Fixes for some GFX
- Fixed the witch hunters having 0 mercs
- Added an option to ruler designer to start with magic
- Some fixes to the warpstone stuff (no longer shall the world descend into addiction and death)
- Limshof now has a holder
- Mausoleum temple building should be fixed for Vampires
- Increased maintenence cost for Vampire Retinues
- Added a Game Rule for the Vampire Wars:
    Default: ~55K troops for Vlad
    Stronger: ~100k troops for Vlad (great for multiplayer in The Empire)
    Off: The wars will not be scripted
------------------------------------------------------
Legacy_v1.1.5:
------------------------------------------------------
- Malekith should now be incapacitated properly just like a tomb king in combat and from murder plots instead of just continually walking away unscathed
- Restored some of the unique buidlings removed in the past as others have become wonders
- Added chaos religion icon for Mapmode and topbar
- Added greenskin religion icon for Mapmode and topbar
- Updated khorne_berserker trait to be **RED**
- Adjusted the new chaos character frames
- Fixes to the Assign Racial Trait system
- Fix so the ai wont back out of the convert to chaos horde decision
- Added a prestige and is_adult requirement to reestablish_naggaroth decision
- Fixed Arabyan castle buildings
- Added a max limit of 1000/500 to a bunch scaled_wealth commands in prosperity events and claim fabrication
- Fixed find court physician doing nothing
- The ai can now only assign a courtier with a matching religion and culture as their court tutor
- Empire Elective is now fixed
- Fixed backup event to kill characters born of incompatible parents or races that shouldnt reproduce which only checked the father scope not true_father, so hidden bastards could still be born
- The Duel against the Green Knight on your grail quests are to the death!
- Fix for weak_warboss modifier being permanent with no way to remove it, now winning a challenger duel will remove the modifier, also made sure orc duels are to the death
- Set custom tooltips for the laws to reduce the overall size of the tooltips.
- Fixed a dynasty (33098) which random Lowborns of all cultures where being randomly given to, dynasty had no name in the files
- Munzig was one of the provinces that is supposed to have a gold mine in it, but wasnt one of the provinces that allowed a tradepost
- Dissabled the blocking of internal vassal wars for Druchii
- You can now take the forge bloodline ambition multiple times provided you havent already forged a bloodline with that character, prestige cost to take the ambition scales up from 20000 > 40000 > 50000 > 60000 and capping at 75000 once you have four forged bloodlines
- Freebootaz and Pirates have begun to get some love:
    Seagit(goblin pirates) and Freeboota(orc pirates) cultures and portrait gfx added
    Freeboota government implemented
    Finished Pirate Fleet government as well as some alterations to account for it
    spritetypes file set up for Pirate Fleet and Freebootaz government
    localisation file for Pirate Fleet and Freebootaz governments
- Restored the "Enforce Realm Peace" Button. Though its still up for debate wether to just remove it completely
- Fix for the child portraits, elves and dwafs who reach 16 should have the correct portrait
- Fixed Hellebrons Dark Fire amulet not showing its gfx correctly
- Dark Elves and High Elves no longer lose opinion from having troops raised too long
- Added a random event that can trigger every decade or so when you are old world religion ruler and border an openly chaos realm or across across a short sea from one.
    A group of cultists will enter the realm and move to random realm lords court and join an appropriate cult society if able.
    This event has a higher chance to trigger if bordering a realm ruled by a demon prince or chosen.
    The cultist have a higher chance of being caught depending on your state intrigue (unless you spymaster is a secret cultist).
    Realms that have expelled the witch hunters will always fail to catch them.
- Fixed it so the hunt apostate lord spiritual action gives people burnt at the stake the burned portrait same as those burnt by witch hunters.
- Added Warpstone Meteors and Veins
- Overhauled Warpstone System
- Added Black Marketplace
- Increased Vlads starting forces for both the player and the AI
- Overhauled Vampire Retinues
    Undead Horde, summoned troops with a 100% offensive and 50% morale bonus
    Dire Wolves, summoned troops with a 10% offensive 50% morale bonus
    Crypt Ghouls, light infantry with a 40% offensive and 20% defensive bonus
    Cairn Wraiths, pikemen with a 40% offensive and 20% defensive bonus
    Grave Guard, heavy infantry with a 20% offensive and 40% defensive bonus
    Hexwraiths, light cavalry with a 40% offensive and 20% defensive bonus
    Black Knights, heavy cavalry with a 20% offensive and 40% defensive bonus
    Vampire Knights, special troops, with a 70% offensive, 30% defensive, and 50% morale bonus
    Corpse Carts, chariots, 50% defensive and 50% morale bonus
    Crypt Horrors, war beasts, 50% offensive and 100% defensive bonus
    Vargheists, war beasts, 100% offensive 50% defensive bonus
- Vlad Von Carstein now starts with a Large Retinue Army to match the other Elector Counts
- Fixed Daemon Portraits
- Fixed a bunch of minor bugs
------------------------------------------------------
Legacy_v1.1.3:
------------------------------------------------------
- Added ai_check_interval to all WH decisions, which will help performance as well as the frequency of greenskin/beastmen duels etc.
- "Empire Unification" decision made more difficult to achieve until it can be updated completely
- Updated map/terrain/"colormap" with new effects for the vortex static model
- Updated map/terrain/"colormap" with new effects for Kislev/Norsca/Troll County
- Updated map/terrain/"colormap_water" with new effects for the vortex static model
- Updated map/trees for an overall better map
- Imported Vortex Model and Shader **credit: Arasakes**
- Imported Gold Mine Models around the old world
- Updated Green Knight portrait/trait with community version
- Repaired missing Bretonnian on_actions for knight errant trait
- Repaired and split the grail knight and questing knight event chains (not perfect but until the overhaul it will work 100%)
- Compressed GFX files
- Quick and dirty removal of mass conversions
- Chaos cult uprisings correctly give demon event troops and a demon commander to the leader, also cultist leaders who are independent rulers are more willing to declare their true faith.
- Beastmen are no longer acceptable marriage material for everyone
- Updated the worship trait icons in gfx in case we use them
- Added some Druchii artifacts to main characters
- Added Modern GFX for Druchii artifacts
- Removed Galleys from Skavenblight
- Capped Skaven breeding events file. **REQUIRES MORE TESTING**
- Daemon Prince reinforcements from the Warp now last longer
- Fixed mutations. I removed the brackets from the culture_groups. culture_group = goblin_group instead of culture_group = { goblin_group }
- Resized custom government icons
- Kislev now gets its own government type: "Tzardom" with unique charframes and more!
- Chaos now gets its own government types:
        "Chaos Horde" for nomads
        "Chaos Host" for tribals
        "Chaos Court" for feudal
- Unique Chaos charframes and more! (perhaps darken/tweak charframes in the future)
- Arkhan the Black is now properly recognized by his peers as a fellow Tomb King and not a Liche Priest. His portrait remains the same though.
- e_cathay_west_governor title added so the game doesnt keep endlessly creating new versions of it for the offmap power.
- ai_cleanup_events has been restored which should enable the following
    Demand Religious conversion decision now works.
    Dwarf traits at start cleanup
    Elven maturity
    Court cleansing for Khemri Servants and Skaven Breeders
    Dwarf babies should not be born old already
    Elven youth trait assignment
    Everqueen inheritance
    Free mage_apprentices and pet_consorts on death of Master
    The Red Duke is dead, destroy the special title
    Big Akghan succession
    Martek Scholar succession
    Destroy Samurs Witch Hunter Chapter
- Merged RD_Trait distribution system from FaolDeTeine
- Added and localized the Ruler Designed Vampire trait for people who want to start as a vampire
- Made it much harder to become the Everchosen
- Sacrificing prisoners for necromantic power as Vlad now lasts 4 months instead of 1
- Beginning of the warpstone overhaul!
        For now you can consume warpstone for magic power just like sacrificing prisoners
        Vlad starts with 5 Clusters of Warpstone that his minions gathered from mordheim
        More to come!
- Changed WH_Defines to allow consorts to be dismissed
- Unlocked the Everchosen events for players, with some restrictions
- Adjusted the winds of magic and its affect on the world
- Chaos Mark traits added and localized
- Fixed a minor graphical error on a loading screen
- Cleaned up and overhauled the landed titles folder (should also fix realm colors instead of renaming the files)
- Ostrosk history file repaired no longer an instant game over
- Changed **EVERY SINGLE** file to ANSI - CRLF - Windows 1252
- The King of Bretonnia now starts with the brave trait to stop him from occasionally starting craven
- Bretonnia buildings changed into local culture checks
- Same treatment for
        Araby
        Tilea
        Estalia
        Kislev
- Skaven Congested province modifier nerfed to -5% from -50% since its stackable
- Repaired Localization everywhere
- Temp fix for greensking buildings bug, not a proper fix but will stop the capital being nuked atleast if we cant find the root cause
- Added recent_county_uprising to a bunch of revolt events, all the non vanilla adapted ones didnt stop additional rebellions triggering.
- Added a likely fix for the save corruption issue caused by beastmen, less chance it will incorrectly link two nomad beastman titles together and cause the save to brick.
- Added decision icon for grail quest
- skaven_foreignconquest cb requirements relaxed to allow dukes to use it, but at a cost of 1500 prestige
- Updated the Circlet of Iron so that you need magic potential to use it.
- Replaced Neueslander Gunnery School with Pistoliers
- Removed the duplicate files and fixes the castle wall requirements for halflings
- Cleaned tooltips and added scripted triggers
- Quick fix for the holy war CB bug
- Increased the amount of consorts allowed across all applicable religions
- Changed magic polymorph to properly change your gender and give appropriate traits
- Updated take consort decision to allow to take male - male concubines and female - female concubines
- Cleaned up employment decisions and allowed you to hire council positions
- Beginning of the Trade system overhaul:
        New Routes
        New Buildings
        New Balance
        Reworked systems from vanilla
            Gold(Empire, Bretonnia, Border Princes, Araby)
            Cloth(Estalia)
            Salt(Kislev)
- Removed all trade posts at game start from the old system
- Placed new Trade Posts at Game Start
- Akendorf unique building restored
- Restored Vlads Subjugation Localization
- Loosened Building restrictions for Sudenburg
- Shared portrait properties overhaul (bloodsplatter/hairlip/blackeye)
- c_calxi no longer believes its a desert or ocean. Ive informed it of its jungle status
- Polish Sylvanian Buildings
- Nehekharan removal submod created
- Reworked Khorne blood tournament to use HF calculations
- Reforming Myrmidia will now give you byzantine elective
- Fixed Enactic Succession
- Removed duplicate Halfling buildings
- Orcs can no longer be elected to rule Bretonnia, in fact most races should now be excluded properly from elections
- Made the ship-creation decisions for lizardmen and skaven easier and checked more often so they dont have to walk around the world (May also do this for orcs)
- Fixed Bloodline for Chaos Dwarfs and the localization for the Empire Bloodline
- Fixed Warpstone artifact Loacalization
- Extended Trade Routes all the way offmap
- Added GFX for new employment decisions
- Made Grail Quest a High Priority decision
- Repaired on_actions file with updates from vanilla, Sway/Antagonize should now work
- new_character_effect adds extra age to elves and dwarfs between the ages of 16 and their respective ages of majority so only a few randomly generated characters are too young to marry or hold land
- fixed a broke else_if in the new_character_effect breaking the system for non humans and removed a dupe extra age from wh_setup.5 for tomb kings
- Added a new decision (Return to the Old Ways if you are Hung/Kurgan, Become Chaos Horde otherwise) that lets non nomadic chaos worshipers convert to Chaos Host gov if their realm is entirely within the chaos wastes region. Hung/Kurgan are much more likely to do this
- Added GFX for this decision
- Made a champion for the each of the chaos gods out of the 4 norscan brothers (3 of whom are in the border princes area)
- Fixed localisation error for the minor title "Champion" in the empire.
- Added can_use_retinue_trigger to every retinue
- Elector Counts now start with state troops
- Sudenburg now starts with raised retinues
- Reworked the respective chaos chosen of each of the ruinous powers to actually represent their god a bit more in traits, education, and base stats.
- Also gave The Chosen of Khorne a bit more land to see if he does anything when not limited by his tributaries
- Added Cold One Mount GFX
- Made the PTSD event HFP.11019 have different options and descriptions for some cultures/religions that dont mind killing
- Fixed an infinite while loop caused by old magic calculations
- Changed the chaos champions to be around their 20s, Added a wife for nurgle champion from the khagan of Khursaze
- The Fay Enchantress is now human, but retains her beauty forever, as it should be
- Fixed history files. Birth, marriage, and age stuff. Missing = in trait assignments. removed old unused traits.  Fixed mount for the red duke not spawning. Nickname fixes
- Khalida artifact and new face mask(Needs to be applied to khalida)
- Added Generic Druchii artifacts
- Fix to Drakenhof starting with a city as the capital and fixed the drakenhof unique buildings
- Tribals can hold castles if the county culture is the same, some tribals e.g. amazons cant become feudal, so if their land was taken and upgraded to a castle it becomes useless to them if retaken
- Disinherited Neferatas and Ushorans brother and his children so if they die we dont end up with a random tomb king in the badlands/mountains
- Fixed crash with pick_main_deity, by coincidence a large number of ai took the decision at once, but because the modifier that stopped them taking the decision again was done after the events chain they seemed to pick it hundreds of time in a row
- Merged Malekith death and overthrown empire destruction event. Now when Malekith loses his empire or dies e_naggaroth is destroyed
- If Malekith held e_ulthuan as well and the the heir to e_naggaroth gets both empires and is not in the asur_group then e_ulthuan is destroyed as well
- Malekith will also permanently lose access to his unique government if he is overthrown to show his authority has been broken beyond repair (Not sure on this change specifically may adjust)
- Added decision for reclaiming e_naggaroth if you have the whole capital kingdom and either a large enough realm size or completely control 2 other kingdoms in Naggaroth
- Chaos Dwarfs also get some extra age for adult characters spawned by events. So they can potentially be made commanders
- Removed the trait addict from Valka. Addict gives you events where you lose base stats currently
- First wonder in the Chaos wastes, the Inevitable City, notably give big population max and pop growth to chaos nomads along with other minor boosts, no custom upgrades right now
- Added chaos cult sleeper agents:
    The ai can attempt to recruit even when the society has reached the max membership limit, if they succeed in the event chain the recruited target will not join the full society
    and instead simply change secret religion and be flagged a sleeper agent
    Every 5 years the sleeper agents will check if the society has dipped in membership below the limit and join automatically if it has, when a general cultist uprising happens
    any sleeper agents will convert, leave any non chaos societies and join in alongside the normal society members
    People the player recruit will always join the society bypassing the limit same as before.
    rank 3 members of the cult can now also declare an uprising, as the cults are global and members in realms other than the single rank 4 member were essentially useless
    the ai will not currently declare an uprising if the player is in the same realm as a rank 3 or 4 member
- Added lots of flavor to the greenskin-specific events
- First pass at Clean Up\Rebalance of Chaos traits
- Added our first minor race: The Fimir
    This is just the framework, they will be polished and expanded on in future patches
- Fixed "Become Mason" decision
------------------------------------------------------
Legacy_v1.0.1:
------------------------------------------------------
- I modified the Legacy religion files to allow for certain religions that by all reason SHOULD allow for women to take consorts, to do so
- Updated some of the traits for new combat rating scale (Chaos, Daemons, Vampires)
- "Aztec Sacrifice" decision now gives 0.2 favour instead of 1. Needed a nerf and it should also now apply favor to you and not your sacrifice
- Z_magic_effects.txt, Z_magic_item.txt, Z_magic_power_calculations.txt, z_magic_resist_test.txt, Z_magic_setup.txt, Z_miscast_test.txt, z_spell_process.txt.  -Removed from scripted_triggers
- Characters birthdate/landed_titles files fixed. Deadmen cant hold titles
- Province: 158 - Straghov.txt  | 172 - Sepkuzy.txt |  179 - Krasicyno.txt | AND 196 - The Blight.txt were duplicate and removed.
- Fixed Greenskin traits
- Found the COA issue: d_webba_weavahrs.tga - should be d_webba_weavahs.tga
------------------------------------------------------
Legacy_v1.0.0:
------------------------------------------------------
- @Mitsu can no longer kill tomb kings in a duel
- Removed developer tools: wake slaan/challenge to duel decisions
- Merged duplicate Become Celibate decisions
- Removed all that extra blood Finubar was running around with
- All flavors of Aelves should now be immune to mutations (though I believe this was a feature not a bug)
- Numerous portrait repairs made (Halflings and Amazonian Men shouldnt be so "pale" anymore)
- Orks are less mysterious about their size trait
- Your sick fetishes can now be realized! (allowed to join cult of pleasure again)
- The Red Duke has a slighly better chance at winning his war, though he's unsure if he'll crash the game if he does
- Orks should no longer contract a venereal disease
- Renamed both "vales of florida" to the "floridian vales" which fixed the cut off
- Repaired the champion minor title, This was conflicting with the Emperors Champion minor title, which I also repaired and
    Balanced allowing the champion to be given the drakwald runfang/removing it if he is no longer champion
- Master of elephants restricted to region = world_greater_araby
- Roman events removed, they were only kept for inspiration on reformation mechanics
- Removed duplicate decisions and localized "use magic item"
- All flavors of Dawi should now be immune to mutations
- Removed some excess GFX
- Removed the extra witchhunter council position as it was unused
- Fixed a few parse errors
- Stopped Druchii usurp spam
- checked schaos.99 and daemon prince requirements
- removed old gift artifact decisions
- Repaired chaos dwarf sorceror trait
- Sacrificing prisoners should now give chaos favor (however there are still many things that should give favor that dont)
- Removed tribal/nomad requirements from the chaos raid CB
- Investigated several broken event chains before "nopeing" right out of there. Those fixes will come in time
- Boosted the piety and prestige gained from Vlads Subjugation CB (both win/lose) from 100 to 1000
- Fixed Ghal Maraz localisation
- Repaired all intermarriage links in the wh_religions file
- Fixed succession realm collapse for chaos/norscans
- The precluding succession event that fires warning of unworthy heir converted to a bi-yearly pulse on_action instead of a monthly MTTH
- Fixed more missing trait icons (Skaven, Goblins, Damsels, etc.)
- Allowed Ruler Designer, not all WH traits are available and definetly not balanced... but its there if you want it.
- Mortensholm changed to Mortensheimr
- Sylvania no longer has access to the imperial gunnery school
- Relocalized "china"/"chinese" to "cathay"/"cathayan"
- Buffed Beastman "Gather Army" decision from 80 troops to 500
- Immortal characters using the child portrait repaired in history (investigation into event for long term required)
- "Ensnared" opinion modifier now lasts 3 months (Jade Vampires)
- The Clone wars have ended! The Green Knight will now ride back into the mist from whence he came.
- As a reward he has been given the "Green Knight" trait, a buffed version of Grail Knight, along with some descriptive localization for flavour
- Restored Miyan Halfling retinue
- Replaced all instances of "Ursun" with the proper "kislev_gods"
- Ice witches will no longer die out in a single generation
- Back down to 2x starting horde for the Red Duke (Instead of 3x)
- Applied conversion of MTTH to on_actions supplied by @justyn
- Removed the infertility event
- Instances of chinese culture changed to oriental_group
- Removed govenor portrait from the off_map screen
- Removed state troops (*again*) @manuswag snuck them back in there on me
- The Children of Doom Society no longer requires you to be kind, but also not kind.
- First pass at limiting the building of wonders ( no beastmen, orcs, etc)
- Localisation fix for the "Brazen Bull" event
- Elective Leagues now have an option to decline (Will apply a cooldown opinion modifier that will exclude you from leagues for 6 months)
- Ai Elective leagues moved to yearly on_action
- "Bloodthirsty Games/Mass Sacrifice" should now work properly including traits for all Khorne, Chaos, Norscan Gods, Cytharai
- Fixed Malekiths government type. At game start, in case multiple governments are eligible, the first eligible one will be taken. I placed the malektih government above the druchi government in the files. That seems to have fixed it
- Skaven no longer get galleys in their building chains but through a special event (this should help not only performance but also the skaven financial crisis)(decision requires gfx icon)
- Lizardmen no longer get galleys in their building chains but through a special event (decision requires gfx icon)
- Lizardmen cities no longer have access to vanilla ports
- Skaven "Breeding Pits" now cost less prestige to hopefully make game-overs a little less common
- "Nurgles Touch" now limited to the proper religions
- Artillery retinues buffed to stop them being eradicated easily in battles
- Diseases and Mutations should now be properly limited
- HF duel engine plugged into bretonnian quests and orc/beastman supremacy fights *SHOULD* work (duelengine.1 removed replaced with HFP.10095 etc.)
- Fixed province modifier icons (added 40 new ones from vanilla and shifted WH modifiers down by 40) still need a bit of cleanup on the art (some are off center) but its workable for now.
------------------------------------------------------
*Relevant Changes Before Legacy Development Began.
------------------------------------------------------
 ###############################
 WH:Geheimnisnacht Master Branch
 ###############################
 Changelog V1.3.16
 ###########################
 # Minor Changes I
 ###########################
    -General localisation
    -Finalized design on intro loading screen
    -Added a few more loading screens from "HAMMK"
    -Finished installer
    -Fixed unitpanel_specialunits gfx
    -Integrated Fake Map Modes (This is somewhat incomplete as the technology section will be repurposed for our needs perhaps to check chaos/vampiric taint)
 ###########################
 # Building Overhaul I
 ###########################
 # Castle
    # Unique Buildings, more to come!
    -Altdorf, garrison size, knights, galleys, income
    -Middenheim, fort level, garrison size, heavy infantry
    -Talabheim, fort level, garrison size, archers
    -Nuln, garrison size, military tech, gunpowder, income
    -Marienburg, garrison size, light infantry, galleys, tax income
    -Sudenburg, garrison size, pikemen, tax income, commander limit, court size
    -Grand Moot, reduces short reign penalty up to 10 years
    -Three Smoke Rings, garrison size, tax income, local revolt risk reduction
    -Sauerapfel, tax income, tech growth, levy size
  # Traditional Buildings
    -Keeps, gives levy and garrison size
    -Wall quality, gives fort level
    -Walls, gives fort level, levy size and income
    -Castle Town, gives income and increases court size
    -Shipyard, gives galleys
    -Library, tech growth and retinue size
    -Armoury, gives morale and reinforcement rate
    -Militia Barracks, gives light infantry and archers
    -Barracks, gives heavy infantry and pikemen, adjusted for more pikemen in the WH world
    -Stable, gives light cavalry and some heavy cavalry
  # The Empire
    -Imperial Castle, replaces keep, slightly more garrison for slightly less levy, produces knights
    -Imperial Castle Town, replaces Castle Town, gives extra income, increases court size, and lowers retinue cost up to 50%
    -Private Estates, increases income and retinue size
    -Gunnery School, provides handgunners
  # Sudenburg
    -Sudenburger castle, replaces Keep/Castle Town, boost to taxes up to 30%, court size, less levy and replaces heavy infantry with light infantry/archers
    -House of Knowledge, replaces library, spreads tech growth and increases retinue size
    -Exotic Fruit Plantation, replaces Private Estates, increases income
    -Satrap Free Companies, replaces Militia Barracks, gives light infantry and archers with an offensive bonus up to 30%
    -Infantry Focus, heavy infantry/pikemen offensive and defensive bonus, unlocks Barracks
    -Cavalry Focus, light calv/knights offensive and defensive bonus, unlocks Stables
    -Satrap Infantry Companies, replaces Barracks, balanced towards pikemen
    -Satrap Cavalry Companies, replaces Stables, gives more knights
    -Gunpowder Focus, 40% offensive/defensive bonus, unlocks gunners
    -Artillery Focus, 40% offensive/defensive bonus, unlocks artillery
    -Elephant Focus, 40% offensive/defensive bonus, unlocks elephants
    -Satrap Gunner Companies
    -Satrap Artillery Companies
    -Satrap Elephant Companies
  # Neueslander Special Buildings
    -Neue Towns, replaces Castle Town. gives income and levy reinforcement up to 30%
    -Neue Soldaten, replaces Militia Barracks, less Light infantry, increased morale regeneration
    -Rough Riders, replaces Stable, light cavalry only, increases their defense/morale up to 20%
  # Halflings
    -Halfling Moot, replaces Keep/Castle Town, less levy/garrison, a lot less heavy infantry, increases court size and income
    -Hot-Pot Catapults, replaces Castle Fortifications, gives artillery and archers but less fort level
    -Halfling Shepherds, replaces Castle Wall, levy size and income but no fort level
    -Halfling Militia, replaces Militia Barracks, replaces light infantry with pikemen, less levy overall.
    -Halfling Muster, replaces Barracks, Light infantry/archers instead of heavy infantry/pikemen
    -War Sheep Riders, replaces Stable, light cavalry only
    -Half-tank Foundry, gives artillery, prestige, and morale
 # City
  # Traditional Buildings
    -Wall quality, gives fort level
    -Walls, gives fort level, levy size and income
    -City Guard, gives pikemen and handgunners
    -Merchant Republic Arsenal, gives fort level, garrison size, levy size, and galleys
    -City Shipyard, gives galleys
    -City Port, gives tax income
    -Marketplace, gives tax income
    -Training grounds, gives levy size, and garrison size
    -Mustering Ground, gives light infantry, light cavalry and archers
    -University, gives tech growth and techpoints
  # Terrain Locked
    -Farmlands, terrain locked, trade value and garrison size
    -Mines, terrain locked, trade value and garrison size
    -Forest Villages, terrain locked, trade value and garrison size
    -Desert Villages, terrain locked, trade value and garrison size
    -Tundra Villages, terrain locked, trade value and garrison size
    -Steppe Villages, terrain locked, trade value and garrison size
  # The Empire
    -Imperial Port, gives extra income
    -Imperial Marketplace, gives extra income
    -Imperial Militia Grounds, slightly more garrison for slightly less levy
    -Coaching Inns, levy reinforcement, land organisation and local movement speed up to 30%
  # Halflings
    -Mootland Ogres, Gives heavy infantry and increases their offensive/defensive up to 50%
 # Temple
  # Unique Buildings
    -Great Temple of Sigmar, garrison size, prestige/piety, gunpowder and heavy infantry with 15% morale bonus
    -Temple of the Sacred Flame, fort level, garrison size, prestige/piety, heavy infantry and some knights with 15% defensive bonuses
    -Centre For Manaan, more galleys, some tax income, prestige/piety and heavy infantry
    -Witch Hunter Temple in Sudenburg, fort level, garrison size, prestige/piety, gunpowder and heavy infantry with 15% morale bonus
  # Traditional Buildings
    -Temple Wall, fort level, levy size and tax income
    -Temple Fortifications, increases fort level
    -Elite Barracks, gives Heavy Infantry
    -Temple Monastery, gives levy/garrison size
    -Militia Quarters, Gives light infantry and archers
    -Temple Town, gives income
    -Shipyard, gives galleys
    -School, gives tech growth, culture points
  # The Empire, as well as most of the human races in the game
    -Sigmar, replaces Temple Fortifications, fort level, heavy infantry and improves morale up to 10%
    -Ulric, replaces Elite Barracks, gives Heavy infantry, and improves offensive up to 10%
    -Myrmidia, replaces Temple Monastery, gives slightly less levy/garrison size for some levy reinforcement rate up to 25%
    -Taal and Rhya, replaces Barracks, gives more archers than light infantry, and improves archer defensive and offensive up to 10%
    -Shallyan Hospice, replaces Temple Town, gives income and piety
    -Gardens of Morr, gives knights and improves offensive up to 10%
    -Manaan Shrine, replaces Shipyard, gives galleys and tax income
    -Verena Library, replaces School, gives tech growth, culture and economy tech points
  # Halflings
    -Esmerelda, replaces Temple Monastery, gives almost no levy/garrison, decreases local revolt risk up to 30%
  # Brettonia
    -Grail Chapel, replaces Temple Fortifications, fort level, light cavalry and horse archers to represent mounted yeomen
  # Tilea
    -Lares Shrine, replaces Temple Fortifications, fort level and Pikemen
  # Estalia
    -Santiago Shrine, replaces Temple Fortifications, fort level, light cavalry and Knights
 ###########################
 # Retinue Overhaul I
 ###########################
 # RELIGION RESTRICTED REGIMENTS
    -Warrior Priests of Sigmar, sigmarite, heavy infantry with a 50% offensive and 100% morale bonus
    -Wolves of Ulric, ulrican, heavy infantry with a 100% offensive and 50% morale bonus
    -Company of the Green Hat, taalite, archers with a 100% offensive and 50% defensive bonus
    -Druids of the Secret Fire, old faith, light infantry with a 100% defensive and 50% morale bonus
    -Stormguard, manannite, heavy infantry with a 50% offensive/defensive and morale bonus
 # THE EMPIRE
    # STATE TROOPS
    -Swordsmen, light infantry with a 40% offensive and 20% defensive bonus
    -Spearmen, light infantry with a 20% offensive and 40% defensive bonus
    -Archers, archers with a 30% offensive and 30% defensive bonus
    -Crossbows, archers with a 60% offensive bonus
    -Halbadiers, pikemen with a 20% offensive and 40% defensive bonus
    -Greatswords, heavy infantry with an 40% offensive and 20% morale bonus
    -Outriders, light cavalry with a 40% defensive and 20% morale bonus
    -Imperial Knights, heavy cavalry with a 40% offensive and 20% morale bonus
    -Handgunners, gunpowder with an 40% offensive and 20% morale bonus
    # UNIQUE REPLACEMENT REGIMENTS
    -Deathwatch, Stirland, light infantry with a 20% offensive and 60% morale bonus
    -Berserkers, Nordland, heavy infantry with a 50% offensive and 30% morale bonus
    -Beasthunters, Talabacland, archers with a 50% offensive and 30% defensive bonus
    -Landsknecht, Averland, pikemen with a 50% offensive and 30% morale bonus
    -Carroburg Greatswords, Middenland, heavy infantry with a 60% offensive and 20% morale bonus
    -Forlorn Hope, Sylvania, heavy infantry with a 20% offensive and 60% morale bonus
    -Black Riders, Solland, light cavalry with a 40% offensive and 40% morale bonus
    -Reiksguard, Reikland, heavy cavalry with a 50% offensive and 30% morale bonus
    -Long Rifle Company, Hochland, gunpowder with a 60% offensive and 20% defensive bonus
     # UNIQUE ADDITIONAL REGIMENTS
    -Ostland Ogres, Ostland, heavy infantry and gunpowder with a 100% offensive/defensive bonus for both
    -Pike-and-Shot Company, Ostermark, pikemen and gunpowder with a 50% offensive/defensive bonus for both
    -Westerland Marines, Westerland, heavy infantry and light infantry with a 40% offensive bonus for both
    -Wissengun, Wissenland, artillery with a 60% offensive bonus
    -Wissengun, Wissenland, artillery with a 40% offensive and 20% defensive bonus
  # SUDENBURG
    # TRADITIONAL COMPANIES
    -Imperial Free Company, archers and light infantry, 30% defensive bonus for both
    -Imperial Infantry Company, pikemen and heavy infantry, 20% defensive bonus for both
    -Imperial Cavalry Company, light cavalry and heavy cavalry, 20% offensive bonus for both
    # FOCUS DEPENDENT COMPANIES
    -Imperial Gunner Company, gunpowder units, 20% offensive/morale bonus
    -Imperial Artillery Company, artillery units, 20% offensive/morale bonus
    -Imperial Elephant Company, elephant units, 20% offensive/morale bonus
  # HALFLINGS
    -Crazy Chefs, light infantry, 20% offensive/defensive bonus
    -Halfling Trackers, archers, 20% offensive/defensive bonus
    -Pantry Guards, pikemen and heavy infantry, 20% offensive/defensive bonus
    -War Sheep Riders, light_cavalry, 20% offensive/defensive bonus
    -Battle Ram Riders, heavy cavalry, 20% offensive/defensive bonus
    -Hot Pot Catapults, artillery, 100% offensive/defensive bonus
    -Great Eagle Riders, war beasts, 100% offensive/defensive bonus
  # VAMPIRES
    -Undead Horde, summoned troops with a 100% offensive and 50% morale bonus
    -Dire Wolves, summoned troops with a 10% offensive 50% morale bonus
    -Crypt Ghouls, light infantry with a 40% offensive and 20% defensive bonus
    -Cairn Wraiths, pikemen with a 40% offensive and 20% defensive bonus
    -Grave Guard, heavy infantry with a 20% offensive and 40% defensive bonus
    -Hexwraiths, light cavalry with a 40% offensive and 20% defensive bonus
    -Black Knights, heavy cavalry with a 20% offensive and 40% defensive bonus
    -Vampire Knights, special troops, with a 70% offensive, 30% defensive, and 50% morale bonus
    -Corpse Carts, chariots, 50% defensive and 50% morale bonus
    -Crypt Horrors, war beasts, 50% offensive and 100% defensive bonus
    -Vargheists, war beasts, 100% offensive 50% defensive bonus
 ###########################
Changelog V1.3.17
 ###########################
 # Minor Changes II
 ###########################
     -Updated Frontend GFX for the loading bar and the hints section
     -Converted the new popup sections of the Frontend GUI used for the featured ruler/ck3 trailer
     -Moved the new Map Mode job to the spymaster
     -for now the offmap "china" power has been moved to the southlands and araby. This will be converted into Cathay in the southlands overhaul
     -All bugs reported from V1.3.16 are fixed
 ###########################
 # Cassus Belli Overhaul I
 ###########################
     -Grail crusades will continue to use the old crusade system
     -The new crusade system will be converted to work for chaos, these "Black Crusades" will be elaborated on in the chaos overhaul
     -A Northern crusade can be called by Holy Orders of the Empire
     -Reconquista system has been converted to the Tilea/Estalia regions of the old world.
     -IN PROGRESS...
 ###########################
 # Decision Overhaul I
 ###########################
     -Created "offer brief non-aggression pact" targetted decision, this is intended as a new way to form alliances. Limited to your religion group usually though there are exceptions (such as between humans and dwarfs/elves)
     -IN PROGRESS...
