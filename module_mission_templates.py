# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from module_constants import *
#SW - needed to add unused_horse_animation
from module_animations import *
#SW - needed to add for toggle_weapon_capabilities code
from header_items import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
#
####################################################################################################################

####>>>>>>>
#Motomataru's new AI
common_ranged_avoid_melee =	(.3, 0, 0, [], [(call_script, "script_ranged_avoid_melee")])

#AI triggers v3 by motomataru
AI_triggers = [

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,
]
####>>>>>>>

#SW - modified pilgrim disguise
pilgrim_disguise = [itm_transparent_helmet,itm_vest_closed_a,itm_black_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_westar,itm_energy_shield_yellow_small]
#SW - modified af_spacestation_lord
#af_spacestation_lord = af_override_horse | af_override_weapons| af_require_civilian
af_spacestation_lord = af_override_horse | af_override_weapons

#SW MF stuff for stay in battle after knockdown and death-cam- BIG Thanks to silverkatana & DMOD Valkyrie for base code - http://forums.taleworlds.com/index.php/topic,60329.msg1559908.html

sw_victory_defeat_conditions = (
	5, 2, 3,
	[(all_enemies_defeated),],
	[

		(assign, "$battle_won",1),
		(assign, "$g_battle_result", 1),
		(display_message,"str_msg_battle_won"),
		(set_mission_result, 1),
	])

sw_deathcam_follow_troop = (0, 0, 0,[
	(eq, "$dmod_move_camera", 2),
		(agent_get_position, 1, "$dmod_current_agent"),
		(get_player_agent_no, ":player_agent"),
		(agent_set_position, ":player_agent", 1)

     ],[])
sw_deathcam_valkyrie_move_camera = (0, 1, 2.1,[
	(eq, "$dmod_move_camera", 1),
        (agent_get_position, 2, "$dmod_current_agent"),
        (position_move_z, 2, 300),
        (mission_cam_set_mode,1),
        (mission_cam_set_position, 2),
        (position_move_z, 2, 600),
        (mission_cam_animate_to_position, 2, 1000),
     ],[
        (mission_cam_set_mode, 0, 1000, 1),
        (assign, "$dmod_move_camera", 2),
     ])
sw_deathcam_cycle_fowards =	 (0, 0, 0,[
		#(key_clicked, key_m),
		(key_clicked, "$deathcam_forward_key"),
		(main_hero_fallen),
        (call_script, "script_dmod_cycle_forwards"),
        ], [])

sw_deathcam_cycle_backwards = (0, 0, 0,[
		#(key_clicked, key_n),
		(key_clicked, "$deathcam_backward_key"),
		(main_hero_fallen),
        (call_script, "script_dmod_cycle_backwards"),
        ], [])




############################################################################################################
##### Custom Commander(CC)
############################################################################################################
common_check_player_can_join_battle = (
  0, 0, ti_once,
  [
    (neq,"$g_player_troop","trp_player"),
    (store_troop_health, "$g_player_begin_hp", "trp_player"),
    (neg|troop_is_wounded, "trp_player"),
    (get_player_agent_no, ":player_agent"),
    (ge, ":player_agent", 0),
    (agent_get_team, ":player_team", ":player_agent"),
    (agent_get_position, pos49, ":player_agent"),
    (position_move_x, pos49, -100),
    (set_spawn_position, pos49),
    (spawn_agent,"trp_player"),
    (agent_set_team, reg0, ":player_team"),
  ], [])

##  dismounted: for siege and inner battle to override the player's horse
##  when a NPC was selected as the commander
common_check_player_can_join_battle_dismounted = (
  0, 0, ti_once,
  [
    (neq,"$g_player_troop","trp_player"),
    (store_troop_health, "$g_player_begin_hp", "trp_player"),
    (neg|troop_is_wounded, "trp_player"),
    (get_player_agent_no, ":player_agent"),
    (ge, ":player_agent", 0),
    (agent_get_team, ":player_team", ":player_agent"),
    (agent_get_position, pos49, ":player_agent"),
    (position_move_x, pos49, -100),
    (set_spawn_position, pos49),
    (troop_get_inventory_slot, ":player_horse_item", "trp_player", 8),  ## ek_horse = 8
    (troop_get_inventory_slot_modifier, ":player_horse_item_modifier", "trp_player", 8),
    (troop_set_inventory_slot, "trp_player", 8, -1),
    (spawn_agent,"trp_player"),
    (agent_set_team, reg0, ":player_team"),
    (troop_set_inventory_slot, "trp_player", 8, ":player_horse_item"),
    (troop_set_inventory_slot_modifier, "trp_player", 8, ":player_horse_item_modifier"),
  ], [])

##  display messages about the changes of npc's proficiency
##  when he/she was selected as the commander
common_npc_proficiency_limit =(
  0, 0, ti_once, [(neq, "$g_player_troop", "trp_player")],
  [
    (store_proficiency_level, "$g_cur_one_handed_weapon_limt", "$g_player_troop", wpt_one_handed_weapon),
    (store_proficiency_level, "$g_cur_two_handed_weapon_limt", "$g_player_troop", wpt_two_handed_weapon),
    (store_proficiency_level, "$g_cur_polearm_limt", "$g_player_troop", wpt_polearm),
    (store_proficiency_level, "$g_cur_archery_limt", "$g_player_troop", wpt_archery),
    (store_proficiency_level, "$g_cur_crossbow_limt", "$g_player_troop", wpt_crossbow),
    (store_proficiency_level, "$g_cur_throwing_limt", "$g_player_troop", wpt_throwing),
	#SW - added firearm
	(store_proficiency_level, "$g_cur_firearm_limt", "$g_player_troop", wpt_firearm),
  ])

common_npc_raise_proficiency =(
  1, 0, 0, [(neq, "$g_player_troop", "trp_player")],
  [
    (store_proficiency_level, ":cur_one_handed_weapon", "$g_player_troop", wpt_one_handed_weapon),
    (store_proficiency_level, ":cur_two_handed_weapon", "$g_player_troop", wpt_two_handed_weapon),
    (store_proficiency_level, ":cur_polearm", "$g_player_troop", wpt_polearm),
    (store_proficiency_level, ":cur_archery", "$g_player_troop", wpt_archery),
    (store_proficiency_level, ":cur_crossbow", "$g_player_troop", wpt_crossbow),
    (store_proficiency_level, ":cur_throwing", "$g_player_troop", wpt_throwing),
	#SW - added firearm
	(store_proficiency_level, ":cur_firearm", "$g_player_troop", wpt_firearm),
    (str_store_troop_name, s1, "$g_player_troop"),
    (try_begin),
      (gt, ":cur_one_handed_weapon", "$g_cur_one_handed_weapon_limt"),
      (store_sub, ":amout", ":cur_one_handed_weapon", "$g_cur_one_handed_weapon_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_one_handed_weapon"),
      (display_message, "@{reg3?{s1}'s proficiency in one handed weapon has improved by {reg2} to {reg1}.:{s1}'s one handed weapon proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_one_handed_weapon_limt", ":cur_one_handed_weapon"),
    (else_try),
      (gt, ":cur_two_handed_weapon", "$g_cur_two_handed_weapon_limt"),
      (store_sub, ":amout", ":cur_two_handed_weapon", "$g_cur_two_handed_weapon_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_two_handed_weapon"),
      (display_message, "@{reg3?{s1}'s proficiency in two handed weapon has improved by {reg2} to {reg1}.:{s1}'s two handed weapon proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_two_handed_weapon_limt", ":cur_two_handed_weapon"),
    (else_try),
      (gt, ":cur_polearm", "$g_cur_polearm_limt"),
      (store_sub, ":amout", ":cur_polearm", "$g_cur_polearm_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_polearm"),
      (display_message, "@{reg3?{s1}'s proficiency in polearm has improved by {reg2} to {reg1}.:{s1}'s polearm proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_polearm_limt", ":cur_polearm"),
    (else_try),
      (gt, ":cur_archery", "$g_cur_archery_limt"),
      (store_sub, ":amout", ":cur_archery", "$g_cur_archery_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_archery"),
      (display_message, "@{reg3?{s1}'s proficiency in archery has improved by {reg2} to {reg1}.:{s1}'s archery proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_archery_limt", ":cur_archery"),
    (else_try),
      (gt, ":cur_crossbow", "$g_cur_crossbow_limt"),
      (store_sub, ":amout", ":cur_crossbow", "$g_cur_crossbow_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_crossbow"),
      (display_message, "@{reg3?{s1}'s proficiency in crossbow has improved by {reg2} to {reg1}.:{s1}'s crossbow proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_crossbow_limt", ":cur_crossbow"),
    (else_try),
      (gt, ":cur_throwing", "$g_cur_throwing_limt"),
      (store_sub, ":amout", ":cur_throwing", "$g_cur_throwing_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_throwing"),
      (display_message, "@{reg3?{s1}'s proficiency in throwing has improved by {reg2} to {reg1}.:{s1}'s throwing proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_throwing_limt", ":cur_throwing"),
	#SW - added firearm else_try
    (else_try),
      (gt, ":cur_firearm", "$g_cur_firearm_limt"),
      (store_sub, ":amout", ":cur_firearm", "$g_cur_firearm_limt"),
      (assign, reg2, ":amout"),
      (val_sub, ":amout", 1),
      (assign, reg3, ":amout"),
      (assign, reg1, ":cur_firearm"),
      (display_message, "@{reg3?{s1}'s proficiency in firearms has improved by {reg2} to {reg1}.:{s1}'s firearm proficiency have reach to {reg1}.}", 0xEEEE00),
      (assign, "$g_cur_firearm_limt", ":cur_firearm"),
    (try_end),
  ])
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
##### more scripts by rubik
# common_custom_commander_camera = (
  # 0, 0, 0, [],
  # [
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_look_position, pos1, ":player_agent"),
    # (position_move_z, pos1, "$g_camera_z"),
    # (position_move_y, pos1, "$g_camera_y"),
    # (agent_get_horse, ":horse_agent", ":player_agent"),
    # (try_begin),
      # (ge, ":horse_agent", 0),
      # (position_move_z, pos1, 80),
    # (try_end),
    # (mission_cam_set_position, pos1),
    # (try_begin),
      # (key_is_down, key_left_control),
      # (assign, ":move_val", 50),
    # (else_try),
      # (assign, ":move_val", 10),
    # (try_end),
    # (try_begin),
      # (key_clicked, key_up),
      # (mission_cam_set_mode, 1, 50),
      # (val_add, "$g_camera_z", ":move_val"),
    # (else_try),
      # (key_clicked, key_down),
      # (mission_cam_set_mode, 1, 50),
      # (val_sub, "$g_camera_z", ":move_val"),
    # (else_try),
      # (key_clicked, key_left),
      # (mission_cam_set_mode, 1, 50),
      # (val_add, "$g_camera_y", ":move_val"),
    # (else_try),
      # (key_clicked, key_right),
      # (mission_cam_set_mode, 1, 50),
      # (val_sub, "$g_camera_y", ":move_val"),
    # (try_end),
    # (try_begin),
      # (this_or_next|game_key_clicked, gk_view_char),
      # (game_key_clicked, gk_cam_toggle),
      # (mission_cam_set_mode, 0),
    # (try_end),
  # ])
############################################################################################################

#Highlander begin--------------------------------------
common_physics_init = (
ti_before_mission_start,0,0,[],
[(assign,"$timer",0),
#(assign,"$timer_in_seconds",0),
(assign,"$timer_speed",5),
(try_for_range,":projectile",0,256),
  (troop_set_slot,"trp_pjct_active",":projectile",0),
(try_end),

(try_for_range,":scene_prop",0,"spr_scene_props_end"),
 (scene_prop_get_num_instances,":num_instances",":scene_prop"),
 (try_for_range,":instance_no",0,":num_instances"),
  (scene_prop_get_instance,":instance",":scene_prop",":instance_no"),
  (troop_set_slot,"trp_instance_attached_to",":instance",0),
 (try_end),
(try_end),
])
common_timer = (0.05,0,0,
[(val_add,"$timer","$timer_speed"),
#(store_mission_timer_a,":time_in_sec"),
#(try_begin),
#  (neq,":time_in_sec","$timer_in_seconds"),
#  (val_mul,"$timer_speed",100),
#  (store_mul,":timer_delta_sub","$timer_in_seconds",100),
#  (store_sub,":timer_delta","$timer",":timer_delta_sub"),
#  (val_div,"$timer_speed",":timer_delta"),
#  (store_mul,"$timer",":time_in_sec",100),
#  (assign,"$timer_in_seconds",":time_in_sec"),
#(try_end),
],[])
common_physics = (
0.05,1.75,0,
[
(set_fixed_point_multiplier,100),
(assign,":one_explosion_or_more",0),
(try_for_range,":projectile",0,256),
  (troop_slot_eq,"trp_pjct_active",":projectile",1),

  #movement
  (troop_get_slot,":emit_time","trp_pjct_emit_time",":projectile"),
  (troop_get_slot,":x_pos","trp_pjct_x",":projectile"),
  (troop_get_slot,":y_pos","trp_pjct_y",":projectile"),
  (troop_get_slot,":z_pos","trp_pjct_z",":projectile"),
  (troop_get_slot,":x_velocity","trp_pjct_x_velocity",":projectile"),
  (troop_get_slot,":y_velocity","trp_pjct_y_velocity",":projectile"),
  (troop_get_slot,":z_velocity","trp_pjct_z_velocity",":projectile"),
  (store_sub,":dt","$timer",":emit_time"),
  (val_mul,":x_velocity",":dt"),
  (val_mul,":y_velocity",":dt"),
  (val_mul,":z_velocity",":dt"),
  (assign,":gravity",981),
  (val_mul,":gravity",":dt"),
  (val_mul,":gravity",":dt"),
  (val_div,":gravity",10000),
  (val_add,":x_pos",":x_velocity"),
  (val_add,":y_pos",":y_velocity"),
  (val_sub,":z_velocity",":gravity"),
  (val_add,":z_pos",":z_velocity"),
  (init_position,pos1),
  (position_set_x,pos1,":x_pos"),
  (position_set_y,pos1,":y_pos"),
  (position_set_z,pos1,":z_pos"),

  #particle_system
  (troop_get_slot,":particle_system","trp_pjct_particle_system",":projectile"),
  (try_begin),
    (ge,":particle_system",0),
#    (copy_position,pos3,pos1),
#    (party_get_slot,":x_velocity",":projectile",pjct_x_velocity),
#    (party_get_slot,":y_velocity",":projectile",pjct_y_velocity),
#    (party_get_slot,":z_velocity",":projectile",pjct_z_velocity),
#    (store_mul,":gravity",981,":dt"),
#    (val_div,":gravity",5000),
#    (val_sub,":z_velocity",":gravity"),
#    (party_get_slot,":particle_system_magnitude",":projectile",pjct_particle_system_magnitude),
#    (val_div,":x_velocity",":particle_system_magnitude"),
#    (val_div,":y_velocity",":particle_system_magnitude"),
#    (val_div,":z_velocity",":particle_system_magnitude"),
#    (val_mul,":particle_system_magnitude",10),
#    (try_for_range,":unused",0,":particle_system_magnitude"),
	(particle_system_burst,":particle_system",pos1,10),
#	(position_move_x,pos3,":x_velocity"),
#	(position_move_y,pos3,":y_velocity"),
#	(position_move_z,pos3,":z_velocity"),
#    (try_end),
  (try_end),

  (copy_position,pos2,pos1),
  (copy_position,pos3,pos1),
  (troop_get_slot,":x_velocity","trp_pjct_x_velocity",":projectile"),
  (troop_get_slot,":y_velocity","trp_pjct_y_velocity",":projectile"),
  (troop_get_slot,":z_velocity","trp_pjct_z_velocity",":projectile"),

  (store_mul,":velocity",":x_velocity",":x_velocity"),
  (store_mul,":velocity_b",":y_velocity",":y_velocity"),
  (val_add,":velocity",":velocity_b"),
  (store_mul,":velocity_b",":z_velocity",":z_velocity"),
  (val_add,":velocity",":velocity_b"),
  (store_sqrt,":all_in_all_velocity",":velocity"),

  (store_mul,":gravity",981,":dt"),
  (val_div,":gravity",10000),
  (val_sub,":z_velocity",":gravity"),
  (position_move_x,pos3,":x_velocity"),
  (position_move_y,pos3,":y_velocity"),
  (position_move_z,pos3,":z_velocity"),
  (call_script,"script_position_face_position",pos2,pos3),
  (position_copy_rotation,pos3,pos2),

  (troop_get_slot,":instance","trp_pjct_attach_scene_prop",":projectile"),
  (try_begin),
    (ge,":instance",0),
    (prop_instance_animate_to_position,":instance",pos3,10),
  (try_end),

  #hit an agent?
  (troop_get_slot,":damage","trp_pjct_damage",":projectile"),
  (try_begin),
    (gt,":damage",0),
    (troop_get_slot,":agent_deliverer","trp_pjct_source_agent",":projectile"),
    (try_for_agents,":agent"),
      (agent_is_alive,":agent"),
      (agent_get_position,pos3,":agent"),
      (position_move_z,pos3,100),
      (position_transform_position_to_local,pos4,pos2,pos3),
      (position_get_y,":pos_y",pos4),
      (is_between,":pos_y",0,":all_in_all_velocity"),
      (position_get_x,":pos_x",pos4),
      (is_between,":pos_x",-100,100),
      (position_get_z,":pos_z",pos4),
      (is_between,":pos_z",-100,100),
      (call_script,"script_agent_deliver_damage_to_agent",":agent_deliverer",":agent",":damage"),
      (assign,":explosition",1),
    (try_end),
  (try_end),

  (position_get_z,":pos_z",pos1),

  (copy_position,pos2,pos1),
  (position_set_z,pos2,10000),
  (position_set_z_to_ground_level,pos2),
  (position_get_z,":ground",pos2),
  (val_sub,":pos_z",":ground"),
  (assign,":explosition",0),

  (try_begin),
    (troop_slot_eq,"trp_pjct_check_collision",":projectile",0),
    (position_get_z,":pos_z",pos1),
    (try_begin),
      (le, ":pos_z","$ground_level"),
      (assign,":ground","$ground_level"),
      (assign,":pos_z",9),
    (else_try),
      (assign,":pos_z",10),
    (try_end),
  (try_end),

  (try_begin),
  #check explosition countdown
    (troop_get_slot,":explosion_countdown","trp_pjct_explosion_countdown",":projectile"),
    (gt,"$timer",":explosion_countdown"),
    (assign,":explosition",1),
  (else_try),
  #ground hit
    (lt,":pos_z",10),
    (troop_get_slot,":explode_on_ground_hit","trp_pjct_explode_on_ground_hit",":projectile"),
    (try_begin),
      (eq,":explode_on_ground_hit",1),
      (assign,":explosition",1),
    (else_try),
      (troop_get_slot,":bounce_effect","trp_pjct_bounce_effect",":projectile"),
      (troop_get_slot,":x_velocity","trp_pjct_x_velocity",":projectile"),
      (troop_get_slot,":y_velocity","trp_pjct_y_velocity",":projectile"),
      (troop_get_slot,":z_velocity","trp_pjct_z_velocity",":projectile"),
      (store_mul,":gravity_velocity",981,":dt"),
      (val_div,":gravity_velocity",10000),
      (val_sub,":z_velocity",":gravity_velocity"),
      (val_mul,":x_velocity",":bounce_effect"),
      (val_mul,":y_velocity",":bounce_effect"),
      (val_mul,":z_velocity",":bounce_effect"),
      (val_div,":z_velocity",-10),
      (val_div,":x_velocity",10),
      (val_div,":y_velocity",10),
      (troop_set_slot,"trp_pjct_x_velocity",":projectile",":x_velocity"),
      (troop_set_slot,"trp_pjct_y_velocity",":projectile",":y_velocity"),
      (troop_set_slot,"trp_pjct_z_velocity",":projectile",":z_velocity"),
      (troop_set_slot,"trp_pjct_emit_time",":projectile","$timer"),
      (troop_set_slot,"trp_pjct_x",":projectile",":x_pos"),
      (troop_set_slot,"trp_pjct_y",":projectile",":y_pos"),
      (val_add,":ground",10),
      (troop_set_slot,"trp_pjct_z",":projectile",":ground"),
    (try_end),
  (try_end),

  #explosition
  (try_begin),
    (eq,":explosition",1),
    (troop_get_slot,":explosive","trp_pjct_explosive",":projectile"),
    (try_begin),
      (eq,":explosive",1),
      (assign,":one_explosion_or_more",1),
      (troop_get_slot,":explosion_area","trp_pjct_explosion_area",":projectile"),
      (troop_get_slot,":explosion_damage","trp_pjct_explosion_damage",":projectile"),
      (troop_get_slot,":agent_deliverer","trp_pjct_source_agent",":projectile"),
      (particle_system_burst, "psys_explosion_fire_b", pos1, 40),
#      (particle_system_burst, "psys_explosion_fire", pos1, 10),
#      (particle_system_burst, "psys_explosion_smoke", pos1, 60),
      (play_sound,"snd_loud_explosion"),
      (try_for_agents,":agent"),
       (agent_is_alive,":agent"),
       (agent_is_human,":agent"),
       (agent_get_position,pos2,":agent"),
       (position_move_z,pos2,100),
       (get_distance_between_positions,":distance",pos1,pos2),
       (gt,":explosion_area",":distance"),
       (store_sub,":distance_inverse",":explosion_area",":distance"),
       (val_mul,":explosion_damage",":distance_inverse"),
       (val_div,":explosion_damage",":explosion_area"),
       (call_script,"script_agent_deliver_damage_to_agent",":agent_deliverer",":agent",":explosion_damage"),
      (try_end),
      (val_mul,":explosion_damage",2),
      (val_mul,":explosion_area",2),
      (try_for_agents,":agent"),
       (agent_is_alive,":agent"),
       (neg|agent_is_human,":agent"),
       (agent_get_position,pos2,":agent"),
       (position_move_z,pos2,100),
       (get_distance_between_positions,":distance",pos1,pos2),
       (gt,":explosion_area",":distance"),
       (store_sub,":distance_inverse",":explosion_area",":distance"),
       (val_mul,":explosion_damage",":distance_inverse"),
       (val_div,":explosion_damage",":explosion_area"),
       (call_script,"script_agent_deliver_damage_to_agent",":agent_deliverer",":agent",":explosion_damage"),
      (try_end),
      (scene_prop_get_num_instances,":num_instances","spr_explosion"),
      (gt,":num_instances",0),
      (scene_prop_get_instance,":instance", "spr_explosion", 0),
      (position_copy_origin,pos2,pos1),
      (prop_instance_set_position,":instance",pos2),
      (position_move_z,pos2,1000),
      (prop_instance_animate_to_position,":instance",pos2,175),
    (try_end),

#destroy particle
    (troop_set_slot,"trp_pjct_active",":projectile",0),

    (troop_get_slot,":instance","trp_pjct_attach_scene_prop",":projectile"),
    (try_begin),
      (ge,":instance",0),
      (troop_set_slot,"trp_instance_attached_to",":instance",0),
    (try_end),
  (try_end),
(try_end),
(eq,":one_explosion_or_more",1),
],
[
      (scene_prop_get_num_instances,":num_instances","spr_explosion"),
      (gt,":num_instances",0),
      (scene_prop_get_instance,":instance", "spr_explosion", 0),
      (prop_instance_get_position,pos2,":instance"),
      (position_move_z,pos2,-1000),
      (prop_instance_animate_to_position,":instance",pos2,300),
])
#Highlander end--------------------------------------

common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

common_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (eq, "$battle_won", 1),
      (call_script, "script_count_mission_casualties_from_agents"),
	  (call_script, "script_flush_gatesys_cache"),
      (finish_mission,0),
	(else_try),
		(eq, "$pin_player_fallen", 1),
		(call_script, "script_simulate_retreat", 5, 20),
		(str_store_string, s5, "str_retreat"),
		(call_script, "script_count_mission_casualties_from_agents"),
		(set_mission_result, -1),
		(finish_mission,0),
    (else_try),
      (call_script, "script_cf_check_enemies_nearby"),
      (question_box,"str_do_you_want_to_retreat"),
    (else_try),
      (display_message,"str_can_not_retreat"),
    (try_end),
    ])

common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_fight"),
    ])

#SW BSG integration - new popup box
common_space_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_training"),
    ])

common_custom_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (neq, "$g_battle_result", 0),
      (call_script, "script_custom_battle_end"),
	  (call_script, "script_flush_gatesys_cache"),
      (finish_mission),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ])

custom_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 2),
#    (neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign, "$battle_won",1),
    (assign, "$g_battle_result", 1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission, 1),
    ])

custom_battle_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen),
    (assign,"$g_battle_result",-1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission),
    ])

common_battle_victory_display = (
  4, 0, 0, [],
  [
    (eq,"$battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$pin_player_fallen", 0),
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":agent_team", ":player_agent"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_custom_battle_question_answered = (
   ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$g_battle_result", -1),
     (call_script, "script_custom_battle_end"),
     (finish_mission),
     ])

common_custom_siege_init = (
  0, 0, ti_once, [],
  [
    (assign, "$g_battle_result", 0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign,"$battle_won",0),
    (assign,"$defender_reinforcement_stage",0),
    (assign,"$attacker_reinforcement_stage",0),
    (assign,"$g_presentation_battle_active", 0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_music_situation_update = (
  30, 0, 0, [],
  [
    (call_script, "script_combat_music_set_situation_with_culture"),
    ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_2 = (
  0, 0, ti_once,
  [
    (set_show_messages, 0),
    (entry_point_get_position, pos10, 10),
    (team_give_order, "$defender_team", grc_infantry, mordr_hold),
    (team_give_order, "$defender_team", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team", grc_everyone, pos10),
    (team_give_order, "$defender_team_2", grc_infantry, mordr_hold),
    (team_give_order, "$defender_team_2", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team_2", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team_2", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team_2", grc_everyone, pos10),
    (set_show_messages, 1),
    ], [])

common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

common_siege_defender_reinforcement_check = (
  3, 0, 5, [],
  [(lt, "$defender_reinforcement_stage", 7),
   (store_mission_timer_a,":mission_time"),
   (ge,":mission_time",10),
   (store_normalized_team_count,":num_defenders",0),
   (lt,":num_defenders",10),
   (add_reinforcements_to_entry,4, 7),
   (val_add,"$defender_reinforcement_stage",1),
   (try_begin),
     (ge, "$defender_reinforcement_stage", 2),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (set_show_messages, 1),
     (ge, "$defender_reinforcement_stage", 4),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (set_show_messages, 1),
   (try_end),
   ])


common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

common_siege_attacker_reinforcement_check = (
  1, 0, 5,
  [
    (lt,"$attacker_reinforcement_stage",5),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
    (lt,":num_attackers",6)
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])

common_siege_attacker_do_not_stall = (
  5, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),
##      (neg|agent_is_defender, ":agent_no"),
      (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
    (try_end),
    ])

common_battle_check_friendly_kills = (
  2, 0, 0, [],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
 #   (neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign,"$battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission, 1),
    ])

common_battle_victory_display = (
  4, 0, 0, [],
  [
    (eq,"$battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_refill_ammo = (
  120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    (get_player_agent_no, ":player_agent"),
    (try_for_agents,":cur_agent"),
      (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
##      (agent_is_defender, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
    (try_end),
    ])

common_siege_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen)
    ],
  [
    (assign, "$pin_player_fallen", 1),
	(display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
	(call_script,"script_get_key","$deathcam_forward_key"),
	(str_store_string,s1,s13),
	(call_script,"script_get_key","$deathcam_backward_key"),
	(str_store_string,s2,s13),
	#(display_message, "@If you choose to watch the fight you can use the M and N keys to change your camera view."),
	(display_message, "@If you choose to watch the fight you can use the '{s1}' and '{s2}' keys to change your camera view."),
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_team, ":agent_team", ":player_agent"),
    # (try_begin),
      # (neq, "$attacker_team", ":agent_team"),
      # (neq, "$attacker_team_2", ":agent_team"),
      # (str_store_string, s5, "str_siege_continues"),
      # (call_script, "script_simulate_retreat", 8, 15),
    # (else_try),
      # (str_store_string, s5, "str_retreat"),
      # (call_script, "script_simulate_retreat", 5, 20),
    # (try_end),
    # (assign, "$g_battle_result", -1),
    # (set_mission_result,-1),
    # (call_script, "script_count_mission_casualties_from_agents"),
    # (finish_mission,0),
    ])

common_battle_order_panel = (
  0, 0, 0, [],
  [
    (game_key_clicked, gk_view_orders),
    (start_presentation, "prsnt_battle"),
    ])

common_battle_order_panel_tick = (
  0.1, 0, 0, [],
  [
    (eq, "$g_presentation_battle_active", 1),
    (call_script, "script_update_order_panel_statistics_and_map"),
    ])

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (display_message,"str_use_baggage_for_inventory"),
    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now"),
    ], [])

common_siege_init_ai_and_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_siege_init_ai_and_belfry"),
    ], [])

common_siege_move_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_belfry"),
    ], [])

common_siege_rotate_belfry = (
  0, 2, ti_once,
  [
    (call_script, "script_cf_siege_rotate_belfry_platform"),
    ],
  [
    (assign, "$belfry_positioned", 3),
    ])

common_siege_assign_men_to_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_assign_men_to_belfry"),
    ], [])

#SW - Chronicles of Talera regen rate script by Kardiophylax START
common_regeneration_store_info = (
  0, 0, ti_once, [], [                      # run this only once at the start of battle
   (get_player_agent_no, "$agent_for_player"), 						# these aren't required, I use them for other things
   #(agent_get_team, "$agent_for_player_team", "$agent_for_player"),  # these aren't required, I use them for other things

   (try_for_agents, "$talera_agent"),
      #(agent_set_slot, "$talera_agent", slot_agent_regen_rate, 0),  # this is probably redundant, I think all agents have new, fresh ids when created
   (try_end),

   (try_for_agents, "$talera_agent"),
       (agent_get_troop_id, "$agent_troop_type", "$talera_agent"),
       (try_begin),
          (is_between, "$agent_troop_type", kings_begin, kings_end),
          (agent_set_slot, "$talera_agent", slot_agent_regen_rate, 4),
       (else_try),
          (is_between, "$agent_troop_type", faction_heroes_begin, faction_heroes_end),
          (agent_set_slot, "$talera_agent", slot_agent_regen_rate, 3),
       (try_end),
   (try_end),

   # for testing
   (agent_set_slot, "$agent_for_player", slot_agent_regen_rate, 4),
  ]
)

common_regeneration = (
1, 0, 0, [], [
    (try_for_agents, "$talera_agent"),
       (agent_is_alive, "$talera_agent"),
       (agent_get_slot, ":regen_rate", "$talera_agent", slot_agent_regen_rate),
       (ge, ":regen_rate", 1),
       (store_agent_hit_points, ":agent_health", "$talera_agent", 1),
       (val_add, ":agent_health", ":regen_rate"),
       (agent_set_hit_points, "$talera_agent", ":agent_health", 1),
    (try_end),
  ]
)
#SW - Chronicles of Talera regen rate script by Kardiophylax END

