# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

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

	# NEW MUSIC TRACKS
	#main title
	("mount_and_blade_title_screen", "SWC_Intro.ogg", mtf_sit_main_title|mtf_start_immediately|mtf_module_track, 0),

	#SW - some music track names are called by play_track and play_cue_track so these must be the same names as native
	("captured", "SWC-Capture.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	#("empty_village", "encounter_looted_planet.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("escape", "SWC-Escape.ogg", mtf_persist_until_finished|mtf_module_track, 0),  #track_escape  	
	
	#ARENA
	("arena_1", "SWC-Arena-1.ogg", mtf_sit_arena|mtf_module_track, mtf_sit_arena),
	("arena_2", "SWC-Arena-2.ogg", mtf_sit_arena|mtf_module_track, mtf_sit_arena),	

	#FIGHT/BATTLE
	("battle_2", "SWC-Battle-2.ogg", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	("battle_3", "SWC-Battle-3.ogg", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	#("battle_empire", "SWC-Battle-Empire.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_culture_all),
	("battle_empire", "SWC-Battle-Empire.ogg", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	
	#TAVERN/CANTINA
	("cantina_1", "SWC-Cantina.ogg", mtf_sit_tavern|mtf_module_track, mtf_sit_tavern),
	("cantina_fight", "SWC-Bar_Fight.ogg", mtf_persist_until_finished|mtf_module_track, 0),		#only used in cantina bar fights

	#DEFEAT/KILLED
	("killed", "SWC-Defeat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),
	
	#MAP
	("map_dspace", "SWC-Deep_Space.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_1", "SWC-map-1.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_2", "SWC-map-2.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_3", "SWC-map-3.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_4", "SWC-map-4.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_5", "SWC-map-5.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_6", "SWC-map-6.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_7", "SWC-map-7.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),

	#VICTORY
	("victory", "SWC-Victory.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
	
	#TOWN/PLANET TRACKS
	("town_bizaar", "SWC-BizaarPlanetTexture.ogg", mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),	
	("town_gentle", "SWC-Gentle-Planet.ogg",       mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),
	("town_beautiful", "SWC-Beautiful_Planet.ogg", mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),		
	#TOWN SPECIFIC (doesn't seem to work correctly with the play_track commands so I had to add mtf_persist_until_finished)
	("town_desert", "SWC-Dessert-Planet.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("town_wookiee", "SWC-WookiePlanetTexture.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("town_endor", "SWC-Endor.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("town_bothawui",   "SWC-Bothawui.ogg",    mtf_persist_until_finished|mtf_module_track, 0),	
	("town_felucia",    "SWC-Felucia.ogg",     mtf_persist_until_finished|mtf_module_track, 0),	
	("town_nalhutta",   "SWC-Nul_Hutta.ogg",   mtf_persist_until_finished|mtf_module_track, 0),	
	("town_raxusprime", "SWC-Raxus_Prime.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	#TOWN BATTLES? maybe also use for fights or town_infiltrate ?
	("town_battle", "SWC-Planet_Battle.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	#TOWN TESTING
	#("town_test", "test_music.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	
	#NEW Throne Room Tracks (may also be used for castle entry)
	("throne_empire_1", "SWC-Empire_Throne_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_empire_2", "SWC-Empire_Throne_2.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_empire_3", "SWC-Empire_Throne_3.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_hutt_1", "SWC-Hutt_Throne_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_hutt_2", "SWC-Hutt_Throne_2.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_hutt_3", "SWC-Hutt_Throne_3.ogg", mtf_persist_until_finished|mtf_module_track, 0),	
	("throne_rebel_1", "SWC-Rebel_Throne_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_2", "SWC-Rebel_Throne_2.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_3", "SWC-Rebel_Throne_3.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_4", "SWC-Rebel_Throne_4.ogg", mtf_persist_until_finished|mtf_module_track, 0),

########################################################################################################################  

]
