# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_minorplanet = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main_Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-35.1,-31.47),[(trp_player,1,0)]),
  ("temp_party","temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_unarmed_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed","enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

#  ("minorplanet_reinforcements","minorplanet_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

#Tavern recruitment and ale START
  ("town_merc_1","town1_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_2","town2_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_3","town3_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_4","town4_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_5","town5_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_6","town6_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_7","town7_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_8","town8_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_9","town9_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_10","town10_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_11","town11_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_12","town12_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_13","town13_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_14","town14_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_15","town15_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_16","town16_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_17","town17_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_18","town18_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_19","town19_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_20","town20_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
  ("town_merc_21","town21_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),
#Tavern recruitment and ale END

###############################################################  
  #("zendar","Zendar",pf_disabled|icon_sw_town_green|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.56,-23.48),[]),
 #SW MF added base (ie. shipyards)
  ("shipyard_trade_federation","Trade_Federation",icon_cis_star_cruiser|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.41,-27.52),[],260),
  ("shipyard_kuat","Kuat_Shipyards",icon_XQ_04_Station_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.81, -19.65),[],260),
  ("shipyard_raxus","Raxus_Prime_Shipyards",icon_XQ_04_Station_4|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.63, 102.11),[],260), #[swycartographr] prev. coords: (130.52, 124.81)
  ("shipyard_corellia","Corellia_Shipyards",icon_XQ_04_Station_1|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.96, -42.40),[],260),
  ("shipyard_moncal","Mon_Cal_Shipyards",icon_XQ_04_Station_2|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.30, 80.93),[],260),
  ("shipyard_mandalore","Mandalore_Shipyards",icon_XQ_04_Station_5|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.65, 64.01),[],260),
  ("shipyard_fondor","Fondor_Shipyards",icon_XQ_04_Station_3|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.70, -52.52),[],260),
  
  

  # Note - if you rename towns make sure to update the center_#_faction in module_strings.py
  ("mandalore","Mandalore",  icon_sw_swy_rePlanet_earth|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.6,86.7),[],170), #new pos
 #("byss","Byss",     icon_sw_swy_Planet_Endor|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.27,-25.15),[], 120),  
  ("christophsis","Christophsis", icon_sw_swy_christophsis|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.59,-105.27),[], 120), #newpos   #[swycartographr] prev. coords: (-59, -101)
  ("endor","Endor",   icon_sw_swy_Planet_Endor|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.79,-94.34),[],80), #new pos      #[swycartographr] prev. coords: (-88, -99)
  ("corellia","Corellia",     icon_sw_swy_rePlanet_kashyyyk|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.81,-5.16),[],290), #new pos #[swycartographr] prev. coords: (-5.7, -2.5)
  ("naboo","Naboo",  icon_sw_swy_rePlanet_kashyyyk|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.81,-84.66),[], 90), #new pos   #[swycartographr] prev. coords: (26.6, -104)
  ("kessel","Kessel",   icon_sw_swy_Planet_Kessel|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(111.7,30),[], 155),   #new pos
  ("dantooine","Dantooine",   icon_sw_swy_rePlanet_wilderness|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.5,125.46),[],240), #new pos-custom #[swycartographr] prev. coords: (-29.21, 129.68)
  ("geonosis","Geonosis", icon_sw_swy_Planet_geonosis|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.99,-98.68),[], 175),  #new pos #[swycartographr] prev. coords: (78.7, -103.7)
  ("mon_cal","Mon_Cal",   icon_sw_swy_rePlanet_water|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.16,98.66),[],90), #new pos
  ("kashyyyk","Kashyyyk",   icon_sw_swy_rePlanet_kashyyyk|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.5,36.5),[], 310),  #new pos
  ("hoth","Hoth",   icon_sw_swy_rePlanet_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.02,-123.04),[], 150), #new pos--close enough   #[swycartographr] prev. coords: (-45, -136.7)
  ("gamorr","Gamorr", icon_sw_swy_rePlanet_gas|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.41,-49.92),[],25), #new pos
  ("yavin_iv","Yavin_IV",icon_sw_swy_rePlanet_wilderness|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.69,107.87),[],60), #new pos #[swycartographr] prev. coords: (47.74, 112.5)
  ("tatooine","Tatooine",  icon_sw_swy_Planet_Tatooine|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.28,-82.5),[],135), #new pos #[swycartographr] prev. coords: (77.3, -96.6)
 #("reecee","Reecee",  icon_sw_swy_rePlanet_ice|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.73,28.57),[],135),
  ("manaan","Manaan",  icon_sw_swy_rePlanet_water|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24,6.2),[],135), #new pos
  ("coruscant","Coruscant",  icon_sw_swy_Planet_Coruscant|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.5,34),[],135), #new pos
  ("ryloth","Ryloth",  icon_sw_swy_Planet_Tatooine|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.25,-129.63),[], 135), #new pos--close enough  #[swycartographr] prev. coords: (82, -116.12)
  ("nalhutta","Nal_Hutta",  icon_sw_swy_Planet_Tatooine|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89, -6),[],135),  #new pos
  ("bothawui","Bothawui",  icon_sw_swy_rePlanet_kashyyyk|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75,-50.78),[],135), #new pos
  ("mustafar","Mustafar",  icon_sw_swy_Planet_lava|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.12,-125.6),[],135), #custom pos #[swycartographr] prev. coords: (-24.1, -144.38)
  ("kamino","Kamino",  icon_sw_swy_rePlanet_water|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100,-59),[],135), #new pos--close enough
  ## SWY 0.9.0.3 - Added Taris
  ("taris","Taris",  icon_sw_swy_Planet_Taris|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.66,90.63),[],135), #new pos
  
  ## SWY 0.9.0.4 - Added Raxus Prime and Sarapin
  ("raxusprime","Raxus_Prime",  icon_sw_swy_Planet_RaxusPrime|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.90,106.6),[],135), #newpos #[swycartographr] prev. coords: (99.9, 114.62)
  ("sarapin","Sarapin",  icon_sw_swy_Planet_Sarapin|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.5,17),[],135), #new pos
  ("hypori","Hypori",  icon_sw_swy_Planet_Tatooine|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.86,-71.17),[],135), #new pos  #[swycartographr] prev. coords: (92, -91)
  ("felucia","Felucia",  icon_sw_swy_Planet_forest|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.56,108.78),[],135), #newpos
  ("bespin","Bespin",icon_sw_swy_rePlanet_gas|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.22,-102),[],50), #new pos--close enough #[swycartographr] prev. coords: (-50, -129.7)
  