#SW - start of special weapon noise by Jinnai - http://forums.taleworlds.net/index.php/topic,56917.msg1475545.html#msg1475545
lightsaber_noise_idle = (
	1, 0, 0, [],
		[
		(try_for_agents, ":agent"),
		  (agent_is_alive, ":agent"),
		  (agent_is_human, ":agent"),
		  (agent_get_wielded_item, ":handone", ":agent", 0),
		  (agent_get_wielded_item, ":handtwo", ":agent", 1),
		  #(this_or_next|eq, ":handone", "itm_special_weapon"),
		  #(this_or_next|eq, ":handone", "itm_lightsaber_green"),
		  (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
		  #(eq, ":handtwo", "itm_special_weapon"),
		  #(eq, ":handtwo", "itm_lightsaber_green"),
		  (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
		  #(agent_play_sound,":agent","snd_special_weapon_idle"), #This assumes it's a 1 second long clip, change trigger length if it's different
		  (agent_play_sound,":agent","snd_lightsaber_idle"), #This assumes it's a 1 second long clip, change trigger length if it's different
		(try_end),
		]
)
lightsaber_noise_agent = (
	0.1, 0, 0, [],
		[
		(get_player_agent_no, ":player_agent"),
		(try_for_agents, ":agent"),
		  (agent_is_alive, ":agent"),
		  (agent_is_human, ":agent"),
		  (neq, ":agent", ":player_agent"),		#we have a different trigger for the player_agent
		  (agent_get_wielded_item, ":handone", ":agent", 0),
		  (agent_get_wielded_item, ":handtwo", ":agent", 1),
		  #(this_or_next|eq, ":handone", "itm_special_weapon"),
		  #(this_or_next|eq, ":handone", "itm_lightsaber_green"),
		  (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
		  #(eq, ":handtwo", "itm_special_weapon"),
		  #(eq, ":handtwo", "itm_lightsaber_green"),
		  (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
		  (agent_get_combat_state, ":state", ":agent"),
			(try_begin),
			  (eq,":state",4), #This is the combat state for melee swing
			  (agent_slot_eq,":agent",slot_agent_attack_sound, 0),
			  (agent_set_slot, ":agent", slot_agent_attack_sound, 1),
			  #(agent_play_sound,":agent","snd_special_weapon_attack"),
			  (agent_play_sound,":agent","snd_lightsaber_swing"),
			(else_try),
			  (neq,":state",4),
			  (agent_set_slot, ":agent", slot_agent_attack_sound, 0),
			(try_end),
		(try_end),
		]
)
# old code (plays sound when you click the attack key)
lightsaber_noise_player = (
	0, 0, 1, 	#there's a 1 second refresh timer to give the attack sound time to complete
		[
		(neg|conversation_screen_is_active),
		(game_key_clicked, gk_attack),
		(neg|game_key_is_down, gk_defend),
		],
		[
		  (get_player_agent_no, ":agent"),
		  (agent_is_alive, ":agent"),
		  (agent_get_wielded_item, ":handone", ":agent", 0),
		  (agent_get_wielded_item, ":handtwo", ":agent", 1),
		  (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
		  (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
		  (agent_play_sound,":agent","snd_lightsaber_swing"),
		]
)

# # new code (plays sound when you release the attack key, uses play_sound because agent_play_sound didn't work) - however, the code doesn't sound great when you jam on the buttons a lot so I went back to the old method....
# lightsaber_noise_player = (
	# 0, 0, 0,	# check, delay, re-arm interval (re-arm after 1 second so the sound has a change to play, this doesn't work for some reason?)
		# [
		  # (this_or_next|game_key_is_down, gk_attack),
		  # (eq, "$attack_key", 1),	#attack key was previously down (0 = up, 1 = down,)
		  # (neg|conversation_screen_is_active),	#don't play sound when on a conversation screen
		  # (neg|eq, "$play_sound_lock", 1),
		# ],
		# [
		  # (assign, "$play_sound_lock", 1),
		  # (get_player_agent_no, ":player_agent"),
		  # (agent_is_alive, ":player_agent"),    	# only check if player is alive
		  # (try_begin),
			# (game_key_is_down, gk_attack),
			# (assign, "$attack_key", 1),	#attack key is down (0 = up, 1 = down)
		  # (else_try),	#attack key was just released
			# (assign, "$attack_key", 0),	#attack key was released (0 = up, 1 = down)
			# #(display_message, "@attack key was released."),
			# (agent_get_wielded_item, ":handone", ":player_agent", 0),
			# (agent_get_wielded_item, ":handtwo", ":player_agent", 1),
			# (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
			# (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
			# (play_sound,"snd_lightsaber_swing"),
			# #(play_sound,"snd_lightsaber_swing", sf_2d),
		  # (try_end),
		  # (assign, "$play_sound_lock", 0),
		# ]
# )

# lightsaber_noise_player = (
	# 0, 0, 0,
		# [
		  # (this_or_next|game_key_is_down, gk_attack),
		  # (eq, "$attack_key", 1),	#attack key was previously down (0 = up, 1 = down, 2 = released)
		  # (neq, "$attack_key", 2),	#attack key was just released (0 = up, 1 = down, 2 = released)
		# ],
		# [
		  # (try_begin),
			# (game_key_is_down, gk_attack),
			# (assign, "$attack_key", 1),	#attack key is down (0 = up, 1 = down, 2 = released)
		  # (else_try),	#attack key was just released
			# (assign, "$attack_key", 2),	#attack key was released (0 = up, 1 = down, 2 = released)
			# (display_message, "@attack key was released."),
		  # (try_end),
		# ]
# )
# # new code (plays sound when you release the attack key)
# lightsaber_noise_player_2 = (
	# 0, 0, 1.5,	#there's a 1.5 second refresh timer to give the attack sound time to complete
		# [
		  # (eq, "$attack_key", 2),	#attack key was released (0 = up, 1 = down, 2 = released)
		# ],
		# [
		  # (display_message, "@now play a custom sound since the attack key was released."),
		  # (get_player_agent_no, ":player_agent"),
		  # (try_begin),
		  	# (agent_is_alive, ":player_agent"),
			# (agent_get_wielded_item, ":handone", ":player_agent", 0),
			# (agent_get_wielded_item, ":handtwo", ":player_agent", 1),
			# (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
			# (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
			# (agent_play_sound,":player_agent","snd_lightsaber_swing"),
		  # (try_end),
		  # (assign, "$attack_key", 0),	#attack key is up (0 = up, 1 = down, 2 = released)
		# ]
# )

#SW - end of special weapon noise by Jinnai

# #SW - new warcry noise
# warcry_player = (
	# 0, 0, 1,	#there's a 1 second refresh timer to give the sound time to complete
		# [
			# #(key_clicked, key_e),
			# (key_clicked, "$warcry_key"),
			# (neg|conversation_screen_is_active),
		# ],
		# [
		  # #(display_message, "@warcry_player started."),		#debug
		  # (get_player_agent_no, ":agent"),
		  # (agent_is_alive, ":agent"),
		  # #(troop_get_type, ":race", "$g_player_troop"),
		  # (troop_get_type, ":race", ":agent"),
		  # (try_begin),
		  # (eq, ":race", 1),	#female
			# (agent_play_sound,":agent","snd_woman_victory"),
			# (agent_set_animation, ":agent", "anim_cheer"),
		  # (else_try),
			# (agent_play_sound,":agent","snd_man_victory"),
			# (agent_set_animation, ":agent", "anim_cheer"),
		  # (try_end),
		  # #(display_message, "@warcry_player finished."),		#debug
		# ]
# )
# #SW - end of new warcry noise

common_switch_sw_scene_props = (
  ti_before_mission_start, 0, 0, [],
  [
		#get the current towns faction
		(store_faction_of_party, ":center_faction", "$current_town"),
		(try_begin),
			(eq, ":center_faction", "fac_galacticempire"),	#empire
			(assign, ":faction_sign_begin", sw_empire_sign_begin),
			(assign, ":faction_sign_end", sw_empire_sign_end),
			(assign, ":faction_poster_begin", sw_empire_poster_begin),
			(assign, ":faction_poster_end", sw_empire_poster_end),
		(else_try),
			(eq, ":center_faction", "fac_rebelalliance"),	#rebel
			(assign, ":faction_sign_begin", sw_rebel_sign_begin),
			(assign, ":faction_sign_end", sw_rebel_sign_end),
			(assign, ":faction_poster_begin", sw_rebel_poster_begin),
			(assign, ":faction_poster_end", sw_rebel_poster_end),
		(else_try),
			#other
			(assign, ":faction_sign_begin", sw_generic_sign_begin),
			(assign, ":faction_sign_end", sw_generic_sign_end),
			(assign, ":faction_poster_begin", sw_generic_poster_begin),
			(assign, ":faction_poster_end", sw_generic_poster_end),
		(try_end),

		#SW - replace signs
		(store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
		(replace_scene_props, "spr_sw_sign_random_all_1", ":sign"),
		(store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
		(replace_scene_props, "spr_sw_sign_random_all_2", ":sign"),
		(store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
		(replace_scene_props, "spr_sw_sign_random_all_3", ":sign"),
		(store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
		(replace_scene_props, "spr_sw_sign_random_all_4", ":sign"),
		(store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
		(replace_scene_props, "spr_sw_sign_random_galacticempire", ":sign"),
		(store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
		(replace_scene_props, "spr_sw_sign_random_rebelalliance", ":sign"),
		(store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
		(replace_scene_props, "spr_sw_sign_random_huttcartel", ":sign"),
		(store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
		(replace_scene_props, "spr_sw_sign_random_galacticempire", ":sign"),
		(store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
		(replace_scene_props, "spr_sw_sign_random_generic_1", ":sign"),
		(store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
		(replace_scene_props, "spr_sw_sign_random_generic_2", ":sign"),
		(store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
		(replace_scene_props, "spr_sw_sign_random_generic_3", ":sign"),
		(store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
		(replace_scene_props, "spr_sw_sign_random_generic_4", ":sign"),
		#SW - replace posters
		(store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
		(replace_scene_props, "spr_sw_poster_random_all_1", ":poster"),
		(store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
		(replace_scene_props, "spr_sw_poster_random_all_2", ":poster"),
		(store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
		(replace_scene_props, "spr_sw_poster_random_all_3", ":poster"),
		(store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
		(replace_scene_props, "spr_sw_poster_random_all_4", ":poster"),
		(store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
		(replace_scene_props, "spr_sw_poster_random_towngalacticempire", ":poster"),
		(store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
		(replace_scene_props, "spr_sw_poster_random_townrebelalliance", ":poster"),
		(store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
		(replace_scene_props, "spr_sw_poster_random_townhuttcartel", ":poster"),
		(store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
		(replace_scene_props, "spr_sw_poster_random_townfaction_4", ":poster"),
		(store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
		(replace_scene_props, "spr_sw_poster_random_generic_1", ":poster"),
		(store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
		(replace_scene_props, "spr_sw_poster_random_generic_2", ":poster"),
		(store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
		(replace_scene_props, "spr_sw_poster_random_generic_3", ":poster"),
		(store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
		(replace_scene_props, "spr_sw_poster_random_generic_4", ":poster"),

    ])

common_agent_droid_refill_trigger = (
	30, 0, 0,	# check every 5 seconds
		[],
		[
			#(display_message, "@running common_agent_droid_refill_trigger"),	#debug
			(get_player_agent_no, ":player_agent"),
			(assign, ":player_agent_refilled_ammo", 0),
			(assign, ":player_agent_refilled_health", 0),
			(assign, ":power_droid_agent", 0),
			(assign, ":med_droid_agent", 0),
			(try_for_agents, ":agent"),
				(agent_is_alive, ":agent"),	#so we don't try dead agents
				(agent_is_human,":agent"),	#agent is a human
				#(agent_get_troop_id, ":agent_troop", ":agent"),
				#(eq, ":agent_troop", "trp_power_droid"),
				#(display_message, "@trp_power_droid found!"),	#debug
				(try_begin),
					#check for power droids to refill ammo
					(this_or_next|agent_has_item_equipped,":agent","itm_power_droid_grey"),
					(this_or_next|agent_has_item_equipped,":agent","itm_power_droid_snow"),
					(agent_has_item_equipped,":agent","itm_power_droid_tan"),
					(agent_get_position,pos1,":agent"),
					(agent_get_team,":agent_team", ":agent"),
					(try_for_agents, ":chosen"),
						(agent_is_alive, ":chosen"),	#so we don't try dead agents
						(agent_is_human,":chosen"),	#agent is a human
						(agent_get_team  ,":chosen_team", ":chosen"),
						(eq, ":agent_team", ":chosen_team"),
						(agent_get_position, pos2, ":chosen"),
						(get_distance_between_positions,":dist",pos1,pos2),
						(lt,":dist",400),	#SW - how close they have to be to refill ammo
						(agent_refill_ammo, ":chosen"),
						(eq, ":chosen",":player_agent"),
						(assign, ":player_agent_refilled_ammo", 1),
						(assign, ":power_droid_agent", ":agent"),	#remember an agent that refilled the players ammo
					(try_end),
				(else_try),
					#check for med droids to refill health
					(agent_has_item_equipped,":agent","itm_fxseries_droid_armor"),
					(agent_get_position,pos1,":agent"),
					(agent_get_team,":agent_team", ":agent"),
					(try_for_agents, ":chosen"),
						(agent_is_alive, ":chosen"),	#so we don't try dead agents
						(agent_is_human,":chosen"),	#agent is a human
						(agent_get_team  ,":chosen_team", ":chosen"),
						(eq, ":agent_team", ":chosen_team"),
						(agent_get_position, pos2, ":chosen"),
						(get_distance_between_positions,":dist",pos1,pos2),
						(lt,":dist",400),	#SW - how close they have to be to refill ammo
						(store_agent_hit_points,":chosen_health",":chosen",0),	#relative number, 0-100%
						(lt, ":chosen_health", 100),
						(val_add, ":chosen_health", 5),	#add 5%
						(try_begin),
							(gt, ":chosen_health", 100),
							(assign, ":chosen_health", 100),		#so we don't try and set hit points > 100%
						(try_end),
						(agent_set_hit_points,":chosen",":chosen_health",0),	#relative number, 0-100%
						(eq, ":chosen",":player_agent"),
						(assign, ":player_agent_refilled_health", 1),
						(assign, ":med_droid_agent", ":agent"),	#remember an agent that refilled the players ammo
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":player_agent_refilled_ammo", 1),
				(display_message, "@A Power Droid refilled your ammo!"),
				(agent_play_sound, ":power_droid_agent", "snd_gonk_noise"),	#play a sound from the agent that refilled the player's ammo
			(try_end),
			(try_begin),
				(eq, ":player_agent_refilled_health", 1),
				(display_message, "@A Medical Droid refilled some of your health!"),
				(agent_play_sound, ":med_droid_agent", "snd_bacta_heal"),	#play a sound from the agent that refilled the player's health
			(try_end),
		])

common_speeder_trigger_1 = (
	 # SW - script to stop riderless horses (ie. speeders) from moving (script from KON_Air)
	 5, 0, 0,	#length of stationary animation
	 #0, 0, ti_once,	#only need to run once since I used agent_set_stand_animation, nope, didn't work....
      [],
	  [
	  (try_for_agents, ":cur_agent"),
	   (agent_is_alive, ":cur_agent"),	#so we don't try dead agents
	    (neg|agent_is_human,":cur_agent"),	#agent is a horse
	     (agent_get_rider,":cur_rider", ":cur_agent"),
		  (try_begin),
	        (lt, ":cur_rider", 0),	#horse does not have a rider
		    (agent_play_sound,":cur_agent","snd_speeder_noise_idle"),
			#(display_message, "@debug: sound played - no rider"),
		    (agent_set_animation, ":cur_agent", "anim_speeder_stationary"),	#so the horse doesn't move, must include module_animations at the top
		    #(agent_set_stand_animation, ":cur_agent", "anim_speeder_stationary"),	#doesn't work to stop them?
		  #(else_try),
		  #  (agent_play_sound,":cur_agent","snd_speeder_noise_moving"),
			#(agent_play_sound,":cur_rider","snd_speeder_noise_moving"),
			#(display_message, "@debug: sound played - with rider"),
		  (try_end),
	  (try_end),
      ])

common_speeder_trigger_2 = (
	 # SW - script to stop riderless horses (ie. speeders) from moving (script from KON_Air)
	 0.5, 0, 0,	#check more often then common_speeder_trigger_1
      [],
	  [
	  (get_player_agent_no, ":player_agent"),
	  (try_for_agents, ":cur_agent"),
	   (agent_is_alive, ":cur_agent"),	#so we don't try dead agents
	    (neg|agent_is_human,":cur_agent"),	#agent is a horse
	     (agent_get_rider,":cur_rider", ":cur_agent"),
		 (agent_get_slot, ":speeder_movement", ":cur_agent", slot_agent_speeder_movement),
		  (try_begin),
	        (lt, ":cur_rider", 0),	#horse does not have a rider
			(lt, ":speeder_movement", 0),	#slot is not set
			(agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 0),	#horse does not have a rider
		  (else_try),
	        (ge, ":cur_rider", 0),	#horse has a rider
			(lt, ":speeder_movement", 0),	#slot is not set
			(agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 1),	#horse has a rider
		  (else_try),
	        (lt, ":cur_rider", 0),	#horse does not have a rider
			(eq, ":speeder_movement", 1),	#speeder was previously mounted
			(agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 0),	#horse does not have a rider
			(eq, ":cur_agent", ":player_agent"),
			(stop_all_sounds,2),	#so we stop the speeder's engine noise loop that started for the player
			#(display_message, "@debug: agent got OFF a speeder"),
		  (else_try),
	        (ge, ":cur_rider", 0),	#horse has a rider
			(eq, ":speeder_movement", 0),	#speeder was previously not mounted
			(agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 1),	#horse has a rider
			#(display_message, "@debug: agent got ON a speeder"),
			 (agent_set_animation, ":cur_agent", "anim_speeder_allow_movement"),	#cancel the current animation and allow the horse to move
			 #(agent_play_sound, ":cur_agent", "snd_speeder_noise_begin"),
			 (eq, ":cur_agent", ":player_agent"),
			 (play_sound, "snd_speeder_noise_loop", sf_looping),
		  (else_try),
			(ge, ":cur_rider", 0),	#horse has a rider
			(eq, ":speeder_movement", 1),	#speeder is mounted
			#(agent_play_sound,":cur_agent","snd_speeder_noise_moving"),		#make moving sound (doesn't work all that well)
		  (try_end),
		    # (agent_play_sound,":cur_agent","snd_speeder_noise_idle"),
			# (display_message, "@sound played - no rider"),
		    # (agent_set_animation, ":cur_agent", "anim_speeder_stationary"),	#so the horse doesn't move, must include module_animations at the top
		    # #(agent_set_stand_animation, ":cur_agent", "anim_speeder_stationary"),	#doesn't work to stop them?
		  # (else_try),
		    # (agent_play_sound,":cur_agent","snd_speeder_noise_moving"),
			# #(agent_play_sound,":cur_rider","snd_speeder_noise_moving"),
			# (display_message, "@sound played - with rider"),
	  (try_end),
      ])

common_check_town_fight = (
	3, 0, 0,	[

					#SW - maybe use all_enemies_defeated ?
					#(all_enemies_defeated, 5),

					#(assign, reg1, "$g_init_fight"),					#debug only
					#(display_message, "@g_init_fight = {reg1}"),		#debug only

					#(assign, reg1, "$g_player_current_own_troop_kills"),
					(try_begin),
						(eq, "$g_init_fight", 1),	#no battle, allow player to start a town fight

						# #-------------------------- OLD CODE -------------------------------------
						# #(get_player_agent_kill_count, ":wound_count", 1),	#can use this to get the wound_count instead of kill count?
						# #(assign, reg1, "$player_current_friendly_kills"),
						# (get_player_agent_own_troop_kill_count, ":count"),
						# #(assign, reg2, ":count"),
						# #(display_message, "@g_player = {reg1}, own_troop_kill = {reg2}"),
						# (try_begin),
							# (gt, ":count", "$player_current_friendly_kills"),
							# (dialog_box,"@You have killed a citizen and are now wanted by the local authorities!", "@Alert"),	# display dialog popup ?
							# (call_script, "script_start_town_fight"),
							# (assign, "$g_init_fight", 2),
						# (try_end),

						(get_player_agent_no, ":player_agent"),
						(assign, ":wounded", 0),
						#(assign, ":killed", 0),
						(try_for_agents, ":agent"),
							(agent_is_human,":agent"), # SWY @> It shouldn't be triggered by horse damage
							(agent_get_team  ,":team", ":agent"),(eq, ":team", 2),	#citizens
							(neq, ":agent", ":player_agent"), # SWY @> non-player agents only
							(store_agent_hit_points,":agent_hp",":agent",1),	#set to 1 to retrive absolute hp
							(agent_get_slot, ":old_agent_hp", ":agent", slot_agent_hit_points),
							(try_begin),
								(lt, ":agent_hp", ":old_agent_hp"),
								(val_add, ":wounded", 1),
							(try_end),
							#check if you have killed anybody?  then all citizens attack
						(try_end),
						(try_begin),
							(eq, "$tavern_brawl", 1),
							(assign, "$g_init_fight", 2),
						(else_try),
							(gt, ":wounded", 0),
							(dialog_box,"@You have attacked a citizen and are now wanted by the local authorities!", "@Alert"),	# display dialog popup ?
							(call_script, "script_start_town_fight"),
							(assign, "$g_init_fight", 2),
						(try_end),

					(else_try),
						(eq, "$g_init_fight", 2),	#random scene battle
						(get_player_agent_no, ":player_agent"),
						#set_party_battle_mode is off, so manually set the players hit points so they are injured after battle
						(store_agent_hit_points,":player_agent_health",":player_agent",0),	#relative health (0-100)
						#(troop_set_health, "trp_player", ":player_agent_health"),
						(troop_set_health, "$g_player_troop", ":player_agent_health"),
						#count the teams
						#(agent_get_team, ":player_team", ":player_agent"),
						(assign, ":enemies",0),
						(try_for_agents,":agent"),
							(agent_is_human,":agent"),
							#SW - now try and check if we need to decrease the companions health
							(agent_get_entry_no,":entry_no",":agent"),
							(try_begin),
								(this_or_next|eq,":entry_no",48),		#player's companion
								(eq,":entry_no",49),					#player's companion
								(agent_get_troop_id, ":agent_troop_id", ":agent"),
								(is_between,":agent_troop_id", companions_begin, companions_end),	#verify they are a npc
								(store_agent_hit_points,":agent_health",":agent",0),	#relative health (0-100)
								(troop_set_health, ":agent_troop_id", ":agent_health"),
							(try_end),
							#now check the rest of the agents to see if there are any enemies
							(agent_is_alive,":agent"),
							(neg|agent_is_ally, ":agent"),
							(val_add, ":enemies", 1),
							#debug
							#(assign, reg1, ":player_team_count"),
							#(display_message, "@player_team_count = {reg1}, other_team_count = {reg2}"),
						(try_end),
						(try_begin),
							(eq,":enemies",0),
							(dialog_box,"@All enemies at this location have been defeated!", "@Success"),	# display dialog popup ?
							(add_xp_to_troop,100,"$g_player_troop"),	#since custom commander is integrated
							(call_script, "script_troop_add_gold", "$g_player_troop", 100),
							(assign, "$g_init_fight", 0),	#turn it off
									#@> SWY - Added some conditionals for changing nynamically the faction ralections
									(try_begin),
										(eq, "$g_started_battle_random_by_enemy_faction", 1),
										(store_faction_of_party, ":minorplanet_faction", "$current_town"),
										(call_script, "script_change_player_relation_with_faction", ":minorplanet_faction", 1),
									(else_try),
										#(eq,"$g_started_battle_random_by_enemy_faction",1),
										(store_faction_of_party, ":minorplanet_faction", "$current_town"),
										(call_script, "script_change_player_relation_with_faction", ":minorplanet_faction", -3),
									(try_end),
						(try_end),
					(try_end),


				],[])

#SW - START OF SHIELD BASH
#shield bash integration - http://forums.taleworlds.net/index.php/topic,44290.0.html
shield_bash_kit_1 = (
	ti_before_mission_start, 0, 0, [], [
										(le, "$shield_bash_toggle", 0),
										(assign,"$bash_readiness",0),
										])
shield_bash_kit_2 = (
    0.1, 0, 0, [], [
					(le, "$shield_bash_toggle", 0),
					(val_add,"$bash_readiness",1),
					])
shield_bash_kit_3 = (
    0, 0, 0, [
			(le, "$shield_bash_toggle", 0),
			(game_key_is_down, gk_defend),
			(game_key_clicked, gk_attack),
			],
	[(assign,":continue",0),
	(get_player_agent_no,":player"),
	(agent_is_alive,":player"),
    #SW - modified to add shields_begin and shields_end
	#(try_for_range,":shield","itm_wooden_shield","itm_jarid"),
	(try_for_range,":shield",shield_bash_begin,shield_bash_end),
	  (agent_has_item_equipped,":player",":shield"),
	  (assign,":continue",1),
	(end_try),
	(eq,":continue",1),
	(agent_get_horse,":horse",":player"),
	(neg|gt,":horse",0),
	(ge,"$bash_readiness",10),
	(assign,"$bash_readiness",0),
	(call_script,"script_cf_agent_shield_bash",":player"),
	])
shield_bash_kit_4 = (
    1.0, 0, 0, [
				(le, "$shield_bash_toggle", 0),
				],
	[
	(get_player_agent_no,":player"),
	(try_for_agents,":agent"),
		(agent_is_alive,":agent"),
		(agent_is_human,":agent"),
		(neq,":agent",":player"),
		(agent_get_class ,":class", ":agent"),
		(neq,":class",grc_cavalry),
		(assign,":continue",0),
		#SW - modified to add shields_begin and shields_end
		#(try_for_range,":shield","itm_wooden_shield","itm_jarid"),
		(try_for_range,":shield",shield_bash_begin,shield_bash_end),
		  (agent_has_item_equipped,":agent",":shield"),
		  (assign,":continue",1),
		(end_try),
		(eq,":continue",1),
		(assign,":chances",0),
		(agent_get_team,":team",":agent"),
		(agent_get_position,pos1,":agent"),
		(try_for_agents,":other"),
		  (agent_is_alive,":other"),
		  (agent_is_human,":other"),
		  (agent_get_class ,":class", ":other"),
		  (neq,":class",grc_cavalry),
		  (agent_get_team,":otherteam",":other"),
		  (neq,":team",":otherteam"),
		  (agent_get_position,pos2,":other"),
		  (get_distance_between_positions,":dist",pos1,pos2),
		  (neg|position_is_behind_position,pos2,pos1),
		  (lt,":dist",200),
		  (val_add,":chances",1),
		(end_try),
		(store_agent_hit_points,":health",":agent",0),
		(val_mul,":health",-1),
		(val_add,":health",100),
		(val_div,":health",10),
		(val_mul,":chances",":health"),
		(store_random_in_range,":rand",1,25),
		(lt,":rand",":chances"),
		(call_script,"script_cf_agent_shield_bash",":agent"),
	(end_try),])
# END OF SHIELD BASH

#--------------------------------------------------------------------------------------------------------------------------
#SW - common_alternative_attack code from Highlander (only disadvantage is that ammo is refilled)
# I also switched the code from trp_player to $g_player_troop since I use custom commander
#common_alternative_attack = (0,0,0,

#SW - actually, this code causes issues with the battle summary at the end since it reports the player was injured, so I am no longer using it
#	- there is also another issue that you see your dead body indoor scenes, but this would not be a problem in warband since there is now a remove_agent

# common_toggle_weapon_capabilities = (0, 0, 0,
# [
  # #(key_clicked, key_t),
  # (key_clicked, "$toggle_weapon_key"),
  # (neg|conversation_screen_is_active),
  # (get_player_agent_no,":player"),
  # (agent_is_alive, ":player"),    	# only continue if player is alive
  # (agent_get_team,":team",":player"),
  # (agent_get_wielded_item,":item",":player",0),
  # (gt,":item",-1),
  # #(item_get_slot,":item_b",":item",slot_item_alternative_attack),
  # (item_get_slot,":item_b",":item",slot_item_alternate_weapon),
  # (gt,":item_b",0),
  # (set_show_messages,0),
  # (agent_get_horse,":horse",":player"),
  # (troop_get_inventory_slot,":slot_horse","$g_player_troop",ek_horse),
  # (troop_get_inventory_slot_modifier,":slot_horse_modifier","$g_player_troop",ek_horse),
  # (init_position,pos2),
  # (try_begin),
    # (lt,":horse",0),
	# (troop_set_inventory_slot,"$g_player_troop",ek_horse,"itm_no_item"),
    # (troop_remove_item, "$g_player_troop", "itm_no_item"),
  # (else_try),
    # (agent_get_item_id,":horse_item",":horse"),
	# (troop_set_inventory_slot,"$g_player_troop",ek_horse,":horse_item"),
   # (agent_set_position,":horse",pos2),
  # (try_end),
  # (try_for_range,":slot",0,4),
	# (troop_get_inventory_slot,":slot_item","$g_player_troop",":slot"),
    # (troop_get_inventory_slot_modifier,":slot_modifier","$g_player_troop",":slot"),
    # (eq,":slot_item",":item"),
	# (troop_get_inventory_slot,":slot_item_0","$g_player_troop",0),
    # (troop_get_inventory_slot_modifier,":slot_modifier_0","$g_player_troop",0),
    # (troop_set_inventory_slot,"$g_player_troop",0,":item_b"),
    # (troop_set_inventory_slot_modifier,"$g_player_troop",0,":slot_modifier"),
    # (neq,":slot",0),
	# (troop_set_inventory_slot,"$g_player_troop",":slot",":slot_item_0"),
    # (troop_set_inventory_slot_modifier,"$g_player_troop",":slot",":slot_modifier_0"),
  # (try_end),
  # (store_agent_hit_points,":hit_points",":player",1),
  # (agent_get_position,pos1,":player"),
  # (agent_set_position,":player",pos2),
  # (call_script,"script_dmod_kill_agent",":player"),
  # (set_spawn_position,pos1),
  # (spawn_agent,"$g_player_troop"),
  # (agent_set_hit_points,reg0,":hit_points",1),
  # (agent_set_team,reg0,":team"),
  # (try_begin),
    # (lt,":slot_horse",0),
	# (troop_set_inventory_slot,"$g_player_troop",ek_horse,"itm_no_item"),
	# (troop_remove_item, "$g_player_troop", "itm_no_item"),
  # (else_try),
	# (troop_set_inventory_slot,"$g_player_troop",ek_horse,":slot_horse"),
	# (troop_set_inventory_slot_modifier,"$g_player_troop",ek_horse,":slot_horse_modifier"),
  # (try_end),
  # (set_show_messages,1),
# ],[])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - old toggle_weapon_capabilities code (you must display a dialog and ammo is refilled)
#common_toggle_weapon_capabilities_w_popup = (0, 0, 0, [
common_toggle_weapon_capabilities = (0, 0, 0, [
	#(key_clicked, key_t),
	(key_clicked, "$toggle_weapon_key"),
	(neg|conversation_screen_is_active),
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		#clear the strings
		(str_clear, s1),(str_clear, s2),(str_clear, s10),(str_clear, s11),(str_clear, s12),(str_clear, s13),
		(assign, "$show_switch_weapon_dialog", 0),
		#old code concept below that switches all weapons
		# (try_for_range, ":slot_no", 0, 4),
			# (troop_get_inventory_slot, ":item", "$g_player_troop",":slot_no"),	#since custom commander is integrated
			# (try_begin),
				# (ge, ":item", 0),	#don't check empty item slots
				# (item_slot_ge, ":item", slot_item_alternate_weapon, 1),	#see if the item has an alternate weapon slot defined
				# (item_get_slot, ":alternate_weapon", ":item", slot_item_alternate_weapon),	#get the alternate weapon
				# (troop_get_inventory_slot_modifier, ":modifier", "$g_player_troop", ":slot_no"),	#get the modifier
				# (troop_set_inventory_slot, "$g_player_troop", ":slot_no", ":alternate_weapon"),	#set the alternate weapon
				# (troop_set_inventory_slot_modifier, "$g_player_troop", ":slot_no", ":modifier"),	#set the modifier
				# #record the names to display in the dialog later
				# (str_store_item_name, s1, ":item"),
				# (str_store_item_name, s2, ":alternate_weapon"),
				# (try_begin),
					# (eq, ":slot_no", 0),
					# (str_store_string, s10, "@{s1} switched to {s2}"),
				# (else_try),
					# (eq, ":slot_no", 1),
					# (str_store_string, s11, "@{s1} switched to {s2}"),
				# (else_try),
					# (eq, ":slot_no", 2),
					# (str_store_string, s12, "@{s1} switched to {s2}"),
				# (else_try),
					# (eq, ":slot_no", 3),
					# (str_store_string, s13, "@{s1} switched to {s2}"),
				# (try_end),
				# (assign, "$show_switch_weapon_dialog", 1),
			# (try_end),
		# (try_end),
		(agent_get_wielded_item,":wielded_item",":player_agent",0),
		(try_begin),
			(gt,":wielded_item",-1),
			(item_slot_ge, ":wielded_item", slot_item_alternate_weapon, 1),	#see if the item has an alternate weapon slot defined
			(item_get_slot, ":alternate_weapon", ":wielded_item", slot_item_alternate_weapon),	#get the alternate weapon
			(try_for_range, ":slot_no", 0, 4),
				(troop_get_inventory_slot, ":item_in_slot", "$g_player_troop",":slot_no"),	#since custom commander is integrated
				(eq, ":item_in_slot", ":wielded_item"),
				(troop_get_inventory_slot_modifier, ":modifier", "$g_player_troop", ":slot_no"),	#get the modifier
				(troop_set_inventory_slot, "$g_player_troop", ":slot_no", ":alternate_weapon"),	#set the alternate weapon
				(troop_set_inventory_slot_modifier, "$g_player_troop", ":slot_no", ":modifier"),	#set the modifier
				#record the names to display in the dialog later
				(str_store_item_name, s1, ":wielded_item"),
				(str_store_item_name, s2, ":alternate_weapon"),
				(str_store_string, s10, "@{s1} switched to {s2}"),
				(assign, "$show_switch_weapon_dialog", 1),
			(try_end),
		(try_end),
		(try_begin),
			(eq, "$show_switch_weapon_dialog", 1),
			(start_mission_conversation, "$g_player_troop"),	#workaround since weapons don't automatically switch
		(try_end),
	])
#--------------------------------------------------------------------------------------------------------------------------------------------------
# #SW - new player_damage
# common_player_damage = (1, 0, ti_once, [
	# #(neg|conversation_screen_is_active),
	# #(le, "$player_damage", 0),

		# #SW - so it neverruns
		# (eq, 0, 1),

	# ],
	# [
		# (get_player_agent_no, ":player_agent"),
		# #(agent_is_alive, ":player_agent"),
		# # (store_agent_hit_points,":player_hp",":player_agent",0),	# set absolute to 1 to retrieve actual hps, otherwise will return relative hp in range [0..100]
		# # (try_begin),
			# # (eq, ":player_hp", "$player_hp_previous"),
			# # #do nothing
		# # (else_try),
			# # (le, ":player_hp", 90),
		# # (try_begin),
			# # (le, ":player_hp", 75),
			# # #(display_message, "@prsnt_player_damage..."),
			# # (start_presentation, "prsnt_player_damage"),
		# # (try_end),
		# (start_presentation, "prsnt_player_damage"),

		# (assign, "$player_hp_previous", ":player_hp"),
	# ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
# common_crouch_toggle = (0, 0, 0, [
	# (key_clicked, key_f),(neg|conversation_screen_is_active)
	# ],
	# [
		# #(get_player_agent_no, ":player_agent"),
		# #(assign, ":cur_agent", ":player_agent"),

		# (try_begin),
			# (le, "$crouch_toggle", 0),	#incase this variable isn't set yet
			# (assign, "$crouch_toggle", 1),	#turn it on
			# (try_for_agents, ":cur_agent"),
				# (agent_is_alive, ":cur_agent"),
				# (agent_set_speed_limit, ":cur_agent", 1),		#forces them to walk, it affects AI only
				# (agent_set_stand_animation, ":cur_agent", "anim_stand_crouch"),					#only works when weapons aren't equipped
				# (agent_set_walk_forward_animation, ":cur_agent", "anim_walk_forward_crouch"),	#only works when weapons aren't equipped
			# (try_end),
			# (display_message, "@crouch is now ON."),
		# (else_try),
			# (assign, "$crouch_toggle", 0),	#turn it off
			# (try_for_agents, ":cur_agent"),
				# (agent_set_speed_limit, ":cur_agent", 100),		#set it high so they can run again, it affects AI only
				# (agent_set_stand_animation, ":cur_agent", "anim_stand"),				#only works when weapons aren't equipped
				# (agent_set_walk_forward_animation, ":cur_agent", "anim_walk_forward"),	#only works when weapons aren't equipped
			# (try_end),
			# (display_message, "@crouch is now OFF."),
		# (try_end),
	# ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Swyter Turret Code
common_turret = (0, 0, 0,
	[
		(neg|conversation_screen_is_active),
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		(agent_get_horse, ":horse", ":player_agent"),
		(eq, ":horse", -1),		#can only crouch if you aren't on a horse
	],
	[
		# (get_player_agent_no, ":player_agent"),

		# (agent_get_position,pos1,":player_agent"),
		##(prop_instance_get_position,1,"$ship"),
        # (assign,":dist",150),
           # (scene_prop_get_num_instances,reg50,"spr_swy_hoth_turret"),
           # (val_add,reg50,1),
           # (try_for_range,":instance",0,reg50),
              # (scene_prop_get_instance,":thechosenturret", "spr_swy_hoth_turret", ":instance"),
              # (prop_instance_get_position,2,":thechosenturret"),
              # (get_distance_between_positions,":distance",1,2),
              # (lt,":distance",":dist"),
              # (assign,":dist",":distance"),

			  ##(key_is_down, "$crouch_key"),
			  # (neq|position_is_behind_position,pos1,pos2),
			# (prop_instance_get_position,pos1,":thechosenturret"),
			# (position_rotate_z,pos1,90),
			# (prop_instance_animate_to_position,":thechosenturret",pos1,2),
            # (end_try),


			(get_player_agent_no, ":player_agent"),
			(scene_prop_get_num_instances,":num_instances","spr_swy_hoth_turret_cannon"),
			(gt, ":num_instances", 0),
			(try_for_range, ":cur_i", 0, ":num_instances"),
				(scene_prop_get_instance,":instance", "spr_swy_hoth_turret_cannon", ":cur_i"),
				(prop_instance_get_position,pos1,":instance"),
				(agent_get_position, pos2, ":player_agent"),
				(get_distance_between_positions,":dist",pos1,pos2),
				#get health
				#(store_agent_hit_points,":player_agent_health",":player_agent",0),	#relative number, 0-100
				#(try_begin),
				(try_begin),
					#(eq, ":player_agent_health", 100),	#player is fully healed
					#(le, ":dist", 125),	#very close
					(le, ":dist", 425),	#very close
					(eq, "$mounted_turret", 0),
					(neq|position_is_behind_position,pos2,pos1),
					(game_key_is_down, gk_action),


					(agent_play_sound, ":player_agent", "snd_bacta_heal"),
					#(init_position,pos3),
					#(copy_position,pos2,pos3),
					#(agent_set_position, ":player_agent", pos1),
					(assign, "$mounted_turret", 1),
					(display_message, "@Mounted on Turret:"),
					##@(display_message, ":instance"),
				(else_try),
					#(le, ":dist", 425),	#very close
					(eq, "$mounted_turret", 1),
					(position_copy_rotation,pos2,pos1),
					(prop_instance_animate_to_position,":instance",pos1,100),

					        (position_move_z,pos1,260),
							(position_rotate_x,pos1,-5),
							(position_move_y,pos1,-1000),

							(mission_cam_animate_to_position, pos1,100,1),



					(game_key_is_down, gk_action),
					(agent_play_sound, ":player_agent", "snd_bacta_heal"),
					#(agent_set_position, ":player_agent", pos3),
					(mission_cam_set_target_agent, ":player_agent",1),
					(assign, "$mounted_turret", 0),
					(display_message, "@Dismounted of Turret:"),
					##@(display_message, ":instance"),
					#(display_message, "@You are not injured and do not need the Bacta Tank at this time."),
				#(else_try),
					#(lt, ":player_agent_health", 100),	#player is injured
					#(le, ":dist", 125),	#very close
					#(display_message, "@You are being healed by the Bacta Tank..."),
					#(val_add, ":player_agent_health", 10),	#add 10%
					#(try_begin),
						#(gt, ":player_agent_health", 100),
						#(assign, ":player_agent_health", 100),		#so we don't try and set hit points > 100%
					#(try_end),
					#(agent_set_hit_points,":player_agent",":player_agent_health",0),
					#(troop_set_health, "$g_player_troop", ":player_agent_health"),

				(else_try),
					(le, ":dist", 1300),	#in room
					(eq, "$mounted_turret", 0),
					#(display_message, "@Debug: Far of turret:"),
					#(display_message, ":dist"),
					(position_rotate_z,pos1,90),
					(prop_instance_animate_to_position,":instance",pos1,200),
				(try_end),
			(try_end),



	])

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Swyter Gate System Code - Vertical Single side kind.
common_gate_system = (1, 1, 0,
	[],
		[ 
        #@~ Original code		
		(try_begin),
		    (scene_prop_get_num_instances,":num_instances","spr_swy_gate.sys"),
			(gt, ":num_instances", 0),
				(try_for_range, ":cur_i", 0, ":num_instances"),  #-> Try for every door in the scene
					#(assign,":break_try",0),
					(troop_set_slot, "trp_gate_sys_counter", ":cur_i",0),
						(try_for_agents,":gate_sys_agent"), #-> Try for every guy in the scene
							#(eq,":break_try",0),
							(scene_prop_get_instance,":instance", "spr_swy_gate.sys", ":cur_i"),
							(prop_instance_get_position,pos1,":instance"),
							(agent_get_position, pos2, ":gate_sys_agent"),
							(get_distance_between_positions,":dist",pos1,pos2),
							
								(try_begin), # How many people it's soon to the door?
									(le, ":dist", 700), 
									(troop_get_slot,reg1,"trp_gate_sys_counter",":cur_i"),
									(val_add,reg1,1),
									(troop_set_slot, "trp_gate_sys_counter", ":cur_i",reg1),
								(try_end),
						(try_end),
							
						(try_begin),
							#(eq,":break_try",0),
							#(le, ":dist", 700), 
								
									(try_begin), #CLOSE DOOR -> Need to handle various ids
											#(eq,":break_try",0),
											#(le, ":dist", 700),	
											(troop_get_slot,reg1,"trp_gate_sys_counter",":cur_i"),
											(eq,reg1,0),
											
											(troop_get_slot,":is_open","trp_gate_sys_array",":cur_i"),
											(eq,":is_open",1),
											
											(agent_play_sound, ":gate_sys_agent", "snd_blast_door_close"),
											#(display_message, "@@SWY -> Door opened / {reg1}"),
										
											#(assign,":break_try",1),
											(troop_set_slot, "trp_gate_sys_array", ":cur_i",0), #used as save array: door[id]=0/1
											
											#@> We move the door...
											(position_move_z,pos1,-400),
											(prop_instance_animate_to_position,":instance",pos1,100),
									(try_end),
									(try_begin), #OPEN DOOR -> When a guy it's 0.7 meters far from the gate it will open
											(troop_get_slot,reg1,"trp_gate_sys_counter",":cur_i"),
											(gt,reg1,0),
											
											(troop_get_slot,":is_open","trp_gate_sys_array",":cur_i"),
											(neq|eq,":is_open",1),
											
											#(eq,":break_try",0),
											#(le, ":dist", 700), 
											#(troop_get_slot,":is_closed","trp_gate_sys_array",":cur_i"),
											#(eq,":is_closed",1),

											(agent_play_sound, ":gate_sys_agent", "snd_blast_door_open"),
											#(display_message, "@@SWY -> Door closed / {reg1}"),
											
											#(assign,":break_try",1),
											(troop_set_slot, "trp_gate_sys_array", ":cur_i",1), #used as save array: door[id]=0/1
											
											#@> We move the door...
											(position_move_z,pos1,400),
											(prop_instance_animate_to_position,":instance",pos1,100),
									(try_end),

						(try_end),
										
				(try_end),
		(try_end), #--> Original code end
		#@~ Death Star Blast Doors [deathstar_parts_1_door]
		(try_begin),
			(scene_prop_get_num_instances,":num_instances","spr_deathstar_parts_1_door"),
			(gt, ":num_instances", 0),
				(try_for_range, ":cur_i", 0, ":num_instances"),  #-> Try for every door in the scene
					(troop_set_slot, "trp_gate_sys_counter2", ":cur_i",0),
						(try_for_agents,":gate_sys_agent"), #-> Try for every guy in the scene
							(scene_prop_get_instance,":instance", "spr_deathstar_parts_1_door", ":cur_i"),
							(prop_instance_get_position,pos1,":instance"),
							(agent_get_position, pos2, ":gate_sys_agent"),
							(get_distance_between_positions,":dist",pos1,pos2),
							
								(try_begin), # How many people it's close to the door?
									(le, ":dist", 1000), 
									(troop_get_slot,reg1,"trp_gate_sys_counter2",":cur_i"),
									(val_add,reg1,1),
									(troop_set_slot, "trp_gate_sys_counter2", ":cur_i",reg1),
								(try_end),
						(try_end),
							
						(try_begin),
								
									(try_begin), #CLOSE DOOR -> Need to handle various ids

											(troop_get_slot,reg1,"trp_gate_sys_counter2",":cur_i"),
											(eq,reg1,0),
											
											(troop_get_slot,":is_open","trp_gate_sys_array2",":cur_i"),
											(eq,":is_open",1),
											
											(agent_play_sound, ":gate_sys_agent", "snd_blast_door_close"),
											(troop_set_slot, "trp_gate_sys_array2", ":cur_i",0), #used as save array: door[id]=0/1
											
											#@> We move the door...
											(position_move_x,pos1,400),
											(prop_instance_animate_to_position,":instance",pos1,200),
									(try_end),
									(try_begin), #OPEN DOOR -> When a guy it's 0.7 meters far from the gate it will open
											(troop_get_slot,reg1,"trp_gate_sys_counter2",":cur_i"),
											(gt,reg1,0),
											
											(troop_get_slot,":is_open","trp_gate_sys_array2",":cur_i"),
											(neq|eq,":is_open",1),

											(agent_play_sound, ":gate_sys_agent", "snd_blast_door_open"),
											(troop_set_slot, "trp_gate_sys_array2", ":cur_i",1), #used as save array: door[id]=0/1
											
											#@> We move the door...
											(position_move_x,pos1,-400),
											(prop_instance_animate_to_position,":instance",pos1,200),
									(try_end),
						(try_end),
										
				(try_end),
		(try_end), #--> Death Star Blast door end
	])


#holo_animate =(1.34567, 5, 0,
# 	[],
# [ 
# #my brand new movable holographic signs
# 	(scene_prop_get_num_instances,":num_instances","spr_swy_sign_arena"),
# 	(gt, ":num_instances", 0),
# 	(try_for_range, ":cur_i", 0, ":num_instances"),
# 		(scene_prop_get_instance,":instance", "spr_swy_sign_arena", ":cur_i"),
# 		(prop_instance_get_position,pos1,":instance"),
# 		(position_rotate_z,pos1,360),
# 		(prop_instance_animate_to_position,":instance",pos1,500),
# 	(try_end),
# #my brand new movable holographic signs
# 	(scene_prop_get_num_instances,":num_instances","spr_swy_sign_cantina"),
# 	(gt, ":num_instances", 0),
# 	(try_for_range, ":cur_i", 0, ":num_instances"),
# 		(scene_prop_get_instance,":instance", "spr_swy_sign_cantina", ":cur_i"),
# 		(prop_instance_get_position,pos1,":instance"),
# 		(position_rotate_z,pos1,360),
# 		(prop_instance_animate_to_position,":instance",pos1,500),
# 	(try_end),
# #my brand new movable holographic signs
# 	(scene_prop_get_num_instances,":num_instances","spr_swy_sign_shop"),
# 	(gt, ":num_instances", 0),
# 	(try_for_range, ":cur_i", 0, ":num_instances"),
# 		(scene_prop_get_instance,":instance", "spr_swy_sign_shop", ":cur_i"),
# 		(prop_instance_get_position,pos1,":instance"),
# 		(position_rotate_z,pos1,360),
# 		(prop_instance_animate_to_position,":instance",pos1,500),
# 	(try_end),
# ])
	
#--------------------------------------------------------------------------------------------------------------------------------------------------
common_crouch_button = (0, 0, 0,
	[
		(neg|conversation_screen_is_active),
		(get_player_agent_no, ":player_agent"),
		(agent_get_horse, ":horse", ":player_agent"),
		(eq, ":horse", -1),		#can only crouch if you aren't on a horse
		(this_or_next|key_is_down, "$crouch_key"),
		(eq, "$crouch_key_down", 1),		#crouch key was previously down ( 0 = up, 1 = down )
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		(try_begin),
			(key_is_down, "$crouch_key"),
			(eq, "$crouch_key_down", 0),
			#player just pressed crouch key, play an animation
			(agent_set_animation, ":player_agent", "anim_crouch"),	#play a crouch animation that loops
			(assign, "$crouch_key_down", 1),		#crouch key is down ( 0 = up, 1 = down )
		(else_try),
			(key_is_down, "$crouch_key"),
			(eq, "$crouch_key_down", 1),
			#player is still holding down the crouch key, do nothing unless they are trying to walk forward?
			#(game_key_is_down, gk_move_forward),
			#player is trying to move forward, set the animation
			#(agent_set_animation, ":player_agent", "anim_walk_forward_crouch"),	#play a walk forward crouch animation
		(else_try),
			(neg|key_is_down, "$crouch_key"),
			#player no longer has the crouch key down, play an animation to turn it off
			(agent_set_animation, ":player_agent", "anim_crouch_stop"),	#play a quick animation to turn it off
			(assign, "$crouch_key_down", 0),		#crouch key is up ( 0 = up, 1 = down )
		(try_end),

	])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - new helmet view
common_helmet_view = (0, 0, 0, [
	#(key_clicked, key_v),
	(key_clicked, "$helmet_view_key"),
	(neg|conversation_screen_is_active),
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),

		(try_begin),
			(le, "$helmet_view", 0),	#incase this variable isn't set yet
			(assign, "$helmet_view", 1),
			(start_presentation, "prsnt_helmet_view"),
		(else_try),
			(assign, "$helmet_view", 0),
		(try_end),
	])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - new zoom view
common_zoom_view = (0, 0, 0, [
		(game_key_is_down, gk_zoom),(neg|conversation_screen_is_active)
	],
	[
		#(display_message,"@zoom is down"),	#debug
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		#(display_message,"@player is alive"),	#debug

		#(try_begin),
		#	(le, "$zoom_view", 0),	#incase this variable isn't set yet
		#	(assign, "$zoom_view", 1),
			(start_presentation, "prsnt_zoom_view"),
			#(display_message,"@presentation started"),	#debug
		#(try_end),
	])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - fix_droid_walking
common_fix_droid_walking = (ti_on_agent_spawn, 0, 0, [],
	[
		(store_trigger_param_1, ":cur_agent"),
		(try_begin),
			(agent_is_alive,":cur_agent"),
			(agent_is_human,":cur_agent"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_blue"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_green"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_orange"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_purple"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_lin_droid_armor"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_lin_droid_armor_w_arm"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_mse6_armor"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_power_droid_grey"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_power_droid_snow"),
			(this_or_next|agent_has_item_equipped,":cur_agent","itm_power_droid_tan"),
			(agent_has_item_equipped,":cur_agent","itm_fxseries_droid_armor"),
			#(display_message, "@its a droid, setting agent to use anim_droid_walk_forward..."),
			(agent_set_walk_forward_animation, ":cur_agent", "anim_droid_walk_forward"),	#make these agents use a different walking animation, only works if they don't have a weapon equipped
		(try_end),
	])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - Super-Mario Stype Super Jump concept - http://forums.taleworlds.net/index.php/topic,65520.msg1703891.html
common_use_jetpack = (0, 0, 0, [
	#(key_clicked, key_j),
	(key_clicked, "$jetpack_key"),
	(neg|conversation_screen_is_active),
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		(try_begin),
			(this_or_next|player_has_item,"itm_jetpack"),
			(player_has_item,"itm_force_jump"),
			(agent_get_horse, ":player_horse", ":player_agent"),
			#(assign, reg7, ":player_horse"), #diagnostic only
            #(display_message, "@Player Horse = {reg7}"),#diagnostic only
			(try_begin),
				(eq, ":player_horse",-1),
				#run the animation
				(agent_set_animation, ":player_agent", "anim_jetpack"),
			(else_try),
				(display_message, "@Can't use while mounted!"),
			(try_end),
		(else_try),
			(display_message, "@You don't have a Jetpack or Force Jump in inventory!"),
		(try_end),

		# #(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
		# (troop_get_inventory_capacity, ":inv_cap", "$g_player_troop"),	#since custom commander is integrated
		# (assign, ":binocular_slot", -1),
		# (try_for_range, ":slot_no", 0, ":inv_cap"),
			# #(troop_get_inventory_slot,":item_id","trp_player",":slot_no"),
			# (troop_get_inventory_slot,":item_id","$g_player_troop",":slot_no"),	#since custom commander is integrated
			# #check for binoculars
			# (try_begin),
				# (eq, ":item_id", "itm_binocular"),
				# (assign, ":binocular_slot", ":slot_no"),
			# (try_end),
		# (try_end),

	])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - zoom in/out code by jik and WilliamBerne - http://forums.taleworlds.net/index.php/topic,68192.0.html - modified further by HokieBT
common_use_binocular_1 = (0, 0, 0, [
	#(key_clicked, key_b),
	(key_clicked, "$binoculars_key"),
	(neg|conversation_screen_is_active),
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		#(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
		(troop_get_inventory_capacity, ":inv_cap", "$g_player_troop"),	#since custom commander is integrated
		(assign, ":binocular_slot", -1),
		(try_for_range, ":slot_no", 0, ":inv_cap"),
			#(troop_get_inventory_slot,":item_id","trp_player",":slot_no"),
			(troop_get_inventory_slot,":item_id","$g_player_troop",":slot_no"),	#since custom commander is integrated
			#check for binoculars
			(try_begin),
				(eq, ":item_id", "itm_binocular"),
				(assign, ":binocular_slot", ":slot_no"),
			(try_end),
		(try_end),

		(try_begin),
			(eq, ":binocular_slot", -1),
			(display_message, "@You don't have any Macrobinoculars in your inventory!"),
		(else_try),

			(try_begin),
				(le, "$binocular_magnification", 0),	#incase this variable isn't set yet
				(assign, "$binocular_magnification", 2000),
				(display_message, "@Macrobinocular Zoom is 2x"),
			(else_try),
				(eq, "$binocular_magnification", 2000),
				(assign, "$binocular_magnification", 4000),
				(display_message, "@Macrobinocular Zoom is 4x"),
			(else_try),
				(eq, "$binocular_magnification", 4000),
				(assign, "$binocular_magnification", 6000),
				(display_message, "@Macrobinocular Zoom is 6x"),
			(else_try),
				(eq, "$binocular_magnification", 6000),
				(assign, "$binocular_magnification", 8000),
				(display_message, "@Macrobinocular Zoom is 8x"),
			(else_try),
				(eq, "$binocular_magnification", 8000),
				(assign, "$binocular_magnification", 0),
				(display_message, "@Macrobinocular Zoom is off"),
			(try_end),
			#change the zoom
			(try_begin),
				(le, "$binocular_magnification", 0),
				(mission_cam_clear_target_agent),
				(mission_cam_set_mode,0),
				(mission_cam_set_target_agent, ":player_agent", 1),
			(else_try),
				(mission_cam_clear_target_agent),
				(assign,":height",0),
				#get where the player is looking
				(agent_get_look_position, pos1, ":player_agent"),
				(position_move_y,pos1,"$binocular_magnification"),
				(position_get_z,":height",pos1),
				(try_begin),
					(lt,":height",50),
					(position_move_z,pos1,200),
				(try_end),
				(mission_cam_set_mode,1),
				(mission_cam_animate_to_position, pos1, 100, 0),		#the speed of the zoom-in
				(start_presentation, "prsnt_binocular_display"),
			(try_end),
		(try_end),
	])

common_use_binocular_2 = (
  0.1, 0, 0,
   [
		(try_begin),
			(gt, "$binocular_magnification", 0),
			(get_player_agent_no, ":player_agent"),
			(agent_is_alive, ":player_agent"),
			#(agent_set_animation, ":player_agent", "anim_unused_human_anim_1"),	#so the player doesn't move, must include module_animations at the top of the python file
			(agent_set_animation, ":player_agent", "anim_defend_fist"),	#so the player looks more like they are holding binoculars
			(agent_get_horse, ":player_horse", ":player_agent"),
			(try_begin),
				(ge, ":player_horse", 0),
				(agent_is_alive, ":player_horse"),	#so we don't try dead agents
				(agent_set_animation, ":player_horse", "anim_unused_horse_anim_1"),	#so the horse doesn't move, must include module_animations at the top of the python file
			(try_end),
			#(try_for_agents, ":cur_agent"),
			#	(agent_is_alive, ":cur_agent"),	#so we don't try dead agents
			#	(neg|agent_is_human,":cur_agent"),	#agent is a horse
			#	(agent_get_rider,":cur_rider", ":cur_agent"),
			#	(eq, ":cur_rider", ":player_agent"),	#rider of this horse is the player
			#	(agent_set_animation, ":cur_agent", "anim_unused_horse_anim_1"),	#so the horse doesn't move, must include module_animations at the top of the python file
			#(try_end),

			#fix the camera to follow the mouse movement
			#reset the camera (not sure all of these steps are necessary?)
			(mission_cam_clear_target_agent),
			(mission_cam_set_mode,0),
			(mission_cam_set_target_agent, ":player_agent", 1),
			#zoom in the camera (removed the height check so the camera wouldn't jump on the z-axis as the player moved the mouse around)
			(mission_cam_clear_target_agent),
			(agent_get_look_position, pos1, ":player_agent"),
			(position_move_y,pos1,"$binocular_magnification"),
			(mission_cam_set_mode,1),
			(mission_cam_animate_to_position, pos1, 1, 0),		#the speed of the zoom-in (really fast for the mouse movement camera, zero doesn't work)
			#(start_presentation, "prsnt_binocular_display"),	#not necessary

		(try_end),
    ],
   [
    ])
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#SW - new zoom view
common_speeder_attack = (0, 0, 0, [
		(key_clicked, key_e),(neg|conversation_screen_is_active)
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		(agent_get_horse, ":player_horse", ":player_agent"),
		(try_begin),
			(eq, ":player_horse",-1),	# player is on foot
		(else_try),
			 (try_for_range,reg5,1,500),
				(particle_system_burst, "psys_food_steam", pos1, 15),
				(position_move_y,pos1,10),
				(copy_position,pos2,pos1),
				(position_set_z_to_ground_level, pos2),
				(get_distance_between_positions,":dist",pos1,pos2),
				(lt,":dist",10),
				(play_sound,"snd_concussion_fire"),
				(try_for_agents,":agent"),
				   (agent_get_position,pos2,":agent"),
				   (get_distance_between_positions,":dist",pos1,pos2),
				   (lt,":dist",300),
				   (agent_set_hit_points,":agent",1,0),
				   #(agent_set_hit_points,":agent",0,1),
				   #(agent_deliver_damage_to_agent,":agent",":agent"),	#SW modified
				   (agent_deliver_damage_to_agent,":player_agent",":agent"),
				(end_try),
				(scene_prop_get_instance,":instance", "spr_explosion", 0),
				(position_copy_origin,pos2,pos1),
				(prop_instance_set_position,":instance",pos2),
				(position_move_z,pos2,1000),
				(prop_instance_animate_to_position,":instance",pos2,175),
				(assign,reg5,1000),
			  (end_try),
		(try_end),
	])

#---------------------------------------------------------------------------------------------------------------------------------------------------
sw_common_battle_kill_underwater = (
	# code concept from http://forums.taleworlds.net/index.php/topic,68852.0.html and http://forums.taleworlds.net/index.php/topic,58880.15.html
  5, 0, 1, [],	#one second refresh to allow sound time to complete
	[
		(try_for_agents,":agent"),
			(agent_is_alive,":agent"),
			(agent_get_position,pos1,":agent"),
			(position_get_z, ":pos_z", pos1),
			#(assign, reg1, ":pos_z"), #debug only
			#(display_message, "@agent z-position is {reg1}"),	#debug only
			(try_begin),
				(le, ":pos_z",-150),	#agent is about 6ft underwater
				(store_agent_hit_points,":hp",":agent",1),
				#(val_sub,":hp",7),
				(val_sub,":hp",10),
				(try_begin),
					(le, ":hp", 0),
					(agent_set_hit_points,":agent",0,0),
				(else_try),
					(agent_set_hit_points,":agent",":hp",1),
				(try_end),
				#(play_sound,"snd_man_grunt"),
				(agent_play_sound,":agent","snd_man_grunt"),
				(agent_deliver_damage_to_agent,":agent",":agent"),
			(try_end),
		(try_end),
	])

#SW - healthpack code by ConstantA - http://forums.taleworlds.net/index.php/topic,66181.msg1719939.html#msg1719939 - modified further by HokieBT
common_use_healthpack = (0, 0, 0, [
	#(key_clicked, key_h),
	(key_clicked, "$bacta_injector_key"),
	(neg|conversation_screen_is_active),
	],
	[
		(get_player_agent_no, ":player_agent"),
		(agent_is_alive, ":player_agent"),
		(store_agent_hit_points, ":player_hp", ":player_agent"),
		(try_begin),
			(lt, ":player_hp", 100),
			#(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
			(troop_get_inventory_capacity, ":inv_cap", "$g_player_troop"),	#since custom commander is integrated
			(assign, ":healing_item_injector_slot", -1),
			(assign, ":healing_item_capsule_slot", -1),
			(assign, reg1, 0),
			(try_for_range, ":slot_no", 0, ":inv_cap"),
				#(troop_get_inventory_slot,":item_id","trp_player",":slot_no"),
				(troop_get_inventory_slot,":item_id","$g_player_troop",":slot_no"),	#since custom commander is integrated
				(try_begin),
					(eq, ":item_id", "itm_bacta_injector"),
						(assign, ":healing_item_injector_slot", ":slot_no"),
				(else_try),
					(eq, ":item_id", "itm_bacta_capsule"),
						(assign, ":healing_item_capsule_slot", ":slot_no"),
						(val_add, reg1, 1),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":healing_item_injector_slot", -1),
					(display_message, "@You don't have a Bacta Injector in inventory!"),
			(else_try),
				(le, reg1, 0),
					(display_message, "@You don't have any Bacta Capsules in inventory!"),
			(else_try),
					(store_agent_hit_points, ":player_hp", ":player_agent", 1),
					(val_add, ":player_hp", 20), #hp to add
					(agent_set_hit_points, ":player_agent", ":player_hp", 1),
					#(troop_set_inventory_slot,"trp_player",":healing_item_capsule_slot", -1),
					(troop_set_inventory_slot,"$g_player_troop",":healing_item_capsule_slot", -1),	#since custom commander is integrated
					(val_sub, reg1,1),
					(agent_play_sound,":player_agent","snd_bacta_injector"),
					(display_message, "@You were healed for 20 hp and have {reg1} bacta capsules left."),
			(try_end),
		(else_try),
			(display_message, "@You are not hurt."),
		(try_end),
	])
#--------------------------------------------------------------------------------------------------------------------------

common_change_fog = (
  0, 0, ti_once,
  [
	#SW - set_fog_distance to a very high number to disable fog in scenes
	(try_begin),
		(eq, "$current_town","p_kamino"),
		(set_fog_distance, 170, 0xFF121118),
	(else_try),
		(eq, "$current_town","p_mustafar"),
		(set_fog_distance, 170, 0xFF272222),
	(else_try),
		(eq, "$current_town","p_corellia"),
		(set_fog_distance, 170, 0xFF654a2f),
	(else_try),
		(eq, "$current_town","p_felucia"),
		(set_fog_distance, 170, 0xFF92b595), 
	(else_try),
		(eq, "$current_town","p_raxusprime"),
		(set_fog_distance, 220, 0xFFBDAF86), 
	(else_try),
		(this_or_next|eq, "$current_town","p_tatooine"),
		(eq, "$current_town","p_ryloth"),
		(set_fog_distance, 170, 0xFF655436),
	(else_try),
		(eq, "$current_town","p_spacestation_4"), #Dagobah
		(set_fog_distance, 220, 0xFF222722),
	(else_try),
		(set_fog_distance, 100000000),
	(try_end),
    ], [])

tournament_triggers = [
  (ti_before_mission_start, 0, 0, [], [
										(call_script, "script_change_banners_and_chest"),
										(assign, "$g_arena_training_num_agents_spawned", 0),
										#SW - added script_change_rain
										(call_script, "script_change_rain", "$current_town"),
									   ]),

   #SW - added shield bash integration
   shield_bash_kit_1,
   shield_bash_kit_2,
   shield_bash_kit_3,
   shield_bash_kit_4,

   #SW - added common_battle_kill_underwater
   sw_common_battle_kill_underwater,

   #SW - added regen for certain agents
   #common_regeneration_store_info,
   #common_regeneration,

	#SW - add custom lightsaber noise
	#lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	lightsaber_noise_player,
	lightsaber_noise_agent,
	common_change_fog,
	#common_use_healthpack,		#not usable in tournaments
	##common_use_binocular_1,		#not usable in tournaments
	##common_use_binocular_2,		#not usable in tournaments
	#common_helmet_view,			#not usable in tournaments
	#common_zoom_view,			#not usable in tournaments
	#common_use_jetpack,	  		#not usable in tournaments
	#common_toggle_weapon_capabilities, #not usable in tournaments
	common_switch_sw_scene_props,
	common_crouch_button,



  (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
  (ti_tab_pressed, 0, 0, [],
   [(try_begin),
      (eq, "$g_mt_mode", abm_visit),
      (set_trigger_result, 1),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ]),
  (ti_question_answered, 0, 0, [],
   [(store_trigger_param_1,":answer"),
    (eq,":answer",0),
    (try_begin),
      (eq, "$g_mt_mode", abm_tournament),
      (call_script, "script_end_tournament_fight", 0),
    (else_try),
      (eq, "$g_mt_mode", abm_training),
      (get_player_agent_no, ":player_agent"),
      (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
    (try_end),
    (finish_mission,0),
    ]),

  (1, 0, ti_once, [], [
      (eq, "$g_mt_mode", abm_visit),
      (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (store_current_scene, reg(1)),
      (scene_set_slot, reg(1), slot_scene_visited, 1),
      (mission_enable_talk),
      (get_player_agent_no, ":player_agent"),
      (assign, ":team_set", 0),
      (try_for_agents, ":agent_no"),
        (neq, ":agent_no", ":player_agent"),
        (agent_get_troop_id, ":troop_id", ":agent_no"),
        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
        (eq, ":team_set", 0),
        (agent_set_team, ":agent_no", 1),
        (assign, ":team_set", 1),
      (try_end),
    ]),
##
##  (0, 0, 0, [],
##   [
##      #refresh hit points for arena visit trainers
##      (eq, "$g_mt_mode", abm_visit),
##      (get_player_agent_no, ":player_agent"),
##      (try_for_agents, ":agent_no"),
##        (neq, ":agent_no", ":player_agent"),
##        (agent_get_troop_id, ":troop_id", ":agent_no"),
##        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
##        (agent_set_hit_points, ":agent_no", 100),
##      (try_end),
##    ]),

##      (1, 4, ti_once, [(eq, "$g_mt_mode", abm_fight),
##                       (this_or_next|main_hero_fallen),
##                       (num_active_teams_le,1)],
##       [
##           (try_begin),
##             (num_active_teams_le,1),
##             (neg|main_hero_fallen),
##             (assign,"$arena_fight_won",1),
##             #Fight won, decrease odds
##             (assign, ":player_odds_sub", 0),
##             (try_begin),
##               (ge,"$arena_bet_amount",1),
##               (store_div, ":player_odds_sub", "$arena_win_amount", 2),
##             (try_end),
##             (party_get_slot, ":player_odds", "$g_encountered_party", slot_mainplanet_player_odds),
##             (val_add, ":player_odds_sub", 5),
##             (val_sub, ":player_odds", ":player_odds_sub"),
##             (val_max, ":player_odds", 250),
##             (party_set_slot, "$g_encountered_party", slot_mainplanet_player_odds, ":player_odds"),
##           (else_try),
##             #Fight lost, increase odds
##             (assign, ":player_odds_add", 0),
##             (try_begin),
##               (ge,"$arena_bet_amount",1),
##               (store_div, ":player_odds_add", "$arena_win_amount", 2),
##             (try_end),
##             (party_get_slot, ":player_odds", "$g_encountered_party", slot_mainplanet_player_odds),
##             (val_add, ":player_odds_add", 5),
##             (val_add, ":player_odds", ":player_odds_add"),
##             (val_min, ":player_odds", 4000),
##             (party_set_slot, "$g_encountered_party", slot_mainplanet_player_odds, ":player_odds"),
##           (try_end),
##           (store_remaining_team_no,"$arena_winner_team"),
##           (assign, "$g_mt_mode", abm_visit),
##           (party_get_slot, ":arena_mission_template", "$current_town", slot_mainplanet_arena_template),
##           (set_jump_mission, ":arena_mission_template"),
##           (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
##           (modify_visitors_at_site, ":arena_scene"),
##           (reset_visitors),
##           (set_visitor, 35, "trp_veteran_fighter"),
##           (set_visitor, 36, "trp_hired_blade"),
##           (set_jump_entry, 50),
##           (jump_to_scene, ":arena_scene"),
##           ]),

  (0, 0, ti_once, [],
   [
     (eq, "$g_mt_mode", abm_tournament),
     (play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
     ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   (this_or_next|main_hero_fallen),
                   (num_active_teams_le, 1)],
   [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_end_tournament_fight", 1),
         (call_script, "script_play_victorious_sound"),
         (finish_mission),
       (else_try),
         (call_script, "script_end_tournament_fight", 0),
         (finish_mission),
       (try_end),
       ]),

  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),(start_presentation, "prsnt_arena_training")]),
  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),
                       #(assign, "$g_arena_training_max_opponents", 40),
					   (assign, "$g_arena_training_max_opponents", 50),		#SW - increased the number of arena opponents
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_training),
                   (store_mission_timer_a, ":cur_time"),
                   (gt, ":cur_time", 3),
                   (assign, ":win_cond", 0),
                   (try_begin),
                     (ge, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),#spawn at most X agents
                     (num_active_teams_le, 1),
                     (assign, ":win_cond", 1),
                   (try_end),
                   (this_or_next|eq, ":win_cond", 1),
                   (main_hero_fallen)],
   [
       (get_player_agent_no, ":player_agent"),
       (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
       (assign, "$g_arena_training_won", 0),
       (try_begin),
         (neg|main_hero_fallen),
         (assign, "$g_arena_training_won", 1),#use this for conversation
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_veteran_fighter"),
	   #SW - modified set_visitor
	   (set_visitor, 36, "trp_champion_fighter"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
       ]),


  #SW - this appears to be the refresh that spawns the arena fighters
  (0.2, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       #(lt, ":num_active_fighters", 7),
	   (lt, ":num_active_fighters", 9),		#SW - increase the number of fighters in arena at one time
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 6),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       (val_mod, ":added_troop_sequence", 6),
       (val_add, ":added_troop", ":added_troop_sequence"),
       (val_min, ":added_troop", 9),
       (val_add, ":added_troop", "trp_arena_training_fighter_1"),
       (assign, ":end_cond", 10000),
       (get_player_agent_no, ":player_agent"),
       (agent_get_position, pos5, ":player_agent"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 32, 40),
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 1200), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),

		#SW - added script_set_items_for_arena so we can toggle what weapons are used
		(call_script, "script_set_items_for_arena", ":random_entry_point",":added_troop"),

       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
	   #SW - modified how quickly agents spawn
       #(store_add, "$g_arena_training_next_spawn_time", ":cur_time", 14),
       #(store_div, ":time_reduction", ":new_spawned_count", 3),
       #(val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
	   (try_begin),
			(le, ":new_spawned_count", 10),
			(store_add, "$g_arena_training_next_spawn_time", ":cur_time", 15),
		(else_try),
			(le, ":new_spawned_count", 30),
			(store_add, "$g_arena_training_next_spawn_time", ":cur_time", 10),
		(else_try),
			(store_add, "$g_arena_training_next_spawn_time", ":cur_time", 5),
		(try_end),


       ]),

  (0, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training)
       ],
    [
       (assign, ":max_teams", 6),
       (val_max, ":max_teams", 1),
       (get_player_agent_no, ":player_agent"),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_slot_eq, ":agent_no", slot_agent_arena_team_set, 0),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (try_begin),
           (eq, ":agent_no", ":player_agent"),
           (agent_set_team, ":agent_no", 6), #player is always team 6.
         (else_try),
           (store_random_in_range, ":selected_team", 0, ":max_teams"),
          # find strongest team
           (try_for_range, ":t", 0, 6),
             (troop_set_slot, "trp_temp_array_a", ":t", 0),
           (try_end),
           (try_for_agents, ":other_agent_no"),
             (agent_is_human, ":other_agent_no"),
             (agent_is_alive, ":other_agent_no"),
             (neq, ":agent_no", ":player_agent"),
             (agent_slot_eq, ":other_agent_no", slot_agent_arena_team_set, 1),
             (agent_get_team, ":other_agent_team", ":other_agent_no"),
             (troop_get_slot, ":count", "trp_temp_array_a", ":other_agent_team"),
             (val_add, ":count", 1),
             (troop_set_slot, "trp_temp_array_a", ":other_agent_team", ":count"),
           (try_end),
           (assign, ":strongest_team", 0),
           (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", 0),
           (try_for_range, ":t", 1, 6),
             (troop_slot_ge, "trp_temp_array_a", ":t", ":strongest_team_count"),
             (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", ":t"),
             (assign, ":strongest_team", ":t"),
           (try_end),
           (store_random_in_range, ":rand", 5, 100),
           (try_begin),
             (lt, ":rand", "$g_arena_training_num_agents_spawned"),
             (assign, ":selected_team", ":strongest_team"),
           (try_end),
           (agent_set_team, ":agent_no", ":selected_team"),
         (try_end),
         (agent_set_slot, ":agent_no", slot_agent_arena_team_set, 1),
         (try_begin),
           (neq, ":agent_no", ":player_agent"),
           (val_add, "$g_arena_training_num_agents_spawned", 1),
         (try_end),
       (try_end),
       ]),

  ]

mission_templates = [
  (
    "town_default",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),(9,mtef_scene_source,af_override_horse,0,1,[]),(10,mtef_scene_source,af_override_horse,0,1,[]),(11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),(24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
###>> Motomataru's AI
#AI_triggers,
    [


      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (try_begin),
            (eq, "$sneaked_into_town", 1),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
          (else_try),
            (eq, "$talk_context", tc_tavern_talk),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
          (else_try),
			#SW - attempting to fix bug with mtf_sit_town (nevermind, the town_default mission template seems to be used for a lot of random scenes?)
            (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
			#(call_script, "script_music_set_situation_with_culture", mtf_sit_town),
          (try_end),

        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      #SW - from blackjack mod
	  #(ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      #(ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_inventory_key_pressed, 0, 0, [
          (eq, "$black_jack",0),#plus blackjack
          (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [
          (eq, "$black_jack",0),#plus blackjack
          (set_trigger_result,1)], []),

	  #SW - add custom lightsaber noise to town scenes
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  #lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_switch_sw_scene_props,
	  common_crouch_button,

	#SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
    ],
  ),

# This template is used in party encounters and such.
#
  (
    "conversation_encounter",0,-1,
    "Conversation_encounter",
#SW - modified conversation_encounter so you can see the helmet by removing af_override_fullhelm ?
    [( 0,mtef_visitor_source,0,0,1,[]),( 1,mtef_visitor_source,0,0,1,[]),
     ( 2,mtef_visitor_source,0,0,1,[]),( 3,mtef_visitor_source,0,0,1,[]),( 4,mtef_visitor_source,0,0,1,[]),( 5,mtef_visitor_source,0,0,1,[]),( 6,mtef_visitor_source,0,0,1,[]),
     ( 7,mtef_visitor_source,0,0,1,[]),( 8,mtef_visitor_source,0,0,1,[]),( 9,mtef_visitor_source,0,0,1,[]),(10,mtef_visitor_source,0,0,1,[]),(11,mtef_visitor_source,0,0,1,[]),
    #prisoners now...
     (12,mtef_visitor_source,0,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),(16,mtef_visitor_source,0,0,1,[]),
    #Other party
     (17,mtef_visitor_source,0,0,1,[]),(18,mtef_visitor_source,0,0,1,[]),(19,mtef_visitor_source,0,0,1,[]),(20,mtef_visitor_source,0,0,1,[]),(21,mtef_visitor_source,0,0,1,[]),
     (22,mtef_visitor_source,0,0,1,[]),(23,mtef_visitor_source,0,0,1,[]),(24,mtef_visitor_source,0,0,1,[]),(25,mtef_visitor_source,0,0,1,[]),(26,mtef_visitor_source,0,0,1,[]),
     (27,mtef_visitor_source,0,0,1,[]),(28,mtef_visitor_source,0,0,1,[]),(29,mtef_visitor_source,0,0,1,[]),(30,mtef_visitor_source,0,0,1,[]),(31,mtef_visitor_source,0,0,1,[]),
     ],
    [

		  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),

	],
  ),

#----------------------------------------------------------------
#mission templates before this point are hardwired into the game.
#-----------------------------------------------------------------

################################################################################################################
#SW - new cantina_default  mission template, do not put higher since those are hard coded in the game
  (
    "cantina_default",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),(9,mtef_scene_source,af_override_horse,0,1,[]),(10,mtef_scene_source,af_override_horse,0,1,[]),(11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),(24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
	 (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
	 #SW - new cantina_drinkers
	 (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
 ###>> Motomataru's AI
#AI_triggers,
    [

      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
		  #start the cantina_ambiance
		  (play_sound, "snd_cantina_ambiance", sf_looping),
		  #set the music
          (try_begin),
            (eq, "$sneaked_into_town", 1),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
          (else_try),
            (eq, "$talk_context", tc_tavern_talk),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
          (else_try),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
          (try_end),
        ]),

	# #tavern brawl
	# (0, 0, ti_once,[
					# (get_player_agent_no, ":player_agent"),
					# (try_for_agents, ":cur_agent"),
						# #(agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
						# #(eq, ":cur_agent_troop", "$g_assassin"),
						# (neq, ":cur_agent", ":player_agent"),
						# (agent_set_team, ":cur_agent", 1),	# maybe it is possible to also give them the aif_start_alarmed flag?
					# (try_end),
					# ],[]),

      (ti_before_mission_start, 0, 0, [], 	[
											(assign, "$tavern_brawl", 0),	#tavern brawl is deactivated
											(call_script, "script_change_banners_and_chest")
											]),
      #SW - from blackjack mod
	  #(ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      #(ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_inventory_key_pressed, 0, 0, [
          (eq, "$black_jack",0),#plus blackjack
          (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [
          (eq, "$black_jack",0),#plus blackjack
		  (call_script, "script_flush_gatesys_cache"),
          (set_trigger_result,1)], []),

		(1, 0, ti_once,[],
			[
			(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
			(assign, "$g_init_fight", 1),
			]
		),

		# #set seated animation for agents
		# (30, 0, 0, [], [
		#(2, 0, ti_once, [], [
		(0, 0, ti_once, [], [

			(eq, "$tavern_brawl", 0),	#only set animations when not in a brawl
			(get_player_agent_no, ":player_agent"),
			(try_begin),
				(scene_prop_get_num_instances,":num_instances","spr_sw_chair_a_no_collision"),
				(gt, ":num_instances", 0),
				(try_for_range, ":cur_i", 0, ":num_instances"),
					(scene_prop_get_instance,":instance", "spr_sw_chair_a_no_collision", ":cur_i"),
					(prop_instance_get_position,pos1,":instance"),
					(try_for_agents, ":agent"),
						(neq, ":agent", ":player_agent",),
						(agent_get_position,pos2,":agent"),
						(get_distance_between_positions,":dist",pos1,pos2),
						(try_begin),
							(le, ":dist", 75),	#sitting
							#(store_random_in_range, ":random_num", 0, 100),
							(try_begin),
								(agent_has_item_equipped, ":agent", "itm_grey_gloves_with_bottle"),		#bottle is equipped, make them drink
								#(le, ":random_num", 25),
								#(agent_set_animation, ":agent", "anim_drinking"),
								#(agent_set_animation, ":agent", "anim_sitting"),
								(agent_set_stand_animation, ":agent", "anim_drinking"),
								(agent_set_animation, ":agent", "anim_drinking"),
								(store_random_in_range, ":random_no", 0, 100),
								(agent_set_animation_progress, ":agent", ":random_no"),
							(else_try),
								#(agent_set_animation, ":agent", "anim_sitting"),
								(agent_set_stand_animation, ":agent", "anim_sitting"),
								(agent_set_animation, ":agent", "anim_sitting"),
								(store_random_in_range, ":random_no", 0, 100),
								(agent_set_animation_progress, ":agent", ":random_no"),
							(try_end),
						(try_end),
					(try_end),
				(try_end),
			(try_end),
		]),

		#set seated animation for agents
		# (0, 0, ti_once, [], [

			# (eq, "$tavern_brawl", 0),	#only set animations when not in a brawl
			# (get_player_agent_no, ":player_agent"),
			# (try_begin),
				# (scene_prop_get_num_instances,":num_instances","spr_sw_chair_a_no_collision"),
				# (gt, ":num_instances", 0),
				# (try_for_range, ":cur_i", 0, ":num_instances"),
					# (scene_prop_get_instance,":instance", "spr_sw_chair_a_no_collision", ":cur_i"),
					# (prop_instance_get_position,pos1,":instance"),
					# (try_for_agents, ":agent"),
						# (neq, ":agent", ":player_agent",),
						# (agent_get_position,pos2,":agent"),
						# (get_distance_between_positions,":dist",pos1,pos2),
						# (try_begin),
							# (le, ":dist", 75),	#sitting
							# #(agent_set_stand_animation, ":agent", "anim_sitting"),
							# #(agent_set_stand_animation, ":agent", "anim_sitting"),
							# (agent_set_stand_animation, ":agent", "anim_sit_cantina_agent"),
							# #move them to the proper spot (nevermind, moving on the z position doesn't work)
							# #(agent_get_position, pos2, ":agent"),	#get the agent's position
							# #(position_move_x, pos2, 100),
							# #(position_move_y, pos2, 100),
							# #(position_move_z, pos2, 200),	#blah, doesn't work for agents...
							# #(agent_set_position, ":agent", pos2),
						# (try_end),
					# (try_end),
				# (try_end),
			# (try_end),
		# ]),

#random scene encounters
	# commented out tavern attack since there isn't an AI mesh and since the cantina_walkers don't move the assassin will spawn on top of somebody
	#(0, 0, ti_once,[(call_script, "script_cf_setup_random_scene_encounter",1,20)],[]),
#End random scene encounters

			#SW - commented out since cantina noise will now be 'music'
      # (0, 0, ti_once, [],
		# [
			# (try_begin),
			  # (eq, "$talk_context", tc_tavern_talk),
				# (stop_all_sounds, 2),
				# #(play_sound, "snd_cantina_ambience", sf_looping),
				# (play_sound, "snd_cantina_ambience"),
			# (try_end),
		# ]
	  # ),

	  common_check_town_fight,

	  #SW - add custom lightsaber noise to town scenes
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  #lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_switch_sw_scene_props,
	  common_crouch_button,
	  common_gate_system,

	 #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),

    ],
  ),
################################################################################################################

  (
    "town_center",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),

     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
#     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
#     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
#     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(31,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),
     (32,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(33,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(34,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(35,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(36,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(37,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(38,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(39,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

	 #SW - new entry point for player's companion - seems like you need to play for a few minutes before you can set_visitors?
	 #new entry points for player companions (when player uses entry point 0, no horse)
	 (48,mtef_visitor_source,af_override_horse,0,1,[]),
	 #new entry points for player companions (when player uses entry point 1, with horse)
	 (49,mtef_visitor_source,0,0,1,[]),

     ],

	 ###>> Motomataru's AI
#AI_triggers,
    [
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
         ]),


        (0.7, 0, ti_once, [],
         [
           (try_begin),
             (eq, "$g_mt_mode", tcm_default),
             (store_current_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
           (try_end),
           (call_script, "script_init_town_walker_agents"),
           (try_begin),
             (eq, "$sneaked_into_town", 1),
             (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
           (else_try),
		     #SW - modified town_center situation/culture
             #(call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
			 #(music_set_situation, 0),
			 (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
			 (music_set_culture, 0),
           

			#------------------------------------------------------------------------------------------------------------------------------------------------------
			#set music depending on the location
			#SW - attempting to add town specific music (this concept doesn't seem to work at all?  I had to add that persist until finished flag...)
			(try_begin),
				(this_or_next|eq, "$current_town", "p_endor"),		#Endor
				(eq, "$current_town", "p_dantooine"),		#Dantooine
				(play_track, "track_town_endor", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
			(else_try),
				(this_or_next|eq, "$current_town", "p_gamorr"),		#Gamorr
				(this_or_next|eq, "$current_town", "p_kashyyyk"),		#Kashyyyk
				(eq, "$current_town", "p_nalhutta"),		#Nal_Hutta
				(play_track, "track_town_wookiee", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
			(else_try),
				(this_or_next|eq, "$current_town", "p_tatooine"),		#Tatooine
				(eq, "$current_town", "p_ryloth"),		#Ryloth
				(play_track, "track_town_desert", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
				#(play_track, "track_town_test", 2),		# 0 = default, 1 = fade out current track, 2 = stop current track
			(try_end),
			#------------------------------------------------------------------------------------------------------------------------------------------------------

			(try_end),
		 ]),

        (ti_before_mission_start, 0, 0, [],
			[
				(call_script, "script_change_banners_and_chest"),
				#SW - added script_change_rain
				(call_script, "script_change_rain", "$current_town"),
			]),
        (ti_inventory_key_pressed, 0, 0,
         [
           (try_begin),
             (this_or_next|eq, "$g_mt_mode", tcm_default),
			 (eq, "$g_init_fight", 0),
             (set_trigger_result,1),
           (else_try),
             (eq, "$g_mt_mode", tcm_disguised),
             (display_message,"str_cant_use_inventory_disguised"),
           (else_try),
             (display_message, "str_cant_use_inventory_now"),
           (try_end),
           ], []),
        (ti_tab_pressed, 0, 0,
         [
           (try_begin),
             (this_or_next|eq, "$g_mt_mode", tcm_default),
             (this_or_next|eq, "$g_mt_mode", tcm_disguised),
			 (eq, "$g_init_fight", 0),
			 (call_script, "script_flush_gatesys_cache"),
             (set_trigger_result,1),
           (else_try),
             (display_message, "@Cannot leave now."),
           (try_end),
           ], []),
        (ti_on_leave_area, 0, 0,
         [
            (try_begin),
              (eq, "$g_defending_against_siege", 0),
              (assign,"$g_leave_town",1),
            (try_end),
            ], []),

	# #SW - trigger to have companion follow player around the scene (code by Highlander of 1866 mod) - nevermind, I'm going to try team_give_order
    # (1,0,0,[],
		# [
		   # (get_player_agent_no,":player_agent"),
		   # (assign,":cur_agent",-1),
		   # (try_for_agents,":agent"),
		     # (agent_get_entry_no,":entry_no",":agent"),
		     # (this_or_next|eq,":entry_no",48),
		     # (eq,":entry_no",49),
		     # (assign,":cur_agent",":agent"),
		   # (try_end),
		   # (gt,":cur_agent",0),
		   # (agent_get_position,pos1,":player_agent"),
		   # (agent_get_position,pos2,":cur_agent"),
		   # (get_distance_between_positions,":distance",pos1,pos2),
		   # (gt,":distance",500),
		   # (assign,":lowest_distance",99999),
		   # (assign,":cur_degrees",0),
		   # (try_for_range,":degrees",0,36),
		     # (copy_position,pos3,pos1),
		     # (val_mul,":degrees",10),
		     # (position_rotate_z,pos3,":degrees"),
		     # (position_move_y,pos3,400),
		     # (get_distance_between_positions,":distance",pos1,pos3),
		     # (lt,":distance",":lowest_distance"),
		     # (assign,":cur_degrees",":degrees"),
		   # (try_end),
		   # (copy_position,pos3,pos1),
		   # (position_rotate_z,pos3,":cur_degrees"),
		   # (position_move_y,pos3,200),
		   # (agent_set_scripted_destination,":cur_agent",pos3,1),
		# ]),

    (1.2,0,ti_once,[],
		[
			(set_show_messages, 0),		#0 disables window messages 1 re-enables them.
			(team_give_order, 0, grc_everyone, mordr_follow),		#so your companions follow you
			(set_show_messages, 1),		#0 disables window messages 1 re-enables them.
		]),


#random scene encounters
	#(0, 0, ti_once,[(call_script, "script_cf_setup_random_scene_encounter",0,40)],[]),
	(1.5, 0, ti_once,[
					(assign, "$g_init_fight", 0),
					(try_begin),
						(eq, "$g_mt_mode", tcm_default),	#default town visit, setup a random battle or allow the player to start a fight

						(store_random_in_range, ":random", 1, 101),
						(try_begin),
							(le, ":random", 50),	#give assassin first priority over random scene battle
							#assassins code first
							(store_random_in_range, ":random", 1, 101),
							(try_begin),
								(le, ":random", "$random_scene_assassination"),	#start a random assassination
								(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
								(call_script, "script_cf_setup_random_scene_assassination",0),		#sets assassin to team 1
								#(dialog_box, "@An informant warns you that an assassin has been spotted in the area!", "@Warning"),	# display dialog popup ?
								(assign, "$g_init_fight", 1),				#so we don't check if the player killed a friendly troop
							(else_try),
								(le, ":random", "$random_scene_battles"),	#start a random battle
								(call_script, "script_init_town_fight"),	#sets everybody to team 0
								(assign, "$g_init_fight", 2),				#so we don't check if the player killed a friendly troop
								(call_script, "script_cf_setup_random_scene_encounter",0),		#sets some enemies to team 1
								(dialog_box, "@As you land your ship you notice that this area is under attack!", "@Alert"),	# display dialog popup ?
								(assign, "$g_started_battle_random_by_enemy_faction", 1),

								#play a specific music track for the start of the fight
								(play_track, "track_town_battle", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track

								#switch the music situtation after the fight track finishes
								(call_script, "script_music_set_situation_with_culture", mtf_sit_fight),

							(else_try),
								(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
								(assign, "$g_init_fight", 1),
							(try_end),
						(else_try),
							#give scene battle first priority over random assassin
							(store_random_in_range, ":random", 1, 101),
							(try_begin),
								(le, ":random", "$random_scene_battles"),	#start a random battle
								(call_script, "script_init_town_fight"),	#sets everybody to team 0
								(assign, "$g_init_fight", 2),				#so we don't check if the player killed a friendly troop
								(call_script, "script_cf_setup_random_scene_encounter",0),		#sets some enemies to team 1
								(dialog_box, "@As you land your ship you notice that this area is under attack!", "@Alert"),	# display dialog popup ?
								(assign, "$g_started_battle_random_by_enemy_faction", 1),
								#play a specific music track for the start of the fight
								(play_track, "track_town_battle", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track

								#switch the music situtation after the fight track finishes
								(call_script, "script_music_set_situation_with_culture", mtf_sit_fight),

							(else_try),
								(le, ":random", "$random_scene_assassination"),	#start a random assassination
								(call_script, "script_init_town_fight"),	#sets everybody to team 0
								(call_script, "script_cf_setup_random_scene_assassination",0),		#sets assassin to team 1
								#(dialog_box, "@An informant warns you that an assassin has been spotted in the area!", "@Warning"),	# display dialog popup ?
								(assign, "$g_init_fight", 1),				#so we don't check if the player killed a friendly troop
							(else_try),
								(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
								(assign, "$g_init_fight", 1),
							(try_end),
						(try_end),
					(else_try),
						(eq, "$g_mt_mode", tcm_disguised),	#disguised town visit, allow the player to start a fight
						(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
						(assign, "$g_init_fight", 1),
					(try_end),
					],[]),
#End random scene encounters

		common_check_town_fight,

        (0.1, 0, ti_once, [], [(party_slot_eq, "$current_town", slot_party_type, spt_mainplanet),
                             (call_script, "script_town_init_doors", 0),
                             (try_begin),
                               (eq, "$town_nighttime", 0),
                               (play_sound, "snd_town_ambiance", sf_looping),
                             (try_end),
                             ]),
        (3, 0, 0, [(call_script, "script_tick_town_walkers")], []),
        (2, 0, 0, [(call_script, "script_center_ambiance_sounds")], []),

		#SW - added shield bash integration
		shield_bash_kit_1,
		shield_bash_kit_2,
		shield_bash_kit_3,
		shield_bash_kit_4,

	    #SW - add custom lightsaber noise to town scenes
	    #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	    lightsaber_noise_player,
	    #lightsaber_noise_agent,
		common_change_fog,
		common_use_healthpack,
		#common_use_binocular_1,
		#common_use_binocular_2,
		common_helmet_view,
		#common_player_damage,
		common_zoom_view,
		common_use_jetpack,
		common_fix_droid_walking,
		common_toggle_weapon_capabilities,
		#warcry_player,
		common_speeder_trigger_1,
		common_speeder_trigger_2,
		common_switch_sw_scene_props,
		common_crouch_button,
		#common_turret, -> unstable
		common_gate_system,
		#holo_animate,
      ],
    ),

  (
    "minorplanet_center",0,-1,
    "center",
    [(0,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),

     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (call_script, "script_init_town_walker_agents"),
		  #SW - attempting to fix bug with mtf_sit_town
          #(call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
		  (call_script, "script_music_set_situation_with_culture", mtf_sit_town),

        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_hunt_down_fugitive"),
                                (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                                (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                                (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                                  (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
                                (try_end),
                              (try_end),
							  (call_script, "script_flush_gatesys_cache"),
                              (set_trigger_result,1)], []),
      (ti_on_leave_area, 0, 0, [
          (try_begin),
            (assign,"$g_leave_town",1),
          (try_end),
          ], []),
      (3, 0, 0, [(call_script, "script_tick_town_walkers")], []),
      (2, 0, 0, [(call_script, "script_center_ambiance_sounds")], []),

	  #SW - allow player to start a fight
	  (1, 0, ti_once, [
						(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
						(assign, "$g_init_fight", 1),
					  ], []),


      (1, 0, ti_once, [(check_quest_active, "qst_hunt_down_fugitive"),
                       (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                       (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
          (finish_mission, 4),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$current_town", -2),
          (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
        (try_end),
        ]),

		#SW - Bounty Hunting Start - http://forums.taleworlds.com/index.php/topic,59300.0.html
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_bounty_1"),
                                (neg|check_quest_succeeded, "qst_bounty_1"),
                                (neg|check_quest_failed, "qst_bounty_1"),
                                (quest_slot_eq, "qst_bounty_1", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_1"),
                                  (call_script, "script_fail_quest", "qst_bounty_1"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_bounty_1"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_bounty_2"),
                                (neg|check_quest_succeeded, "qst_bounty_2"),
                                (neg|check_quest_failed, "qst_bounty_2"),
                                (quest_slot_eq, "qst_bounty_2", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_2"),
                                  (call_script, "script_fail_quest", "qst_bounty_2"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_bounty_2"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_bounty_3"),
                                (neg|check_quest_succeeded, "qst_bounty_3"),
                                (neg|check_quest_failed, "qst_bounty_3"),
                                (quest_slot_eq, "qst_bounty_3", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_3"),
                                  (call_script, "script_fail_quest", "qst_bounty_3"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_bounty_3"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_bounty_4"),
                                (neg|check_quest_succeeded, "qst_bounty_4"),
                                (neg|check_quest_failed, "qst_bounty_4"),
                                (quest_slot_eq, "qst_bounty_4", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_4"),
                                  (call_script, "script_fail_quest", "qst_bounty_4"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_bounty_4"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_bounty_5"),
                                (neg|check_quest_succeeded, "qst_bounty_5"),
                                (neg|check_quest_failed, "qst_bounty_5"),
                                (quest_slot_eq, "qst_bounty_5", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_5"),
                                  (call_script, "script_fail_quest", "qst_bounty_5"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_bounty_5"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_bounty_6"),
                                (neg|check_quest_succeeded, "qst_bounty_6"),
                                (neg|check_quest_failed, "qst_bounty_6"),
                                (quest_slot_eq, "qst_bounty_6", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_6"),
                                  (call_script, "script_fail_quest", "qst_bounty_6"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_bounty_6"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),

      (1, 0, ti_once, [(check_quest_active, "qst_bounty_1"),
                       (neg|check_quest_succeeded, "qst_bounty_1"),
                       (neg|check_quest_failed, "qst_bounty_1"),
                       (quest_slot_eq, "qst_bounty_1", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),

					   	#(assign, reg1, "$bounty_target_1"), #debug only
						#(display_message, "@bounty_target_1 = {reg1}"),	#debug only

                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_1"),
						 #3(display_message, "@agent is alive!"),
                       (else_try),
                         (assign, ":not_alive", 1),
						 #3(display_message, "@agent is NOT alive!"),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_bounty_1"),
          (finish_mission, 4),
        (else_try),
          #(call_script, "script_change_player_relation_with_center", "$current_town", -2),		#SW - commented out relation hit
          (call_script, "script_succeed_quest", "qst_bounty_1"),
        (try_end),
        ]),
      (1, 0, ti_once, [(check_quest_active, "qst_bounty_2"),
                       (neg|check_quest_succeeded, "qst_bounty_2"),
                       (neg|check_quest_failed, "qst_bounty_2"),
                       (quest_slot_eq, "qst_bounty_2", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_2"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_bounty_2"),
          (finish_mission, 4),
        (else_try),
          #(call_script, "script_change_player_relation_with_center", "$current_town", -2),		#SW - commented out relation hit
          (call_script, "script_succeed_quest", "qst_bounty_2"),
        (try_end),
        ]),
      (1, 0, ti_once, [(check_quest_active, "qst_bounty_3"),
                       (neg|check_quest_succeeded, "qst_bounty_3"),
                       (neg|check_quest_failed, "qst_bounty_3"),
                       (quest_slot_eq, "qst_bounty_3", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_3"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_bounty_3"),
          (finish_mission, 4),
        (else_try),
          #(call_script, "script_change_player_relation_with_center", "$current_town", -2),		#SW - commented out relation hit
          (call_script, "script_succeed_quest", "qst_bounty_3"),
        (try_end),
        ]),
      (1, 0, ti_once, [(check_quest_active, "qst_bounty_4"),
                       (neg|check_quest_succeeded, "qst_bounty_4"),
                       (neg|check_quest_failed, "qst_bounty_4"),
                       (quest_slot_eq, "qst_bounty_4", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_4"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_bounty_4"),
          (finish_mission, 4),
        (else_try),
          #(call_script, "script_change_player_relation_with_center", "$current_town", -2),		#SW - commented out relation hit
          (call_script, "script_succeed_quest", "qst_bounty_4"),
        (try_end),
        ]),
      (1, 0, ti_once, [(check_quest_active, "qst_bounty_5"),
                       (neg|check_quest_succeeded, "qst_bounty_5"),
                       (neg|check_quest_failed, "qst_bounty_5"),
                       (quest_slot_eq, "qst_bounty_5", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_5"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_bounty_5"),
          (finish_mission, 4),
        (else_try),
          #(call_script, "script_change_player_relation_with_center", "$current_town", -2),		#SW - commented out relation hit
          (call_script, "script_succeed_quest", "qst_bounty_5"),
        (try_end),
        ]),
      (1, 0, ti_once, [(check_quest_active, "qst_bounty_6"),
                       (neg|check_quest_succeeded, "qst_bounty_6"),
                       (neg|check_quest_failed, "qst_bounty_6"),
                       (quest_slot_eq, "qst_bounty_6", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "$bounty_target_6"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_minorplanet_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_bounty_6"),
          (finish_mission, 4),
        (else_try),
          #(call_script, "script_change_player_relation_with_center", "$current_town", -2),		#SW - commented out relation hit
          (call_script, "script_succeed_quest", "qst_bounty_6"),
        (try_end),
        ]),
		#SW - Bounty Hunting End

		#SW - added shield bash integration
		shield_bash_kit_1,
		shield_bash_kit_2,
		shield_bash_kit_3,
		shield_bash_kit_4,

		#SW - added the ability to start a fight
		common_check_town_fight,

	    #SW - add custom lightsaber noise to town scenes
	    #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	    lightsaber_noise_player,
		#lightsaber_noise_player_2,			# play sound on release doesn't seem to work correctly
	    #lightsaber_noise_agent,
		common_change_fog,
		common_use_healthpack,
		#common_use_binocular_1,
		#common_use_binocular_2,
		common_helmet_view,
		common_zoom_view,
		common_use_jetpack,
		common_fix_droid_walking,
		common_toggle_weapon_capabilities,
		#common_speeder_attack,	#testing
		common_speeder_trigger_1,
		common_speeder_trigger_2,
		common_switch_sw_scene_props,
		common_crouch_button,
		#common_turret, -> unstable
		common_gate_system,
		
			#SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),



    ],
  ),

  (
    "bandits_at_night",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, []),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),

     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(28,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
		lightsaber_noise_player,
		common_change_fog,
		common_use_healthpack,
		#common_use_binocular_1,
		#common_use_binocular_2,
		common_helmet_view,
		common_zoom_view,
		common_use_jetpack,
		common_toggle_weapon_capabilities,
		common_crouch_button,


      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (neq, ":troop_no", "trp_player"),
         (agent_set_team, ":agent_no", 1),
         ]),

      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_inventory_not_available,

      (ti_tab_pressed, 0, 0,
       [
         (display_message, "@Cannot leave now."),
         ], []),
      (ti_on_leave_area, 0, 0,
       [
         (try_begin),
           (eq, "$g_defending_against_siege", 0),
           (assign,"$g_leave_town",1),
         (try_end),
         ], []),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
         (party_slot_eq, "$current_town", slot_party_type, spt_mainplanet),
         (call_script, "script_town_init_doors", 0),
        ]),

      (1, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [
         (try_begin),
           (main_hero_fallen),
           (jump_to_menu, "mnu_town_bandits_failed"),
         (else_try),
           (jump_to_menu, "mnu_town_bandits_succeeded"),
         (try_end),
         (finish_mission),
         ]),


		 #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

		#SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
      ],
    ),


  (
    "minorplanet_training", mtf_arena_fight, -1,
    "minorplanet_training",
    [
	 #SW - modified af_override and weapons (switched practice_staff to durasteel_staff)
	 #(2,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_durasteel_staff, itm_practice_boots]),
     #(4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_durasteel_staff, itm_practice_boots]),
	 (2,mtef_visitor_source|mtef_team_0,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_durasteel_staff, itm_practice_boots]),
     (4,mtef_visitor_source|mtef_team_1,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_durasteel_staff, itm_practice_boots]),
     ],
    [

	lightsaber_noise_player,
	common_change_fog,
	common_use_healthpack,
	#common_use_binocular_1,
	#common_use_binocular_2,
	common_helmet_view,
	common_zoom_view,
	common_use_jetpack,
	common_toggle_weapon_capabilities,
	common_crouch_button,


      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_train_peasants_against_bandits_training_succeeded", 0),
         (call_script, "script_change_banners_and_chest"),
         ]),

      common_arena_fight_tab_press,

      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (finish_mission),
         ]),

      common_inventory_not_available,

      (1, 4, ti_once,
       [
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_train_peasants_against_bandits_training_succeeded", 1),
         (try_end),
         (finish_mission),
         ]),

#Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),

      ],
###>> Motomataru's AI
#AI_triggers,
    ),

  (
    "visit_town_castle",0,-1,
    "You enter the halls of the lord.",
	#SW - modified so you do not remove your helmet when you enter a lords hall (removed af_override_head flag)
	[(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), #for doors
     (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_visitor_source,af_override_horse,0,1,[]),(9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_scene_source,af_override_horse,0,1,[]),(11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_spacestation_lord,0,1,[]),(17,mtef_visitor_source,af_spacestation_lord,0,1,[]),(18,mtef_visitor_source,af_spacestation_lord,0,1,[]),(19,mtef_visitor_source,af_spacestation_lord,0,1,[]),(20,mtef_visitor_source,af_spacestation_lord,0,1,[]),(21,mtef_visitor_source,af_spacestation_lord,0,1,[]),(22,mtef_visitor_source,af_spacestation_lord,0,1,[]),(23,mtef_visitor_source,af_spacestation_lord,0,1,[]),(24,mtef_visitor_source,af_spacestation_lord,0,1,[]),
     (25,mtef_visitor_source,af_spacestation_lord,0,1,[]),(26,mtef_visitor_source,af_spacestation_lord,0,1,[]),(27,mtef_visitor_source,af_spacestation_lord,0,1,[]),(28,mtef_visitor_source,af_spacestation_lord,0,1,[]),(29,mtef_visitor_source,af_spacestation_lord,0,1,[]),(30,mtef_visitor_source,af_spacestation_lord,0,1,[]),(31,mtef_visitor_source,af_spacestation_lord,0,1,[]),
	 #new entry points (unused)
	 (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),
	 #entry point #38 & 39 are for slave dancers
	 (38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
	 #SWY - entry point 40-45 for extra guards in Yavin and Hoth
	 (40,mtef_scene_source,af_override_horse,0,1,[]),(41,mtef_scene_source,af_override_horse,0,1,[]),(42,mtef_scene_source,af_override_horse,0,1,[]),(43,mtef_scene_source,af_override_horse,0,1,[]),(44,mtef_scene_source,af_override_horse,0,1,[]),(45,mtef_scene_source,af_override_horse,0,1,[])
     ],
	 ###>> Motomataru's AI
#AI_triggers,
    [
	  lightsaber_noise_player,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_switch_sw_scene_props,
	  common_crouch_button,


	  (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
         ]),
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
         ]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(call_script, "script_flush_gatesys_cache"),(set_trigger_result,1)], []),
      (0, 0, ti_once, [], [
        #(set_fog_distance, 150, 0xFF736252)
        (try_begin),
          (eq, "$talk_context", tc_court_talk),
#          (call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", 0), #prison
        (try_end),
        ]),

      (0, 0, ti_once, [],
			[
			#------------------------------------------------------------------------------------------------------------------------------------------------------
			#set music depending on the faction
			#SW - attempting to add castle specific music (this concept doesn't seem to work at all?  I had to add that persist until finished flag...)
			(store_faction_of_party, ":spacestation_faction", "$current_town"),
			(try_begin),
				(eq, ":spacestation_faction", "fac_galacticempire"), 	#empire
				(store_random_in_range, ":random", 1, 4),
				(try_begin),
					(eq, ":random", 1),
					(assign, ":spacestation_track", "track_throne_empire_1"),
				(else_try),
					(eq, ":random", 2),
					(assign, ":spacestation_track", "track_throne_empire_2"),
				(else_try),
					#(eq, ":random", 3),
					(assign, ":spacestation_track", "track_throne_empire_3"),
				(try_end),
			(else_try),
				(eq, ":spacestation_faction", "fac_rebelalliance"), 	#rebel
				(store_random_in_range, ":random", 1, 5),
				(try_begin),
					(eq, ":random", 1),
					(assign, ":spacestation_track", "track_throne_rebel_1"),
				(else_try),
					(eq, ":random", 2),
					(assign, ":spacestation_track", "track_throne_rebel_2"),
				(else_try),
					(eq, ":random", 3),
					(assign, ":spacestation_track", "track_throne_rebel_3"),
				(else_try),
					#(eq, ":random", 4),
					(assign, ":spacestation_track", "track_throne_rebel_4"),
				(try_end),
			(else_try),
				#hutt/other
				(store_random_in_range, ":random", 1, 4),
				(try_begin),
					(eq, ":random", 1),
					(assign, ":spacestation_track", "track_throne_hutt_1"),
				(else_try),
					(eq, ":random", 2),
					(assign, ":spacestation_track", "track_throne_hutt_2"),
				(else_try),
					#(eq, ":random", 3),
					(assign, ":spacestation_track", "track_throne_hutt_3"),
				(try_end),
			(try_end),
			(play_track, ":spacestation_track", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
			#------------------------------------------------------------------------------------------------------------------------------------------------------

			]),

	  #SWY - trigger to make unique agents behavior
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",1)]),
	   common_gate_system,

    ],
  ),

  (
    "back_alley_kill_local_merchant",mtf_arena_fight,-1,
    "You enter the back alley",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
	lightsaber_noise_player,
	common_change_fog,
	common_use_healthpack,
	#common_use_binocular_1,
	#common_use_binocular_2,
	common_helmet_view,
	common_zoom_view,
	common_use_jetpack,
	common_toggle_weapon_capabilities,
	common_crouch_button,

      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),


      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         ]),

      (0, 0, ti_once, [
          (store_mission_timer_a,":cur_time"),
          (ge,":cur_time",1),
          (assign, ":merchant_hp", 0),
          (assign, ":player_hp", 0),
          (assign, ":merchant_hp", 0),
          (assign, ":merchant_agent", -1),
          (assign, ":player_agent", -1),
          (try_for_agents, ":agent_no"),
            (agent_get_troop_id, ":troop_id", ":agent_no"),
            (try_begin),
              (eq, ":troop_id", "trp_local_merchant"),
              (store_agent_hit_points, ":merchant_hp",":agent_no"),
              (assign, ":merchant_agent", ":agent_no"),
            (else_try),
              (eq, ":troop_id", "trp_player"),
              (store_agent_hit_points, ":player_hp",":agent_no"),
              (assign, ":player_agent", ":agent_no"),
            (try_end),
          (try_end),
          (ge, ":player_agent", 0),
          (ge, ":merchant_agent", 0),
          (agent_is_alive, ":player_agent"),
          (agent_is_alive, ":merchant_agent"),
          (is_between, ":merchant_hp", 1, 30),
          (gt, ":player_hp", 50),
          (start_mission_conversation, "trp_local_merchant"),
          ], []),

      (1, 4, ti_once, [(assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_local_merchant"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_kill_local_merchant"),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -4),
             (call_script, "script_succeed_quest", "qst_kill_local_merchant"),
           (try_end),
           (finish_mission),
           ]),


	#SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
    ],
  ),

  (
    "back_alley_revolt",mtf_battle_mode,charge,
    "You lead your men to battle.",
	#SW - modified so you do not remove your helmet (removed af_override_head flag) also switched weapon to a durasteel staff
	[(0,mtef_team_0|mtef_use_exact_number,af_override_horse|af_override_weapons,aif_start_alarmed,4,[itm_durasteel_staff]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [

	lightsaber_noise_player,
	common_change_fog,
	common_use_healthpack,
	#common_use_binocular_1,
	#common_use_binocular_2,
	common_helmet_view,
	common_zoom_view,
	common_use_jetpack,
	common_toggle_weapon_capabilities,
    common_inventory_not_available,
	common_crouch_button,


      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_want_to_retreat"),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (jump_to_menu, "mnu_collect_taxes_failed"),
        (finish_mission),]),

      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (jump_to_menu, "mnu_collect_taxes_failed"),
           (else_try),
             (jump_to_menu, "mnu_collect_taxes_rebels_killed"),
           (try_end),
           (finish_mission),
           ]),

		   #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    ],
  ),

  (
    "lead_charge",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (1,mtef_defenders|mtef_team_0,0,aif_start_alarmed,12,[]),
     (0,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [

sw_victory_defeat_conditions,

  (4, 0, 0, [(eq,"$battle_won",1),], [ (display_message,"str_msg_battle_won"), ]),

#Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics",1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Highlander begin--------------------------------------
common_physics_init,
common_timer,
common_physics,
#Highlander end--------------------------------------

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),
         ]),

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),
         ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1.223455, 0, 5.429003, [(lt,"$defender_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6),
#                 (assign, reg2, ":num_defenders"),
#                 (display_message,"@num_defenders = {reg2}")
                 ],
           [(add_reinforcements_to_entry,0,7),(val_add,"$defender_reinforcement_stage",1)]),

      (1.997115, 0, 5.644421, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6),
#                 (assign, reg2, ":num_attackers"),
#                 (display_message,"@num_attackers = {reg2}")
                 ],
           [(add_reinforcements_to_entry,3,7),(val_add,"$attacker_reinforcement_stage",1)]),


      (1.395044, 4.56644, ti_once, [(main_hero_fallen)],
          [
			  (call_script,"script_battle_speech",3),
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
			  (call_script,"script_get_key","$deathcam_forward_key"),
			  (str_store_string,s1,s13),
			  (call_script,"script_get_key","$deathcam_backward_key"),
			  (str_store_string,s2,s13),
			  #(display_message, "@If you choose to watch the fight you can use the M and N keys to change your camera view."),
			  (display_message, "@If you choose to watch the fight you can use the '{s1}' and '{s2}' keys to change your camera view."),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
			  ]),

#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,

      common_battle_inventory,

      #SW - added shield bash integration
      shield_bash_kit_1,
      shield_bash_kit_2,
      shield_bash_kit_3,
      shield_bash_kit_4,

      #SW - added regen for certain agents
      #common_regeneration_store_info,
      #common_regeneration,

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_speeder_trigger_1,
	  common_speeder_trigger_2,
	  common_agent_droid_refill_trigger,
	  common_fix_droid_walking,
	  common_crouch_button,



      #AI Tiggers
       #(0, 0, ti_once, [
       #   (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
       #   ],
       #[(call_script, "script_select_battle_tactic"),
       # (call_script, "script_battle_tactic_init")]),

      #(5, 0, 0, [
       #   (store_mission_timer_a,":mission_time"),(ge,":mission_time",3),
       #   (call_script, "script_battle_tactic_apply"),
       #   ], []),

      common_battle_order_panel,
      common_battle_order_panel_tick,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

	#@> Swyter Battle Speech
	(3.6543, 0, ti_once, [(eq,"$battle_won",1),],[(call_script,"script_battle_speech",2)]),
	(0, 5.4332, ti_once, [], [(call_script,"script_battle_speech",1)]),

	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
		common_gate_system,

    ],
  ),

#########################################################################################################################
#SW - new lead_charge_no_horse mission_template (used for ship battles) - added af_override_horse

  (
    "lead_charge_no_horse",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (1,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (4,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (4,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),

     ],
    [

##@> Swyter's Hangar Speech
(1.5,0,ti_once,[],
[
(faction_get_slot,":hangar_faction","fac_player_supporters_faction", slot_faction_culture),
#(store_troop_faction,":hangar_faction","trp_player"),
(play_sound,"snd_swc_hangar_siren",1),

	(try_begin),
		(eq, ":hangar_faction", "fac_culture_1"),
		(play_sound,"snd_swc_hangar_imperial",1),
	(else_try),
		(eq, ":hangar_faction", "fac_culture_2"),
		(play_sound,"snd_swc_hangar_rebel",1),
	(else_try),
		(eq, ":hangar_faction", "fac_culture_3"),
		(play_sound,"snd_swc_hangar_hutt",1),
	(else_try),
		(eq, ":hangar_faction", "fac_culture_4"),
		(play_sound,"snd_swc_hangar_wookie",1),
	(else_try),
		(eq, ":hangar_faction", "fac_culture_5"),
		(play_sound,"snd_swc_hangar_sith",1),
	(else_try),
		(eq, ":hangar_faction", "fac_culture_6"),
		(play_sound,"snd_swc_hangar_clones",1),
	(else_try),
		(eq, ":hangar_faction", "fac_culture_7"),
		(play_sound,"snd_swc_hangar_trandoshan",1),
	(else_try),
		(play_sound,"snd_swc_hangar_neutral",1),
	(try_end),
]),

(20,0,ti_once,[],
[
(stop_all_sounds),
]),

(53,0,ti_once,[],
[
(play_sound,"snd_swc_hangar_siren",1),
]),

(73,0,ti_once,[],
[
(stop_all_sounds),
]),
#Highlander begin--------------------------------------
(0.06933,0,ti_once,[],
[
(get_player_agent_no,":agent"),
(agent_get_position,pos1,":agent"),
(position_get_z,"$ground_level",pos1),
]),
common_physics_init,
common_timer,
common_physics,
#Highlander end--------------------------------------

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),
         ]),

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

		 #SW - disable rain in lead_charge_no_horse (ship battle)
		 (set_rain,1,0),

         ]),


      (0, 0, ti_once, [], [(assign,"$battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (assign,"$g_presentation_battle_active", 0),
						   #SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
                           (call_script, "script_place_player_banner_near_inventory"),
                           (call_script, "script_combat_music_set_situation_with_culture"),

                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6),
#                 (assign, reg2, ":num_defenders"),
#                 (display_message,"@num_defenders = {reg2}")
                 ],
           [(add_reinforcements_to_entry,0,7),(val_add,"$defender_reinforcement_stage",1)]),

      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6),
#                 (assign, reg2, ":num_attackers"),
#                 (display_message,"@num_attackers = {reg2}")
                 ],
           [(add_reinforcements_to_entry,3,7),(val_add,"$attacker_reinforcement_stage",1)]),

      sw_victory_defeat_conditions,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have fallen in battle. You can watch the rest of the fight or press tab to exit"),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
			  ]),

#Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,

      common_battle_inventory,

      #SW - added shield bash integration
      shield_bash_kit_1,
      shield_bash_kit_2,
      shield_bash_kit_3,
      shield_bash_kit_4,

      #SW - added regen for certain agents
      #common_regeneration_store_info,
      #common_regeneration,

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_agent_droid_refill_trigger,
	  common_fix_droid_walking,
	  common_crouch_button,


      #AI Tiggers
      #(0, 0, ti_once, [
      #    (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
      #    ],
      # [(call_script, "script_select_battle_tactic"),
       # (call_script, "script_battle_tactic_init")]),

      #(5, 0, 0, [
      #    (store_mission_timer_a,":mission_time"),(ge,":mission_time",3),
      #    (call_script, "script_battle_tactic_apply"),
      #    ], []),

      common_battle_order_panel,
      common_battle_order_panel_tick,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

	  #SWYTER - Darth Vader Scripting
	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),


	 # SW - script to stop riderless horses (ie. speeders) from moving (script from KON_Air) - not necessary in lead_charge_no_horse mt
#     (0.1, 0, 0,
#      [
#	  (try_for_agents, ":cur_agent"),
#	   (agent_is_alive, ":cur_agent"),	#so we don't try dead agents
#	    (neg|agent_is_human,":cur_agent"),	#agent is a horse
#	     (agent_get_rider,":cur_rider", ":cur_agent"),
#	      (lt, ":cur_rider", 0),	#horse does not have a rider
#		   (agent_set_animation, ":cur_agent", "anim_speeder_stationary"),	#so the horse doesn't move, must include module_animations at the top
#	  (try_end),
#      ], []),
    ],
  ),

#########################################################################################################################

  (
    "minorplanet_attack_bandits",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     ],
    [
	lightsaber_noise_player,
	lightsaber_noise_agent,
	common_change_fog,
	common_use_healthpack,
	#common_use_binocular_1,
	#common_use_binocular_2,
	common_helmet_view,
	common_zoom_view,
	common_use_jetpack,
	common_toggle_weapon_capabilities,
	common_agent_droid_refill_trigger,
	common_crouch_button,


    common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           (assign, "$g_presentation_battle_active", 0),
							#SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
                           (try_begin),
                             (eq, "$g_mt_mode", vba_after_training),
                             (add_reinforcements_to_entry, 1, 6),
                           (else_try),
                             (add_reinforcements_to_entry, 1, 29),
                           (try_end),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      sw_victory_defeat_conditions,
      common_battle_victory_display,

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have fallen in battle. Watch the rest of the fight or press tab to exit"),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result, -1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission, 0)
			  ]),

#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,

      common_battle_inventory,
      common_battle_order_panel,
      common_battle_order_panel_tick,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

    ],
  ),



  (
    "minorplanet_raid",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [
		lightsaber_noise_player,
		lightsaber_noise_agent,
		common_change_fog,
		common_use_healthpack,
		#common_use_binocular_1,
		#common_use_binocular_2,
		common_helmet_view,
		common_zoom_view,
		common_use_jetpack,
		common_toggle_weapon_capabilities,
		common_agent_droid_refill_trigger,
		common_crouch_button,


		common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign,"$battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (assign, "$g_presentation_battle_active", 0),
						   #SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

	#Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,6),(val_add,"$defender_reinforcement_stage",1)]),
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,6),(val_add,"$attacker_reinforcement_stage",1)]),

      (1, 60, ti_once,
       [
         (store_mission_timer_a,reg(1)),
         (ge,reg(1),10),
         (all_enemies_defeated, 5),
 #        (neg|main_hero_fallen, 0),
         (set_mission_result,1),
         (display_message,"str_msg_battle_won"),
         (assign,"$battle_won",1),
         (assign, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_minorplanet_raid_evil", 0),
           (call_script, "script_play_victorious_sound"),
         (else_try),
			#SW - didn't want to have to include track_victorious_evil in module_music.py
           #(play_track, "track_victorious_evil", 1),
		   (call_script, "script_play_victorious_sound"),
         (try_end),
         ],
       [
         (call_script, "script_count_mission_casualties_from_agents"),
         (finish_mission, 1),
         ]),

      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have fallen in battle. Watch the rest of the fight or press tab to exit"),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 10, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
			  ]),
#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,


      common_battle_inventory,
      common_battle_order_panel,
      common_battle_order_panel_tick,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

##      #AI Tiggers
##      (0, 0, ti_once, [
##          (store_mission_timer_a,reg(1)),(ge,reg(1),4),
##          (call_script, "script_select_battle_tactic"),
##          (call_script, "script_battle_tactic_init"),
##          ], []),
##      (1, 0, 0, [
##          (store_mission_timer_a,reg(1)),(ge,reg(1),4),
##          (call_script, "script_battle_tactic_apply"),
##          ], []),
    ],
  ),



##  (
##    "charge_with_allies",mtf_battle_mode,charge_with_ally,
##    "Taking a handful of fighters with you, you set off to patrol the area.",
##    [
##     (1,mtef_defenders,0,0|aif_start_alarmed,8,[]),
##     (0,mtef_defenders,0,0|aif_start_alarmed,0,[]),
##     (4,mtef_attackers,0,aif_start_alarmed,8,[]),
##     (4,mtef_attackers,0,aif_start_alarmed,0,[]),
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),
##        (eq,":answer",0),
##        (assign, "$pin_player_fallen", 0),
##        (str_store_string, s5, "str_retreat"),
##        (call_script, "script_simulate_retreat", 10, 30),
##        (finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$battle_won",0),(assign,"$defender_reinforcement_stage",0),(assign,"$attacker_reinforcement_stage",0)]),
##      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_defender_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,0,4),(val_add,"$defender_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_attacker_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,3,4),(val_add,"$attacker_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),(all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$battle_won",1)],
##           [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$battle_won",1),(display_message,"str_msg_battle_won")]),
##
##      (1, 4, ti_once, [(main_hero_fallen)],
##          [
##              (assign, "$pin_player_fallen", 1),
##              (str_store_string, s5, "str_retreat"),
##              (call_script, "script_simulate_retreat", 20, 30),
##              (assign, "$g_battle_result", -1),
##              (set_mission_result,-1),(finish_mission,0)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),

##  (
##    "charge_with_allies_old",mtf_battle_mode,charge_with_ally,
##    "Taking a handful of fighters with you, you set off to patrol the area.",
##    [(1,mtef_leader_only,0,0,1,[]),
##     (1,mtef_no_leader,0,0|aif_start_alarmed,2,[]),
##     (1,mtef_reverse_order|mtef_ally_party,0,0|aif_start_alarmed,3,[]),
##     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
##     (0,mtef_reverse_order|mtef_ally_party,0,0|aif_start_alarmed,0,[]),
##     (3,mtef_reverse_order|mtef_enemy_party,0,aif_start_alarmed,6,[]),
##     (4,mtef_reverse_order|mtef_enemy_party,0,aif_start_alarmed,0,[])],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),(eq,":answer",0),(finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$battle_won",0),(assign,"$enemy_reinforcement_stage",0),(assign,"$friend_reinforcement_stage",0),(assign,"$ally_reinforcement_stage",0)]),
##
##      (1, 0, 5, [(lt,"$enemy_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_enemy_count,reg(2)),(lt,reg(2),3)],
##       [(add_reinforcements_to_entry,6,3),(val_add,"$enemy_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$friend_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_friend_count,reg(2)),(lt,reg(2),2)],
##       [(add_reinforcements_to_entry,3,1),(val_add,"$friend_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$ally_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_ally_count,reg(2)),  (lt,reg(2),2)],
##       [(add_reinforcements_to_entry,4,2),(val_add,"$ally_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),
##                        (all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$battle_won",1),
##                        ],
##       [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$battle_won",1),(display_message,"str_msg_battle_won")]),
##      (1, 4, ti_once, [(main_hero_fallen,0)],
##       [(set_mission_result,-1),(finish_mission,1)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),
##  (
##    "lead_charge_old",mtf_battle_mode,charge,
##    "You lead your men to battle.",
##    [
##     (1,mtef_leader_only,0,0,1,[]),
##     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
##     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
##     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
##     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),(eq,":answer",0),(finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$battle_won",0),(assign,"$enemy_reinforcement_stage",0),(assign,"$friend_reinforcement_stage",0)]),
##      (1, 0, 5, [(lt,"$enemy_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_enemy_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,4,3),(val_add,"$enemy_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$friend_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_friend_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,2,3),(val_add,"$friend_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),(all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$battle_won",1)],
##           [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$battle_won",1),(display_message,"str_msg_battle_won")]),
##      (1, 4, ti_once, [(main_hero_fallen)],
##          [
##              (assign, "$g_battle_result", -1),
##              (set_mission_result,-1),(finish_mission,1)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),



  (
    "besiege_inner_battle_castle",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (17, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (18, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (19, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (20, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
		lightsaber_noise_player,
		lightsaber_noise_agent,
		common_change_fog,
		common_use_healthpack,
		#common_use_binocular_1,
		#common_use_binocular_2,
		common_helmet_view,
		common_zoom_view,
		common_use_jetpack,
		common_toggle_weapon_capabilities,
		common_agent_droid_refill_trigger,
		common_crouch_button,


      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),

      (0, 0, ti_once, [], [(assign,"$battle_won",0),
                           (assign,"$g_presentation_battle_active", 0),
						   #SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
                           (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ]),

      #AI Tiggers
      #(0, 0, ti_once, [
      #    (assign, "$defender_team", 0),
      #    (assign, "$attacker_team", 1),
      #    (assign, "$defender_team_2", 2),
      #    (assign, "$attacker_team_2", 3),
       #   ], []),

      common_battle_check_friendly_kills,
      sw_victory_defeat_conditions,
      common_battle_victory_display,

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have fallen in battle. Watch the rest of the fight or press tab to exit"),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 5, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
              ]),

#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,


      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle_dismounted,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

    ],
###>> Motomataru's AI
#AI_triggers,
common_gate_system
  ),

  (
    "besiege_inner_battle_town_center",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,4,[]),
     (2, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (23, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (24, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (25, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (26, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (27, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (28, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_agent_droid_refill_trigger,
	  common_crouch_button,


      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),

      (0, 0, ti_once, [], [(assign,"$battle_won",0),
                           (assign,"$g_presentation_battle_active", 0),
						   #SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
                           (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ]),

      #AI Tiggers
     # (0, 0, ti_once, [
          #(assign, "$defender_team", 0),
          #(assign, "$attacker_team", 1),
          #(assign, "$defender_team_2", 2),
          #(assign, "$attacker_team_2", 3),
         # ], []),

      common_battle_check_friendly_kills,
      sw_victory_defeat_conditions,
      common_battle_victory_display,

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have fallen in battle. Watch the rest of the fight or press tab to exit"),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 5, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result,-1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
              ]),
#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,

      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle_dismounted,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

    ],
###>> Motomataru's AI
#AI_triggers,
common_gate_system
  ),

  (
    "spacestation_attack_walls_defenders_sally",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     ],
    [
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_agent_droid_refill_trigger,
	  common_crouch_button,


      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_change_banners_and_chest"),
         (call_script, "script_remove_siege_objects"),
         ]),

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign,"$battle_won",0),
                           (assign,"$g_presentation_battle_active", 0),
						   #SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 60, ti_once, [(store_mission_timer_a, reg(1)),
                        (ge, reg(1), 10),
                        (all_enemies_defeated, 2),
    #                    (neg|main_hero_fallen,0),
                        (set_mission_result,1),
                        (display_message,"str_msg_battle_won"),
                        (assign, "$battle_won", 1),
                        (assign, "$g_battle_result", 1),
                        (assign, "$g_siege_sallied_out_once", 1),
                        (assign, "$g_siege_method", 1), #reset siege timer
                        (call_script, "script_play_victorious_sound"),
                        ],
           [(call_script, "script_count_mission_casualties_from_agents"),
            (finish_mission,1)]),


      common_battle_victory_display,

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
			  (display_message, "@You have fallen in battle. Watch the rest of the fight or press tab to exit"),
              # (str_store_string, s5, "str_retreat"),
              # (call_script, "script_simulate_retreat", 5, 20),
              # (assign, "$g_battle_result", -1),
              # (set_mission_result, -1),
              # (call_script, "script_count_mission_casualties_from_agents"),
              # (finish_mission,0)
			  ]),
#SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,


      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle_dismounted,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
common_gate_system,
    ],
  ),


  (
    "spacestation_attack_walls_belfry",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (47,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,


      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,

      (0, 0, ti_once,
       [
         (set_show_messages, 0),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
		 #SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
         (set_show_messages, 1),
         ], []),

      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      sw_victory_defeat_conditions,
      common_battle_victory_display,

      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
	  #SW - modified inventory to be available in battle
      #common_inventory_not_available,
	  (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
	  #SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle_dismounted,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
common_gate_system,
    ],
  ),

  (
    "spacestation_attack_walls_ladder",mtf_battle_mode,-1,
    "You attack the walls of the castle...",
    [
	#SW - increased attacker troops from 12 to 15
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,15,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
	 #SW - decreased defender infantry troops from 7 to 5
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,5,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

	#SW increased the number of archer troops at each entry point from 1 to 4
     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,4,[]),
     ],
    [
	(0, 0, ti_once, [],[
							#SW Deathcam
						   (assign, "$dmod_current_agent", -1),
						   (assign, "$dmod_move_camera", -1),
						   ]),
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,


      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      sw_victory_defeat_conditions,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
	  #SW - modified inventory to be available in battle
      #common_inventory_not_available,
	  #SW Deathcam

sw_deathcam_follow_troop,
sw_deathcam_valkyrie_move_camera,
sw_deathcam_cycle_fowards,
sw_deathcam_cycle_backwards,
	  (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      common_npc_proficiency_limit,
      common_npc_raise_proficiency,
      common_check_player_can_join_battle_dismounted,
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
common_gate_system,

##      (15, 0, 0,
##       [
##         (get_player_agent_no, ":player_agent"),
##         (agent_get_team, ":agent_team", ":player_agent"),
##         (neq, "$attacker_team", ":agent_team"),
##         (assign, ":non_ranged", 0),
##         (assign, ":ranged", 0),
##         (assign, ":ranged_pos_x", 0),
##         (assign, ":ranged_pos_y", 0),
##         (set_fixed_point_multiplier, 100),
##         (try_for_agents, ":agent_no"),
##           (eq, ":non_ranged", 0),
##           (agent_is_human, ":agent_no"),
##           (agent_is_alive, ":agent_no"),
##           (neg|agent_is_defender, ":agent_no"),
##           (agent_get_class, ":agent_class", ":agent_no"),
##           (try_begin),
##             (neq, ":agent_class", grc_archers),
##             (val_add, ":non_ranged", 1),
##           (else_try),
##             (val_add, ":ranged", 1),
##             (agent_get_position, pos0, ":agent_no"),
##             (position_get_x, ":pos_x", pos0),
##             (position_get_y, ":pos_y", pos0),
##             (val_add, ":ranged_pos_x", ":pos_x"),
##             (val_add, ":ranged_pos_y", ":pos_y"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (eq, ":non_ranged", 0),
##           (gt, ":ranged", 0),
##           (val_div, ":ranged_pos_x", ":ranged"),
##           (val_div, ":ranged_pos_y", ":ranged"),
##           (entry_point_get_position, pos0, 10),
##           (init_position, pos1),
##           (position_set_x, pos1, ":ranged_pos_x"),
##           (position_set_y, pos1, ":ranged_pos_y"),
##           (position_get_z, ":pos_z", pos0),
##           (position_set_z, pos1, ":pos_z"),
##           (get_distance_between_positions, ":dist", pos0, pos1),
##           (gt, ":dist", 1000), #average position of archers is more than 10 meters far from entry point 10
##           (team_give_order, "$attacker_team", grc_archers, mordr_hold),
##           (team_set_order_position, "$attacker_team", grc_archers, pos0),
##         (else_try),
##           (team_give_order, "$attacker_team", grc_everyone, mordr_charge),
##         (try_end),
##         ],
##       []),
    ],
  ),


  (
    "spacestation_visit",0,-1,
    "Castle visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(10,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(11,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (12,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(13,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(14,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(15,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (16,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(17,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(18,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(19,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (20,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(21,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(22,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(23,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (24,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(25,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(26,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(27,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (28,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(29,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(30,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(31,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (32,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(33,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(34,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(35,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (36,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(37,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 #entry point #38 & 39 are for slave dancers
	 (38,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(39,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     # Party members
     (40,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (41,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (42,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (43,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (44,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (45,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (46,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     ],
    [


	  #SW - trigger to make some agents dance in the scene
	  (1, 0, ti_once, [], [
      #(ti_on_agent_spawn, 0, 0, [], [
		#(store_trigger_param_1, ":agent_no"),
		(try_for_agents, ":agent_no"),
			(agent_get_entry_no, ":entry_no", ":agent_no"),
			(this_or_next|eq,":entry_no",38),
			(eq,":entry_no",39),
			(agent_set_stand_animation, ":agent_no", "anim_slave_dance"),
			(agent_set_animation, ":agent_no", "anim_slave_dance"),
			(store_random_in_range, ":random_no", 0, 100),
			(agent_set_animation_progress, ":agent_no", ":random_no"),
		(try_end),
      ]),

	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_switch_sw_scene_props,
	  common_crouch_button,


      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
         ]),
      (ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
                                           (call_script, "script_remove_siege_objects"),
                                           ]),

		common_gate_system,

      (0, 0, ti_once, [],
       [
#         (call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
         ]),

#      (ti_before_mission_start, 0, 0, [],
#          [(scene_prop_disable,"spr_ramp_12m"),(scene_prop_disable,"spr_portcullis")]),
    ],
  ),


  (
    "training_ground_trainer_talk", 0, -1,
    "Training.",
    [
      (0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (1,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (2,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (3,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (4,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (5,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (6,mtef_scene_source|mtef_team_0,0,0,1,[]),
    ],
    [
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
         ]),
      (ti_inventory_key_pressed, 0, 0,
       [
         (set_trigger_result,1),
         ], []),
      (ti_tab_pressed, 0, 0,
       [
         (set_trigger_result,1),
         ], []),
     (0.0, 1.0, 2.0,
      [(lt, "$trainer_help_message", 2),
        ],
      [(try_begin),
         (eq, "$trainer_help_message", 0),
         (tutorial_box, "str_trainer_help_1", "@Tutorial"),
       (else_try),
         (tutorial_box, "str_trainer_help_2", "@Tutorial"),
       (try_end),
       (val_add, "$trainer_help_message", 1),
          ]),

    ],
  ),

  (
    "training_ground_trainer_training",mtf_arena_fight,-1,
    "You will fight a match in the arena.",
    [
	  #SW - modified training equipment
      (16, mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_arena_tunic_green,itm_vibro_sword3_gold,itm_energy_shield_yellow_small]),
      (17, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_arena_tunic_red,itm_vibro_sword2b]),
      (18, mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_arena_tunic_blue,itm_vibro_sword1b,itm_energy_shield_yellow_small]),
      (19, mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_arena_tunic_yellow,itm_vibro_axe_long_2h]),
      (20, mtef_visitor_source,0,0,1,[]),
    ],
    [
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_arena_fight_tab_press,

      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1, ":answer"),
         (eq, ":answer", 0),
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (1, 3, ti_once, [(main_hero_fallen,0)],
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (1, 3, ti_once,
       [
         (store_mission_timer_a, reg1),
         (ge, reg1, 1),
         (num_active_teams_le, 1),
         (neg|main_hero_fallen),
         (assign, "$training_fight_won", 1),
         ],
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
    ],
  ),


  (
    "training_ground_training", mtf_arena_fight, -1,
    "Training.",
    [
	  #SW - switched itm_practice_staff to itm_electro_staff_long, switched af_override functionalityaaa
      #(0,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_vibro_sword3_gold]),
      #(1,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_vibro_sword3_gold]),
      #(2,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_vibro_sword3_gold]),
      #(3,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_vibro_sword3_gold]),
      #(4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_vibro_sword3_gold]),
      (0,mtef_visitor_source|mtef_team_0,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_electro_staff_long]),
      (1,mtef_visitor_source|mtef_team_1,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_electro_staff_long]),
      (2,mtef_visitor_source|mtef_team_1,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_electro_staff_long]),
      (3,mtef_visitor_source|mtef_team_1,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_electro_staff_long]),
      (4,mtef_visitor_source|mtef_team_1,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_electro_staff_long]),

	  #SW - modified so you do not remove your helmet (removed af_override_head flag)
      (8,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (9,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (10,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (11,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (12,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (13,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (14,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
      (15,mtef_visitor_source,af_override_weapons|af_override_horse,0,1,[]),
    ],
    [
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_last_destroyed_gourds", 0),
         (call_script, "script_change_banners_and_chest")]),

      common_arena_fight_tab_press,

      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (assign, "$g_training_ground_training_success_ratio", 0),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      common_inventory_not_available,

      (0, 0, ti_once,
       [
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (set_fixed_point_multiplier, 100),
           (entry_point_get_position, pos1, 0),
           (init_position, pos2),
           (position_set_y, pos2, "$g_training_ground_ranged_distance"),
           (position_transform_position_to_parent, pos3, pos1, pos2),
           (copy_position, pos1, pos3),
           (assign, ":end_cond", 10),
           (assign, ":shift_value", 0),
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_sub, ":cur_instance", ":cur_i", ":shift_value"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_instance"),
             (copy_position, pos2, pos1),
             (init_position, pos0),
             (store_random_in_range, ":random_no", 0, 360),
             (position_rotate_z, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 50, 600),
             (position_move_x, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 0, 360),
             (position_transform_position_to_local, pos3, pos1, pos2),
             (position_rotate_z, pos0, ":random_no"),
             (position_transform_position_to_parent, pos4, pos0, pos3),
             (position_transform_position_to_parent, pos2, pos1, pos4),
             (position_set_z_to_ground_level, pos2),
             (position_move_z, pos2, 150),
             (assign, ":valid", 1),
             (try_for_range, ":cur_instance_2", 0, 10),
               (eq, ":valid", 1),
               (neq, ":cur_instance", ":cur_instance_2"),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd", ":cur_instance_2"),
               (prop_instance_get_position, pos3, ":target_object_2"),
               (get_distance_between_positions, ":dist", pos2, pos3),
               (lt, ":dist", 100),
               (assign, ":valid", 0),
             (try_end),
             (try_begin),
               (eq, ":valid", 0),
               (val_add, ":end_cond", 1),
               (val_add, ":shift_value", 1),
             (else_try),
               (prop_instance_set_position, ":target_object", pos2),
               (prop_instance_animate_to_position, ":target_object", pos2, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_instance"),
               (position_move_z, pos2, -150), #moving back to ground level
               (prop_instance_set_position, ":target_object_2", pos2),
               (prop_instance_animate_to_position, ":target_object_2", pos2, 1),
             (try_end),
           (try_end),
         (else_try),
           (eq, "$g_mt_mode", ctm_mounted),
           (assign, ":num_gourds", 0),
           #First, placing gourds on the spikes
           (try_for_range, ":cur_i", 0, 100),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_i"),
             (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_i"),
             (ge, ":target_object", 0),
             (ge, ":target_object_2", 0),
             (val_add, ":num_gourds", 1),
             (prop_instance_get_position, pos0, ":target_object_2"),
             #SW - raised the height of the gourd
			 #(position_move_z, pos0, 150),
			 (position_move_z, pos0, 200),
             (prop_instance_set_position, ":target_object", pos0),
             (prop_instance_animate_to_position, ":target_object", pos0, 1),
           (try_end),
           (store_sub, ":end_cond", ":num_gourds", "$g_training_ground_training_num_gourds_to_destroy"),
           #Second, removing gourds and their spikes randomly
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_random_in_range, ":random_instance", 0, ":num_gourds"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":random_instance"),
             (prop_instance_get_position, pos0, ":target_object"),
             (position_get_z, ":pos_z", pos0),
             (try_begin),
               (lt, ":pos_z", -50000),
               (val_add, ":end_cond", 1), #removed already, try again
             (else_try),
               (position_set_z, pos0, -100000),
               (prop_instance_set_position, ":target_object", pos0),
               (prop_instance_animate_to_position, ":target_object", pos0, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":random_instance"),
               (prop_instance_set_position, ":target_object_2", pos0),
               (prop_instance_animate_to_position, ":target_object_2", pos0, 1),
             (try_end),
           (try_end),
         (try_end),
         ],
       []),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_melee),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_training_ground_training_success_ratio", 100),
         (else_try),
           (assign, ":alive_enemies", 0),
           (try_for_agents, ":agent_no"),
             (agent_is_alive, ":agent_no"),
             (agent_is_human, ":agent_no"),
             (agent_get_team, ":team_no", ":agent_no"),
             (eq, ":team_no", 1),
             (val_add, ":alive_enemies", 1),
           (try_end),
           (store_sub, ":dead_enemies", "$g_training_ground_training_num_enemies", ":alive_enemies"),
           (store_mul, "$g_training_ground_training_success_ratio", ":dead_enemies", 100),
           (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_enemies"),
         (try_end),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_ranged),
         (get_player_agent_no, ":player_agent"),
         (agent_get_ammo, ":ammo", ":player_agent"),
         (store_mission_timer_a, ":cur_seconds"),
         (this_or_next|main_hero_fallen),
         (this_or_next|eq, ":ammo", 0),
         (gt, ":cur_seconds", 116),
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 10),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_mounted),
         (get_player_agent_no, ":player_agent"),
         (agent_get_horse, ":player_horse", ":player_agent"),
         (store_mission_timer_a, ":cur_seconds"),
         (this_or_next|lt, ":player_horse", 0),
         (this_or_next|main_hero_fallen),
         (this_or_next|ge, "$scene_num_total_gourds_destroyed", "$g_training_ground_training_num_gourds_to_destroy"),
         (gt, ":cur_seconds", 120),
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 100),
         (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_gourds_to_destroy"),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (0, 0, 0,
       [
         (gt, "$g_last_destroyed_gourds", 0),
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (entry_point_get_position, pos1, 0),
           (position_move_y, pos1, 100, 0),
           (get_player_agent_no, ":player_agent"),
           (agent_get_position, pos2, ":player_agent"),
           (try_begin),
             (position_is_behind_position, pos2, pos1),
             (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
           (else_try),
             (display_message, "@You must stay behind the line on the ground! Point is not counted."),
           (try_end),
         (else_try),
           (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
         (try_end),
         (assign, "$g_last_destroyed_gourds", 0),
         ],
       []),
    ],
  ),

  (
    "sneak_caught_fight",mtf_arena_fight,-1,
    "You must fight your way out!",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
      (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
#      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
    ],
    [
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,


      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),(eq,":answer",0),(jump_to_menu,"mnu_captivity_start_spacestation_defeat"),(finish_mission,0),]),

      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
      (0, 3, 0,
       [
           (main_hero_fallen,0),
        ],
       [(jump_to_menu,"mnu_captivity_start_spacestation_defeat"),(finish_mission,0)]),
      (5, 1, ti_once, [(num_active_teams_le,1),(neg|main_hero_fallen)],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),(finish_mission,1)]),
      (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    ],
###>> Motomataru's AI
#AI_triggers,
  ),

   (
    "ai_training",0,-1,
    "You start training.",
    [
#     (0,0,af_override_horse,aif_start_alarmed,1,[]),
     (0,0,0,aif_start_alarmed,30,[]),
#     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
#     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
#     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
#     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
     ],
    [
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),

      (0, 0, ti_once, [], [(assign,"$g_presentation_battle_active", 0),
                           ]),

      common_battle_order_panel,
      common_battle_order_panel_tick,
    ],
  ),
   (
    "camera_test",0,-1,
    "camera Test.",
    [
#     (0,mtef_attackers,0,aif_start_alarmed,5,[]),
     ],
    [
      (1, 0, 0, [(mission_cam_set_mode,1),
          (entry_point_get_position, pos3, 3),
          (mission_cam_set_position, pos3)], []),
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),
    ],
  ),

  (
    "arena_melee_fight",mtf_arena_fight,-1,
    #"You enter a melee fight in the arena.",
	"You enter a fight in the arena.",
    [

	  #SW - 0 to 31 used for tournament participants ?		switched af_override_all to af_override_everything (so it also overrides boots, so I added boots to all of these)
      (0,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_speeder,itm_vibro_sword2b]),
      (1,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (2,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_speeder,itm_vibro_axe_long_2h]),
      (3,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_energy_shield_yellow_medium,itm_vibro_sword1b]),
      (4,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (5,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_speeder,itm_vibro_sword2b]),
      (6,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_energy_shield_yellow_medium,itm_vibro_axe_medium_1h]),
      (7,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_red,itm_vibro_axe_long_2h]),

      (8,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_speeder,itm_vibro_sword2b]),
      (9,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (10,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_speeder,itm_vibro_axe_long_2h]),
      (11,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_energy_shield_yellow_medium,itm_vibro_sword1b]),
      (12,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (13,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_speeder,itm_vibro_sword2b]),
      (14,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_energy_shield_yellow_medium,itm_vibro_axe_medium_1h]),
      (15,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_blue,itm_vibro_axe_long_2h]),

      (16,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_speeder,itm_vibro_sword2b]),
      (17,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (18,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_speeder,itm_vibro_axe_long_2h]),
      (19,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_energy_shield_yellow_medium,itm_vibro_sword1b]),
      (20,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (21,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_speeder,itm_vibro_sword2b]),
      (22,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_energy_shield_yellow_medium,itm_vibro_axe_medium_1h]),
      (23,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_green,itm_vibro_axe_long_2h]),

      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_speeder,itm_vibro_sword2b]),
      (25,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (26,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_speeder,itm_vibro_axe_long_2h]),
      (27,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_energy_shield_yellow_medium,itm_vibro_sword1b]),
      (28,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_energy_shield_yellow_medium,itm_vibro_sword3_gold]),
      (29,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_speeder,itm_vibro_sword2b]),
      (30,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_energy_shield_yellow_medium,itm_vibro_axe_medium_1h]),
      (31,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_yellow,itm_vibro_axe_long_2h]),
