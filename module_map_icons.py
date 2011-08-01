# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.35
#avatar_scale = 0.15
planet_main_scale = 0.80
planet_training_scale = 0.55
planet_minor_scale = 0.5
death_star_scale = 0.7
spacestation_scale = 0.5
cis_star_cruiser_scale = 0.60

ship_verylarge_scale = 0.80
ship_large_scale = 0.65
ship_medium_scale = 0.50
ship_small_scale = 0.40
ship_verysmall_scale = 0.30

#SW - switched all map icons to planets or ships

map_icons = [
  #("player",mcn_no_shadow,"civilian_transport", ship_verysmall_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("player",mcn_no_shadow,"Action_IV", ship_verysmall_scale, snd_ship_noise, 0.15, 0.173, 0),
  
  ##@> //purchasable ships - empire
  ("imperial_star_destroyer",mcn_no_shadow,"Imp_ISD", ship_verylarge_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("imperial_star_destroyer_interdictor",mcn_no_shadow,"Imp_ISD_Interdictor", ship_verylarge_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("imperial_victory_c2_frigate",mcn_no_shadow,"Imp_Victory_Class_II_Frigate", ship_verylarge_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("imperial_dreadnaught_frigate",mcn_no_shadow,"Imp_Dreadnaught_Frigate", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("imperial_trade_frigate",mcn_no_shadow,"Imp_trade_frigate", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("tie_fighter",mcn_no_shadow,"tie_fighter", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("imperial_shuttle",mcn_no_shadow,"imperial_shuttle", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ##@> //purchasable ships - rebel
  ("a_wing",mcn_no_shadow,"a_wing", ship_verysmall_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ("rebel_transport",mcn_no_shadow,"rebel_transport", ship_large_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("corellian_gunship",mcn_no_shadow,"Cor_Gunship", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("corellian_corvette",mcn_no_shadow,"swy_corellian_corvette", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("moncal_cruiser",mcn_no_shadow,"Moncal_Cruiser", ship_large_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("x_wing",mcn_no_shadow,"xwing", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ("x_wing2",mcn_no_shadow,"xwing_2", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ("x_wing3",mcn_no_shadow,"xwing_3", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ("x_wing4",mcn_no_shadow,"xwing_4", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ("x_wing5",mcn_no_shadow,"xwing_5", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ("y_wing",mcn_no_shadow,"y_wing_gold", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  ##@> //purchasable ships - hutt
  ("hutt_cruiser",mcn_no_shadow,"Hutt_Cruiser", ship_large_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("hutt_frigate_mk2",mcn_no_shadow,"Hutt_Frigate_MK2", ship_large_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("hutt_frigate_mk1",mcn_no_shadow,"Hutt_Frigate_MK1", ship_large_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("hutt_trade",mcn_no_shadow,"Hutt_Trade", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("hutt_patrol",mcn_no_shadow,"Hutt_Patrol", ship_verysmall_scale, snd_ship_noise, 0.15, 0.173, 0),
  ##@> //purchasable ships - other
  ("nebulon",mcn_no_shadow,"swy_nebulon", cis_star_cruiser_scale,0),
  ("starchaser",mcn_no_shadow,"vec_starchaser", ship_small_scale,0),
  ("z95",mcn_no_shadow,"z96", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("tran_slaver",mcn_no_shadow,"tran_slaver", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("scyk_fighter",mcn_no_shadow,"hutt_scyk_fighter", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),	
  #("mercenary_raider",mcn_no_shadow,"mercenary_raider", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("mercenary_raider",mcn_no_shadow,"Wild_Karrde", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
 # ("freighter",mcn_no_shadow,"freighter", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("freighter",mcn_no_shadow,"swy_nebulon", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0), 
  ("bulk_freighter",mcn_no_shadow,"bulk_frigate", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),  
  #("mercenary_fighter",mcn_no_shadow,"z95", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),    
  ("mercenary_fighter",mcn_no_shadow,"vec_starchaser", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),    
  #("mercenary_shuttle",mcn_no_shadow,"shuttle", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),    
  ("mercenary_shuttle",mcn_no_shadow,"Interceptor_IV", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),   
  #("civilian_transport",mcn_no_shadow,"civilian_transport", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  #("civilian_cruiser",mcn_no_shadow,"civilian_transport_2", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("civilian_transport",mcn_no_shadow,"Action_IV", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("civilian_cruiser",mcn_no_shadow,"swy_nebulon", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("cis_star_cruiser",mcn_no_shadow,"CIS_Station", cis_star_cruiser_scale,0),
  ##@> //other, not currently purchasable or used
  ##@> //purchasable ships - rebel
  
  ##@> //Purchasable ships
  ("shuttle",mcn_no_shadow,"shuttle_civilian", ship_verysmall_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("mercenary_raider_grey",mcn_no_shadow,"mercenary_raider_grey", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("jawa_ship",mcn_no_shadow,"jawaship", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("mercenary_raider_brown",mcn_no_shadow,"Action_IV_Tusken", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),
  ("mercenary_shuttle_grey",mcn_no_shadow,"shuttle_grey", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("mercenary_shuttle_brown",mcn_no_shadow,"Wild_Karrde", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("mercenary_fighter_grey",mcn_no_shadow,"z95_grey", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("mercenary_fighter_brown",mcn_no_shadow,"z95_brown", ship_small_scale, snd_ship_noise, 0.15, 0.173, 0),  
  #unique icons
  ##@> SWY, deprecated, new DS icon ("death_star",mcn_no_shadow,"death_star",death_star_scale,0),
  
  #ship debris
  ("y_wing_debris",mcn_no_shadow,"y_wing_gold_debris", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),	  
  ("z95_debris",mcn_no_shadow,"z95_debris", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),  
  ("tie_fighter_debris",mcn_no_shadow,"tie_fighter_debris", ship_medium_scale, snd_ship_noise, 0.15, 0.173, 0),  
  
  #castles  
  #SW - new base & outpost icon & planet
  ("sw_planet_green",mcn_no_shadow,"planet_green", spacestation_scale,0),
  #("sw_outpost",mcn_no_shadow,"spacestation1", spacestation_scale,0),
  #("sw_outpost_grey",mcn_no_shadow,"spacestation1_grey", spacestation_scale,0),
  #("sw_base1",mcn_no_shadow,"spacestation5", spacestation_scale,0),
  #("sw_base2",mcn_no_shadow,"spacestation3", spacestation_scale,0),
  #("sw_base3",mcn_no_shadow,"spacestation4", spacestation_scale,0),
  ("asteroid_base",mcn_no_shadow,"asteroid_base", spacestation_scale,0),
  #("shipyard",mcn_no_shadow,"spacestation1", spacestation_scale,0),
  ("shipyard",mcn_no_shadow,"spacestation1", spacestation_scale,0),
  ("battlestation",mcn_no_shadow,"spacestation5", spacestation_scale,0),
  #("outpost_a",mcn_no_shadow,"spacestation3", spacestation_scale,0),
  ("outpost_imp",mcn_no_shadow,"spacestation8", spacestation_scale,0),
  #("outpost_b",mcn_no_shadow,"spacestation4", spacestation_scale,0),
  ("outpost_reb",mcn_no_shadow,"spacestation6", spacestation_scale,0),
  ("outpost_hut",mcn_no_shadow,"spacestation7", spacestation_scale,0), 
  
  #@> SWC 0.9.0.4 - New Vector Space Stations
  #("spacestation5",mcn_no_shadow,"spacestation5", spacestation_scale,0),
  #("spacestation6",mcn_no_shadow,"spacestation6", spacestation_scale,0),
  #("spacestation7",mcn_no_shadow,"spacestation7", spacestation_scale,0), <--- Commented out because replaced them up there ^   :)
  #("spacestation8",mcn_no_shadow,"spacestation8", spacestation_scale,0),
  
  ("XQ_04_Station_1",mcn_no_shadow,"XQ_04_Station_1", spacestation_scale,0),
  ("XQ_04_Station_2",mcn_no_shadow,"XQ_04_Station_2", spacestation_scale,0),
  ("XQ_04_Station_3",mcn_no_shadow,"XQ_04_Station_3", spacestation_scale,0),
  ("XQ_04_Station_4",mcn_no_shadow,"XQ_04_Station_4", spacestation_scale,0),
  ("XQ_04_Station_5",mcn_no_shadow,"XQ_04_Station_5", spacestation_scale,0),

  #SW - have to use native icons when using the map editor
  # ("sw_planet_green",mcn_no_shadow,"map_spacestation_a", 0.35,0),
  # ("sw_outpost",mcn_no_shadow,"map_spacestation_a", 0.35,0),
  # ("sw_outpost_grey",mcn_no_shadow,"map_spacestation_a", 0.35,0),
  # ("sw_base1",mcn_no_shadow,"map_spacestation_a", 0.35,0),
  # ("sw_base2",mcn_no_shadow,"map_spacestation_a", 0.35,0),
  # ("sw_base3",mcn_no_shadow,"map_spacestation_a", 0.35,0),    
  # ("asteroid_base",mcn_no_shadow,"map_spacestation_a", spacestation_scale,0),
  # ("trade_federation_base",mcn_no_shadow,"map_spacestation_a", spacestation_scale,0),
  
#towns
  #SW - new town icon
  ("sw_town_green",mcn_no_shadow,"planet_green",planet_main_scale,0),
  ("sw_town_green_water",mcn_no_shadow,"planet_green_water",planet_main_scale,0),  
  ("sw_town_snow",mcn_no_shadow,"planet_snow",planet_main_scale,0),  
  ("sw_town_snow_water",mcn_no_shadow,"planet_snow",planet_main_scale,0),    
  #("sw_town_gas",mcn_no_shadow,"planet_gas",planet_main_scale,0),      
  ("sw_town_plain",mcn_no_shadow,"planet_plain",planet_main_scale,0),        
  ("sw_town_craters",mcn_no_shadow,"planet_craters",planet_main_scale,0),   
  ("sw_town_green_b",mcn_no_shadow,"planet_green_b",planet_main_scale,0),   
  ("sw_town_green_rock",mcn_no_shadow,"planet_green_rock",planet_main_scale,0),   
  ("sw_town_ice_rock",mcn_no_shadow,"planet_ice_rock",planet_main_scale,0),   
  ("sw_town_red_rock",mcn_no_shadow,"planet_red_rock",planet_main_scale,0),   
  ("sw_town_volcanic",mcn_no_shadow,"planet_volcanic",planet_main_scale,0),   
  ("sw_town_water",mcn_no_shadow,"planet_water",planet_main_scale,0),   
  ("sw_town_industrial",mcn_no_shadow,"planet_industrial", planet_main_scale,0),
  
 #SW - have to use these icons when using the map editor?
  # ("sw_town_green",mcn_no_shadow,"map_town_a",planet_main_scale,0),
  # ("sw_town_green_water",mcn_no_shadow,"map_town_a",planet_main_scale,0),  
  # ("sw_town_snow",mcn_no_shadow,"map_town_a",planet_main_scale,0),  
  # ("sw_town_snow_water",mcn_no_shadow,"map_town_a",planet_main_scale,0),    
  # #("sw_town_gas",mcn_no_shadow,"planet_gas",planet_main_scale,0),      
  # ("sw_town_plain",mcn_no_shadow,"map_town_a",planet_main_scale,0),        
  # ("sw_town_craters",mcn_no_shadow,"map_town_a",planet_main_scale,0),            
  
  #death star
  
#villages  
  ("minorplanet_a",mcn_no_shadow,"planet_craters",planet_minor_scale, 0, []),
  ("minorplanet_burnt_a",mcn_no_shadow,"planet_craters", planet_minor_scale, 0, []),
  ("minorplanet_deserted_a",mcn_no_shadow,"planet_craters",planet_minor_scale, 0, []),
  ("minorplanet_snow_a",mcn_no_shadow,"planet_gas",planet_minor_scale, 0, []),
  ("minorplanet_snow_burnt_a",mcn_no_shadow,"planet_gas",planet_minor_scale, 0, []),
  ("minorplanet_snow_deserted_a",mcn_no_shadow,"planet_gas",planet_minor_scale, 0, []),  
  #new icons for villages
  ("sw_minorplanet_01",mcn_no_shadow,"Planet_Var_01",planet_minor_scale, 0, []),
  ("sw_minorplanet_02",mcn_no_shadow,"Planet_Var_02",planet_minor_scale, 0, []),
  ("sw_minorplanet_03",mcn_no_shadow,"Planet_Var_03",planet_minor_scale, 0, []),
  ("sw_minorplanet_04",mcn_no_shadow,"Planet_Var_04",planet_minor_scale, 0, []),
  ("sw_minorplanet_05",mcn_no_shadow,"Planet_Var_05",planet_minor_scale, 0, []),
  ("sw_minorplanet_06",mcn_no_shadow,"Planet_Var_06",planet_minor_scale, 0, []),
  ("sw_minorplanet_07",mcn_no_shadow,"Planet_Var_07",planet_minor_scale, 0, []),
  ("sw_minorplanet_08",mcn_no_shadow,"Planet_Var_08",planet_minor_scale, 0, []),
  ("sw_minorplanet_09",mcn_no_shadow,"Planet_Var_09",planet_minor_scale, 0, []),
  ("sw_minorplanet_10",mcn_no_shadow,"Planet_Var_10",planet_minor_scale, 0, []),
  ("sw_minorplanet_11",mcn_no_shadow,"Planet_Var_11",planet_minor_scale, 0, []),
  ("sw_minorplanet_12",mcn_no_shadow,"Planet_Var_12",planet_minor_scale, 0, []),
  ("sw_minorplanet_13",mcn_no_shadow,"Planet_Var_13",planet_minor_scale, 0, []),
  ("sw_minorplanet_14",mcn_no_shadow,"Planet_Var_14",planet_minor_scale, 0, []),
  ("sw_minorplanet_15",mcn_no_shadow,"Planet_Var_15",planet_minor_scale, 0, []),
  ("sw_minorplanet_16",mcn_no_shadow,"Planet_Var_16",planet_minor_scale, 0, []),
  ("sw_minorplanet_17",mcn_no_shadow,"Planet_Var_17",planet_minor_scale, 0, []),
  ("sw_minorplanet_18",mcn_no_shadow,"Planet_Var_18",planet_minor_scale, 0, []),
  ("sw_minorplanet_19",mcn_no_shadow,"Planet_Var_19",planet_minor_scale, 0, []),
  ("sw_minorplanet_20",mcn_no_shadow,"Planet_Var_20",planet_minor_scale, 0, []),
  ("sw_minorplanet_21",mcn_no_shadow,"Planet_Var_21",planet_minor_scale, 0, []),

  #SW - have to use these icons when using the map editor
  # ("minorplanet_a",mcn_no_shadow,"map_minorplanet_a",planet_minor_scale, 0),
  # ("minorplanet_burnt_a",mcn_no_shadow,"map_minorplanet_a", planet_minor_scale, 0),
  # ("minorplanet_deserted_a",mcn_no_shadow,"map_minorplanet_a",planet_minor_scale, 0),
  # ("minorplanet_snow_a",mcn_no_shadow,"map_minorplanet_a",planet_minor_scale, 0),
  # ("minorplanet_snow_burnt_a",mcn_no_shadow,"map_minorplanet_a",planet_minor_scale, 0),
  # ("minorplanet_snow_deserted_a",mcn_no_shadow,"map_minorplanet_a",planet_minor_scale, 0),  
  
#training ground
  ("training_ground",mcn_no_shadow,"planet_industrial", planet_training_scale,0, [(ti_on_init_map_icon,[(store_trigger_param_1, ":planet_id"),(party_clear_particle_systems, ":planet_id"),(party_clear_particle_systems, ":planet_id"),(party_add_particle_system, ":planet_id", "psys_planet_icon_atmospheric_effect_polution"),  ]),]),
  ("strategicmap_sun",mcn_no_shadow,"planet_red", 0.0001,0, [(ti_on_init_map_icon,[(store_trigger_param_1, ":planet_id"),(party_clear_particle_systems, ":planet_id"),(party_clear_particle_systems, ":planet_id"),(party_add_particle_system, ":planet_id", "psys_sun_icon_effect"),  ]),]),

  #bridges  
  ("bridge_a",mcn_no_shadow,"planet_red", 0.4,0),
  ("bridge_b",mcn_no_shadow,"planet_red", 0.4,0),
  ("bridge_snow_a",mcn_no_shadow,"planet_red", 0.4,0),
#SW - have to use native icons when using the map editor
# #training ground
  # ("training_ground",mcn_no_shadow,"map_spacestation_a", planet_training_scale,0),
# #bridges  
  # ("bridge_a",mcn_no_shadow,"map_spacestation_a", 0.4,0),
  # ("bridge_b",mcn_no_shadow,"map_spacestation_a", 0.4,0),
  # ("bridge_snow_a",mcn_no_shadow,"map_spacestation_a", 0.4,0),  
  
  ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_mainplanet_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_mainplanet_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_mainplanet_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
        (try_end),
        ]),
     ]),

  # Banners
  #SW - modified banner_# for map_flags
  # ("banner_01",0,"map_flag_01", banner_scale,0),
  #banner_a.dds
  ("banner_01",0,"sw_map_banner_01", banner_scale,0),
  ("banner_02",0,"sw_map_banner_02", banner_scale,0),  
  ("banner_03",0,"sw_map_banner_03", banner_scale,0),    
  ("banner_04",0,"sw_map_banner_04", banner_scale,0),
  ("banner_05",0,"sw_map_banner_05", banner_scale,0),
  ("banner_06",0,"sw_map_banner_06", banner_scale,0),
  ("banner_07",0,"sw_map_banner_07", banner_scale,0),
  ("banner_08",0,"sw_map_banner_08", banner_scale,0),
  ("banner_09",0,"sw_map_banner_09", banner_scale,0),
  ("banner_10",0,"sw_map_banner_10", banner_scale,0),
  ("banner_11",0,"sw_map_banner_11", banner_scale,0),
  ("banner_12",0,"sw_map_banner_12", banner_scale,0),
  ("banner_13",0,"sw_map_banner_13", banner_scale,0),
  ("banner_14",0,"sw_map_banner_14", banner_scale,0),  
  ("banner_15",0,"sw_map_banner_15", banner_scale,0),
  ("banner_16",0,"sw_map_banner_16", banner_scale,0),
  ("banner_17",0,"sw_map_banner_17", banner_scale,0),
  ("banner_18",0,"sw_map_banner_18", banner_scale,0),
  ("banner_19",0,"sw_map_banner_19", banner_scale,0),
  ("banner_20",0,"sw_map_banner_20", banner_scale,0),
  ("banner_21",0,"sw_map_banner_21", banner_scale,0),
  #banner_b.dds
  ("banner_22",0,"sw_map_banner_22", banner_scale,0),
  ("banner_23",0,"sw_map_banner_23", banner_scale,0),
  ("banner_24",0,"sw_map_banner_24", banner_scale,0),
  ("banner_25",0,"sw_map_banner_25", banner_scale,0),
  ("banner_26",0,"sw_map_banner_26", banner_scale,0),
  ("banner_27",0,"sw_map_banner_27", banner_scale,0),
  ("banner_28",0,"sw_map_banner_28", banner_scale,0),
  ("banner_29",0,"sw_map_banner_29", banner_scale,0),
  ("banner_30",0,"sw_map_banner_30", banner_scale,0),
  ("banner_31",0,"sw_map_banner_31", banner_scale,0),
  ("banner_32",0,"sw_map_banner_32", banner_scale,0),
  ("banner_33",0,"sw_map_banner_33", banner_scale,0),
  ("banner_34",0,"sw_map_banner_34", banner_scale,0),
  ("banner_35",0,"sw_map_banner_35", banner_scale,0),
  ("banner_36",0,"sw_map_banner_36", banner_scale,0),
  ("banner_37",0,"sw_map_banner_37", banner_scale,0),
  ("banner_38",0,"sw_map_banner_38", banner_scale,0),
  ("banner_39",0,"sw_map_banner_39", banner_scale,0),
  ("banner_40",0,"sw_map_banner_40", banner_scale,0),
  ("banner_41",0,"sw_map_banner_41", banner_scale,0),
  ("banner_42",0,"sw_map_banner_41", banner_scale,0),
  #native
  # ("banner_43",0,"map_flag_43", banner_scale,0),
  # ("banner_44",0,"map_flag_44", banner_scale,0),
  # ("banner_45",0,"map_flag_45", banner_scale,0),
  # ("banner_46",0,"map_flag_46", banner_scale,0),
  # ("banner_47",0,"map_flag_47", banner_scale,0),
  # ("banner_48",0,"map_flag_48", banner_scale,0),
  # ("banner_49",0,"map_flag_49", banner_scale,0),
  # ("banner_50",0,"map_flag_50", banner_scale,0),
  # ("banner_51",0,"map_flag_51", banner_scale,0),
  # ("banner_52",0,"map_flag_52", banner_scale,0),
  # ("banner_53",0,"map_flag_53", banner_scale,0),
  # ("banner_54",0,"map_flag_54", banner_scale,0),
  # ("banner_55",0,"map_flag_55", banner_scale,0),
  # ("banner_56",0,"map_flag_56", banner_scale,0),
  # ("banner_57",0,"map_flag_57", banner_scale,0),
  # ("banner_58",0,"map_flag_58", banner_scale,0),
  # ("banner_59",0,"map_flag_59", banner_scale,0),
  # ("banner_60",0,"map_flag_60", banner_scale,0),
  # ("banner_61",0,"map_flag_61", banner_scale,0),
  # ("banner_62",0,"map_flag_62", banner_scale,0),
  # ("banner_63",0,"map_flag_63", banner_scale,0),
  # ("banner_64",0,"map_flag_d01", banner_scale,0),
  # ("banner_65",0,"map_flag_d02", banner_scale,0),
  # ("banner_66",0,"map_flag_d03", banner_scale,0),
  # ("banner_67",0,"map_flag_d04", banner_scale,0),
  # ("banner_68",0,"map_flag_d05", banner_scale,0),
  # ("banner_69",0,"map_flag_d06", banner_scale,0),
  # ("banner_70",0,"map_flag_d07", banner_scale,0),
  # ("banner_71",0,"map_flag_d08", banner_scale,0),
  # ("banner_72",0,"map_flag_d09", banner_scale,0),
  # ("banner_73",0,"map_flag_d10", banner_scale,0),
  # ("banner_74",0,"map_flag_d11", banner_scale,0),
  # ("banner_75",0,"map_flag_d12", banner_scale,0),
  # ("banner_76",0,"map_flag_d13", banner_scale,0),
  # ("banner_77",0,"map_flag_d14", banner_scale,0),
  # ("banner_78",0,"map_flag_d15", banner_scale,0),
  # ("banner_79",0,"map_flag_d16", banner_scale,0),
  # ("banner_80",0,"map_flag_d17", banner_scale,0),
  # ("banner_81",0,"map_flag_d18", banner_scale,0),
  # ("banner_82",0,"map_flag_d19", banner_scale,0),
  # ("banner_83",0,"map_flag_d20", banner_scale,0),
  # ("banner_84",0,"map_flag_d21", banner_scale,0),
  # ("banner_85",0,"map_flag_e01", banner_scale,0),
  # ("banner_86",0,"map_flag_e02", banner_scale,0),
  # ("banner_87",0,"map_flag_e03", banner_scale,0),
  # ("banner_88",0,"map_flag_e04", banner_scale,0),
  # ("banner_89",0,"map_flag_e05", banner_scale,0),
  # ("banner_90",0,"map_flag_e06", banner_scale,0),
  # ("banner_91",0,"map_flag_e07", banner_scale,0),
  # ("banner_92",0,"map_flag_e08", banner_scale,0),
  # ("banner_93",0,"map_flag_e09", banner_scale,0),
  # ("banner_94",0,"map_flag_e10", banner_scale,0),
  # ("banner_95",0,"map_flag_e11", banner_scale,0),
  # ("banner_96",0,"map_flag_e12", banner_scale,0),
  # ("banner_97",0,"map_flag_e13", banner_scale,0),
  # ("banner_98",0,"map_flag_e14", banner_scale,0),
  # ("banner_99",0,"map_flag_e15", banner_scale,0),
  # ("banner_100",0,"map_flag_e16", banner_scale,0),
  # ("banner_101",0,"map_flag_e17", banner_scale,0),
  # ("banner_102",0,"map_flag_e18", banner_scale,0),
  # ("banner_103",0,"map_flag_e19", banner_scale,0),
  # ("banner_104",0,"map_flag_e20", banner_scale,0),
  # ("banner_105",0,"map_flag_e21", banner_scale,0),
  # ("banner_106",0,"map_flag_f01", banner_scale,0),
  # ("banner_107",0,"map_flag_f02", banner_scale,0),
  # ("banner_108",0,"map_flag_f03", banner_scale,0),
  # ("banner_109",0,"map_flag_f04", banner_scale,0),
  # ("banner_110",0,"map_flag_f05", banner_scale,0),
  # ("banner_111",0,"map_flag_f06", banner_scale,0),
  # ("banner_112",0,"map_flag_f07", banner_scale,0),
  # ("banner_113",0,"map_flag_f08", banner_scale,0),
  # ("banner_114",0,"map_flag_f09", banner_scale,0),
  # ("banner_115",0,"map_flag_f10", banner_scale,0),
  # ("banner_116",0,"map_flag_f11", banner_scale,0),
  # ("banner_117",0,"map_flag_f12", banner_scale,0),
  # ("banner_118",0,"map_flag_f13", banner_scale,0),
  # ("banner_119",0,"map_flag_f14", banner_scale,0),
  # ("banner_120",0,"map_flag_f15", banner_scale,0),
  # ("banner_121",0,"map_flag_f16", banner_scale,0),
  # ("banner_122",0,"map_flag_f17", banner_scale,0),
  # ("banner_123",0,"map_flag_f18", banner_scale,0),
  # ("banner_124",0,"map_flag_f19", banner_scale,0),
  # ("banner_125",0,"map_flag_f20", banner_scale,0),
  # ("banner_126",0,"map_flag_15", banner_scale,0),
  
  
  
  # New map icons - Swyter
  	##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  MAIN PLANET ICONS
	
    ("sw_swy_Death_Star",mcn_no_shadow,"swy_Death_Star",spacestation_scale,0),
	 
	("sw_swy_Planet_Coruscant",mcn_no_shadow,"swy_Planet_Coruscant",planet_main_scale,0,
		   []),
	 
	("sw_swy_Planet_Endor",mcn_no_shadow,"swy_Planet_Endor",planet_main_scale,0,
		   []),

	("sw_swy_christophsis",mcn_no_shadow,"swy_christophsis",planet_main_scale,0,
		   []),	
	
	("sw_swy_Planet_forest",mcn_no_shadow,"swy_Planet_forest",planet_main_scale,0,
		   []),
	
	("sw_swy_Planet_Taris",mcn_no_shadow,"swy_Planet_Taris",planet_main_scale,0,
		   []),
	
	("sw_swy_Planet_Tatooine",mcn_no_shadow,"swy_Planet_Tatooine",planet_main_scale,0,
		   []),
	
	("sw_swy_Planet_geonosis",mcn_no_shadow,"swy_Planet_geonosis",planet_main_scale,0,
		   []),
	
	("sw_swy_Planet_Kessel",mcn_no_shadow,"swy_Planet_Kessel",planet_main_scale,0,
		   []),
	
	("sw_swy_Planet_frozen",mcn_no_shadow,"swy_Planet_frozen",planet_main_scale,0,
		   []),
	
	("sw_swy_Planet_lava",mcn_no_shadow,"swy_Planet_lava",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_gas",mcn_no_shadow,"swy_rePlanet_gas",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_earth",mcn_no_shadow,"swy_rePlanet_earth",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_snow",mcn_no_shadow,"swy_rePlanet_snow",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_ice",mcn_no_shadow,"swy_rePlanet_ice",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_craters",mcn_no_shadow,"swy_rePlanet_craters",planet_minor_scale,0,
		   []),
	
	("sw_swy_rePlanet_water",mcn_no_shadow,"swy_rePlanet_water",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_kashyyyk",mcn_no_shadow,"swy_rePlanet_kashyyyk",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_wilderness",mcn_no_shadow,"swy_rePlanet_wilderness",planet_main_scale,0,
		   []),
	
	("sw_swy_rePlanet_rock",mcn_no_shadow,"swy_rePlanet_rock",planet_main_scale,0,	
		   []),
	
	# ("sw_galaxy",mcn_no_shadow,"swy_rePlanet_rock",planet_main_scale,0,
	# 	   []),
	
	("sw_swy_Planet_Sarapin",mcn_no_shadow,"swy_Planet_Sarapin",planet_main_scale,0,	
		   []),
	
	("sw_swy_Planet_RaxusPrime",mcn_no_shadow,"swy_Planet_RaxusPrime",planet_main_scale,0,	
		   []),
	
	##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  MOON PLANET ICONS
	("sw_swy_NarShadda",mcn_no_shadow,"swy_Planet_Coruscant",planet_minor_scale,0,
		   []),
	
]
