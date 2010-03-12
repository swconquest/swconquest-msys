from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [

#########################################################################################################
#SW - modified music

	#main title
	("mount_and_blade_title_screen", "SWC-Title.mp3", mtf_sit_main_title|mtf_start_immediately|mtf_module_track, 0),

	#SW - some music track names are called by play_track and play_cue_track so these must be the same names as native
	#("captured", "captured.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("captured", "SWC-Capture.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	#("empty_village", "encounter_looted_planet.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	#("escape", "escape.mp3", mtf_persist_until_finished|mtf_module_track, 0),  #track_escape  
	("escape", "SWC-Escape.mp3", mtf_persist_until_finished|mtf_module_track, 0),  #track_escape  
  
	#ambushed/siege
	# ("ambushed_1", "ambushed_1.mp3", mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight),
	# ("ambushed_2", "ambushed_2.mp3", mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight),
	# #("ambushed_by_empire", "ambushed_by_empire.mp3",  mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_culture_all),
	# #("ambushed_by_rebel",  "ambushed_by_rebel.mp3",  mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_culture_all),
	# #("ambushed_by_hutt", "ambushed_by_hutt.mp3",    mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_culture_all),
	
	# #siege
	# ("seige_1", "seige_1.mp3", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed),
	# ("seige_2", "seige_2.mp3", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed),

	# #travel
	# ("travel_1", "SWC-map-1.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
	# ("travel_2", "SWC-map-2.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
	# ("travel_3", "SWC-map-3.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
	# ("travel_4", "SWC-map-4.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
	# ("travel_5", "SWC-map-5.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
	# ("travel_6", "SWC-map-6.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
	# #("travel_empire", "travel_empire.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
	# #("travel_rebel",  "travel_rebel.mp3",  mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),    
	# #("travel_hutt", "travel_hutt.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
	# # ("armorer", "armorer.ogg", mtf_sit_travel|mtf_module_track, 0),  

	# #town
	# ("town_1", "SWC-Gentle-Planet.mp3", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
	# #("town_2", "SWC-WookiePlanetTexture.mp3", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
	# ("town_3", "SWC-BizaarPlanetTexture.mp3", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
	# #("town_4", "SWC-Dessert-Planet.mp3", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
	# #("town_5", "SWC-Endor.mp3", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),
	# #
	# #("town_empire", "town_empire.mp3", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
	# #("town_rebel", "town_rebel.mp3", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
	# #("town_hutt", "town_hutt.mp3", mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
	# #
	# #("town_desert", "SWC-Dessert-Planet.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	# #("town_wookiee", "SWC-WookiePlanetTexture.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	# #("town_endor", "SWC-Endor.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	 #("town_desert", "SWC-Dessert-Planet.mp3", mtf_module_track, 0),
	 #("town_wookiee", "SWC-WookiePlanetTexture.mp3", mtf_module_track, 0),
	 #("town_endor", "SWC-Endor.mp3", mtf_module_track, 0),	
	 #("town_test", "test_music.mp3", mtf_module_track, 0),
	
	# #night
	# ("night_1", "night_1.mp3", mtf_sit_night|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
	# ("night_2", "night_2.mp3", mtf_sit_night|mtf_module_track, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  
	# #arena
	# #("arena_1", "arena_1.mp3", mtf_sit_arena|mtf_module_track, 0),
	# ("arena_1", "SWC-Arena-1.mp3", mtf_sit_arena|mtf_module_track, 0),
	# ("arena_2", "SWC-Arena-2.mp3", mtf_sit_arena|mtf_module_track, 0),	
	
	# #tavern
	# ("tavern_1", "tavern_1.mp3", mtf_sit_tavern|mtf_module_track, 0),
	# ("tavern_2", "tavern_2.mp3", mtf_sit_tavern|mtf_module_track, 0),
	# ("tavern_3", "tavern_3.mp3", mtf_sit_tavern|mtf_module_track, 0),

	# #defeat/killed
	# #("killed_1", "killed_1.mp3",mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
	# ("killed_1", "SWC-Defeat.mp3",mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
	# #("killed_by_empire", "killed_by_empire.mp3", mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed|mtf_module_track, 0),
	# #("killed_by_rebel", "killed_by_rebel.mp3", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed|mtf_module_track, 0),
	# #("killed_by_hutt", "killed_by_hutt.mp3", mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed|mtf_module_track, 0),

	# #fight/ambushed
	# ("fight_1", "fight_1.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
	# ("fight_2", "fight_2.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
	# ("fight_3", "fight_3.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
	# ("fight_4", "fight_4.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
	# ("fight_5", "fight_5.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_module_track, 0),
	# ("fight_empire", "SWC-Battle-Empire.mp3", mtf_culture_1|mtf_sit_fight|mtf_module_track, mtf_culture_all),
	# #("fight_rebel", "fight_as_rebel.mp3", mtf_culture_2|mtf_sit_fight|mtf_module_track, mtf_culture_all),
	# #("fight_hutt", "fight_as_hutt.mp3", mtf_culture_3|mtf_sit_fight|mtf_module_track, mtf_culture_all),
	
	# #infiltrate
	# ("infiltrate_1", "infiltrate_1.mp3", mtf_sit_town_infiltrate|mtf_module_track, 0),
	# ("infiltrate_2", "infiltrate_2.mp3", mtf_sit_town_infiltrate|mtf_module_track, 0),
	# #("infiltrate_empire", "infiltrate_empire.mp3", mtf_culture_1|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_all),
	# #("infiltrate_rebel", "infiltrate_rebel.mp3", mtf_culture_2|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_all),
	# #("infiltrate_hutt", "infiltrate_hutt.mp3", mtf_culture_3|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_all),
	
	# #hostile
	# ("encounter_hostile_1", "encounter_hostile_1.mp3", mtf_persist_until_finished|mtf_sit_encounter_hostile|mtf_module_track, 0),
	# ("encounter_hostile_2", "encounter_hostile_2.mp3", mtf_persist_until_finished|mtf_sit_encounter_hostile|mtf_module_track, 0),

	# #victorious
	# #("victorious_1", "victorious_1.mp3", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
	# ("victorious_1", "SWC-Victory.mp3", mtf_persist_until_finished|mtf_sit_victorious|mtf_module_track, 0),
	# #("victorious_empire", "victorious_empire.mp3", mtf_persist_until_finished|mtf_culture_1|mtf_sit_victorious|mtf_module_track, 0),
	# #("victorious_rebel", "victorious_rebel.mp3", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious|mtf_module_track, 0),
	# #("victorious_hutt", "victorious_hutt.mp3", mtf_persist_until_finished|mtf_culture_3|mtf_sit_victorious|mtf_module_track, 0),
	

	# NEW MUSIC TRACKS
	#main title
	#("mount_and_blade_title_screen", "SWC-Title.mp3", mtf_sit_main_title|mtf_start_immediately|mtf_module_track, 0),
	("mount_and_blade_title_screen", "SWC-Battle-Empire.mp3", mtf_sit_main_title|mtf_start_immediately|mtf_module_track, 0),

	#SW - some music track names are called by play_track and play_cue_track so these must be the same names as native
	("captured", "SWC-Capture.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	#("empty_village", "encounter_looted_planet.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("escape", "SWC-Escape.mp3", mtf_persist_until_finished|mtf_module_track, 0),  #track_escape  	
	
	#ARENA
	("arena_1", "SWC-Arena-1.mp3", mtf_sit_arena|mtf_module_track, mtf_sit_arena),
	("arena_2", "SWC-Arena-2.mp3", mtf_sit_arena|mtf_module_track, mtf_sit_arena),	

	#FIGHT/BATTLE
	("battle_2", "SWC-Battle-2.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	("battle_3", "SWC-Battle-3.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	#("battle_empire", "SWC-Battle-Empire.mp3", mtf_culture_1|mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_culture_all),
	("battle_empire", "SWC-Battle-Empire.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	
	#TAVERN/CANTINA
	("cantina_1", "SWC-Cantina.mp3", mtf_sit_tavern|mtf_module_track, mtf_sit_tavern),
	("cantina_fight", "SWC_Bar_Fight.mp3", mtf_persist_until_finished|mtf_module_track, 0),		#only used in cantina bar fights

	#DEFEAT/KILLED
	("killed", "SWC-Defeat.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
	
	#MAP
	("map_1", "SWC-map-1.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_2", "SWC-map-2.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_3", "SWC-map-3.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_4", "SWC-map-4.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_5", "SWC-map-5.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_6", "SWC-map-6.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_7", "SWC-map-7.mp3", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),

	#VICTORY
	("victory", "SWC-Victory.mp3", mtf_persist_until_finished|mtf_sit_victorious, 0),
	
	#TOWN/PLANET TRACKS
	("town_bizaar", "SWC-BizaarPlanetTexture.mp3", mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),	
	("town_gentle", "SWC-Gentle-Planet.mp3", mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),
	("town_beautiful", "SWC_Beautiful_Planet.mp3", mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),		
	#TOWN SPECIFIC (doesn't seem to work correctly with the play_track commands so I had to add mtf_persist_until_finished)
	("town_desert", "SWC-Dessert-Planet.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("town_wookiee", "SWC-WookiePlanetTexture.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("town_endor", "SWC-Endor.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	#TOWN BATTLES? maybe also use for fights or town_infiltrate ?
	("town_battle", "SWC_Planet_Battle.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	#TOWN TESTING
	("town_test", "test_music.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	
	#NEW Throne Room Tracks (may also be used for castle entry)
	("throne_empire_1", "SWC_Empire_Throne_1.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_empire_2", "SWC_Empire_Throne_2.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_empire_3", "SWC_Empire_Throne_3.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_hutt_1", "SWC_Hutt_Throne_1.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_hutt_2", "SWC_Hutt_Throne_2.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_hutt_3", "SWC_Hutt_Throne_3.mp3", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_rebel_1", "SWC_Rebel_Throne_1.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_2", "SWC_Rebel_Throne_2.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_3", "SWC_Rebel_Throne_3.mp3", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_4", "SWC_Rebel_Throne_4.mp3", mtf_persist_until_finished|mtf_module_track, 0),

########################################################################################################################  

]