#32
#SW - these appear to be used for the arena fight (ie. force-sensitive arena)
      # (3, mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_green_arena,itm_force_block,itm_arena_tunic_green]),
      # (11,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_green_arena,itm_lightsaber_block_green,itm_arena_tunic_green]),
      # (19,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_blue_arena,itm_force_block,itm_arena_tunic_blue]),
      # (27,mtef_visitor_source|mtef_team_4,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_blue_arena,itm_lightsaber_block_blue,itm_arena_tunic_blue]),
      # (4, mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_yellow_arena,itm_force_block,itm_arena_tunic_yellow]),
      # (12,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_yellow_arena,itm_lightsaber_block_yellow,itm_arena_tunic_yellow]),
      # (20,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_red_arena,itm_force_block,itm_arena_tunic_red]),
      # (28,mtef_visitor_source|mtef_team_4,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_lightsaber_red_arena,itm_lightsaber_block_red,itm_arena_tunic_red]),
      (3, mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_4,af_override_everything,aif_start_alarmed,1,[]),
      (4, mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_4,af_override_everything,aif_start_alarmed,1,[]),
#40-49 not used yet
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),
      (24,mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_leather_boots,itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_vibro_blade1]),

	  #SW - modified so you do not remove your helmet (removed af_override_head flag)
      (50, mtef_scene_source,af_override_horse|af_override_weapons,0,1,[]),
      (51, mtef_visitor_source,af_override_horse|af_override_weapons,0,1,[]),
      (52, mtef_scene_source,af_override_horse,0,1,[]),
