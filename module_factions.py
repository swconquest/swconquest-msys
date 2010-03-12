from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0xFFFF66),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

#SW MF added new factions  
  ("trade_federation","Independent", ff_always_hide_label, 0.5,[("outlaws",-0.5),("peasant_rebels", -0.1),("deserters", -0.2),("mountain_bandits", -0.5),("forest_bandits", -0.5),("slavers", 0.1),("manhunters", 0.1)], [],0xDDDD33),
  #("privateers", "Privateers", 0, 0.5, [("outlaws",-0.5),("peasant_rebels", -0.1),("deserters", -0.2),("mountain_bandits", -0.5),("forest_bandits", -0.5),("slavers", 0.1),("manhunters", 0.1)], [],0xCC2211),
  #("bounty_hunters", "Bounty Hunters", 0, 0.5, [("outlaws",0),("mountain_bandits", 0),("forest_bandits", 0)],[],0x96CDCD),

  ("dark_knights","Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "culture_1", 0, 0.9, [], []),
  ("culture_2",  "culture_2", 0, 0.9, [], []),
  ("culture_3",  "culture_3", 0, 0.9, [], []),
#  ("culture_4",  "culture_4", 0, 0.9, [], []),
#  ("culture_5",  "culture_5", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], [], 0xC0C0FF),
  ("player_supporters_faction","Player Faction",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], []),

  #Colors - 0xCC2211 = red, 0xDDDD33 = yellow, 0x33DDDD = blue, 0x33DD33 = green
  
  #SW - Swadia (Kingdom 1) = Galactic Empire
  ("kingdom_1",  "Galactic Empire", 0, 0.9,   [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_2", -0.4)], [], 0x33DDDD),  # BLUE
  #("kingdom_1",  "Galactic Empire", 0, 0.9,   [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_2", -0.5)], [], 0xCC2211),   # RED
  #SW - Vaegir (Kingdom 2) = Rebal Alliance
  #("kingdom_2",  "Rebel Alliance",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1", -0.4)], [], 0x33DD33),	#GREEN
  ("kingdom_2",  "Rebel Alliance",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1", -0.4)], [], 0xce0b0b),	#RED
  #SW  Khergit Khanate (Kingdom 3) = Hutt Cartel
  ("kingdom_3",  "Hutt Cartel", 0, 0.9,       [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xDD8844),	#ORANGE
#4 = Nords
#  ("kingdom_4",  "Kingdom of Nords",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xDDDD33),
#5 = Rhodoks
#  ("kingdom_5",  "Kingdom of Rhodoks",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x33DDDD),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "robber_knights", 0, 0.1, [], []),

  ("khergits","Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0xFF99CC),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xFFFF66),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xFFFF66),

  ("undeads","Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","Slavers", 0, 0.1, [], []),
  ("peasant_rebels","Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","Noble Refugees", 0, 0.5,[], []),
]