#   Aztaq_Outpost       
#  Malabadi_Outpost
  # Note - if you rename castles make sure to update the center_#_faction in module_strings.py
#  ("spacestation_1","Bespin",icon_sw_swy_rePlanet_gas|pf_castle|pf_disabled|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.44,-93.66),[],50),
  ("spacestation_2","Corellia_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.38,-50.53),[],75),
  ("spacestation_3","Yavin_IV_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.7,101.65),[],100), #[swycartographr] prev. coords: (69.39, 97.03)
  ("spacestation_4","Dagobah",icon_sw_swy_Planet_forest|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.61,-108.43),[],180), #custom-close #[swycartographr] prev. coords: (0.5, -120.47)
  ("spacestation_5","Death Star",icon_sw_swy_Death_Star|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.69,-91.31),[],90),#new pos #[swycartographr] prev. coords: (-93, -93)
  ("spacestation_6","Endor_Outpost",icon_asteroid_base|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.93,-79.38),[],55),     #[swycartographr] prev. coords: (-93.99, -67.09)
  ("spacestation_7","Mon_Cal_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.38,87.90),[],45),
  ("spacestation_8","Ryloth_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.41,-106.50),[],30), #[swycartographr] prev. coords: (67.35, -106.5)
  ("spacestation_9","Christophsis_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86,-30.28),[],100),
  ("spacestation_10","Kessel_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.38,37.59),[],110),
  ("spacestation_11","Avatar_Platform",icon_asteroid_base|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.43,12.32),[],75),
  ("spacestation_12","Manaan_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.11,33.15),[],95),
  ("spacestation_13","Christophsis_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.20,-24.32),[],115),
  ("spacestation_14","Nal_Hutta_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.38,16.21),[],90),
  ("spacestation_15","Dantooine_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.65,88.16),[],235),
  ("spacestation_16","Kashyyyk_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.45,13.6),[],45),      #[swycartographr] prev. coords: (16.12, -3.18)
  ("spacestation_17","Coruscant_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.63,12.47),[],15),
  ("spacestation_18","Hoth_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.64,-113.16),[],300), #[swycartographr] prev. coords: (-113.15, -111.99)
  ("spacestation_19","Bakura",icon_sw_planet_green|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.29,-99.84),[],280), #new pos #[swycartographr] prev. coords: (-106.5, -97.4)
  ("spacestation_20","Gamorr_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.44,-19.18),[],260),
  ("spacestation_21","Mandalore_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.34,59.15),[],260),
  ("spacestation_22","Manaan_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.63,29.82),[],260),
  ("spacestation_23","Corellia_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.37,-48.62),[],80),
  ("spacestation_24","Geonosis_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.41,-116.13),[],260), #[swycartographr] prev. coords: (112.72, -129.28)
  ("spacestation_25","Mandalore_Outpost",icon_asteroid_base|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.67,65.92),[],260),
  ("spacestation_26","Geonosis_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.96,-96.29),[],260),  #[swycartographr] prev. coords: (118.97, -112.78)
  ("spacestation_27","Kessel_Outpost",icon_asteroid_base|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.24,54.11),[],260),
  ("spacestation_28","Dathomir",icon_sw_planet_green|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.84,90.30),[],260),
  ("spacestation_29","Hoth_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.45,-129.02),[],280),
  ("spacestation_30","Tatooine_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.48,-90.26),[],260),
  ("spacestation_31","Gamorr_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.86,-5.82),[],260),
  ("spacestation_32","Ryloth_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.02,-116.90),[],260),    #[swycartographr] prev. coords: (81.95, -116.9)
  ("spacestation_33","Naboo_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.09,-77.19),[],80),       #[swycartographr] prev. coords: (6.69, -83.27)
  ("spacestation_34","Dantooine_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.18,105.38),[],260),
  ("spacestation_35","Naboo_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.33,-94.07),[],260), #[swycartographr] prev. coords: (19.95, -98.34)
  ("spacestation_36","Coruscant_Battlestation",icon_battlestation|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.59,17.84),[],260),
  ("spacestation_37","Yavin_IV_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.13,117.71),[],260),   #[swycartographr] prev. coords: (62.89, 111.74)
  ("spacestation_38","Nal_Hutta_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.23,21.23),[],260),
  ("spacestation_39","Mon_Cal_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.61,78.28),[],280),
  ("spacestation_40","Tatooine_Outpost",icon_outpost_imp|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.59,-83.24),[],260),   #[swycartographr] prev. coords: (108.11, -73.07)
#Rhen Var
  ("spacestation_41","Rhen_Var",icon_sw_swy_rePlanet_snow|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.11,63.07),[],260),
  ("spacestation_42","Saleucami",icon_sw_swy_rePlanet_snow|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.57,-92.93),[],260), #[swycartographr] prev. coords: (-108.11, -93.07)
#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("minorplanet_1","Honoghr",  icon_sw_minorplanet_01|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.20,29.84),[],100),
  ("minorplanet_2","Chandrila",  icon_sw_minorplanet_02|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.65,25.32),[],110),
  ("minorplanet_3","Tholatin",  icon_sw_minorplanet_03|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.55,-15.31),[],120),
  ("minorplanet_4","Ilum",  icon_sw_minorplanet_04|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100,82.36),[],130), #new pos
  ("minorplanet_5","Sernpidal",  icon_sw_minorplanet_05|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.75,133.84),[],170),
  ("minorplanet_6","Velmor",  icon_sw_minorplanet_07|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.74,48.78),[],100),
  ("minorplanet_7","Hoth_Moon",  icon_sw_swy_rePlanet_ice|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.85,-129),[],110), #[swycartographr] prev. coords: (-80.03, -117.63)
  ("minorplanet_8","Bespin_Moon",  icon_sw_minorplanet_08|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.16,-99.25),[],120), #[swycartographr] prev. coords: (-82.94, -101.98)
  ("minorplanet_9","Dubrillion",  icon_sw_minorplanet_09|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.15,124.18),[],130),
  ("minorplanet_10","Riflor",  icon_sw_minorplanet_10|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.48,-82.27),[],170),

  ("minorplanet_11","Siskeen",  icon_sw_minorplanet_11|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.68,-49.02),[],100),
  ("minorplanet_12","Rakata_Prime",  icon_sw_minorplanet_12|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.83,-1.29),[],110), #new pos
  ("minorplanet_13","Myrkr",  icon_sw_minorplanet_13|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.98,35.17),[],120),
  ("minorplanet_14","Ziost",  icon_sw_minorplanet_14|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.17,134.87),[],130), #[swycartographr] prev. coords: (112.93, 131.61)
  ("minorplanet_15","Corellia_Moon",  icon_sw_swy_rePlanet_rock|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.07,-38.26),[],170),
  ("minorplanet_16","Vargnat",  icon_sw_minorplanet_16|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.94,-72.38),[],170),
  ("minorplanet_17","Lannik",  icon_sw_minorplanet_17|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.50,-29.11),[],35),
  ("minorplanet_18","Fondor",  icon_sw_minorplanet_18|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.08,-49.59),[],170),
  ("minorplanet_19","Bakura_Moon",  icon_sw_minorplanet_19|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.16,-67.80),[],170),
  ("minorplanet_20","Mon_Cal_Moon",  icon_sw_minorplanet_16|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.17,92.05),[],170),

  ("minorplanet_21","Isde_Naha",  icon_sw_minorplanet_20|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.71,-117.22),[],100), #[swycartographr] prev. coords: (-55.38, -126.97)
  ("minorplanet_22","Duro",  icon_sw_minorplanet_21|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.05,-46.17),[],110),
  ("minorplanet_23","Coruscant_Moon",  icon_sw_minorplanet_01|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.15,4.68),[],120),
  ("minorplanet_24","Anoth",  icon_sw_minorplanet_02|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.71,-139.42),[],130), #[swycartographr] prev. coords: (-96.76, -145.64)
  ("minorplanet_25","Tatooine_Moon",  icon_sw_minorplanet_12|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.13,-78.73),[],170), #[swycartographr] prev. coords: (128.03, -75.02)
  ("minorplanet_26","Rori",  icon_sw_minorplanet_03|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.32,-72.05),[],170),   #[swycartographr] prev. coords: (26.48, -84.55)
  ("minorplanet_27","Bilbringi",  icon_sw_minorplanet_04|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.26,40.82),[],170),
  ("minorplanet_28","Tynna",  icon_sw_minorplanet_05|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.61,-58.63),[],170),
  ("minorplanet_29","Dantooine_Moon",  icon_sw_minorplanet_07|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.40,105.75),[],170),
  ("minorplanet_30","Corulag",  icon_sw_swy_rePlanet_ice|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.01,1.11),[],170),

  ("minorplanet_31","Togoria",  icon_sw_minorplanet_08|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.01,24.47),[],100),
  ("minorplanet_32","Gall",  icon_sw_minorplanet_09|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.52,-97.6),[],110),    #[swycartographr] prev. coords: (75.23, -92.34)
  ("minorplanet_33","Muunulist",  icon_sw_minorplanet_10|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.31,88.06),[],120),
  ("minorplanet_34","Ruuria",  icon_sw_minorplanet_11|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.28,143.42),[],130),
  ("minorplanet_35","Iridonia",  icon_sw_minorplanet_12|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.63,53.15),[],170),
  ("minorplanet_36","Kessel_Moon",  icon_sw_minorplanet_21|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(119.26,25.67),[],170), #[swycartographr] prev. coords: (134.13, 40.79)
  ("minorplanet_37","Bimmsari",  icon_sw_minorplanet_13|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.11,1.98),[],170),
  ("minorplanet_38","Belkadan",  icon_sw_minorplanet_14|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.34,139.70),[],170),
  ("minorplanet_39","Helska",  icon_sw_swy_rePlanet_rock|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.43,124.49),[],170),
  ("minorplanet_40","Saki",  icon_sw_minorplanet_16|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.34,-30.29),[],170),

  ("minorplanet_41","Nar_Shadda",  icon_sw_swy_NarShadda|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.44,-11),[],100), #new pos
  ("minorplanet_42","Bothawui_Moon",  icon_sw_minorplanet_01|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.38,-47.51),[],110),
  ("minorplanet_43","Alzoc_III",  icon_sw_minorplanet_18|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.67,-138.7),[],120), #[swycartographr] prev. coords: (96.32, -141.22)
  ("minorplanet_44","Ruusan",  icon_sw_minorplanet_19|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.82,-30.01),[],130),
  ("minorplanet_45","Dathomir_Moon",  icon_sw_minorplanet_16|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.07,98.41),[],170),
  ("minorplanet_46","Yag'Dhul",  icon_sw_minorplanet_20|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.96,-66.68),[],170),
  ("minorplanet_47","Selvaris",  icon_sw_minorplanet_21|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.92,27.49),[],170),
  ("minorplanet_48","Sump",  icon_sw_minorplanet_01|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.4,-114.06),[],170), #[swycartographr] prev. coords: (-139.37, -124.54)
  ("minorplanet_49","Mustafar_Moon",  icon_sw_minorplanet_19|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.45,-120.10),[],10), #[swycartographr] prev. coords: (-22.68, -120.1)
  ("minorplanet_50","Dosuun",  icon_sw_minorplanet_02|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.44,-135.1),[],170), #[swycartographr] prev. coords: (-140.92, -144.82)

  ("minorplanet_51","Yaga_Minor",  icon_sw_minorplanet_03|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-135.01,65.11),[],100),
  ("minorplanet_52","Nar_Kreeta",  icon_sw_minorplanet_04|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(67.37,-14),[],110),
  ("minorplanet_53","Pzob",  icon_sw_minorplanet_05|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.5,-80),[],120), #new pos
  ("minorplanet_54","Barab_I",  icon_sw_swy_rePlanet_ice|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.36,8.70),[],130),
  ("minorplanet_55","Lamaredd",  icon_sw_minorplanet_07|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.27,-127.36),[],170), #[swycartographr] prev. coords: (137.56, -132.27)
  ("minorplanet_56","Ithor",  icon_sw_minorplanet_08|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.07,67.51),[],170),
  ("minorplanet_57","Kuat",  icon_sw_minorplanet_09|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.32,-15.23),[],170),
  ("minorplanet_58","Rodia",  icon_sw_minorplanet_13|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.04,-64.79),[],170), #tweaked-approx
  ("minorplanet_59","Bastion",  icon_sw_minorplanet_10|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.31,116.47),[],170),
  ("minorplanet_60","Anobis",  icon_sw_minorplanet_11|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.62,47.73),[],170),

  ("minorplanet_61","Thisspias",  icon_sw_minorplanet_12|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.31,-11.03),[],100),
  ("minorplanet_62","Vjun",  icon_sw_minorplanet_13|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.34,70.70),[],100),
  ("minorplanet_63","Drongar",  icon_sw_minorplanet_14|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80,58),[],100),
  ("minorplanet_64","Kamino_Moon",  icon_sw_swy_rePlanet_rock|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.83,-61.80),[],100),
  ("minorplanet_65","Mimban",  icon_sw_minorplanet_16|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.89,-48.58),[],100),
  ("minorplanet_66","Alaris_Prime",  icon_sw_minorplanet_07|pf_minorplanet,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.60,3.90),[],100),
  ("minorplanet_67","Wayland",  icon_sw_minorplanet_18|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.76,43.36),[],100),
  ("minorplanet_68","Vulpter",  icon_sw_minorplanet_19|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.56,-30.10),[],100),
  ("minorplanet_69","Bimmiel",  icon_sw_minorplanet_20|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.19,40.35),[],100),
  ("minorplanet_70","Gamorr_Moon",  icon_sw_minorplanet_21|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.91,-5.99),[],100),

  ("minorplanet_71","Concordia",  icon_sw_minorplanet_01|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.67,73.98),[],20),
  ("minorplanet_72","Bogden",  icon_sw_minorplanet_02|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.24,23.75),[],60),
  ("minorplanet_73","Dagobah_Moon",  icon_sw_minorplanet_05|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.1,-115.73),[],55), #[swycartographr] prev. coords: (23.12, -131.09)
  ("minorplanet_74","Roon",  icon_sw_minorplanet_03|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.91,-55.59),[],15),
  ("minorplanet_75","Almania",  icon_sw_minorplanet_04|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.87,133.37),[],10), #[swycartographr] prev. coords: (137.88, 140.72)
  ("minorplanet_76","Obroa_Skai",  icon_sw_minorplanet_05|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.17,29.45),[],35),
  ("minorplanet_77","Ord_Mantell",  icon_sw_swy_rePlanet_ice|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.92,52.16),[],160),
  ("minorplanet_78","Charros_IV",  icon_sw_minorplanet_07|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.21,20.24),[],180),
  ("minorplanet_79","Manaan_Moon",  icon_sw_minorplanet_08|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.66,25.29),[],0),
  ("minorplanet_80","N'Zoth",  icon_sw_minorplanet_09|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.9,22.1),[],40), #new pos

  ("minorplanet_81","Brentaal",  icon_sw_minorplanet_10|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.55,5.17),[],20), #[swycartographr] prev. coords: (-19.26, 5.72)
  ("minorplanet_82","Garqi",  icon_sw_minorplanet_11|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.16,76.92),[],60),
  ("minorplanet_83","Xal_3",  icon_sw_minorplanet_12|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.15,-80.89),[],55),
  ("minorplanet_84","Christophsis_Moon",  icon_sw_minorplanet_13|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.02,-18.25),[],15),
  ("minorplanet_85","Phindar",  icon_sw_minorplanet_14|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.02,80.30),[],10),
  ("minorplanet_86","Vaal",  icon_sw_swy_rePlanet_rock|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.09,118.84),[],35),
  ("minorplanet_87","Serenno",  icon_sw_minorplanet_16|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.54,113.54),[],160),
  ("minorplanet_88","Derra_IV",  icon_sw_minorplanet_17|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.88,-66.15),[],180),
  ("minorplanet_89","Ryloth_Moon",  icon_sw_minorplanet_18|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.70,-122.71),[],0), #[swycartographr] prev. coords: (63.7, -121.52)
  ("minorplanet_90","Khomm",  icon_sw_minorplanet_19|pf_minorplanet, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.53,-42.55),[],40),

  #("salt_mine","Salt_Mine",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.02,-41.28),[]),
  #("four_ways_inn","Four_Ways_Inn",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.99,-46.69),[]),
  #("test_scene","test_scene",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.46,-36.24),[]),
  #("battlefields","battlefields",pf_disabled|icon_minorplanet_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.22,-27.59),[]),
  #("dhorak_keep","Dhorak_Keep",icon_sw_town_green|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.17,-31.98),[]),

  ("training_ground","Training_Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.38,-18.65),[]),

  ("training_ground_1","Training_Academy",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.96,67.16),[],100),
  ("training_ground_2","Training_Academy",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.22,116.11),[],100),
  ("training_ground_3","Training_Academy",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.81,-36.04),[],100),
  ("training_ground_4","Training_Academy",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.89,32.46),[],100),
  ("training_ground_5","Training_Academy",  icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.36,-88.41),[],100), #[swycartographr] prev. coords: (-43.21, -90.24)