#not used yet:
      (53, mtef_scene_source,af_override_horse,0,1,[]),(54, mtef_scene_source,af_override_horse,0,1,[]),(55, mtef_scene_source,af_override_horse,0,1,[]),
#used for torunament master scene
      (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_vibro_sword2b, itm_padded_cloth,itm_leather_cap]),
      (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_vibro_sword2b, itm_padded_cloth,itm_leather_cap]),
    ],
	tournament_triggers
  ),

################################## START OF SPARING KIT http://forums.taleworlds.net/index.php/topic,57741.0.html ############################
## Created a new template for sparring, just for simplicity - Jinnai
  ("arena_spar_fight",mtf_arena_fight,-1,
    "You enter a sparring match in the arena.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),

	  #SW - removed af_override_head since some characters should have helmets (ie. darth vader)
      #(50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
	  (50, mtef_scene_source,af_override_horse|af_override_weapons,0,1,[]),
      (52, mtef_scene_source,af_override_horse,0,1,[]),
      (53, mtef_scene_source,af_override_horse,0,1,[]),
      (54, mtef_scene_source,af_override_horse,0,1,[]),
      (55, mtef_scene_source,af_override_horse,0,1,[]),
    ],
    [
    (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
    (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
    (ti_tab_pressed, 0, 0, [],
      [(question_box,"@End the sparring match?")]),
    (ti_question_answered, 0, 0, [],
      [(store_trigger_param_1,":answer"),
       (eq,":answer",0),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_veteran_fighter"),
       (set_visitor, 36, "trp_champion_fighter"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
      ]),

    (0, 0, ti_once, [],
      [(play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
      ]),

    (0.1, 0, 0, [],
      [
	    (get_player_agent_no,":player_no"),		#added to get the player agent
        (try_for_agents,":agent"),
		  (neq,":agent",":player_no"),			#added so player won't have particle effects
          (agent_is_alive,":agent"),
          (agent_is_human,":agent"),
          (agent_get_position,pos1,":agent"),
          (position_set_z_to_ground_level, pos1),
          (agent_get_horse,":horse",":agent"),
          (try_begin),
            (gt,":horse",0),
            (position_move_z,pos1,300),
          (else_try),
            (position_move_z,pos1,225),
          (try_end),
          (agent_get_team, ":team", ":agent"),
          (try_begin),
            (eq,":team",0),
            (particle_system_burst,"psys_team_0",pos1,30),
          (else_try),
            (eq,":team",1),
            (particle_system_burst,"psys_team_1",pos1,30),
          (else_try),
            (eq,":team",2),
            (particle_system_burst,"psys_team_2",pos1,30),
          (else_try),
            (eq,":team",3),
            (particle_system_burst,"psys_team_3",pos1,30),
          (try_end),
        (try_end),
      ]),

    (1, 4, ti_once, [(num_active_teams_le, 1)],
      [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_play_victorious_sound"),
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_veteran_fighter"),
       (set_visitor, 36, "trp_champion_fighter"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
      ]),

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    ],
  ),
################################## END OF SPARING KIT http://forums.taleworlds.net/index.php/topic,57741.0.html ############################
  (
    "arena_challenge_fight",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [
      (56, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
      (58, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
    ],
    [
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_duel_for_lady"),
           (else_try),
             (call_script, "script_succeed_quest", "qst_duel_for_lady"),
           (try_end),
           (finish_mission),
           ]),
    ],
###>> Motomataru's AI
#AI_triggers,
  ),

##   (
##    "tutorial",0,-1,
##    "You enter the training ground.",
##    [
##        (1,mtef_leader_only,af_override_horse,0,1,[]), #af_override_weapons
##        (2,mtef_scene_source,af_override_horse,0,1,[]), #af_override_weapons
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [(question_box,"str_do_you_wish_to_leave_tutorial")]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),
##        (eq,":answer",0),
##        (finish_mission,0),
##        (leave_encounter),
##        (change_screen_return),
##        (troop_remove_item, "trp_player", "itm_tutorial_sword"),
##        (troop_remove_item, "trp_player", "itm_tutorial_axe"),
##        (troop_remove_item, "trp_player", "itm_tutorial_spear"),
##        (troop_remove_item, "trp_player", "itm_tutorial_club"),
##        (troop_remove_item, "trp_player", "itm_tutorial_battle_axe"),
##        (troop_remove_item, "trp_player", "itm_tutorial_arrows"),
##        (troop_remove_item, "trp_player", "itm_tutorial_bolts"),
##        (troop_remove_item, "trp_player", "itm_tutorial_short_bow"),
##        (troop_remove_item, "trp_player", "itm_tutorial_crossbow"),
##        (troop_remove_item, "trp_player", "itm_tutorial_throwing_daggers"),
##
##        (check_quest_active, "qst_destroy_dummies"),
##        (cancel_quest,"qst_destroy_dummies"),
##        ]),
###      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_tutorial")], []),
##      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
##
##
##      (0, 0, ti_once, [],
##       [
##        (assign, "$tutorial_enter_melee", 0),
##        (assign, "$tutorial_enter_ranged", 0),
##        (assign, "$tutorial_enter_mounted", 0),
##        (assign, "$tutorial_camp_stage", 0),
##        (assign, "$tutorial_quest_taken", 0),
##        (assign, "$tutorial_quest_succeeded", 0),
##        (assign, "$tutorial_num_total_dummies_destroyed", 0),
##        (assign, "$tutorial_melee_chest", 0),
##        (assign, "$tutorial_ranged_chest", 0),
##        (assign, "$tutorial_award_taken", 0),
##
##
##        (entry_point_get_position,2,2),#Trainer
##        (entry_point_get_position,16,16),#Horse
##        (set_spawn_position, 16),
##        (spawn_horse, "itm_tutorial_saddle_horse"),
##
##        (troop_remove_item, "trp_tutorial_chest_1", "itm_tutorial_sword"),
##        (troop_remove_item, "trp_tutorial_chest_1", "itm_tutorial_axe"),
##        (troop_remove_item, "trp_tutorial_chest_1", "itm_tutorial_spear"),
##        (troop_remove_item, "trp_tutorial_chest_1", "itm_tutorial_club"),
##        (troop_remove_item, "trp_tutorial_chest_1", "itm_tutorial_battle_axe"),
##        (troop_remove_item, "trp_tutorial_chest_2", "itm_tutorial_arrows"),
##        (troop_remove_item, "trp_tutorial_chest_2", "itm_tutorial_bolts"),
##        (troop_remove_item, "trp_tutorial_chest_2", "itm_tutorial_short_bow"),
##        (troop_remove_item, "trp_tutorial_chest_2", "itm_tutorial_crossbow"),
##        (troop_remove_item, "trp_tutorial_chest_2", "itm_tutorial_throwing_daggers"),
##        (troop_add_item, "trp_tutorial_chest_1", "itm_tutorial_sword"),
##        (troop_add_item, "trp_tutorial_chest_1", "itm_tutorial_axe"),
##        (troop_add_item, "trp_tutorial_chest_1", "itm_tutorial_spear"),
##        (troop_add_item, "trp_tutorial_chest_1", "itm_tutorial_club"),
##        (troop_add_item, "trp_tutorial_chest_1", "itm_tutorial_battle_axe"),
##        (troop_add_item, "trp_tutorial_chest_2", "itm_tutorial_arrows"),
##        (troop_add_item, "trp_tutorial_chest_2", "itm_tutorial_bolts"),
##        (troop_add_item, "trp_tutorial_chest_2", "itm_tutorial_short_bow"),
##        (troop_add_item, "trp_tutorial_chest_2", "itm_tutorial_crossbow"),
##        (troop_add_item, "trp_tutorial_chest_2", "itm_tutorial_throwing_daggers"),
##        ]
##       ),
##
##      (1, 0, ti_once, [(store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (get_player_agent_no, ":player_agent"),
##                       (ge, ":player_agent", 0),
##                       (agent_get_position, pos1, ":player_agent"),
##                       (entry_point_get_position,3,3),
##                       (get_distance_between_positions, ":distance_to_area", 1, 3),
##                       (lt, ":distance_to_area", 500),
##                       (eq, "$tutorial_enter_melee", 0),],
##       [(tutorial_box,"str_tutorial_enter_melee", "str_tutorial"), (val_add,"$tutorial_enter_melee", 1)]),
##      (1, 0, ti_once, [(store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (get_player_agent_no, ":player_agent"),
##                       (ge, ":player_agent", 0),
##                       (neg|conversation_screen_is_active),
##                       (agent_get_position, pos1, ":player_agent"),
##                       (entry_point_get_position,4,4),
##                       (get_distance_between_positions, ":distance_to_area", 1, 4),
##                       (lt, ":distance_to_area", 500),
##                       (eq, "$tutorial_enter_ranged", 0),],
##       [(tutorial_box,"str_tutorial_enter_ranged", "str_tutorial"), (val_add,"$tutorial_enter_ranged", 1)]),
##      (1, 0, ti_once, [(store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (get_player_agent_no, ":player_agent"),
##                       (ge, ":player_agent", 0),
##                       (neg|conversation_screen_is_active),
##                       (agent_get_position, pos1, ":player_agent"),
##                       (entry_point_get_position,5,5),
##                       (get_distance_between_positions, ":distance_to_area", 1, 5),
##                       (lt, ":distance_to_area", 500),
##                       (eq, "$tutorial_enter_mounted", 0),],
##       [(tutorial_box,"str_tutorial_enter_mounted", "str_tutorial"), (val_add,"$tutorial_enter_mounted", 1)]),
##
##
##      (2, 0, ti_once, [(store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (get_player_agent_no, ":player_agent"),
##                       (ge, ":player_agent", 0),
##                       (neg|conversation_screen_is_active),
##                       (agent_get_position, pos1, ":player_agent"),
##                       (entry_point_get_position,6,6),
##                       (get_distance_between_positions, ":distance_to_area", 1, 6),
##                       (lt, ":distance_to_area", 300),
##                       (eq, "$tutorial_melee_chest", 0),],
##       [(tutorial_box,"str_tutorial_melee_chest", "str_tutorial"), (val_add,"$tutorial_melee_chest", 1)]),
##      (2, 0, ti_once, [(store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (get_player_agent_no, ":player_agent"),
##                       (ge, ":player_agent", 0),
##                       (agent_get_position, pos1, ":player_agent"),
##                       (entry_point_get_position,7,7),
##                       (get_distance_between_positions, ":distance_to_area", 1, 7),
##                       (lt, ":distance_to_area", 300),
##                       (eq, "$tutorial_ranged_chest", 0),],
##       [(tutorial_box,"str_tutorial_ranged_chest", "str_tutorial"), (val_add,"$tutorial_ranged_chest", 1)]),
##
##      (2, 0, ti_once, [(store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (eq, "$tutorial_item_equipped", 0),
##                       (try_begin),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_sword"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_axe"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_spear"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_club"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_battle_axe"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_arrows"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_bolts"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_short_bow"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_crossbow"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (else_try),
##                         (troop_has_item_equipped, "trp_player", "itm_tutorial_throwing_daggers"),
##                         (assign, "$tutorial_item_equipped", 1),
##                       (try_end),
##                       (eq, "$tutorial_item_equipped", 1),],
##       [(tutorial_box,"str_tutorial_item_equipped", "str_tutorial")]),
##
##
##
##
###      (2, 0, ti_once, [(get_player_agent_no, ":player_agent"),
###                       (agent_get_position, pos1, ":player_agent"),
###                       (entry_point_get_position,21,21),
###                       (get_distance_between_positions, ":distance_to_area", 1, 21),
###                       (lt, ":distance_to_area", 200),
###                       (eq, "$tutorial_group_of_weapons", 0),],
###       [(tutorial_box,"str_tutorial_group_of_weapons", "str_tutorial"), (val_add,"$tutorial_group_of_weapons", 1)]),
##
##
##
##      (1, 5, ti_once, [(eq,"$tutorial_camp_stage",0),
##                       (neg|conversation_screen_is_active),
##                       (eq,"$tutorial_quest_award_taken",0),
##                       (store_character_level, ":player_level", "trp_player"),
##                       (le, ":player_level", 1),
##                       (tutorial_box,"str_tutorial_camp1","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",1)]),
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",1),
##                       (neg|conversation_screen_is_active),
##                       (tutorial_box,"str_tutorial_camp2","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",1)]),
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",2),
##                       (neg|conversation_screen_is_active),
##                       (tutorial_box,"str_tutorial_camp3","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",1)]),
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",3),(eq, "$tutorial_award_taken", 0),
##                       (neg|conversation_screen_is_active),
##                       (tutorial_box,"str_tutorial_camp4","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",2)]),
##
##
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",5),
##                       (neg|conversation_screen_is_active),
##                       (eq,"$tutorial_quest_taken",1),
##                       (tutorial_box,"str_tutorial_camp6","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",1)]),
##
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",6),
##                       (neg|conversation_screen_is_active),
##                       (ge,"$tutorial_num_total_dummies_destroyed",10),
##                       (tutorial_box,"str_tutorial_camp7","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",1), (assign,"$tutorial_quest_succeeded",1),]),
##
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",7),
##                       (neg|conversation_screen_is_active),
##                       (eq,"$tutorial_quest_award_taken",1),
##                       (tutorial_box,"str_tutorial_camp8","str_tutorial"),
##                       (troop_add_proficiency_points, "trp_player", 10),
##                       (assign, "$tutorial_last_proficiency_sum", 0),
##                       (try_for_range, ":cur_attribute", 0, num_weapon_proficiencies),
##                         (store_proficiency_level, ":cur_attribute_point", "trp_player", ":cur_attribute"),
##                         (val_add, "$tutorial_last_proficiency_sum", ":cur_attribute_point"),
##                       (try_end),],
##       [(val_add,"$tutorial_camp_stage",1),]),
##
##      (1, 3, ti_once, [(eq,"$tutorial_camp_stage",8),
##                       (neg|conversation_screen_is_active),
##                       (assign, ":new_proficiency_sum", 0),
##                       (try_for_range, ":cur_attribute", 0, num_weapon_proficiencies),
##                         (store_proficiency_level, ":cur_attribute_point", "trp_player", ":cur_attribute"),
##                         (val_add, ":new_proficiency_sum", ":cur_attribute_point"),
##                       (try_end),
##                       (assign, reg(48), ":new_proficiency_sum"),
##                       (assign, reg(49), "$tutorial_last_proficiency_sum"),
##                       (lt,"$tutorial_last_proficiency_sum",":new_proficiency_sum"),
##                       (tutorial_box,"str_tutorial_camp9","str_tutorial"),],
##          [(val_add,"$tutorial_camp_stage",1)]),
##
##      (2, 0, 0, [(check_quest_active,"qst_destroy_dummies"),
##                 (le, "$tutorial_num_total_dummies_destroyed", 10),],
##          [
##              (assign, ":progress", "$tutorial_num_total_dummies_destroyed"),
##              (val_mul, ":progress", 10),
##              (set_quest_progression,"qst_destroy_dummies",":progress"),
##              ]
##       ),
##
##    ],
##  ),

  (
    "tutorial_1",0,-1,
    "You enter the training ground.",
    [
	#SW - modified training weapons
    (0,mtef_leader_only,af_override_horse|af_override_weapons,0,1,[itm_arena_tunic_white,itm_energy_shield_yellow_small,itm_tutorial_lightsaber,itm_practice_dl44,itm_laser_bolts_training_pistol]), #af_override_weapons
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [(try_begin),
         (lt, "$tutorial_1_state", 5),
         (question_box, "str_do_you_wish_to_leave_tutorial"),
        (else_try),
          (finish_mission,0),
        (try_end),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (finish_mission,0),
        ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message, "str_cant_use_inventory_tutorial")], []),

      (0, 0, ti_once, [(assign, "$tutorial_1_state", 0),
                       (assign, "$tutorial_1_msg_1_displayed", 0),
                       (assign, "$tutorial_1_msg_2_displayed", 0),
                       (assign, "$tutorial_1_msg_3_displayed", 0),
                       (assign, "$tutorial_1_msg_4_displayed", 0),
                       (assign, "$tutorial_1_msg_5_displayed", 0),
                       (assign, "$tutorial_1_msg_6_displayed", 0),
                       ], []),

      (0, 0, 0, [(try_begin),
                   (eq, "$tutorial_1_state", 0),
                   (try_begin),
                     (eq, "$tutorial_1_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_1_msg_1_displayed", 1),
                     (tutorial_message, "str_tutorial_1_msg_1"),
                     (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                     (entry_point_get_position,pos1,1),
                     (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (try_end),
                   (tutorial_message, "str_tutorial_1_msg_1"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position,pos2,1),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 100),
                   (val_add, "$tutorial_1_state", 1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (entry_point_get_position,pos1,2),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_1_state", 1),
                   (try_begin),
                     (eq, "$tutorial_1_msg_2_displayed", 0),
                     (assign, "$tutorial_1_msg_2_displayed", 1),
                     (tutorial_message, "str_tutorial_1_msg_2"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position,pos2,2),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 100),
                   (val_add, "$tutorial_1_state", 1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 1),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (entry_point_get_position,pos1,3),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_1_state", 2),
                   (try_begin),
                     (eq, "$tutorial_1_msg_3_displayed", 0),
                     (assign, "$tutorial_1_msg_3_displayed", 1),
                     (tutorial_message, "str_tutorial_1_msg_3"),
                     (assign, "$tutorial_num_total_dummies_destroyed", 0),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (ge, "$tutorial_num_total_dummies_destroyed", 4),
                   (val_add, "$tutorial_1_state", 1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 2),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                 (else_try),
                   (eq, "$tutorial_1_state", 3),
                   (try_begin),
                     (eq, "$tutorial_1_msg_4_displayed", 0),
                     (assign, "$tutorial_1_msg_4_displayed", 1),
                     (tutorial_message, "str_tutorial_1_msg_4"),
                     (store_mission_timer_a, "$tutorial_time"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (store_mission_timer_a, ":cur_time"),
                   (val_sub, ":cur_time", "$tutorial_time"),
                   (gt, ":cur_time", 10),
                   (val_add, "$tutorial_1_state", 1),
                 (else_try),
                   (eq, "$tutorial_1_state", 4),
                   (try_begin),
                     (eq, "$tutorial_1_msg_5_displayed", 0),
                     (assign, "$tutorial_1_msg_5_displayed", 1),
                     (tutorial_message, "str_tutorial_1_msg_5"),
                     (assign, "$g_last_archery_point_earned", 0),
                     (assign, "$tutorial_num_arrows_hit", 0),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (try_begin),
                     (get_player_agent_no, ":player_agent"),
                     (agent_get_ammo, ":cur_ammo", ":player_agent"),
                     (le, ":cur_ammo", 0),
                     (agent_refill_ammo, ":player_agent"),
                     (tutorial_message, "str_tutorial_ammo_refilled"),
                   (try_end),
                   (gt, "$g_last_archery_point_earned", 0),
                   (assign, "$g_last_archery_point_earned", 0),
                   (val_add, "$tutorial_num_arrows_hit", 1),
                   (gt, "$tutorial_num_arrows_hit", 2),
                   (val_add, "$tutorial_1_state", 1),
                 (else_try),
                   (eq, "$tutorial_1_state", 5),
                   (eq, "$tutorial_1_msg_6_displayed", 0),
                   (assign, "$tutorial_1_msg_6_displayed", 1),
                   (tutorial_message, "str_tutorial_1_msg_6"),
                   (play_sound, "snd_tutorial_2"),
                   (assign, "$tutorial_1_finished", 1),
                 (try_end),
                 ], []),
    ],
  ),


  (
    "tutorial_2",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
		#SW - modified training shield
        (0,mtef_leader_only|mtef_team_0,af_override_horse|af_override_weapons,0,1,[itm_tutorial_energy_shield]),
        (2,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
        (4,mtef_visitor_source|mtef_team_1,0,0,1,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [(try_begin),
         (lt, "$tutorial_2_state", 9),
         (question_box,"str_do_you_wish_to_leave_tutorial"),
        (else_try),
          (finish_mission,0),
        (try_end),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (finish_mission,0),
        ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_tutorial")], []),
      (0, 0, ti_once, [
          (store_mission_timer_a, ":cur_time"),
          (gt, ":cur_time", 2),
          (main_hero_fallen),
          (assign, "$tutorial_2_state", 100),
        ], []),

      (0, 0, ti_once, [(assign, "$tutorial_2_state", 0),
                       (assign, "$tutorial_2_msg_1_displayed", 0),
                       (assign, "$tutorial_2_msg_2_displayed", 0),
                       (assign, "$tutorial_2_msg_3_displayed", 0),
                       (assign, "$tutorial_2_msg_4_displayed", 0),
                       (assign, "$tutorial_2_msg_5_displayed", 0),
                       (assign, "$tutorial_2_msg_6_displayed", 0),
                       (assign, "$tutorial_2_msg_7_displayed", 0),
                       (assign, "$tutorial_2_msg_8_displayed", 0),
                       (assign, "$tutorial_2_msg_9_displayed", 0),
                       (assign, "$tutorial_2_melee_agent_state", 0),
                       ], []),

      (10, 0, 0, [(call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_archer"),
                  (agent_refill_ammo, reg0)], []),

      (0, 0, 0, [(try_begin),
                   (eq, "$tutorial_2_state", 0),
                   (try_begin),
                     (eq, "$tutorial_2_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_2_msg_1_displayed", 1),
                     (tutorial_message, "str_tutorial_2_msg_1"),
                     (team_give_order, 1, grc_everyone, mordr_stand_ground),
                     (team_give_order, 1, grc_infantry, mordr_charge),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (agent_get_position, pos1, ":cur_agent"),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position,pos2,1),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 1),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 0),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 2),
                   (try_begin),
                     (eq, "$tutorial_2_melee_agent_state", 0),
                     (val_add, "$tutorial_2_melee_agent_state", 1),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (entry_point_get_position, pos1, 3),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (else_try),
                     (eq, "$tutorial_2_melee_agent_state", 1),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (entry_point_get_position, pos1, 3),
                     (agent_get_position, pos2, ":cur_agent"),
                     (get_distance_between_positions, ":cur_distance", pos1, pos2),
                     (le, ":cur_distance", 250),
                     (agent_clear_scripted_mode, ":cur_agent"),
                     (val_add, "$tutorial_2_melee_agent_state", 1),
                     (store_mission_timer_a,"$tutorial_time"),
                   (else_try),
                     (eq, "$tutorial_2_melee_agent_state", 2),
                     (try_begin),
                       (eq, "$tutorial_2_msg_2_displayed", 0),
                       (assign, "$tutorial_2_msg_2_displayed", 1),
                       (play_sound, "snd_tutorial_1"),
                     (try_end),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (store_mission_timer_a,":cur_time"),
                     (val_sub, ":cur_time", "$tutorial_time"),
                     (store_sub, reg3, 20, ":cur_time"),
                     (tutorial_message, "str_tutorial_2_msg_2"),
                     (gt, ":cur_time", 20),
                     (entry_point_get_position, pos1, 3),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                     (val_add, "$tutorial_2_melee_agent_state", 1),
                   (else_try),
                     (eq, "$tutorial_2_melee_agent_state", 3),
                     (try_begin),
                       (eq, "$tutorial_2_msg_3_displayed", 0),
                       (assign, "$tutorial_2_msg_3_displayed", 1),
                       (tutorial_message, "str_tutorial_2_msg_3"),
                       (play_sound, "snd_tutorial_1"),
                     (try_end),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (entry_point_get_position, pos1, 3),
                     (agent_get_position, pos2, ":cur_agent"),
                     (get_distance_between_positions, ":cur_distance", pos1, pos2),
                     (le, ":cur_distance", 250),
                     (entry_point_get_position, pos1, 2),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                     (val_add, "$tutorial_2_melee_agent_state", 1),
                   (else_try),
                     (eq, "$tutorial_2_melee_agent_state", 4),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (entry_point_get_position, pos1, 2),
                     (agent_get_position, pos2, ":cur_agent"),
                     (get_distance_between_positions, ":cur_distance", pos1, pos2),
                     (le, ":cur_distance", 250),
                     (entry_point_get_position, pos1, 30),
                     (agent_set_position, ":cur_agent", pos1),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                     (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 1),
                     (prop_instance_get_position, pos1, ":door_object"),
                     #(position_rotate_z, pos1, 90),
					 (position_move_z,pos1,400),
                     (prop_instance_animate_to_position, ":door_object", pos1, 150),
                     (val_add, "$tutorial_2_melee_agent_state", 1),
                     (val_add, "$tutorial_2_state", 1),
                   (try_end),
                 (else_try),
                   (eq, "$tutorial_2_state", 3),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 1),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 1),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (store_mission_timer_a,"$tutorial_time"),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 4),
                   (try_begin),
                     (eq, "$tutorial_2_msg_4_displayed", 0),
                     (assign, "$tutorial_2_msg_4_displayed", 1),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (store_mission_timer_a,":cur_time"),
                   (val_sub, ":cur_time", "$tutorial_time"),
                   (store_sub, reg3, 20, ":cur_time"),
                   (tutorial_message, "str_tutorial_2_msg_4"),
                   (gt, ":cur_time", 20),
                   (entry_point_get_position,pos1,5),
                   (set_spawn_position, pos1),
                   #SW - modified training sword
				   (spawn_item, "itm_tutorial_lightsaber"),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 3),
                   (agent_set_position, ":cur_agent", pos1),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 2),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 5),
                   (try_begin),
                     (eq, "$tutorial_2_msg_5_displayed", 0),
                     (assign, "$tutorial_2_msg_5_displayed", 1),
                     (tutorial_message, "str_tutorial_2_msg_5"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 2),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 2),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 6),
                   (try_begin),
                     (eq, "$tutorial_2_msg_6_displayed", 0),
                     (assign, "$tutorial_2_msg_6_displayed", 1),
                     (tutorial_message, "str_tutorial_2_msg_6"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   #SW - modified tutorial sword
				   (agent_has_item_equipped, ":player_agent", "itm_tutorial_lightsaber"),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 3),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 7),
                   (try_begin),
                     (eq, "$tutorial_2_msg_7_displayed", 0),
                     (assign, "$tutorial_2_msg_7_displayed", 1),
                     (tutorial_message, "str_tutorial_2_msg_7"),
                     (play_sound, "snd_tutorial_1"),
                     (get_player_agent_no, ":player_agent"),
                     (agent_set_hit_points, ":player_agent", 100),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_archer"),
                   (assign, ":cur_agent", reg0),
                   (neg|agent_is_alive, ":cur_agent"),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (agent_clear_scripted_mode, ":cur_agent"),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_a", 4),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 8),
                   (try_begin),
                     (eq, "$tutorial_2_msg_8_displayed", 0),
                     (assign, "$tutorial_2_msg_8_displayed", 1),
                     (tutorial_message, "str_tutorial_2_msg_8"),
                     (play_sound, "snd_tutorial_1"),
                     (get_player_agent_no, ":player_agent"),
                     (agent_set_hit_points, ":player_agent", 100),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (neg|agent_is_alive, ":cur_agent"),
                   (val_add, "$tutorial_2_state", 1),
                 (else_try),
                   (eq, "$tutorial_2_state", 9),
                   (eq, "$tutorial_2_msg_9_displayed", 0),
                   (assign, "$tutorial_2_msg_9_displayed", 1),
                   (tutorial_message, "str_tutorial_2_msg_9"),
                   (play_sound, "snd_tutorial_2"),
                   (assign, "$tutorial_2_finished", 1),
                 (else_try),
                   (gt, "$tutorial_2_state", 30),
                   (tutorial_message, "str_tutorial_failed"),
                 (try_end),
                 ], []),
    ],
  ),

  (
    "tutorial_3",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
        (0,mtef_leader_only|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
        (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
        (5,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [(try_begin),
         (lt, "$tutorial_3_state", 12),
         (question_box,"str_do_you_wish_to_leave_tutorial"),
        (else_try),
          (finish_mission,0),
        (try_end),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (finish_mission,0),
        ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_tutorial")], []),

      (0, 0, ti_once, [
          (store_mission_timer_a, ":cur_time"),
          (gt, ":cur_time", 2),
          (main_hero_fallen),
          (assign, "$tutorial_3_state", 100),
        ], []),

      (0, 0, ti_once, [(assign, "$tutorial_3_state", 0),
                       (assign, "$tutorial_3_msg_1_displayed", 0),
                       (assign, "$tutorial_3_msg_2_displayed", 0),
                       (assign, "$tutorial_3_msg_3_displayed", 0),
                       (assign, "$tutorial_3_msg_4_displayed", 0),
                       (assign, "$tutorial_3_msg_5_displayed", 0),
                       (assign, "$tutorial_3_msg_6_displayed", 0),
                       ], []),

      (0, 0, 0, [(try_begin),
                   (eq, "$tutorial_3_state", 0),
                   (try_begin),
                     (eq, "$tutorial_3_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_3_msg_1_displayed", 1),
                     (tutorial_message, "str_tutorial_3_msg_1"),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (agent_get_position, pos1, ":cur_agent"),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                     (assign, ":cur_agent", reg0),
                     (agent_get_position, pos1, ":cur_agent"),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                     (entry_point_get_position, pos1, 1),
                     (set_spawn_position, pos1),
					 #SW - modified training items
					 (spawn_item, "itm_practice_vibro_axe_long_no_attack"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   #SW - modified training items
				   (agent_has_item_equipped, ":player_agent", "itm_practice_vibro_axe_long_no_attack"),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 1),
                   (try_begin),
                     (eq, "$tutorial_3_msg_2_displayed", 0),
                     (assign, "$tutorial_3_msg_2_displayed", 1),
                     (tutorial_message, "str_tutorial_3_msg_2"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position,pos2,2),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 2),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 0),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 3),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 4),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 4),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 4),
                   (agent_get_position, pos2, ":cur_agent"),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 250),
                   (agent_clear_scripted_mode, ":cur_agent"),
                   (val_add, "$tutorial_3_state", 1),
                   (store_mission_timer_a,"$tutorial_time"),
                 (else_try),
                   (eq, "$tutorial_3_state", 5),
                   (try_begin),
                     (eq, "$tutorial_3_msg_3_displayed", 0),
                     (assign, "$tutorial_3_msg_3_displayed", 1),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (store_mission_timer_a,":cur_time"),
                   (val_sub, ":cur_time", "$tutorial_time"),
                   (store_sub, reg3, 30, ":cur_time"),
                   (tutorial_message, "str_tutorial_3_msg_3"),
                   (gt, ":cur_time", 30),
                   (entry_point_get_position, pos1, 4),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 6),
                   (try_begin),
                     (eq, "$tutorial_3_msg_4_displayed", 0),
                     (assign, "$tutorial_3_msg_4_displayed", 1),
                     (tutorial_message, "str_tutorial_3_msg_4"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 4),
                   (agent_get_position, pos2, ":cur_agent"),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 250),
                   (entry_point_get_position, pos1, 3),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 7),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 3),
                   (agent_get_position, pos2, ":cur_agent"),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 250),
                   (entry_point_get_position, pos1, 7),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (agent_set_position, ":cur_agent", pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 1),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 3),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 8),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 1),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 1),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 9),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 6),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 10),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 6),
                   (agent_get_position, pos2, ":cur_agent"),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 250),
                   (agent_clear_scripted_mode, ":cur_agent"),
                   (val_add, "$tutorial_3_state", 1),
                   (store_mission_timer_a,"$tutorial_time"),
                 (else_try),
                   (eq, "$tutorial_3_state", 11),
                   (try_begin),
                     (eq, "$tutorial_3_msg_5_displayed", 0),
                     (assign, "$tutorial_3_msg_5_displayed", 1),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (assign, ":cur_agent", reg0),
                   (store_mission_timer_a,":cur_time"),
                   (val_sub, ":cur_time", "$tutorial_time"),
                   (store_sub, reg3, 30, ":cur_time"),
                   (tutorial_message, "str_tutorial_3_msg_5"),
                   (gt, ":cur_time", 30),
                   (entry_point_get_position, pos1, 6),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 12),
                   (try_begin),
                     (eq, "$tutorial_3_msg_6_displayed", 0),
                     (assign, "$tutorial_3_msg_6_displayed", 1),
                     (tutorial_message, "str_tutorial_3_msg_6"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 6),
                   (agent_get_position, pos2, ":cur_agent"),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 250),
                   (entry_point_get_position, pos1, 5),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 13),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (assign, ":cur_agent", reg0),
                   (entry_point_get_position, pos1, 5),
                   (agent_get_position, pos2, ":cur_agent"),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 250),
                   (entry_point_get_position, pos1, 7),
                   (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (agent_set_position, ":cur_agent", pos1),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (gt, "$tutorial_3_state", 30),
                   (tutorial_message, "str_tutorial_failed"),
                 (try_end),
                 ], []),
    ],
  ),

  (
    "tutorial_3_2",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
        #SW - modified training items
		(0,mtef_leader_only|mtef_team_0,af_override_horse|af_override_weapons,0,1,[itm_practice_vibro_axe_long]),
        (4,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
        (6,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [(try_begin),
         (lt, "$tutorial_3_state", 5),
         (question_box,"str_do_you_wish_to_leave_tutorial"),
        (else_try),
          (finish_mission,0),
        (try_end),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (finish_mission,0),
        ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_tutorial")], []),

      (0, 0, ti_once, [
          (store_mission_timer_a, ":cur_time"),
          (gt, ":cur_time", 2),
          (main_hero_fallen),
          (assign, "$tutorial_3_state", 100),
        ], []),


      (0, 0, ti_once, [(assign, "$tutorial_3_state", 0),
                       (assign, "$tutorial_3_msg_1_displayed", 0),
                       (assign, "$tutorial_3_msg_2_displayed", 0),
                       (assign, "$tutorial_3_msg_3_displayed", 0),
                       (assign, "$tutorial_3_msg_4_displayed", 0),
                       (assign, "$tutorial_3_msg_5_displayed", 0),
                       ], []),

      (0, 0, 0, [(try_begin),
                   (eq, "$tutorial_3_state", 0),
                   (try_begin),
                     (eq, "$tutorial_3_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_3_msg_1_displayed", 1),
                     (tutorial_message, "str_tutorial_3_2_msg_1"),
                     (play_sound, "snd_tutorial_1"),
                     (call_script, "script_cf_get_first_agent_with_troop_id","trp_tutorial_maceman"),
                     (assign, ":cur_agent", reg0),
                     (agent_get_position, pos1, ":cur_agent"),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                     (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                     (assign, ":cur_agent", reg0),
                     (agent_get_position, pos1, ":cur_agent"),
                     (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position,pos2,2),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 1),
                   (try_begin),
                     (eq, "$tutorial_3_msg_2_displayed", 0),
                     (assign, "$tutorial_3_msg_2_displayed", 1),
                     (tutorial_message, "str_tutorial_3_2_msg_2"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 0),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 0),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (agent_clear_scripted_mode, reg0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 2),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_maceman"),
                   (neg|agent_is_alive, reg0),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 1),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 3),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, -90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 3),
                   (try_begin),
                     (eq, "$tutorial_3_msg_3_displayed", 0),
                     (assign, "$tutorial_3_msg_3_displayed", 1),
                     (tutorial_message, "str_tutorial_3_2_msg_3"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (scene_prop_get_instance, ":barrier_object", "spr_barrier_4m", 1),
                   (prop_instance_get_position, pos1, ":barrier_object"),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos2, ":player_agent"),
                   (position_is_behind_position, pos2, pos1),
                   (scene_prop_get_instance, ":door_object", "spr_tutorial_door_b", 1),
                   (prop_instance_get_position, pos1, ":door_object"),
                   #(position_rotate_z, pos1, 90),
				   (position_move_z,pos1,400),
                   (prop_instance_animate_to_position, ":door_object", pos1, 150),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (agent_clear_scripted_mode, reg0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 4),
                   (try_begin),
                     (eq, "$tutorial_3_msg_4_displayed", 0),
                     (assign, "$tutorial_3_msg_4_displayed", 1),
                     (tutorial_message, "str_tutorial_3_2_msg_4"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_get_first_agent_with_troop_id", "trp_tutorial_swordsman"),
                   (neg|agent_is_alive, reg0),
                   (val_add, "$tutorial_3_state", 1),
                 (else_try),
                   (eq, "$tutorial_3_state", 5),
                   (eq, "$tutorial_3_msg_5_displayed", 0),
                   (assign, "$tutorial_3_msg_5_displayed", 1),
                   (tutorial_message, "str_tutorial_3_2_msg_5"),
                   (play_sound, "snd_tutorial_2"),
                   (assign, "$tutorial_3_finished", 1),
                 (else_try),
                   (gt, "$tutorial_3_state", 30),
                   (tutorial_message, "str_tutorial_failed"),
                 (try_end),
                 ], []),


    ],
  ),

  (
    "tutorial_4",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
        #SW - modified tutorial items
		(0,mtef_leader_only|mtef_team_0,af_override_horse|af_override_weapons,0,1,[itm_arena_tunic_white,itm_tutorial_lightsaber,itm_practice_dl44,itm_laser_bolts_training_pistol]), #af_override_weapons
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [(try_begin),
         (lt, "$tutorial_4_state", 11),
         (question_box,"str_do_you_wish_to_leave_tutorial"),
        (else_try),
          (finish_mission,0),
        (try_end),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (finish_mission,0),
        ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_tutorial")], []),

      (0, 0, ti_once, [(assign, "$tutorial_4_state", 0),
                       (assign, "$tutorial_4_msg_1_displayed", 0),
                       (assign, "$tutorial_4_msg_2_displayed", 0),
                       (assign, "$tutorial_4_msg_3_displayed", 0),
                       (assign, "$tutorial_4_msg_4_displayed", 0),
                       (assign, "$tutorial_4_msg_5_displayed", 0),
                       (assign, "$tutorial_4_msg_6_displayed", 0),
                       (assign, "$tutorial_4_msg_7_displayed", 0),
                       ], []),

      (0, 0, 0, [(try_begin),
                   (eq, "$tutorial_4_state", 0),
                   (try_begin),
                     (eq, "$tutorial_4_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_4_msg_1_displayed", 1),
                     (tutorial_message, "str_tutorial_4_msg_1"),
                     (entry_point_get_position, pos1, 1),
                     (set_spawn_position, 1),
                     #SW - modified tutorial items
					 (spawn_horse, "itm_practice_speeder"),
                     (assign, "$tutorial_num_total_dummies_destroyed", 0),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_horse, ":horse_agent", ":player_agent"),
                   (ge, ":horse_agent", 0),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 2),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 1),
                   (try_begin),
                     (eq, "$tutorial_4_msg_2_displayed", 0),
                     (assign, "$tutorial_4_msg_2_displayed", 1),
                     (tutorial_message, "str_tutorial_4_msg_2"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 2),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 3),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 2),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 3),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 4),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 3),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 4),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 5),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 4),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 5),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 6),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 5),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 6),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 1),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 6),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 1),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 7),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 7),
                   (try_begin),
                     (eq, "$tutorial_4_msg_3_displayed", 0),
                     (assign, "$tutorial_4_msg_3_displayed", 1),
                     (tutorial_message, "str_tutorial_4_msg_3"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 7),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 20),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 8),
                   (try_begin),
                     (eq, "$tutorial_4_msg_4_displayed", 0),
                     (assign, "$tutorial_4_msg_4_displayed", 1),
                     (tutorial_message, "str_tutorial_4_msg_4"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (ge, "$tutorial_num_total_dummies_destroyed", 2),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 8),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 9),
                   (try_begin),
                     (eq, "$tutorial_4_msg_5_displayed", 0),
                     (assign, "$tutorial_4_msg_5_displayed", 1),
                     (tutorial_message, "str_tutorial_4_msg_5"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 8),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 200),
                   (val_add, "$tutorial_4_state", 1),
                   (entry_point_get_position, pos1, 20),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 10),
                   (try_begin),
                     (eq, "$tutorial_4_msg_6_displayed", 0),
                     (assign, "$tutorial_4_msg_6_displayed", 1),
                     (tutorial_message, "str_tutorial_4_msg_6"),
                     (play_sound, "snd_tutorial_1"),
                     (assign, "$g_last_archery_point_earned", 0),
                     (assign, "$tutorial_num_arrows_hit", 0),
                   (try_end),
                   (try_begin),
                     (get_player_agent_no, ":player_agent"),
                     (agent_get_ammo, ":cur_ammo", ":player_agent"),
                     (le, ":cur_ammo", 0),
                     (agent_refill_ammo, ":player_agent"),
                     (tutorial_message, "str_tutorial_ammo_refilled"),
                   (try_end),
                   (gt, "$g_last_archery_point_earned", 0),
                   (assign, "$g_last_archery_point_earned", 0),
                   (val_add, "$tutorial_num_arrows_hit", 1),
                   (gt, "$tutorial_num_arrows_hit", 2),
                   (val_add, "$tutorial_4_state", 1),
                 (else_try),
                   (eq, "$tutorial_4_state", 11),
                   (eq, "$tutorial_4_msg_7_displayed", 0),
                   (assign, "$tutorial_4_msg_7_displayed", 1),
                   (tutorial_message, "str_tutorial_4_msg_7"),
                   (play_sound, "snd_tutorial_2"),
                   (assign, "$tutorial_4_finished", 1),
                 (try_end),
                 ], []),
    ],
  ),

  (
    "tutorial_5",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
        #SW - modified tutorial arena
		(0,mtef_visitor_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[itm_arena_tunic_white,itm_tutorial_lightsaber,itm_energy_shield_yellow_small,itm_practice_dl44,itm_laser_bolts_training_pistol,itm_practice_speeder]),
        (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
        (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
        (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
        (15,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
        (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [(try_begin),
         (lt, "$tutorial_5_state", 5),
         (question_box,"str_do_you_wish_to_leave_tutorial"),
        (else_try),
          (finish_mission,0),
        (try_end),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (finish_mission,0),
        ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_tutorial")], []),


      (0, 0, ti_once, [
          (store_mission_timer_a, ":cur_time"),
          (gt, ":cur_time", 2),
          (main_hero_fallen),
          (assign, "$tutorial_5_state", 100),
        ], []),

      (0, 0, ti_once, [(assign, "$tutorial_5_state", 0),
                       (assign, "$tutorial_5_msg_1_displayed", 0),
                       (assign, "$tutorial_5_msg_2_displayed", 0),
                       (assign, "$tutorial_5_msg_3_displayed", 0),
                       (assign, "$tutorial_5_msg_4_displayed", 0),
                       (assign, "$tutorial_5_msg_5_displayed", 0),
                       (assign, "$tutorial_5_msg_6_displayed", 0),
                       ], []),

      (0, 0, ti_once, [(set_show_messages, 0),
                       (team_give_order, 0, grc_everyone, mordr_stand_ground),
                       (set_show_messages, 1),
                       (store_mission_timer_a, ":cur_time"),
                       (gt, ":cur_time", 3),
                       ], []),

      (0, 0, 0, [(call_script, "script_cf_turn_windmill_fans", 0)], []),

      (0, 0, 0, [(try_begin),
                   (eq, "$tutorial_5_state", 0),
                   (try_begin),
                     (eq, "$tutorial_5_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_5_msg_1_displayed", 1),
                     (tutorial_message, "str_tutorial_5_msg_1"),
                     (entry_point_get_position, pos1, 5),
                     (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                     (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (try_end),
                   (call_script, "script_cf_team_get_average_position_of_agents_with_type_to_pos1", 0, grc_infantry),
                   (entry_point_get_position, pos2, 5),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 1000),
                   (val_add, "$tutorial_5_state", 1),
                   (entry_point_get_position, pos1, 6),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_red", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_5_state", 1),
                   (try_begin),
                     (eq, "$tutorial_5_msg_2_displayed", 0),
                     (assign, "$tutorial_5_msg_2_displayed", 1),
                     (tutorial_message, "str_tutorial_5_msg_2"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_team_get_average_position_of_agents_with_type_to_pos1", 0, grc_infantry),
                   (entry_point_get_position, pos2, 5),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 1000),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 6),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 500),
                   (val_add, "$tutorial_5_state", 1),
                   (entry_point_get_position, pos1, 7),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (entry_point_get_position, pos1, 30),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_red", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (else_try),
                   (eq, "$tutorial_5_state", 2),
                   (try_begin),
                     (eq, "$tutorial_5_msg_3_displayed", 0),
                     (assign, "$tutorial_5_msg_3_displayed", 1),
                     (tutorial_message, "str_tutorial_5_msg_3"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_position, pos1, ":player_agent"),
                   (entry_point_get_position, pos2, 7),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 500),
                   (val_add, "$tutorial_5_state", 1),
                   (modify_visitors_at_site,"scn_tutorial_5"),
                   (reset_visitors),
				   #SW - modified tutorial troops
                   (set_visitor,5,"trp_security_guard"),
                   (set_visitor,6,"trp_security_guard"),
                   (set_visitor,7,"trp_security_guard"),
                   (entry_point_get_position, pos1, 11),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (entry_point_get_position, pos1, 12),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_red", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (set_show_messages, 0),
                   (team_give_order, 0, grc_archers, mordr_stand_ground),
                   (set_show_messages, 1),
                 (else_try),
                   (eq, "$tutorial_5_state", 3),
                   (try_begin),
                     (eq, "$tutorial_5_msg_4_displayed", 0),
                     (assign, "$tutorial_5_msg_4_displayed", 1),
                     (tutorial_message, "str_tutorial_5_msg_4"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (call_script, "script_cf_team_get_average_position_of_agents_with_type_to_pos1", 0, grc_archers),
                   (entry_point_get_position, pos2, 11),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 1000),
                   (call_script, "script_cf_team_get_average_position_of_agents_with_type_to_pos1", 0, grc_infantry),
                   (entry_point_get_position, pos2, 12),
                   (get_distance_between_positions, ":cur_distance", pos1, pos2),
                   (le, ":cur_distance", 1000),
                   (val_add, "$tutorial_5_state", 1),
                   (entry_point_get_position, pos1, 30),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_red", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (modify_visitors_at_site,"scn_tutorial_5"),
                   (reset_visitors),
                   (set_visitor,8,"trp_bandit"),
                   (set_visitor,9,"trp_bandit"),
                   (set_visitor,10,"trp_bandit"),
                   (set_visitor,11,"trp_bandit"),
                   (team_give_order, 1, grc_everyone, mordr_charge),
                 (else_try),
                   (eq, "$tutorial_5_state", 4),
                   (try_begin),
                     (eq, "$tutorial_5_msg_5_displayed", 0),
                     (assign, "$tutorial_5_msg_5_displayed", 1),
                     (tutorial_message, "str_tutorial_5_msg_5"),
                     (play_sound, "snd_tutorial_1"),
                   (try_end),
                   (assign, ":enemy_count", 0),
                   (try_for_agents, ":cur_agent"),
                     (agent_is_human, ":cur_agent"),
                     (agent_is_alive, ":cur_agent"),
                     (agent_get_team, ":cur_team", ":cur_agent"),
                     (eq, ":cur_team", 1),
                     (val_add, ":enemy_count", 1),
                   (try_end),
                   (eq, ":enemy_count", 0),
                   (val_add, "$tutorial_5_state", 1),
                 (else_try),
                   (eq, "$tutorial_5_state", 5),
                   (eq, "$tutorial_5_msg_6_displayed", 0),
                   (assign, "$tutorial_5_msg_6_displayed", 1),
                   (tutorial_message, "str_tutorial_5_msg_6"),
                   (play_sound, "snd_tutorial_2"),
                   (assign, "$tutorial_5_finished", 1),
                 (else_try),
                   (gt, "$tutorial_5_state", 30),
                   (tutorial_message, "str_tutorial_failed"),
                   (entry_point_get_position, pos1, 30),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_yellow", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                   (scene_prop_get_instance, ":flag_object", "spr_tutorial_flag_red", 0),
                   (prop_instance_animate_to_position, ":flag_object", pos1, 1),
                 (try_end),
                 ], []),

    ],
 ###>> Motomataru's AI
#AI_triggers,
  ),

  (
    "custom_battle",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
	#may cause problems with the victory condition, or Tab function... nevermind, pasted at the end of batch
      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,


	  	  #@> Swyter Battle Speech
   (4, 0, ti_once, [(eq,"$battle_won",1),],[(call_script,"script_battle_speech",2)]),
   (0, 5, ti_once, [], [(call_script,"script_battle_speech",1)]),

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

      (0, 0, ti_once, [],
        [
          (assign, "$g_battle_result", 0),
          (call_script, "script_combat_music_set_situation_with_culture"),
         ]),

      common_music_situation_update,


	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,

	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
    ],
###>> Motomataru's AI
#AI_triggers,
  ),

  (
    "custom_battle_siege",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      common_battle_mission_start,

      (0, 0, ti_once,
       [
         (assign, "$defender_team", 0),
         (assign, "$attacker_team", 1),
         (assign, "$defender_team_2", 2),
         (assign, "$attacker_team_2", 3),
         ], []),

      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,
      common_custom_siege_init,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,
      common_siege_ai_trigger_init_2,

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,

	  	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
      ],
    ),

  (
    "custom_battle_siege_8",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
	  #attackers (team_0)
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  #defenders (team 1, holds ground)
      (2,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (8,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      common_battle_mission_start,

      (0, 0, ti_once,
       [
         #SW - modified
		 (assign, "$defender_team", 1),
         (assign, "$attacker_team", 0),
         (assign, "$defender_team_2", 2),
         (assign, "$attacker_team_2", 3),
         ], []),

      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,
      common_custom_siege_init,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,
      common_siege_ai_trigger_init_2,

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,

	  	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
      ],
    ),

  (
    "custom_battle_5",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

      (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  #SW - added new entry points for endor bunker siege
	  (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

     ],
    [
      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_custom_siege_init,
      common_inventory_not_available,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,

      (0, 0, ti_once,
       [
         (assign, "$defender_team", 1),
         (assign, "$attacker_team", 0),
         (assign, "$defender_team_2", 3),
         (assign, "$attacker_team_2", 2),
         ], []),

      common_siege_ai_trigger_init_2,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,

	  	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
    ],
  ),

#==============================================================================================================
  # START OF CUSTOM BATTLE MOD
#########################
# Custom Battle Templates
#########################

  (
    "custom_battle_standard",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_2,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),

      (36,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (40,mtef_visitor_source|mtef_team_3,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),

      (44,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (48,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_4,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (56,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_5,0,aif_start_alarmed,1,[]),
     ],
    [

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_give_up_fight")]),

	   (ti_before_mission_start,0,0,[],
	   [
		# Setup weather/time choices
		(try_begin),
		(eq, "$g_rain_settings", 1),
		(set_rain,1,20),
		(else_try),
		(eq, "$g_rain_settings", 2),
		(set_rain,1,50),
		(else_try),
		(eq, "$g_rain_settings", 3),
		(set_rain,1,80),
		(else_try),
		(eq, "$g_rain_settings", 4),
		(set_rain,2,20),
		(else_try),
		(eq, "$g_rain_settings", 5),
		(set_rain,2,50),
		(else_try),
		(eq, "$g_rain_settings", 6),
		(set_rain,2,80),
		(end_try),
		(try_begin),
		(eq, "$g_fog_settings", 1),
		(set_fog_distance, 80, 0xFF736252),
		(else_try),
		(eq, "$g_fog_settings", 2),
		(set_fog_distance,50, 0xFF736252),
		(else_try),
		(eq, "$g_fog_settings", 3),
		(set_fog_distance, 20, 0xFF736252),
		(else_try),
		(eq, "$g_fog_settings", 0),
		(end_try),
		]),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$g_battle_result", -1),
        (assign, "$g_custom_battle_team1_death_count", 0),
        (assign, "$g_custom_battle_team2_death_count", 0),
        (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (neg|agent_is_alive, ":cur_agent"),
          (agent_get_team, ":cur_team", ":cur_agent"),
          (try_begin),
            (eq, ":cur_team", 0),
            (val_add, "$g_custom_battle_team1_death_count", 1),
          (else_try),
            (val_add, "$g_custom_battle_team2_death_count", 1),
          (try_end),
        (try_end),
        (finish_mission),]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_now")], []),

     (0, 0, 0,
      [(key_clicked, key_backspace),
       (start_presentation, "prsnt_battle_2"),
        ], []),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (assign,"$g_battle_result",0),
           (try_begin),
             (neg|main_hero_fallen),
             (assign,"$g_battle_result",1),
           (else_try),
             (assign,"$g_battle_result",-1),
           (try_end),
           (assign, "$g_custom_battle_team1_death_count", 0),
           (assign, "$g_custom_battle_team2_death_count", 0),
           (try_for_agents, ":cur_agent"),
             (agent_is_human, ":cur_agent"),
             (neg|agent_is_alive, ":cur_agent"),
             (agent_get_team, ":cur_team", ":cur_agent"),
             (try_begin),
               (eq, ":cur_team", 0),
               (val_add, "$g_custom_battle_team1_death_count", 1),
             (else_try),
               (val_add, "$g_custom_battle_team2_death_count", 1),
             (try_end),
           (try_end),
           (finish_mission),
           ]),
     (0.1, 0, 0,
      [(eq, "$g_presentation_battle_active", 1),
       (call_script, "script_update_order_panel_statistics_and_map_2"),
        ], []),

			  #@> Swyter Battle Speech
   (4, 0, ti_once, [(eq,"$battle_won",1),],[(call_script,"script_battle_speech",2)]),
   (0, 5, ti_once, [], [(call_script,"script_battle_speech",1)]),

		#Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,
	  
	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),
	  
    ],
###>> Motomataru's AI
#AI_triggers,
	 ),
  (
    "custom_battle_2vs2",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

	  (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

	  (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_give_up_fight")]),

	   (ti_before_mission_start,0,0,[],
	   [
		# Setup weather/time choices
		(try_begin),
		(eq, "$g_rain_settings", 1),
		(set_rain,1,20),
		(else_try),
		(eq, "$g_rain_settings", 2),
		(set_rain,1,50),
		(else_try),
		(eq, "$g_rain_settings", 3),
		(set_rain,1,80),
		(else_try),
		(eq, "$g_rain_settings", 4),
		(set_rain,2,20),
		(else_try),
		(eq, "$g_rain_settings", 5),
		(set_rain,2,50),
		(else_try),
		(eq, "$g_rain_settings", 6),
		(set_rain,2,80),
		(end_try),
		(try_begin),
		(eq, "$g_fog_settings", 1),
		(set_fog_distance, 80, 0xFF736252),
		(else_try),
		(eq, "$g_fog_settings", 2),
		(set_fog_distance,50, 0xFF736252),
		(else_try),
		(eq, "$g_fog_settings", 3),
		(set_fog_distance, 20, 0xFF736252),
		(else_try),
		(eq, "$g_fog_settings", 0),
		(end_try),
		]),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$g_battle_result", -1),
        (assign, "$g_custom_battle_team1_death_count", 0),
        (assign, "$g_custom_battle_team2_death_count", 0),
        (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (neg|agent_is_alive, ":cur_agent"),
          (agent_get_team, ":cur_team", ":cur_agent"),
          (try_begin),
            (eq, ":cur_team", 0),
            (val_add, "$g_custom_battle_team1_death_count", 1),
          (else_try),
            (val_add, "$g_custom_battle_team2_death_count", 1),
          (try_end),
        (try_end),
        (finish_mission),]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_now")], []),

	  #@> Swyter Battle Speech
   (4, 0, ti_once, [(eq,"$battle_won",1),],[(call_script,"script_battle_speech",2)]),
   (0, 5, ti_once, [], [(call_script,"script_battle_speech",1)]),

	  #Motomataru's AI Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	(ti_before_mission_start, 0, 0, [], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
	]),

	(0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),	#delay to allow spawning to finish

	(1, .9, 0, [], [
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
		(try_end),

		(try_begin),	#reassess ranged position upon first casualty
			(gt, "$cur_casualties", 0),
			(eq, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(else_try),
			(lt, "$ranged_clock", 10),
			(call_script, "script_SW_field_tactics", 0),
		(else_try),	#reassess ranged position every ten seconds after first casualty
			(gt, "$prev_casualties", 0),
			(call_script, "script_SW_field_tactics", 1),
			(assign, "$ranged_clock", 0),
		(try_end),

		(val_add, "$ranged_clock", 1),
	]),

	common_ranged_avoid_melee,

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

     (0, 0, 0,
      [(key_clicked, key_backspace),
       (start_presentation, "prsnt_battle"),
        ], []),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (assign,"$g_battle_result",0),
           (try_begin),
             (neg|main_hero_fallen),
             (assign,"$g_battle_result",1),
           (else_try),
             (assign,"$g_battle_result",-1),
           (try_end),
           (assign, "$g_custom_battle_team1_death_count", 0),
           (assign, "$g_custom_battle_team2_death_count", 0),
           (try_for_agents, ":cur_agent"),
             (agent_is_human, ":cur_agent"),
             (neg|agent_is_alive, ":cur_agent"),
             (agent_get_team, ":cur_team", ":cur_agent"),
             (try_begin),
               (eq, ":cur_team", 0),
               (val_add, "$g_custom_battle_team1_death_count", 1),
             (else_try),
               (val_add, "$g_custom_battle_team2_death_count", 1),
             (try_end),
           (try_end),
           (finish_mission),
           ]),
     (0.1, 0, 0,
      [(eq, "$g_presentation_battle_active", 1),
       (call_script, "script_update_order_panel_statistics_and_map"),
        ], []),

	  #SW - add custom lightsaber noise
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,

	  
	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),	  
	  
    ],