#  bridge_a
  ("sun_01","<sun01>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.88,128.18),[],100),
  ("sun_02","<sun02>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.74,-106.04),[],100),
  ("sun_03","<sun03>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.50,44.48),[],100),
  ("sun_04","<sun04>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.70,-40.95),[],100),
  ("sun_05","<sun05>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.28,-19.28),[],100),
  ("sun_06","<sun06>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.03,-72.64),[],100),
  ("sun_07","<sun07>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.96,34.87),[],100),
  ("sun_08","<sun08>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.07,-29.46),[],100),
  ("sun_09","<sun09>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.16,-96.57),[],100),
  ("sun_10","<sun10>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.11,95.27),[],100),
  ("sun_11","<sun11>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.37,-97.56),[],100),
  ("sun_12","<sun12>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.49,-72.42),[],100),
  ("sun_13","<sun13>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.26,141.42),[],100),
  ("sun_14","<sun14>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.50,71.45),[],100),
  ("sun_15","<sun15>",icon_strategicmap_sun|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.87,-50.30),[],100),
  
  
#ship debris  
  ("Debris_01","<debris01>",icon_y_wing_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.10,-113.10),[],100),
  ("Debris_02","<debris02>",icon_tie_fighter_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.50,-106.20),[],100),  
  ("Debris_03","<debris03>",icon_z95_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.80,-10.30),[],100),  
  ("Debris_04","<debris04>",icon_tie_fighter_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.50,-33.80),[],100),
  ("Debris_05","<debris05>",icon_z95_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.71,23.11),[],100),
  ("Debris_06","<debris06>",icon_z95_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.77,58.74),[],100),  
  ("Debris_07","<debris07>",icon_tie_fighter_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.75,121.97),[],100),  
  ("Debris_08","<debris08>",icon_y_wing_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.21,132.60),[],100),  
  ("Debris_09","<debris09>",icon_z95_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.02,76.39),[],100),    
  ("Debris_10","<debris10>",icon_tie_fighter_debris|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.19,14.56),[],100),  
  
#  ("Bridge_1","1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.56, 59.89),[], 90),
#  ("Bridge_2","2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.14, 34.13),[], 64),
#  ("Bridge_3","3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.92, 72.98),[], 10),
#  ("Bridge_4","4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.94, 67.25),[], 90),
#  ("Bridge_5","5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.16, 79.18),[], 135),
#  ("Bridge_6","6",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.60, 64.32),[], 120),
#  ("Bridge_7","7",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.47, 43.28),[], 75),
#  ("Bridge_8","8",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.46, 21.19),[], 55),
#  ("Bridge_9","9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.13, 48.21),[], 60),
#  ("Bridge_10","10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.05, 54.55),[], 35),
#  ("Bridge_11","11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.85, -41.40),[], 90),
#  ("Bridge_12","12",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.17, 79.57),[], 135),
#  ("Bridge_13","13",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.16, 81.16),[], 90),
#  ("Bridge_14","14",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.88, 78.80),[], 75),
#  ("Bridge_15","15",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.01, -29.60),[], 15),

  ("jawa_spawn_point"   ,"<jawa_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(43.21,-130.13),[(trp_jawa,15,0)]),
  ("night_fang_pirate_spawn_point"  ,"<steppe_bandit_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-66.83,88.49),[(trp_jawa,15,0)]),
  ("night_fang_pirate_spawn_point_2"  ,"<steppe_bandit_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42.37,47.18),[(trp_jawa,15,0)]),
  ("night_fang_pirate_spawn_point_3"  ,"<steppe_bandit_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35.12,79.88),[(trp_jawa,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_jawa,15,0)]),
  ("blazing_claw_pirate_spawn_point"  ,"<blazing_claw_pirate_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(43.76,104.07),[(trp_jawa,15,0)]),
  ("blazing_claw_pirate_spawn_point_2"  ,"<blazing_claw_pirate_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(25.70,86.21),[(trp_jawa,15,0)]),
  ("blazing_claw_pirate_spawn_point_3"  ,"<blazing_claw_pirate_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(63.68,60),[(trp_jawa,15,0)]),
  ("black_sun_pirate_spawn_point","<black_sun_pirate_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-20.56,-81.35),[(trp_jawa,15,0)]),
  ("black_sun_pirate_spawn_point_2","<black_sun_pirates_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-66.40,-60.25),[(trp_jawa,15,0)]),
  ("black_sun_pirate_spawn_point_3","<black_sun_pirates_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-62.39,-86.97),[(trp_jawa,15,0)]),
  ("tusken_raider_spawn_point_1"   ,"<tusken_raiders_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(133.24,-58.60),[(trp_jawa,15,0)]),
  ("tusken_raider_spawn_point_2"   ,"<tusken_raiders_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.72,-95.88),[(trp_jawa,15,0)]),
  ("tusken_raider_spawn_point_3"   ,"<tusken_raider_sp>",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(79.10,-75.61),[(trp_jawa,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(23,-112.26),[(trp_jawa,15,0)]),
  
  #SW - temp parties to store spaceship information
  #empire - tie_fighter is spaceship_empire_begin
  ("spaceship_tie_fighter","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_imperial_shuttle","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_imperial_trade_frigate","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_imperial_dreadnaught_frigate","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_imperial_victory_c2_frigate","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_imperial_star_destroyer","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_imperial_star_destroyer_interdictor","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  #rebel - a_wing is spaceship_rebel_begin and spaceship_empire_end
  ("spaceship_a_wing","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_x_wing","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_y_wing","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_moncal_cruiser","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_rebel_transport","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_corellian_gunship","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_corellian_corvette","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),

  #hutt - hutt_patrol is spaceship_hutt_begin and spaceship_rebel_end
  ("spaceship_hutt_patrol","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_hutt_trade","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_hutt_frigate_mk1","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_hutt_frigate_mk2","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_hutt_cruiser","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  #other - z95 is spaceship_other_begin and spaceship_hutt_end
  ("spaceship_z95","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_starchaser","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_nebulon","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]), 
  ("spaceship_scyk_fighter","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_civilian_transport","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_civilian_cruiser","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  ("spaceship_mercenary_shuttle","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_mercenary_fighter","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_mercenary_raider","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_freighter","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_bulk_freighter","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  
  ("spaceship_cis_star_cruiser","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),  

  #this next ship is spaceship_end
  ("spaceship_end","Spaceship Array",icon_minorplanet_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.00,-40.00),[]),
  
  
    #Galaxy center sed for part_sys. Nevermind, particle system disapears when player moves the camear, no usable as galaxy surface
  #("Galaxy_center","galaxy_center",icon_sw_galaxy|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[],100),
  
]