###>> Motomataru's AI
#AI_triggers,
	),

# END OF CUSTOM BATTLE
#==============================================================================================================
#SW - HokieBT - added new scene for trade_federation
  (
    "trade_federation",0,-1,
    "Visit Merchants at Trade Federation",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),(9,mtef_scene_source,af_override_horse,0,1,[]),(10,mtef_scene_source,af_override_horse,0,1,[]),(11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),(24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
	 (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
      (1, 0, ti_once, [], [
		(call_script, "script_music_set_situation_with_culture", mtf_sit_town),
      ]),

      (ti_before_mission_start, 0, 0, [], 	[
											(call_script, "script_change_banners_and_chest")
											]),

      (ti_inventory_key_pressed, 0, 0, [
          (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [
          (set_trigger_result,1)], []),

	  #SW - trigger to make some agents dance in the scene
	  # (1, 0, ti_once, [], [
      ##(ti_on_agent_spawn, 0, 0, [], [
		##(store_trigger_param_1, ":agent_no"),
		# (try_for_agents, ":agent_no"),
			# (agent_get_entry_no, ":entry_no", ":agent_no"),
			# (this_or_next|eq,":entry_no",38),
			# (eq,":entry_no",39),
			# (agent_set_stand_animation, ":agent_no", "anim_slave_dance"),
			# (agent_set_animation, ":agent_no", "anim_slave_dance"),
			# (store_random_in_range, ":random_no", 0, 100),
			# (agent_set_animation_progress, ":agent_no", ":random_no"),
		# (try_end),

		# (try_for_agents, ":agent_no"),
			# (agent_get_troop_id,":is_vader", ":agent_no"),
			# (eq,":is_vader","trp_knight_1_1"),
			# (agent_play_sound, ":agent_no", "snd_vader_breath"),
			# (agent_set_stand_animation, ":agent_no", "anim_vader_stand"),
			##(agent_set_animation, ":agent_no", "anim_vader_stand"),
			##(store_random_in_range, ":random_no", 0, 100),
			##(agent_set_animation_progress, ":agent_no", ":random_no"),
		# (try_end),
      # ]),

	  #SW - add custom lightsaber noise to town scenes
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  #lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_switch_sw_scene_props,
	  #common_custom_commander_camera,
	  common_crouch_button,

		  	  #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),

    ],
  ),
#==============================================================================================================
#SW - HokieBT - added new scene for ship_interior
  (
    "ship_interior",0,-1,
    "Walk around the ship.",
    [
	(0,mtef_visitor_source,af_override_horse,0,1,[]),
	(1,mtef_visitor_source,af_override_horse,0,1,[]),(2,mtef_visitor_source,af_override_horse,0,1,[]),(3,mtef_visitor_source,af_override_horse,0,1,[]),(4,mtef_visitor_source,af_override_horse,0,1,[]),(5,mtef_visitor_source,af_override_horse,0,1,[]),
	(6,mtef_visitor_source,af_override_horse,0,1,[]),(7,mtef_visitor_source,af_override_horse,0,1,[]),(8,mtef_visitor_source,af_override_horse,0,1,[]),(9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),
	(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,af_override_horse,0,1,[]),(14,mtef_visitor_source,af_override_horse,0,1,[]),(15,mtef_visitor_source,af_override_horse,0,1,[]),
	(16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),
	(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),(24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),
	(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),
	(31,mtef_visitor_source,af_override_horse,0,1,[]),(32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),
	(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),(40,mtef_visitor_source,af_override_horse,0,1,[]),
	(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),
	(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),(48,mtef_visitor_source,af_override_horse,0,1,[]),(49,mtef_visitor_source,af_override_horse,0,1,[]),(50,mtef_visitor_source,af_override_horse,0,1,[]),
	(51,mtef_visitor_source,af_override_horse,0,1,[]),(52,mtef_visitor_source,af_override_horse,0,1,[]),(53,mtef_visitor_source,af_override_horse,0,1,[]),(54,mtef_visitor_source,af_override_horse,0,1,[]),(55,mtef_visitor_source,af_override_horse,0,1,[]),
	(56,mtef_visitor_source,af_override_horse,0,1,[]),(57,mtef_visitor_source,af_override_horse,0,1,[]),(58,mtef_visitor_source,af_override_horse,0,1,[]),(59,mtef_visitor_source,af_override_horse,0,1,[]),(60,mtef_visitor_source,af_override_horse,0,1,[]),
	#(61,mtef_visitor_source,af_override_horse,0,1,[]),(62,mtef_visitor_source,af_override_horse,0,1,[]),(63,mtef_visitor_source,af_override_horse,0,1,[]),(64,mtef_visitor_source,af_override_horse,0,1,[]),(65,mtef_visitor_source,af_override_horse,0,1,[]),
	#(66,mtef_visitor_source,af_override_horse,0,1,[]),(67,mtef_visitor_source,af_override_horse,0,1,[]),(68,mtef_visitor_source,af_override_horse,0,1,[]),(69,mtef_visitor_source,af_override_horse,0,1,[]),(70,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [

      (1, 0, ti_once, [], [
		(call_script, "script_music_set_situation_with_culture", mtf_sit_town),
      ]),

      (ti_before_mission_start, 0, 0, [], 	[
											(call_script, "script_change_banners_and_chest")
											]),

      (ti_inventory_key_pressed, 0, 0, [
          (set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [
          (set_trigger_result,1)], []),

	  (4, 0, 0, [], [		#run every X seconds
			(get_player_agent_no, ":player_agent"),
			(scene_prop_get_num_instances,":num_instances","spr_sw_bacta_tank_new_heal"),
			(gt, ":num_instances", 0),
			(try_for_range, ":cur_i", 0, ":num_instances"),
				(scene_prop_get_instance,":instance", "spr_sw_bacta_tank_new_heal", ":cur_i"),
				(prop_instance_get_position,pos1,":instance"),
				(agent_get_position, pos2, ":player_agent"),
				(get_distance_between_positions,":dist",pos1,pos2),
				#get health
				(store_agent_hit_points,":player_agent_health",":player_agent",0),	#relative number, 0-100
				(try_begin),
					(eq, ":player_agent_health", 100),	#player is fully healed
					(le, ":dist", 125),	#very close
					(display_message, "@You are not injured and do not need the Bacta Tank at this time."),
				(else_try),
					(lt, ":player_agent_health", 100),	#player is injured
					(le, ":dist", 125),	#very close
					(display_message, "@You are being healed by the Bacta Tank..."),
					(val_add, ":player_agent_health", 10),	#add 10%
					(try_begin),
						(gt, ":player_agent_health", 100),
						(assign, ":player_agent_health", 100),		#so we don't try and set hit points > 100%
					(try_end),
					(agent_set_hit_points,":player_agent",":player_agent_health",0),
					(troop_set_health, "$g_player_troop", ":player_agent_health"),
					(agent_play_sound, ":player_agent", "snd_bacta_heal"),
				(else_try),
					(le, ":dist", 1300),	#in room
					(display_message, "@Walk into the Bacta Tank to heal yourself."),
				(try_end),
			(try_end),
		]),


	  #SW - allow player to start a fight
	  (1, 0, ti_once, [
						(call_script, "script_init_town_fight"),	#allow player to start a fight by shooting somebody
						(assign, "$g_init_fight", 1),
					  ], []),

	  #SW - added the ability to start a fight
	  common_check_town_fight,

	  #SW - add custom lightsaber noise to town scenes
	  #lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	  lightsaber_noise_player,
	  #lightsaber_noise_agent,
	  common_change_fog,
	  common_use_healthpack,
	  #common_use_binocular_1,
	  #common_use_binocular_2,
	  common_helmet_view,
	  common_zoom_view,
	  common_use_jetpack,
	  common_toggle_weapon_capabilities,
	  common_crouch_button,


	  	 #SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),

    ],
  ),



#==============================================================================================================
#SW BSG Integration - EDITED BY SWYTER - Improved controls - Tweaked and polished - Now playable
#==============================================================================================================
  (
    "space_battle_entry",0,-1,
    "space_battle_entry",
	#SW - modified so you do not remove your helmet when you enter a lords hall (removed af_override_head flag)
	[(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
     #(1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 #(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), #for doors
     #(5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     #(8,mtef_visitor_source,af_override_horse,0,1,[]),(9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_scene_source,af_override_horse,0,1,[]),(11,mtef_scene_source,af_override_horse,0,1,[]),
     #(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     #(16,mtef_visitor_source,,0,1,[]),(17,mtef_visitor_source,af_spacestation_lord,0,1,[]),(18,mtef_visitor_source,af_spacestation_lord,0,1,[]),(19,mtef_visitor_source,af_spacestation_lord,0,1,[]),(20,mtef_visitor_source,af_spacestation_lord,0,1,[]),(21,mtef_visitor_source,af_spacestation_lord,0,1,[]),(22,mtef_visitor_source,af_spacestation_lord,0,1,[]),(23,mtef_visitor_source,af_spacestation_lord,0,1,[]),(24,mtef_visitor_source,af_spacestation_lord,0,1,[]),
     #(25,mtef_visitor_source,af_spacestation_lord,0,1,[]),(26,mtef_visitor_source,af_spacestation_lord,0,1,[]),(27,mtef_visitor_source,af_spacestation_lord,0,1,[]),(28,mtef_visitor_source,af_spacestation_lord,0,1,[]),(29,mtef_visitor_source,af_spacestation_lord,0,1,[]),(30,mtef_visitor_source,af_spacestation_lord,0,1,[]),(31,mtef_visitor_source,af_spacestation_lord,0,1,[])
     ],
    [
	  common_change_fog,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
         ]),
      #(ti_before_mission_start, 0, 0, [],
      # [
      #   (call_script, "script_change_banners_and_chest"),
      #   ]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [
			(set_trigger_result,1)
		], []),
      (0, 0, ti_once, [], [
        (try_begin),
          (eq, "$talk_context", tc_court_talk),
#          (call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", 0), #prison
        (try_end),
        ]),
	(0.0, 1.0, ti_once, [],
		[
			(tutorial_box, "str_space_combat_practice", "@Space Combat practice"),
		]
	),
     # (0.0, 1.0, 2.0,
      # [(lt, "$trainer_help_message", 2),
        # ],
      # [(try_begin),
         # (eq, "$trainer_help_message", 0),
         # (tutorial_box, "str_trainer_help_1", "@Tutorial"),
       # (else_try),
         # (tutorial_box, "str_trainer_help_2", "@Tutorial"),
       # (try_end),
       # (val_add, "$trainer_help_message", 1),
          # ]),
    ],
  ),


  (
    "space_battle",0,-1,
    #"You lead your squad to battle.",
	"space_battle",
    [
      (0,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
     common_change_fog,
	 #SW BSG integration - new tab key, question_answered, add_xp_to_troop functionality
	 common_space_battle_tab_press,
	 (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
		   (add_xp_to_troop,100,"$g_player_troop"),	#since custom commander is integrated
		   (stop_all_sounds,2),	#stop the engine sound from the space combat
		   (finish_mission),
         ]),
     (ti_before_mission_start, 0, 0, [], [(set_rain,2,0)]),
      (0, 0, ti_once, [], [
          (assign,"$cam_follow",1),
          (assign,"$player_ship","spr_p_viper_mk7"),
          (assign,"$player_max_speed",200),		#with higher speeds we need to add code to also adjust the position the guns/engine fire from (setting it to 200 for now)
          (assign,"$player_speed",40),
          (assign,"$player_rotate_y",0),
          (assign,"$player_rotate_x",0),
          (assign,"$player_missiles",0),
          #(assign,"$player_cannons",22500000),
		  (assign,"$player_cannons",100000),
          (assign,"$player_damage",100),
          (assign,"$player_cannon_damage",3),
		  (assign,"$mouse_y_control",-1),			#mouse_up = down, mouse_down = up (can toggle with T key)
    #      (assign,"$auto_control",0),
    #      (assign,"$auto_slow_down",0),
          (call_script,"script_set_fighters","spr_cylon_raider","spr_viper_mk7"), #This edited by Ibanez after HokieBT's port.
          (play_sound,"snd_viper_engine_hum"),
          (play_sound,"snd_subspace"),
        ]),




      (0, 0, ti_once, [], [
         (try_for_range,":cylon","trp_cylon_a","trp_cylon_end"),
             (store_random_in_range,":randomized_number",1,11),
             (try_begin),
                 (eq,":randomized_number",1),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 0),
             (else_try),
                 (eq,":randomized_number",2),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 1),
             (else_try),
                 (eq,":randomized_number",3),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 2),
             (else_try),
                 (eq,":randomized_number",4),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 3),
             (else_try),
                 (eq,":randomized_number",5),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 4),
             (else_try),
                 (eq,":randomized_number",6),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 5),
             (else_try),
                 (eq,":randomized_number",7),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 6),
             (else_try),
                 (ge,":randomized_number",8),
                 (scene_prop_get_instance,":s_instance", "$player_ship", 0),
             (end_try),
             (troop_set_slot,":cylon",slot_troop_ai_target,":s_instance"),
         (end_try),
        ]),
     (0, 0, ti_once, [], [
         (try_for_range,":viper","trp_viper_a","trp_viper_end"),
             (store_random_in_range,":randomized_number",1,11),
             (try_begin),
                 (eq,":randomized_number",1),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 0),
             (else_try),
                 (eq,":randomized_number",2),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 1),
             (else_try),
                 (eq,":randomized_number",3),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 2),
             (else_try),
                 (eq,":randomized_number",4),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 3),
             (else_try),
                 (eq,":randomized_number",5),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 4),
             (else_try),
                 (eq,":randomized_number",6),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 5),
             (else_try),
                 (eq,":randomized_number",7),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 6),
             (else_try),
                 (eq,":randomized_number",8),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 7),
             (end_try),
             (troop_set_slot,":viper",slot_troop_ai_target,":s_instance"),
         (end_try),
        ]),
      #camera tracking,particles,status,collision detect,destroy,loopsounds
      (0, 0, ti_once, [], [
		(mission_cam_set_mode,1),
        ]),
      (0, 0, 0, [(eq,"$cam_follow",1),], [
          (scene_prop_get_instance,":s_instance", "$player_ship", 0),
          (prop_instance_get_position,pos1,":s_instance"),

          (position_move_z,pos1,260),
          (position_rotate_x,pos1,-5),
          (position_move_y,pos1,-1000),

          (mission_cam_animate_to_position, pos1,100,1),
        ]),
     (20, 0, 0, [], [
         (play_sound,"snd_viper_engine_hum"),
        ]),
     (4, 0, 0, [], [
         (play_sound,"snd_subspace"),
        ]),
     (0, 0, 0, [], [
          (scene_prop_get_instance,":s_instance", "$player_ship", 0),
          (prop_instance_get_position,pos1,":s_instance"),
          (position_move_y,pos1,-400),	#switched from -350
          (position_move_x,pos1,-140),	#switched from -40
          (position_move_z,pos1,-25),	#switched from 0
          (particle_system_burst,"psys_viper_engine",pos1,10),
          (prop_instance_get_position,pos1,":s_instance"),
          (position_move_y,pos1,-400),	#switched from -350
          (position_move_x,pos1,140),	#switched from 40
          (position_move_z,pos1,-25), #switched from 0
          (particle_system_burst,"psys_viper_engine",pos1,10),
          #(prop_instance_get_position,pos1,":s_instance"),
          #(position_move_y,pos1,-450),	#switched from -350
          #(position_move_x,pos1,0),
          #(position_move_z,pos1,100),	#switched from 75
          #(particle_system_burst,"psys_viper_engine",pos1,2),

          (assign,reg1,"$player_speed"),
          (assign,reg2,"$player_damage"),
          (assign,reg3,"$player_missiles"),
          (assign,reg4,"$player_cannons"),

          (troop_get_slot,reg5,"trp_cylon_a",slot_troop_damage),
          (troop_get_slot,reg6,"trp_cylon_b",slot_troop_damage),
          (troop_get_slot,reg7,"trp_cylon_c",slot_troop_damage),
          (troop_get_slot,reg8,"trp_cylon_d",slot_troop_damage),
          (troop_get_slot,reg9,"trp_cylon_e",slot_troop_damage),
          (troop_get_slot,reg10,"trp_cylon_f",slot_troop_damage),
          (troop_get_slot,reg11,"trp_cylon_g",slot_troop_damage),
          (troop_get_slot,reg12,"trp_cylon_h",slot_troop_damage),
          (troop_get_slot,reg13,"trp_viper_a",slot_troop_damage),
          (troop_get_slot,reg14,"trp_viper_b",slot_troop_damage),
          (troop_get_slot,reg15,"trp_viper_c",slot_troop_damage),
          (troop_get_slot,reg16,"trp_viper_d",slot_troop_damage),
          (troop_get_slot,reg17,"trp_viper_e",slot_troop_damage),
          (troop_get_slot,reg18,"trp_viper_f",slot_troop_damage),
          (troop_get_slot,reg19,"trp_viper_g",slot_troop_damage),
          (troop_get_slot,reg20,"trp_viper_h",slot_troop_damage),

		  #added by swyter


		 # #Little Pos Helper by Kuba begin
		 # #http://forums.taleworlds.com/index.php/topic,8652.msg2373733.html#msg2373733
		 # #(set_fixed_point_multiplier, 1000),
		 # (mouse_get_position, pos1),
		 # (position_get_x, reg21, pos1),
		 # (position_get_y, reg22, pos1),
		 # #(str_store_string, s1, "@DEBUG: x = {reg1}, y = {reg2}"),
		 # #(overlay_set_text, "$g_little_pos_helper", "@DEBUG: x = {reg1}, y = {reg2}"),
		 # (tutorial_message, s1),
		 # #Little Pos Helper by Kuba end

		  #THE MESSAGE IS SHOWN HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          (tutorial_message,"str_viper_status"),
          (call_script,"script_fighter_explosions","spr_cylon_raider","spr_viper_mk7"),
        ]),
     #(0.1, 0, 0, [(key_is_down, key_numpad_plus),(gt,"$player_damage",0),], [
	 (0.1, 0, 0, [(key_is_down, key_c),(gt,"$player_damage",0),], [
          (try_begin),
              (gt,"$cam_follow",0),
              (assign,"$cam_follow",0),
          (else_try),
              (eq,"$cam_follow",0),
              (assign,"$cam_follow",1),
          (try_end),
        ]),
     (0.2, 0, 0, [(gt,"$player_damage",19),], [
          (try_begin),
              (gt,"$cam_follow",2),
              (assign,"$cam_follow",1),
          (try_end),
        ]),
     (0, 0, 0, [(lt,"$player_damage",20),], [
         (scene_prop_get_instance,":s_instance", "$player_ship", 0),
         (prop_instance_get_position,pos1,":s_instance"),
         (particle_system_burst,"psys_viper_smoke",pos1,2),
         (try_begin),
             (neq,"$cam_follow",0),
             (assign,"$cam_follow",2),
         (try_end),
        ]),
     (0, 0, 0, [(lt,"$player_damage",1),], [
         (scene_prop_get_instance,":s_instance", "$player_ship", 0),
         (prop_instance_get_position,pos1,":s_instance"),
         (assign,"$cam_follow",0),
         (try_begin),
             (gt,"$player_speed",0),
             (val_sub,"$player_speed",1),
             (particle_system_burst,"psys_village_fire_big",pos1,1),
             (assign,"$player_rotate_x",-6),
             (assign,"$player_rotate_y",-8),
         (try_end),
         (try_begin),
             (lt,"$player_speed",1),
             (assign,"$player_rotate_x",0),
             (assign,"$player_rotate_y",0),
         (try_end),
        ]),

     ### S W    B S G     C O N T R O L S  ############

	  (0, 0, 0, [
				(key_is_down, key_t),
				],
		[
			(val_mul,"$mouse_y_control",-1),
			#(display_message, "@The vertical mouse control was modified."),
		]
	  ),

	  (0, 0, 0, [
				#(key_is_down, key_middle_mouse_button),
				(gt,"$player_speed",0),
				],
		[
          (mouse_get_position, pos1),
          (set_fixed_point_multiplier, 1000),
          (position_get_x, ":mouse_x", pos1),
          (position_get_y, ":mouse_y", pos1),

		  #CENTER THE XY GRID [LEFT-DOWN BY DEFAULT]
		  (val_sub,":mouse_x",500),
		  (val_sub,":mouse_y",380),


		#MAKE PLAYABLE COORS (LITTLE NUMBERS)
		  (val_div,":mouse_x",70),
		  (val_div,":mouse_y",70),

		  #INVERSE CONTROLS (NEG 2 POSIT & VICEVERSA)
		  (val_mul,":mouse_x",-1),
		  #(val_mul,":mouse_y",-1),		#up/down
		  (val_mul,":mouse_y","$mouse_y_control"),		#up/down

		 # BIND DATA TO THE PLAYER'S SHIP
	     (assign,"$player_rotate_x",":mouse_y"),
	     (assign,"$player_rotate_z",":mouse_x"),



        ]),


     #(0.01, 0, 0, [(key_is_down, key_mouse_scroll_up),(lt,"$player_speed","$player_max_speed"),(gt,"$player_damage",0),], [
     #     (val_add,"$player_speed",30),
     #   ]),
     #(0.01, 0, 0, [(key_is_down, key_mouse_scroll_down),(gt,"$player_speed",0),(gt,"$player_damage",0),], [
     #     (val_sub,"$player_speed",30),
     #   ]),
     #(0.1, 0, 0, [(key_is_down, key_w),(gt,"$player_rotate_x",-6),(gt,"$player_damage",0),], [
	 (0.1, 0, 0, [(key_is_down, key_w),(lt,"$player_speed","$player_max_speed"),(gt,"$player_damage",0),], [
          #(val_add,"$player_speed",50),
		  (val_add,"$player_speed",20),
        ]),
     #(0.1, 0, 0, [(key_is_down, key_s),(lt,"$player_rotate_x",6),(gt,"$player_damage",0),], [
	 (0.1, 0, 0, [(key_is_down, key_s),(gt,"$player_speed",0),(gt,"$player_damage",0),], [
          #(val_sub,"$player_speed",40),
		  (val_sub,"$player_speed",20),
        ]),
     (0.1, 0, 0, [(key_is_down, key_a),(gt,"$player_rotate_y",-8),(gt,"$player_damage",0),], [
          (val_sub,"$player_rotate_y",1),
		]),
		         #SWY - LEFT LIMITER
		        (0.2, 0, 0, [(lt,"$player_rotate_y",1),], [
				(val_add,"$player_rotate_y",1),
        ]),
     (0.1, 0, 0, [(key_is_down, key_d),(lt,"$player_rotate_y",8),(gt,"$player_damage",0),], [
          (val_add,"$player_rotate_y",1),
		]),
		         #SWY - RIGHT LIMITER
		  		(0.2, 0, 0, [(gt,"$player_rotate_y",-1),], [
				(val_sub,"$player_rotate_y",1),
        ]),

		## CONTROLS END ########

     (0, 0, 0, [], [
          (scene_prop_get_instance,":s_instance", "$player_ship", 0),
          (prop_instance_get_position,pos1,":s_instance"),
          (prop_instance_get_position,pos2,":s_instance"),
          (prop_instance_get_position,pos3,":s_instance"),
          (prop_instance_get_position,pos4,":s_instance"),
          (prop_instance_get_position,pos5,":s_instance"),
          (prop_instance_get_position,pos6,":s_instance"),
          (prop_instance_get_position,pos7,":s_instance"),
          (prop_instance_get_position,pos8,":s_instance"),
          (prop_instance_get_position,pos9,":s_instance"),
          (prop_instance_get_position,pos10,":s_instance"),
          (position_rotate_y,pos1,"$player_rotate_y"),
          (position_rotate_x,pos1,"$player_rotate_x"),
		  (position_rotate_z,pos1,"$player_rotate_z"),
          (position_move_y,pos1,"$player_speed"),		#moves the player forward or backwards depending on their speed?
          (prop_instance_animate_to_position,":s_instance",pos1,10),

          (position_move_y,pos2,1000),
          (position_move_y,pos3,1500),
          (position_move_y,pos4,2000),
          (position_move_y,pos5,2500),
          (position_move_y,pos6,3000),
          (position_move_y,pos7,3500),
          (position_move_y,pos8,4000),
          (position_move_y,pos9,4500),
          (position_move_y,pos10,5000),

          (scene_prop_get_instance,":t1_instance", "spr_target1", 0),
          (scene_prop_get_instance,":t2_instance", "spr_target2", 0),
          (scene_prop_get_instance,":t3_instance", "spr_target3", 0),
          (scene_prop_get_instance,":t4_instance", "spr_target4", 0),
          (scene_prop_get_instance,":t5_instance", "spr_target5", 0),
          (scene_prop_get_instance,":t6_instance", "spr_target6", 0),
          (scene_prop_get_instance,":t7_instance", "spr_target7", 0),
          (scene_prop_get_instance,":t8_instance", "spr_target8", 0),
          (scene_prop_get_instance,":t9_instance", "spr_target9", 0),

          (prop_instance_set_position,":t1_instance",pos2),
          (prop_instance_set_position,":t2_instance",pos3),
          (prop_instance_set_position,":t3_instance",pos4),
          (prop_instance_set_position,":t4_instance",pos5),
          (prop_instance_set_position,":t5_instance",pos6),
          (prop_instance_set_position,":t6_instance",pos7),
          (prop_instance_set_position,":t7_instance",pos8),
          (prop_instance_set_position,":t8_instance",pos9),
          (prop_instance_set_position,":t9_instance",pos10),

          (prop_instance_get_position,pos11,":s_instance"),
          (prop_instance_get_position,pos12,":s_instance"),
          (prop_instance_get_position,pos13,":s_instance"),
          (prop_instance_get_position,pos14,":s_instance"),

          (position_move_y,pos11,-200),
          (position_move_x,pos11,150),
          (position_move_z,pos11,-50),
          (position_move_y,pos12,-200),
          (position_move_x,pos12,-150),
          (position_move_z,pos12,-50),
          (position_move_y,pos13,-200),
          (position_move_x,pos13,125),
          (position_move_z,pos13,-20),
          (position_move_y,pos14,-200),
          (position_move_x,pos14,-125),
          (position_move_z,pos14,-20),
          (try_for_range,":collision","spr_viper_mk2","spr_scene_props_end"),
             (scene_prop_get_num_instances,":instance_no", ":collision"),
             (try_for_range,":col_object",0,":instance_no"),
                 (scene_prop_get_instance,":col_instance", ":collision", ":col_object"),
                 (prop_instance_get_position,pos2,":col_instance"),
                 (scene_prop_get_instance,":s_instance", "$player_ship", 0),
                 (prop_instance_get_position,pos1,":s_instance"),
                 (get_distance_between_positions, ":col_distance", pos1, pos2),
                 (try_begin),
                     (lt,":col_distance",400),
                     (val_sub,"$player_damage",1),
                 (end_try),
             (end_try),
         (end_try),
        ]),
     (0, 0, 0, [
				(this_or_next|key_is_down, key_left_mouse_button),
				(key_is_down, key_space),
				(gt,"$player_cannons",0),
				(gt,"$player_damage",0),
				],
				[
         (scene_prop_get_instance,":s_instance", "$player_ship", 0),
         (prop_instance_get_position,pos1,":s_instance"),
         (prop_instance_get_position,pos2,":s_instance"),
         #SW BSG - modified viper_machine_gun to remove the middle gun, pos3
         #(prop_instance_get_position,pos3,":s_instance"),
         (position_move_y,pos1,25),	  #
         (position_move_x,pos1,-230), # original value was -300
         (position_move_z,pos1,30),   # original value was -45
         (position_move_y,pos2,25),
         (position_move_x,pos2,230),  # original value was 300
         (position_move_z,pos2,30),	  #original value was -45
		 #(position_move_y,pos3,-110),
         #(position_move_x,pos3,0),
         #(position_move_z,pos3,190),
         (particle_system_burst,"psys_viper_machine_gun",pos1,1),
         (particle_system_burst,"psys_viper_machine_gun",pos2,1),
         #(particle_system_burst,"psys_viper_machine_gun",pos3,1),
         (particle_system_burst,"psys_cannon_fire",pos1,1),
         (particle_system_burst,"psys_cannon_fire",pos2,1),
         #(particle_system_burst,"psys_cannon_fire",pos3,1),
         (val_sub,"$player_cannons",3),
         (call_script,"script_calculate_fighter_damages"),
         (play_sound,"snd_viper_cannon"),
        ]),
     (0.1, 0, 0, [(this_or_next|key_is_down, key_left_mouse_button),(key_is_down, key_space),(lt,"$player_cannons",1),(gt,"$player_damage",0),], [
         (play_sound,"snd_viper_cannon_impact"),
        ]),
     ################################################
     ####################AI#AI#AI####################
     ################################################
     (0.1, 0, 0, [], [
         (try_for_range,":cylon","trp_cylon_a","trp_cylon_end"),
            (troop_slot_eq,":cylon",slot_troop_status,1),
            (scene_prop_get_num_instances,":instance_no", "spr_cylon_raider"),
            (try_for_range,":col_object",0,":instance_no"),
                (scene_prop_get_instance,":col_instance", "spr_cylon_raider", ":col_object"),
                (prop_instance_get_position,pos1,":col_instance"),
                (call_script,"script_ai_cylon_movements",":col_instance",":cylon"),
            (end_try),
         (end_try),
        ]),
     (0.1, 0, 0, [], [
         (try_for_range,":viper","trp_viper_a","trp_viper_end"),
            (troop_slot_eq,":viper",slot_troop_status,1),
            (scene_prop_get_num_instances,":instance_no", "spr_viper_mk7"),
            (try_for_range,":col_object",0,":instance_no"),
                (scene_prop_get_instance,":col_instance", "spr_viper_mk7", ":col_object"),
                (prop_instance_get_position,pos1,":col_instance"),
                (call_script,"script_ai_viper_movements",":col_instance",":viper"),
            (end_try),
         (end_try),
        ]),
     (30, 0, 0, [], [
         (try_for_range,":cylon","trp_cylon_a","trp_cylon_end"),
             (store_random_in_range,":randomized_number",1,13),
             (try_begin),
                 (eq,":randomized_number",1),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 0),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_a"),
             (else_try),
                 (eq,":randomized_number",2),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 1),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_b"),
             (else_try),
                 (eq,":randomized_number",3),
				 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 2),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_c"),
             (else_try),
                 (eq,":randomized_number",4),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 3),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_d"),
             (else_try),
                 (eq,":randomized_number",5),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 4),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_e"),
             (else_try),
                 (eq,":randomized_number",6),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 5),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_f"),
             (else_try),
                 (eq,":randomized_number",7),
                 (scene_prop_get_instance,":s_instance", "spr_viper_mk7", 6),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_viper_g"),
             (else_try),
                 (ge,":randomized_number",8),
                 (scene_prop_get_instance,":s_instance", "$player_ship", 0),
                 (troop_set_slot,":cylon",slot_troop_ai_target_troop,"trp_player"),
             (end_try),
             (troop_set_slot,":cylon",slot_troop_ai_target,":s_instance"),
         (end_try),
        ]),
     (30, 0, 0, [], [
         (try_for_range,":viper","trp_viper_a","trp_viper_end"),
             (store_random_in_range,":randomized_number",1,9),
             (try_begin),
                 (eq,":randomized_number",1),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 0),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_a"),
             (else_try),
                 (eq,":randomized_number",2),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 1),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_b"),
             (else_try),
                 (eq,":randomized_number",3),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 2),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_c"),
             (else_try),
                 (eq,":randomized_number",4),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 3),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_d"),
             (else_try),
                 (eq,":randomized_number",5),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 4),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_e"),
             (else_try),
                 (eq,":randomized_number",6),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 5),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_f"),
             (else_try),
                 (eq,":randomized_number",7),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 6),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_g"),
             (else_try),
                 (eq,":randomized_number",8),
                 (scene_prop_get_instance,":s_instance", "spr_cylon_raider", 7),
                 (troop_set_slot,":viper",slot_troop_ai_target_troop,"trp_cylon_h"),
             (end_try),
             (troop_set_slot,":viper",slot_troop_ai_target,":s_instance"),
         (end_try),
        ]),

   ],
),

  (
    "space_prop",0,-1,
    "prop_add",
    [
      (0,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
	  common_change_fog,
      (ti_before_mission_start, 0, 0, [], [(set_rain,2,0),]),
    ],
  ),

#==============================================================================================================
#SW BSG Integration   END                 END                END                  END               END
#==============================================================================================================



##############################  # Duel Mod by MartinF Start ##############################

# Below are 8 sets of 2 templates. These are selected by the choices in the dialog. You can change the weapons by adding/removing to the itm_ list
# Entry points are the same for all mounted options and also for all unmounted since only 2 players spawn at a time.
# Duel scores are only kept for duels against heroes (companions, lords and kings).

(
"arena_duel_thing_std",mtf_arena_fight,-1,
"The duel begins!",
[
# visitors 0 and 1 are completely standard
(0, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
(8, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
#visitors 2 and 3 are override horse only
(56, mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, []),
(58, mtef_visitor_source|mtef_team_2, af_override_horse, aif_start_alarmed, 1, []),
#vistiors 4 and 5 are sword/shield standard
(0, mtef_visitor_source|mtef_team_0, af_override_weapons, aif_start_alarmed, 1, [itm_vibro_sword3_gold, itm_energy_shield_yellow_medium]),
(8, mtef_visitor_source|mtef_team_2,af_override_weapons, aif_start_alarmed, 1, [itm_vibro_sword3_gold, itm_energy_shield_yellow_medium]),
#visitors 6 and 7 are sword/shield no horse
(56, mtef_visitor_source|mtef_team_0, af_override_weapons|af_override_horse, aif_start_alarmed, 1, [itm_vibro_sword3_gold, itm_energy_shield_yellow_medium]),
(58, mtef_visitor_source|mtef_team_2,af_override_weapons|af_override_horse, aif_start_alarmed, 1, [itm_vibro_sword3_gold, itm_energy_shield_yellow_medium]),
#vistiors 8 and 9 are 2-H standard
(0, mtef_visitor_source|mtef_team_0, af_override_weapons, aif_start_alarmed, 1, [itm_vibro_axe_long_2h, itm_vibro_sword2b, itm_electro_staff_long]),
(8, mtef_visitor_source|mtef_team_2,af_override_weapons, aif_start_alarmed, 1, [itm_vibro_axe_long_2h, itm_vibro_sword2b, itm_electro_staff_long]),
#visitors 10 and 11 are 2-H no horse
(56, mtef_visitor_source|mtef_team_0, af_override_weapons|af_override_horse, aif_start_alarmed, 1, [itm_vibro_axe_long_2h, itm_vibro_sword2b, itm_electro_staff_long]),
(58, mtef_visitor_source|mtef_team_2,af_override_weapons|af_override_horse, aif_start_alarmed, 1, [itm_vibro_axe_long_2h, itm_vibro_sword2b, itm_electro_staff_long]),
#vistiors 12 and 13 are ranged standard - note that armor is also changed
(0, mtef_visitor_source|mtef_team_0, af_override_all_but_horse|af_override_foot, aif_start_alarmed, 1, [itm_vibro_blade1, itm_westar, itm_westar_shield, itm_laser_bolts_yellow_pistol, itm_mandalorian_commando_armor, itm_mandalorian_commando_helmet, itm_mandalorian_commando_boots, itm_grey_gloves]),
(8, mtef_visitor_source|mtef_team_2, af_override_all_but_horse|af_override_foot, aif_start_alarmed, 1, [itm_vibro_blade1, itm_westar, itm_westar_shield, itm_laser_bolts_yellow_pistol, itm_mandalorian_commando_armor, itm_mandalorian_commando_helmet, itm_mandalorian_commando_boots, itm_grey_gloves]),
#visitors 14 and 15 are ranged no horse - note that armor is also changed
(0, mtef_visitor_source|mtef_team_0, af_override_everything, aif_start_alarmed, 1, [itm_vibro_blade1, itm_westar, itm_westar_shield, itm_laser_bolts_yellow_pistol, itm_mandalorian_commando_armor, itm_mandalorian_commando_helmet, itm_mandalorian_commando_boots, itm_grey_gloves]),
(8, mtef_visitor_source|mtef_team_2, af_override_everything, aif_start_alarmed, 1, [itm_vibro_blade1, itm_westar, itm_westar_shield, itm_laser_bolts_yellow_pistol, itm_mandalorian_commando_armor, itm_mandalorian_commando_helmet, itm_mandalorian_commando_boots, itm_grey_gloves]),

],
[

    #SW - added shield bash integration
    shield_bash_kit_1,
    shield_bash_kit_2,
    shield_bash_kit_3,
    shield_bash_kit_4,

    #SW - added regen for certain agents
    #common_regeneration_store_info,
    #common_regeneration,

	#SW - add custom lightsaber noise
	#lightsaber_noise_idle,			#commented out, not necessary and idle noise sometimes interupts saber swing
	lightsaber_noise_player,
	lightsaber_noise_agent,
	common_change_fog,
	common_use_healthpack,
	#common_use_binocular_1,
	#common_use_binocular_2,
	common_helmet_view,
	common_zoom_view,
	common_use_jetpack,
	common_toggle_weapon_capabilities,
	common_crouch_button,

	common_inventory_not_available,


   (ti_tab_pressed, 0, 0, [],
       [(question_box,"@Do you wish to give up the fight?")]),
    (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
       (eq,":answer",0),
 #add 1 to the slot for amount of duels the player lost against this troop if it is a tf_hero
      (try_begin),
         (troop_is_hero, "$g_talk_troop"),
         (assign, "$g_duel_result", -1),
         (troop_get_slot, ":duel_losses", "$g_talk_troop", slot_troop_duel_lost),
         (val_add, ":duel_losses", 1),
         (troop_set_slot, "$g_talk_troop", slot_troop_duel_lost, ":duel_losses"),
      (try_end),
 #add 1 to the total amount of duels player lost if it is a tf_hero
      (try_begin),
         (troop_is_hero, "$g_talk_troop"),
         (troop_get_slot, ":duel_losses_player", "trp_player", slot_troop_duel_lost),
         (val_add, ":duel_losses_player", 1),
         (troop_set_slot, "trp_player", slot_troop_duel_lost, ":duel_losses_player"),
         (assign, reg(2), ":duel_losses_player"),
         (display_message, "@You've lost a total number of {reg2} duels."),
      (try_end),
      (assign, "$g_duel_result", -1),
      (finish_mission),
      ]),

(1,3, ti_once, [
    (all_enemies_defeated, 1),
    (neg|main_hero_fallen, 0)
    ],
 [
#add 1 to the slot for amount of duels the player won against this troop if it is a tf_hero
   (assign, "$g_duel_result", 1),
   (try_begin),
      (troop_is_hero, "$g_talk_troop"),
      (troop_get_slot, ":duel_wins", "$g_talk_troop", slot_troop_duel_won),
      (val_add, ":duel_wins", 1),
      (troop_set_slot, "$g_talk_troop", slot_troop_duel_won, ":duel_wins"),


#add 1 to the total amount of duels player won if it is a tf_hero

      (troop_get_slot, ":duel_wins_player", "trp_player", slot_troop_duel_won),
      (val_add, ":duel_wins_player", 1),
      (troop_set_slot, "trp_player", slot_troop_duel_won, ":duel_wins_player"),
      (assign, reg(2), ":duel_wins_player"),
      (display_message, "@You've won a total number of {reg2} duels"),
   (try_end),
    (finish_mission),
   ]),

(2, 3, ti_once, [
    (main_hero_fallen),
    ],
   [
#add 1 to the slot for amount of duels the player lost against this troop if it is a tf_hero
    (assign, "$g_duel_result", -1),
   (try_begin),
      (troop_is_hero, "$g_talk_troop"),
      (troop_get_slot, ":duel_losses", "$g_talk_troop", slot_troop_duel_lost),
      (val_add, ":duel_losses", 1),
      (troop_set_slot, "$g_talk_troop", slot_troop_duel_lost, ":duel_losses"),
      (assign, reg(1), ":duel_losses"),

#add 1 to the total amount of duels player lost if it is a tf_hero
      (troop_get_slot, ":duel_losses_player", "trp_player", slot_troop_duel_lost),
      (val_add, ":duel_losses_player", 1),
      (troop_set_slot, "trp_player", slot_troop_duel_lost, ":duel_losses_player"),
      (assign, reg(2), ":duel_losses_player"),
      (display_message, "@You've lost a total number of {reg2} duels."),
   (try_end),
    (finish_mission),
    ]),


		#SWY - trigger to make unique agents behavior - custom scripting
	  (0.352, 0, ti_once, [], [(call_script,"script_swy_unique_units_stuff",-1)]),

 ],
),

########################## Duel Mod End ##############################


]




