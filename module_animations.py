# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_animations import *

####################################################################################################################
#  There are two animation arrays (one for human and one for horse). Each animation in these arrays contains the following fields:
#  1) Animation id (string): used for referencing animations in other files. The prefix anim_ is automatically added before each animation-id .
#  2) Animation flags: could be anything beginning with acf_ defined in header_animations.py
#  3) Animation sequences (list).
#  3.1) Duration of the sequence.
#  3.2) Name of the animation resource.
#  3.3) Beginning frame of the sequence within the animation resource.
#  3.4) Ending frame of the sequence within the animation resource.
#  3.5) Sequence flags: could be anything beginning with arf_ defined in header_animations.py
# 
####################################################################################################################

#plan : 
# basic movement : walk ride etc. 0 -20000
#  on_foot  : 0     - 10000
#  horse    : 10000 - 20000
# combat         :                20000 - 40000
# fall           :                4000 - 70000
# act            : misc.          70000 - ...

horse_move = 10000
combat     = 20000
defend     = 35000
blow       = 40000

attack_parry_duration = 0.45
defend_parry_duration = 0.3
ready_durn     = 0.35
defend_duration = 0.25
pole_defend_duration = 0.4
cancel_duration = 0.25

blend_in_defense = arf_blend_in_5
blend_in_ready = arf_blend_in_6
blend_in_release = arf_blend_in_5
blend_in_parry = arf_blend_in_5

blend_in_walk = arf_blend_in_3

#### Animations begin here

# All of the animations are hardcoded. You can edit the individual sequences, resources or times. But each
# animation must stay at the same position, otherwise the game won't run properly. If you want to add a new animation,
# you can change both the ids and values of the animations which are named as unused_human_anim_???
# and unused_horse_anim_??? (??? = any number). You must not change used animations' ids.

#acm - added Animations Compilation Mod - http://forums.taleworlds.net/index.php/topic,57607.0.html

animations = [
 ["stand", 0,
 #["stand", acf_enforce_lowerbody | acf_synch_with_horse,		#SW - trying to make the player move up/down with the horse_stand animation, nope...
#   [3.0, "myanim", 0, 50, arf_cyclic|arf_loop_pos_0_25],
   [3.0, "anim_human", 50, 52, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [3.0, "anim_human", 60, 62, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.75],
   [3.0, "anim_human", 70, 72, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [3.0, "anim_human", 80, 82, arf_use_stand_progress|arf_cyclic|arf_two_handed_blade, 0, (0, 0, 0), 0.5],
##   [35.0, "stand_woman", 0, 1059, arf_use_stand_progress|arf_cyclic|arf_two_handed_blade, 0, (0, 0, 0), 0.5],
##   [43.0, "stand_woman_public", 0, 1313, arf_use_stand_progress|arf_cyclic|arf_two_handed_blade, 0, (0, 0, 0), 0.5],
#  [35.0, "tavern_stand", 0, 472, arf_cyclic|arf_loop_pos_0_25],
 ],
 ["stand_man", 0,
 #["stand_man", acf_enforce_lowerbody | acf_synch_with_horse,	#SW - trying to make the player move up/down with the horse_stand animation, nope...
#        [3.0, "lord_stand", 0, 72, arf_cyclic|arf_loop_pos_0_25],
   [3.5, "anim_human", 90, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [3.5, "anim_human", 110, 120, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
#   [124.0, "stand_shopkeeper", 0, 3740, arf_cyclic|arf_loop_pos_0_25],
#   [80.0, "stand_guardsman", 0, 2397, arf_cyclic|arf_loop_pos_0_25],
 ],
 ["jump", acf_enforce_lowerbody|acf_displace_position,
 
 [0.6, "sw_jump1", 1, 36, arf_blend_in_1, 0, (0, 0, 0), 0.4], #new jump by swyter
 
   #[1.09, "jump", 22, 48, arf_blend_in_1],
   #@>[1.09, "jump", 22, 48, arf_blend_in_1, 0, (0, 0, 0), 1.0],	#acm modified
   #@>[0.8, "anim_human", 270, 272, arf_blend_in_1, 0, (0, 0, 0), 0.7],	#acm new
##   [0.8, "anim_human", 270, 272, arf_blend_in_4],
 ],
 # Super-Mario Stype Super Jump - http://forums.taleworlds.net/index.php/topic,65520.msg1703891.html
 #["rider_fall_roll", acf_enforce_all|acf_displace_position,
 #  [2.5, "anim_human", blow+ 2000, blow+2084,  arf_blend_in_8, 0, (-0.4,0.2,0), 1.0], 
 #["jump", acf_enforce_lowerbody|acf_displace_position,
   #[1.09, "jump", 22, 48, arf_blend_in_1, 0, (0, 10, 0), 0],
 #], 
 ["jump_end", acf_enforce_lowerbody|acf_displace_position,
 
 [0.5, "sw_jump1", 30, 1, arf_blend_in_1, 0, (0, 0, 0), 0.3], #new jump by swyter
   #[0.3, "jump", 48, 55, arf_blend_in_1],
   #@>[0.3, "jump", 48, 55, arf_blend_in_1, 0, (0, 0, 0), 0.2],	#acm modified
   #@>[0.4, "anim_human", 280, 290, arf_blend_in_1, 0, (0, 0, 0), 0.3],	#acm new
 ],
 ["stand_unarmed", 0,
  #["stand_unarmed", acf_enforce_lowerbody | acf_synch_with_horse,	#SW - trying to make the player move up/down with the horse_stand animation, nope ...
   [8, "noweapon_cstance", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["stand_single", 0, #Used for Lightsaber pair
    #[9.0, "sw_single_saber_static", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
    [9.0, "sword_loop01", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   #[4.0, "sword_loop02", 0, 100, arf_cyclic|arf_loop_pos_0_25],  
   [6.0, "greatsword_cstance", 0, 91, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],  
 ],
 ["stand_greatsword", 0, #used for standard lightsaber
   [6.0, "greatsword_cstance", 0, 91, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],  
   [2.0, "anim_human", 1100, 1120, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.1],  	#acm new
 ],
 ["stand_staff", 0,
 [9.0, "sw_single_saber_static", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 [9.0, "sword_loop01", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   #[2.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  
   #[2.0, "anim_human", 1500, 1520, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  #acm new
 ],
 #SW - modified stand_crossbow
 ["stand_crossbow", 0,
   #[2.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  		#native
   [6.0, "new_rifle_stand", 0, 99, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],  	#from 1866 mod
 ],
 ["walk_forward", acf_enforce_lowerbody,
#   [1.0, "anim_human", 6000, 6020, arf_walk,pack2f(0.4,0.9)],
   [1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_onehanded", acf_enforce_lowerbody,
#   [1.0, "anim_human", 6000, 6020, arf_walk,pack2f(0.4,0.9)],
   [1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_staff", acf_enforce_lowerbody,
   [1.0, "anim_human", 6100, 6120, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   ##[1.0, "sw_staff_anim", 0, 99, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_greatsword", acf_enforce_lowerbody,
   [1.0, "anim_human", 6200, 6220, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward", acf_enforce_lowerbody,
##   [1.0, "anim_human", 6020, 6000, arf_phase_odd|arf_walk,pack2f(0.4,0.9)],
   [1.0, "anim_human", 6020, 6000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_onehanded", acf_enforce_lowerbody,
#   [1.0, "anim_human", 6000, 6020, arf_walk,pack2f(0.4,0.9)],
   [1.0, "man_walk", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_staff", acf_enforce_lowerbody,
   [1.0, "anim_human", 6120, 6100, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   ##[1.0, "sw_staff_anim", 99, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_greatsword", acf_enforce_lowerbody,
   [1.0, "anim_human", 6220, 6200, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["run_forward", acf_enforce_lowerbody,
#   [0.8, "anim_human", 7000, 7040, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.4,0.9)], 
   [0.8, "run_man_forward", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_onehanded", acf_enforce_lowerbody,
#   [0.8, "anim_human", 7000, 7040, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9)], 
#   [0.8, "run_normal", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.4,0.9)], 
   [0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_staff", acf_enforce_lowerbody,

#   [0.8, "anim_human", 7100, 7140, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_greatsword", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ### [0.8, "run_forward_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
    ##[0.8, "sw_staff_anim", 0, 99, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
	[0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_greatsword", acf_enforce_lowerbody,
#   [0.8, "anim_human", 7200, 7240, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_greatsword", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right", acf_enforce_lowerbody,
##   [0.8, "run_normal", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [0.8, "run_man_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 

 ],
 ["run_forward_right_onehanded", acf_enforce_lowerbody,
##   [0.8, "run_crossright_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_staff", acf_enforce_lowerbody,
##   [0.8, "run_crossright_staff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_right_greatsword", acf_enforce_lowerbody,
##   [0.8, "run_crossright_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left", acf_enforce_lowerbody,
##   [0.8, "run_normal", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_onehanded", acf_enforce_lowerbody,
##   [0.8, "run_crossleft_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_staff", acf_enforce_lowerbody,
##   [0.8, "run_crossleft_staff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_forward_left_greatsword", acf_enforce_lowerbody,
##   [0.8, "run_crossleft_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
   [0.8, "run_man_forward_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4], 
 ],
 ["run_backward", acf_enforce_lowerbody,
#   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "run_man_forward", 24, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.4],
 ],
 ["run_backward_onehanded", acf_enforce_lowerbody,
   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["run_backward_staff", acf_enforce_lowerbody,
   #[1.0, "anim_human", 7140, 7100, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "anim_human", 7040, 7000, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["run_backward_greatsword", acf_enforce_lowerbody,
   [1.0, "anim_human", 7240, 7200, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_right", acf_enforce_lowerbody,
   [1.0, "walk_right_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_onehanded", acf_enforce_lowerbody,
   [1.0, "walk_right_onehanded_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_twohanded", acf_enforce_lowerbody,
   [1.0, "walk_right_greatsword_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_right_polearm", acf_enforce_lowerbody,
   #[1.0, "walk_right_staff_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [1.0, "walk_right_onehanded_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_left", acf_enforce_lowerbody,
   [1.0, "walk_left_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_onehanded", acf_enforce_lowerbody,
   [1.0, "walk_left_onehanded_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_twohanded", acf_enforce_lowerbody,
   [1.0, "walk_left_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_left_polearm", acf_enforce_lowerbody,
   #[1.0, "walk_left_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "walk_left_onehanded_r", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_right", acf_enforce_lowerbody,
   [1.0, "walk_crossright_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_onehanded", acf_enforce_lowerbody,
   [1.0, "walk_crossright_onehanded", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_twohanded", acf_enforce_lowerbody,
   [1.0, "walk_crossright_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_right_polearm", acf_enforce_lowerbody,
   #[1.0, "walk_crossright_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [1.0, "walk_crossright_onehanded", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_forward_left", acf_enforce_lowerbody,
   [1.0, "walk_crossleft_normal", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_onehanded", acf_enforce_lowerbody,
   [1.0, "walk_crossleft_onehanded", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_twohanded", acf_enforce_lowerbody,
   [1.0, "walk_crossleft_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_forward_left_polearm", acf_enforce_lowerbody,
   #[1.0, "walk_crossleft_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "walk_crossleft_onehanded", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_left", acf_enforce_lowerbody,
   [1.0, "walk_crossright_normal", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_onehanded", acf_enforce_lowerbody,
   [1.0, "walk_crossright_onehanded", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_twohanded", acf_enforce_lowerbody,
   [1.0, "walk_crossright_greatsword", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_left_polearm", acf_enforce_lowerbody,
   #[1.0, "walk_crossright_staff", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [1.0, "walk_crossright_onehanded", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["walk_backward_right", acf_enforce_lowerbody,
   [1.0, "walk_crossleft_normal", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_onehanded", acf_enforce_lowerbody,
   [1.0, "walk_crossleft_onehanded", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_twohanded", acf_enforce_lowerbody,
   [1.0, "walk_crossleft_greatsword", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["walk_backward_right_polearm", acf_enforce_lowerbody,
   #[1.0, "walk_crossleft_staff", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "walk_crossleft_onehanded", 32, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ],
 ["run_right", acf_enforce_lowerbody,
#   [0.8, "anim_human", 9000, 9020, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_normal", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_onehanded", acf_enforce_lowerbody,
#   [0.8, "run_right_onehanded", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_twohanded", acf_enforce_lowerbody,
#   [0.8, "run_right_greatsword", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_right_polearm", acf_enforce_lowerbody,
#   [0.8, "run_right_staff", 0, 12, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
##   [0.8, "run_right_staff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 #  [0.8, "run_man_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
    [0.8, "run_man_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
 ],
 ["run_left", acf_enforce_lowerbody,
#   [0.8, "anim_human", 9500, 9520, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
##   [0.8, "run_left_normal", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_onehanded", acf_enforce_lowerbody,
#   [0.8, "run_left_onehanded", 0, 12, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 ],
 ["run_left_twohanded", acf_enforce_lowerbody,
#   [0.8, "anim_human", 9500, 9520, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
#   [0.8, "run_left_greatsword", 0, 12, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
##   [0.8, "run_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
   [0.8, "run_man_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  

 ],
 ["run_left_polearm", acf_enforce_lowerbody,
#   [0.8, "run_left_staff", 0, 12, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
##   [0.8, "run_left_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],  
 #  [0.8, "run_man_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0], 
   [0.8, "run_man_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],     
 ],
 #SW - modified ride_0 (nevermind)
 ["ride_0", acf_align_with_ground|acf_enforce_lowerbody,
 #["ride_0", acf_enforce_lowerbody|acf_synch_with_horse,		#synch_with_horse didn't work to get them to move up/down
  ## [10.0, "anim_human", horse_move+2000, horse_move+2100, arf_cyclic],
  # [3.0, "anim_human_02", 600, 644, arf_cyclic],
##   [37.0, "stand_onhorse", 0, 1110, arf_cyclic],
##   [22.0, "stand_onhorse_sword", 0, 671, arf_cyclic],
   #[15.0, "stand_onhorse", 0, 456, arf_cyclic],		#original native animation
   [12.0, "sw_pilot_stand", 0, 199, acf_align_with_ground|arf_cyclic|arf_blend_in_2],
   #[5.0, "sw_pilot_stand", 0, 99, arf_cyclic],
   #[10.0, "sw_pilot_stand", 0, 199, arf_cyclic],
   #[5.0, "sw_speeder_stand", 0, 99, arf_cyclic|arf_use_stand_progress|arf_make_walk_sound, 0, (0, 0, 0), 0.0],	#SW - new horse_stand animation by Swyter   
   
  ],
  #SW - modified ride_1
 ["ride_1", acf_enforce_lowerbody | acf_synch_with_horse | acf_align_with_ground,
   #[1.0, "anim_human_02", 0, 31, arf_cyclic],
   [1.0, "anim_human_02", 0, 0, arf_cyclic],
 ],
 #SW - modified lancer_ride_1
 ["lancer_ride_1", acf_enforce_lowerbody | acf_synch_with_horse,
   #[0.8, "anim_human", horse_move+210, horse_move+250, arf_cyclic |  arf_blend_in_16],
   [0.8, "anim_human", horse_move+210, horse_move+210, arf_cyclic |  arf_blend_in_16],
 ],
 #SW - modified lancer_charge_parried
 ["lancer_charge_parried",acf_enforce_lowerbody,
   #[1.0, "anim_human", horse_move+210, horse_move+220, arf_blend_in_32],
   [1.0, "anim_human", horse_move+210, horse_move+210, arf_blend_in_32],
 ],
 #SW - modified ride_2
 ["ride_2", acf_enforce_lowerbody | acf_synch_with_horse,
   #[0.8, "anim_human_02", 50, 69, arf_cyclic], 
   [0.8, "anim_human_02", 50, 50, arf_cyclic], 
   #[1.0, "anim_human_02", 100, 100, arf_cyclic], 
 ],
 #SW - modified ride_3
 ["ride_3", acf_enforce_lowerbody | acf_synch_with_horse,
   #[0.6, "anim_human_02", 100, 116, arf_cyclic], 
   [0.6, "anim_human_02", 100, 100, arf_cyclic], 
   #[1.0, "anim_human_02", 100, 100, arf_cyclic], 
 ],
 #SW - modified ride_4
 ["ride_4", acf_enforce_lowerbody | acf_synch_with_horse,
   #[0.5, "anim_human_02", 150, 165, arf_cyclic], 
   #[0.5, "anim_human_02", 150, 150, arf_cyclic], 
   [0.5, "anim_human_02", 100, 100, arf_cyclic], 
   #[1.0, "anim_human_02", 100, 100, arf_cyclic], 
 ],
 #SW - modified lancer_ride_4
 ["lancer_ride_4", acf_enforce_lowerbody | acf_synch_with_horse | acf_parallels_for_look_slope|acf_anim_length(100),
   #[0.5, "anim_human", horse_move+610, horse_move+650, arf_cyclic | arf_blend_in_128], 
   [0.5, "anim_human", horse_move+610, horse_move+610, arf_cyclic | arf_blend_in_128], 
 ],
 #SW - modified ride_rear
 #["ride_rear", acf_enforce_lowerbody|acf_ignore_slope,
 ["ride_rear", acf_enforce_lowerbody|acf_ignore_slope,
##   [1.4, "anim_human", horse_move+820, horse_move+837,  arf_blend_in_16],
##   [2.4, "anim_human", horse_move+820, horse_move+837,  arf_blend_in_16],
   #[2.0, "anim_human_02", 260, 301,  arf_blend_in_8],
   [1.0, "anim_human_02", 260, 260,  arf_blend_in_8],   
 ],
 ["ride_spur", acf_enforce_lowerbody,
   [0.3, "anim_human", horse_move+860, horse_move+865,  arf_blend_in_8],
 ],
 ["ride_jump", acf_enforce_lowerbody,
## [1.6, "anim_human_02", 400, 420,  arf_blend_in_16],
   [1.6, "anim_human_02", 205, 222,  arf_blend_in_4],#|arf_end_pos_0_25],
 ],
 ["ride_jump_end", acf_enforce_all,
## [0.1, "anim_human", horse_move+935, horse_move+940,  arf_blend_in_16], 
## [0.3, "anim_human_02", 420, 424,  arf_blend_in_16],
   [0.1, "anim_human_02", 222, 224,  arf_blend_in_16],
 ],
  #SW - modified ride_turn_right (nevermind, this messed up the speeder animations)
 ["ride_turn_right", acf_enforce_lowerbody | acf_synch_with_horse,
   [1.0, "anim_human_02", 500, 533, arf_cyclic],
   #[0.1, "anim_human_02", 500, 500, arf_cyclic],
 ],
 #SW - modified ride_turn_left (nevermind, this messed up the speeder animations)
 ["ride_turn_left", acf_enforce_lowerbody | acf_synch_with_horse,
   [1.0, "anim_human_02", 450, 483, arf_cyclic], 
   #[0.1, "anim_human_02", 450, 450, arf_cyclic], 
 ],
 
 ["mount_horse", acf_enforce_all,
  # [2.0, "anim_human", horse_move+1000, horse_move+1050,  arf_blend_in_1, 0, (0.0,0,0.0)],
  [2.0, "sw_pilot_mount", 0, 100,  arf_blend_in_2, 0, (0.0,0,0.0)],
 ],
 ["dismount_horse", acf_enforce_lowerbody|acf_displace_position,
  # [2.0, "anim_human", horse_move+1100, horse_move+1150,  arf_blend_in_1, 0, (-0.5,0,0)],
  [3.0, "sw_pilot_mount", 100, 0,   arf_blend_in_1, 0, (-0.6,0,0)],
 ],
 #SW - modified lancer_ride_0 (nevermind)
 #["lancer_ride_0", acf_enforce_lowerbody,
 ["lancer_ride_0", acf_enforce_lowerbody | acf_synch_with_horse,
##   [4.0, "anim_human", horse_move + 5000, horse_move + 5057, arf_lancer|arf_cyclic],
   [43.0, "stand_onhorse_staff", 0, 1300, arf_lancer|arf_cyclic],
 ],
 ["equip_default", 0,
##   [0.6, "anim_human", combat+0, combat+20, arf_blend_in_0],
  ##@> 0-9-0-4 by SWYT [0.6, "equip_arms", 206, 221, arf_blend_in_0],   
  [0.6, "equip_arms", 352, 365, arf_blend_in_0],
 ],
 ["unequip_default", 0,
##   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.3, "equip_arms", 207, 200, arf_blend_in_0],
 ],
 ["equip_sword", 0,
   [0.8, "equip_sword", 0, 27, arf_blend_in_0],
##   [0.6, "draw_greatsword", 0, 52, arf_blend_in_0],
##   [0.6, "anim_human", combat+0, combat+20, arf_blend_in_0],
 ],
 ["unequip_sword", 0,
#  [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.3, "equip_sword", 6, 0, arf_blend_in_0],
 ],
 ["equip_greatsword", 0,
   #[1.2, "draw_greatsword", 0, 35, arf_blend_in_0],
   [1.4, "draw_greatsword", 0, 35, arf_blend_in_0],	#acm modified
   [1.2, "brfedit-01", 20000, 20024, arf_blend_in_0, 0, (0, 0, 0), 1.1],	#acm new
 ],
 ["unequip_greatsword", 0,
   [0.3, "draw_greatsword", 10, 0, arf_blend_in_0],
 ],
 ["equip_axe_left_hip", 0,
   [0.8, "draw_axe", 0, 16, arf_blend_in_0],
 ],
 ["unequip_axe_left_hip", 0,
   [0.3, "draw_axe", 6, 0, arf_blend_in_0],
 ],
 ["equip_crossbow", 0,
   [1.2, "equip_greataxe", 0, 20, arf_blend_in_0],
 ],
 ["unequip_crossbow", 0,
   [0.3, "equip_greataxe", 10, 0, arf_blend_in_0],
 ],
 ["equip_spear", 0,
##   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
   [0.8, "equip_arms", 17, 34, arf_blend_in_0],
 ],
 ["unequip_spear", 0,
##   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.3, "equip_arms", 15, 10, arf_blend_in_0],
 ],
 #SW - modified equip_dagger_front_left
 ["equip_dagger_front_left", 0,
##   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
   #[0.8, "equip_arms", 253, 276, arf_blend_in_0],			# original equip_dagger_front_left		MAYBE
   [0.8, "equip_sword", 0, 27, arf_blend_in_0],		# from equip_swordq	GOOD
   #[1.2, "draw_greatsword", 0, 35, arf_blend_in_0],		# from equip_greatsword			MAYBE
   #[0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],	# from equip_katana   		BAD
   [0.8, "draw_axe", 0, 16, arf_blend_in_0],	#equip_axe_left_hip		GOOD
 ],
 ["unequip_dagger_front_left", 0,
##   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.2, "equip_arms", 254, 250, arf_blend_in_0],
 ],
 ["equip_dagger_front_right", 0,
##   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
   [0.8, "equip_arms", 305, 333, arf_blend_in_0],
 ],
 ["unequip_dagger_front_right", 0,
##   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.4, "equip_arms", 306, 300, arf_blend_in_0],
 ],
 ["equip_axe_back", 0,
   [1.0, "equip_greataxe", 0, 17, arf_blend_in_0],
 ],
 ["unequip_axe_back", 0,
   [0.3, "equip_greataxe", 7, 0, arf_blend_in_0],
 ],
 ["equip_revolver_right", 0,
##   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
   [0.6, "equip_arms", 352, 365, arf_blend_in_0],
 ],
 ["unequip_revolver_right", 0,
##   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
   [0.3, "equip_arms", 354, 350, arf_blend_in_0],
 ],
 ["equip_pistol_front_left", 0,
   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
 ],
 ["unequip_pistol_front_left", 0,
   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
 ],
 ["equip_katana", 0,
   [0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],
 ],
 ["unequip_katana", 0,
   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
 ],
 ["equip_wakizashi", 0,
   [0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],
 ],
 ["unequip_wakizashi", 0,
   [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
 ],
 ["equip_shield", 0,
##   [0.6, "anim_human", combat+30, combat+45, arf_blend_in_0],
   [0.8, "equip_arms", 68, 84, arf_blend_in_0],
 ],
 ["unequip_shield", 0,
##   [0.3, "anim_human", combat+40, combat+30, arf_blend_in_0],
   [0.4, "equip_arms", 62, 50, arf_blend_in_0],
 ],
 ["equip_bow_back", 0,
   [0.7, "equip_arms", 161, 179, arf_blend_in_0],
 ],
 ["unequip_bow_back", 0,
   [0.3, "equip_arms", 163, 150, arf_blend_in_0],
 ],
 ["equip_bow_left_hip", 0,
   [0.7, "equip_arms", 110, 148, arf_blend_in_0],
 ],
 ["unequip_bow_left_hip", 0,
   [0.3, "equip_arms", 115, 108, arf_blend_in_0],
 ],

 ["cancel_attack_onehanded", acf_rotate_body,
   [cancel_duration, "anim_human", 110, 111, arf_blend_in_8],
 ],
 ["cancel_attack_twohanded", acf_rotate_body,
   [cancel_duration, "anim_human", 1100, 1100, arf_blend_in_8],
 ],
 ["cancel_attack_polearm", acf_rotate_body,
   [cancel_duration, "anim_human", 1500, 1500, arf_blend_in_8],
 ],
#TODO: ready bow, release javelin and reload crossbow should have the same time 
# duration and controlled via weapon speed.
 ["ready_bow", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   #[1.5, "anim_human", combat+500, combat+530, blend_in_ready|arf_make_custom_sound, pack2f(0.14, 0.44)],
   [1.0, "sw_force_power_1", 0, 47, blend_in_ready|arf_make_custom_sound, pack2f(0.14, 0.44)],	#by Swyter
 ],
 ["release_bow", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   #[0.3, "anim_human", combat+530, combat+532, arf_blend_in_2],
   [1.0, "sw_force_power_1", 47, 99, arf_blend_in_2],		#by Swyter
 ],
 ["ready_bow_mounted", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [1.5, "anim_human", combat+800, combat+830, blend_in_ready|arf_make_custom_sound, pack2f(0.10, 0.40)],
 ],
 ["release_bow_mounted", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.3, "anim_human", combat+830, combat+832, arf_blend_in_2],
 ],
 ["ready_crossbow", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   #[1.5, "anim_human", combat+1300, combat+1320, blend_in_ready],	#native animation
   #[0.3, "new_rifle", 21300, 21330, blend_in_ready],	#1866 animation
   [0.3, "new_rifle_old", 21275, 21300, blend_in_ready],	#1866 animation old animation (better for SWC)
 ],
 ["release_crossbow", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   #[0.2, "anim_human", combat+1330, combat+1331, arf_blend_in_1],		#native animation
   #[0.1, "anim_human", 21330, 21331, arf_blend_in_1],		#1866 animation
   [0.1, "anim_human", 21300, 21300, arf_blend_in_1],		#1866 animation old (better for SWC)
 ],
 #SW - modified reload_crossbow
 ["reload_crossbow", 0,
   #[1.0, "anim_human", combat+1700, combat+1750, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)], 
   #[1.6, "anim_human", combat+1745, combat+1750, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#from reload_crossbow      
   [2.4, "reload", 0, 39, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#Lucke189_animations
 ],
 ["reload_crossbow_horseback", 0,
   [1.6, "anim_human", combat+1800, combat+1877, arf_blend_in_8|arf_make_custom_sound, pack2f(0.27, 0.94)], 
 ],
 # commented out native ready_javelin
 # ["ready_javelin", acf_rotate_body,
   # [0.3, "throw_javelin", 0, 30, blend_in_ready],
   # [0.3, "anim_human", 22000, 22010, blend_in_ready, 0, (0, 0, 0), 0.2],	#acm new
# ],
#SW - used ready_javelin animation for a new ready animations for the ranged weapons
 ["ready_javelin", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.3, "holding_big_gun", 270, 285, blend_in_ready],	#animation from WWII China Battlefield
 ],
 #SW - commented out native release_javelin
 # ["release_javelin", acf_rotate_body,
   # [1.0, "throw_javelin", 55, 100, arf_blend_in_0],
 # ],
#SW - used release_javelin animation for a new ready animations for the ranged weapons
 ["release_javelin", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.1, "holding_big_gun", 285, 285, arf_blend_in_1],		#animation from WWII China Battlefield
 ], 
 ["ready_throwing_knife", acf_rotate_body,
   [0.3, "throw_knife", 10, 30, blend_in_ready],
   [0.3, "anim_human", 22100, 22110, blend_in_ready, 0, (0, 0, 0), 0.2],	#acm new
 ],
 ["release_throwing_knife", acf_rotate_body,
   [0.8, "throw_knife", 30, 70, arf_blend_in_0],
 ],
 ["ready_throwing_axe", acf_rotate_body,
   [0.3, "throw_axe", 0, 40, blend_in_ready],
   [0.3, "anim_human", 22100, 22110, blend_in_ready, 0, (0, 0, 0), 0.2],	#acm new
 ],
 ["release_throwing_axe", acf_rotate_body,
   [0.9, "throw_axe", 40, 90, arf_blend_in_0],
 ],
 ["ready_stone", acf_rotate_body,
##   [0.3, "anim_human", combat+2200, combat+2210, blend_in_ready],
   [0.7, "throw_stone", 0, 21, blend_in_ready],
   #[0.3, "anim_human", 22200, 22210, blend_in_ready, 0, (0, 0, 0), 0.2],	#acm new	#SW - commented out
#SW   [0.3, "throw_knife", 10, 30, blend_in_ready],	#from ready_throwing_knife (doesn't work, I was hoping to keep the spinning knife animation but have the item disapear like stones do...)   
 ],
 ["release_stone", acf_rotate_body,
##   [1.0, "anim_human", combat+2210, combat+2225, arf_blend_in_0],
   [1.0, "throw_stone", 21, 54, arf_blend_in_0],
#SW   [0.8, "throw_knife", 30, 70, arf_blend_in_0],   #from release_throwing_knife (doesn't work, I was hoping to keep the spinning knife animation but have the item disapear like stones do...)   
 ],
 #SW - modified ready_pistol
 ["ready_pistol", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),	#native
   [0.3, "anim_human", combat+2500, combat+2515, arf_blend_in_8], 						#native
   #[0.3, "readypistol_fixed_by_swy", 0, 1, arf_blend_in_8], 						#Lucke189 + CMW animations (fixed by Swyter)	- issue where it doesn't look up/down with aiming tho..
 ],
 #SW - modified release_pistol
 ["release_pistol", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
 #["release_pistol", acf_parallels_for_look_slope|acf_anim_length(100),
   [0.3, "anim_human", combat+2520, combat+2527, arf_blend_in_1],
   #[0.3, "releasepistol_fixed_by_swy", 0, 3, arf_blend_in_1],	#Lucke189 + CMW animations (fixed by Swyter)	- issue where it doesn't look up/down with aiming tho..
 ],
 #SW - trying to modify reload animation 
 ["reload_pistol", 0,
   #[2.0, "anim_human", combat+2650, combat+2860, arf_blend_in_8],
   #[1.5, "anim_human", combat+1745, combat+1750, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#from reload_crossbow
   #[2.0, "reloadpistol", 0, 14, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#Lucke189_animations
   [2.4, "reloadpistol_fixed_by_swy", 0, 14, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#Lucke189_animations  (fixed by Swyter)
 ],
 
 # ["ready_musket", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   # [1.5, "anim_human", combat+1300, combat+1320, blend_in_ready],
 # ],
 # ["release_musket", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   # [0.2, "anim_human", combat+1330, combat+1331, arf_blend_in_1],
 # ],
 #SW - new animations from Highlander's 1866 Mod
 ["ready_musket", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.5, "new_rifle_crouch", combat+1300, combat+1330, blend_in_ready],
 ],
 ["release_musket", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.1, "new_rifle_crouch", combat+1330, combat+1331, arf_blend_in_1],
 ], 
 #SW - trying to modify reload animation 
 ["reload_musket", 0,
   #[2.0, "anim_human", combat+2650, combat+2860, arf_blend_in_8],
   #[1.5, "anim_human", combat+1745, combat+1750, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#from reload_crossbow   
   #[2.2, "reloadpistol", 0, 15, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#Lucke189_animations   
   [2.4, "reload", 0, 39, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],		#Lucke189_animations
 ],

 ["ready_swingright_fist", 0,
   [ready_durn, "right_swing", 0, 15, blend_in_ready], 
   [ready_durn, "anim_human", 24000, 24000, blend_in_ready, 0, (0, 0, 0), 0.25],	#acm new
 ],
 ["release_swingright_fist", 0,
   [0.5, "right_swing", 15, 41, arf_blend_in_3], 
 ],
 ["parry_swingright_fist", 0,
   [attack_parry_duration, "anim_human", combat+4013, combat+4008, blend_in_parry], 
 ],

 ["ready_swingleft_fist", 0,
   [ready_durn, "anim_human", combat+4300, combat+4300, blend_in_ready], 
 ],
 ["release_swingleft_fist", 0,
   [0.5, "anim_human", combat+4300, combat+4335, arf_blend_in_0], 
 ],
 ["parry_swingleft_fist", 0,
   [attack_parry_duration, "anim_human", combat+4313, combat+4308, blend_in_parry], 
 ],

 ["ready_direct_fist", 0,
   [ready_durn, "direct_fist", 0, 16, blend_in_ready], 
   [ready_durn, "anim_human", 24600, 24600, blend_in_ready, 0, (0, 0, 0), 0.25], 	#acm new
 ],
 ["release_direct_fist", 0,
   [0.5, "direct_fist", 17, 36, arf_blend_in_0], 
 ],
 ["parry_direct_fist", 0,
   [attack_parry_duration, "anim_human", combat+4613, combat+4608, blend_in_parry], 
 ],
 ["ready_uppercut_fist", 0,
   [ready_durn, "uppercut", 0, 17, blend_in_ready], 
   [ready_durn, "anim_human", 24900, 24900, blend_in_ready, 0, (0, 0, 0), 0.25], 	#acm new
 ],
 ["release_uppercut_fist", 0,
   [0.5, "uppercut", 17, 34, arf_blend_in_0], 
 ],
 ["parry_uppercut_fist", 0,
   [attack_parry_duration, "anim_human", combat+4913, combat+4908, blend_in_parry], 
 ],

 ["defend_fist", acf_rotate_body,
   [defend_duration, "anim_human", combat+4950, combat+4960, blend_in_defense], 
 ],
 ["defend_fist_keep", acf_rotate_body,
   [2.0, "anim_human", combat+4950, combat+4960, arf_blend_in_2|arf_cyclic], 
 ],
 ["defend_fist_parry", acf_rotate_body,
   [0.3, "anim_human", combat+4962, combat+4970, arf_blend_in_0], 
 ],

 ["ready_slashright_twohanded", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [ready_durn, "anim_human", combat+5700, combat+5710, blend_in_ready], 
#   [0.6, "ani_twohanded", 0, 39, blend_in_ready, 0, (0,0,0), 24.0/39.0], 
 ],
 ["release_slashright_twohanded", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.62, "anim_human", combat+5710, combat+5740, blend_in_release], 
#   [1.3, "ani_twohanded", 39, 81, blend_in_release, 0, (0,0,0), (51.0- 39.0)/(81.0 - 39.0)], 
 ],
 ["parry_slashright_twohanded",acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+5725, combat+5720, blend_in_parry], 
 ],
 ["ready_slashleft_twohanded", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [ready_durn, "anim_human", combat+6400, combat+6410, blend_in_ready], 
 ],
 ["release_slashleft_twohanded", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.62, "anim_human", combat+6410, combat+6436, blend_in_release], 
 ],
 ["parry_slashleft_twohanded",acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+6425, combat+6420, blend_in_parry], 
 ],
 ["ready_thrust_twohanded", acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100),
   [ready_durn, "anim_human", combat+6000, combat+6010, blend_in_ready], 
 ],
 ["release_thrust_twohanded", acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.61, "anim_human", combat+6010, combat+6040, blend_in_release], 
 ],
 ["parry_thrust_twohanded", 0,
   [attack_parry_duration, "anim_human", combat+6015, combat+6016, blend_in_parry], 
 ],
 #["ready_overswing_twohanded", acf_overswing,
 ["ready_overswing_twohanded", 0,	#acm modified
   [ready_durn, "anim_human", combat+6200, combat+6210, blend_in_ready], 
   [ready_durn, "draw_greatsword", 20, 10, blend_in_ready], 	#acm new
   [1.0, "brfedit-01", 20024, 20004, blend_in_ready, 0, (0, 0, 0), 0.95], 	#acm new
 ],
 ["release_overswing_twohanded", acf_overswing,
   [0.63, "anim_human", combat+6210, combat+6241, blend_in_release], 
 ],
 ["parry_overswing_twohanded", 0,
   [attack_parry_duration, "anim_human", combat+6215, combat+6212, blend_in_parry], 
 ],
 #["ready_thrust_onehanded",   acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100)|acf_rotate_body|acf_enforce_rightside,
 ["ready_thrust_onehanded", acf_rotate_body,	#acm modified
   [ready_durn, "anim_human", combat+8500, combat+8510, blend_in_ready], 
   [ready_durn, "equip_sword", 27, 19, blend_in_ready], 
   [ready_durn, "anim_human", 29500, 29510, blend_in_ready], 
   [ready_durn, "brfedit-01", 29500, 29510, blend_in_ready], 
 ],
 ["release_thrust_onehanded", acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100)|acf_rotate_body|acf_enforce_rightside,
   [0.61, "anim_human", combat+8510, combat+8540, blend_in_release], 
   [0.61, "anim_human", 29510, 29540, blend_in_release], 	#acm new
   [0.45, "brfedit-01", 29512, 29530, blend_in_release], 	#acm new
 ],
 ["parry_thrust_onehanded", acf_rotate_body|acf_enforce_rightside,
   [attack_parry_duration, "anim_human", combat+8515, combat+8513, blend_in_parry], 
 ],
 ["ready_thrust_onehanded_lance",   acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100)|acf_rotate_body|acf_enforce_rightside,
   [ready_durn, "anim_human", combat+9500, combat+9510, blend_in_ready], 
   [ready_durn, "equip_arms", 271, 276, blend_in_ready], 	#acm new
   [ready_durn, "brfedit-01", 29500, 29510, blend_in_ready], 	#acm new
 ],
 ["release_thrust_onehanded_lance", acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100)|acf_rotate_body|acf_enforce_rightside,
   [0.61, "anim_human", combat+9510, combat+9540, blend_in_release], 
   [0.45, "brfedit-01", 29512, 29530, blend_in_release], 	#acm new
 ],
 ["parry_thrust_onehanded_lance", acf_rotate_body|acf_enforce_rightside,
   [attack_parry_duration, "anim_human", combat+9515, combat+9513, blend_in_parry], 
 ],
 #["ready_slashright_onehanded", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
 ["ready_slashright_onehanded", 0,	#acm modified
   [ready_durn, "anim_human", combat+8800, combat+8810, blend_in_ready], 
   [ready_durn, "man_cheer", 5, 15, blend_in_ready], 	#acm new
   [ready_durn, "equip_sword", 27, 19, blend_in_ready], 	#acm new
   [ready_durn, "draw_greatsword", 25, 15, blend_in_ready], 	#acm new
   [0.3, "throw_knife", 10, 30, blend_in_ready], 	#acm new
 ],
 ["release_slashright_onehanded", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+8810, combat+8840, blend_in_release], 
 ],
 ["parry_slashright_onehanded", 0,
   [attack_parry_duration, "anim_human", combat+8820, combat+8815, blend_in_parry], 
 ],
 #["ready_slashleft_onehanded", acf_left_cut|acf_parallels_for_look_slope|acf_anim_length(100),
 ["ready_slashleft_onehanded", 0,	#acm modified
   [ready_durn, "anim_human", combat+9100, combat+9110, blend_in_ready], 
   [ready_durn, "throw_stone", 30, 40, blend_in_ready], 	#acm new
 ],
 ["release_slashleft_onehanded", acf_left_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+9110, combat+9140, blend_in_release], 
 ],
 ["parry_slashleft_onehanded", 0,
   [attack_parry_duration, "anim_human", combat+9120, combat+9115, blend_in_parry], 
 ],
 #["ready_overswing_onehanded", acf_overswing|acf_rotate_body|acf_enforce_rightside,
 ["ready_overswing_onehanded", acf_rotate_body,	#acm modified
   [ready_durn, "anim_human", combat+9300, combat+9305, blend_in_ready], 
   [ready_durn, "anim_human", 22060, 22070, blend_in_ready], 	#acm new
   [0.3, "throw_javelin", 0, 30, blend_in_ready], 	#acm new 
   [ready_durn, "brfedit-01", 29300, 29305, blend_in_ready],  	#acm new
   [0.8, "brfedit-01", 20024, 20004, blend_in_ready, 0, (0, 0, 0), 0.75],  	#acm new
#   [0.4, "ani_onehanded", 0, 44, blend_in_ready, 0, (0,0,0), 22.0/44.0], 
 ],
 ["release_overswing_onehanded", acf_overswing|acf_rotate_body|acf_enforce_rightside,
   [0.6, "anim_human", combat+9305, combat+9342, blend_in_release], 
   [0.6, "brfedit-01", 29305, 29342, blend_in_release], 	#acm new
#   [1.0, "ani_onehanded", 44, 85, blend_in_release, 0, (0,0,0), (53.0 - 44.0)/(85.0 - 44.0)], 
 ],
 ["parry_overswing_onehanded", acf_rotate_body|acf_enforce_rightside,
   [attack_parry_duration, "anim_human", combat+9315, combat+9310, blend_in_parry], 
 ],
 #["ready_slash_horseback_right", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
 ["ready_slash_horseback_right", 0,	#acm modified
   [ready_durn, "anim_human", combat+10100, combat+10110, blend_in_ready], 
   [ready_durn, "equip_sword", 27, 19, blend_in_ready], 	#acm new
 ],
 ["release_slash_horseback_right", acf_right_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+10110, combat+10140, blend_in_release], 
 ],
 ["parry_slash_horseback_right",acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+10120, combat+10115, blend_in_parry], 
 ],
 #["ready_slash_horseback_left", acf_left_cut|acf_parallels_for_look_slope|acf_anim_length(100),
 ["ready_slash_horseback_left", 0,	#acm modified
   [ready_durn, "anim_human", combat+10400, combat+10410, blend_in_ready], 
   [ready_durn, "throw_stone", 30, 40, blend_in_ready], 	#acm new
 ],
 ["release_slash_horseback_left", acf_left_cut|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+10410, combat+10440, blend_in_release], 
 ],
 ["parry_slash_horseback_left",acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+10420, combat+10415, blend_in_parry], 
 ],
 ["ready_overswing_staff", acf_overswing,
   [ready_durn, "anim_human", combat+7100, combat+7110, blend_in_ready], 
 ],
 ["release_overswing_staff", acf_overswing,
   [0.6, "anim_human", combat+7110, combat+7140, arf_blend_in_0], 
 ],
 ["parry_overswing_staff", 0,
   [attack_parry_duration, "anim_human", combat+7017, combat+7014, arf_blend_in_2], 
 ],
 ["ready_thrust_staff", acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100),
   [ready_durn, "anim_human", combat+7300, combat+7310, blend_in_ready],
#   [ready_durn, "thrust_staff", 70, 93, blend_in_ready],
 ],
 ["release_thrust_staff", acf_thrust|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+7310, combat+7340, arf_blend_in_2], 
#   [0.6, "thrust_staff", 93, 125, arf_blend_in_2], 
 ],
 ["parry_thrust_staff", acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+7316, combat+7313, arf_blend_in_2], 
#   [attack_parry_duration, "thrust_staff", 102, 97, arf_blend_in_2], 
 ],
 ["ready_slashleft_staff",acf_parallels_for_look_slope|acf_anim_length(100),
   [ready_durn, "anim_human", combat+7600, combat+7610, blend_in_ready], 
 ],
 ["release_slashleft_staff",acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+7610, combat+7640, arf_blend_in_0], 
 ],
 ["parry_slashleft_staff",acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+7615, combat+7613, arf_blend_in_2], 
 ],
 ["ready_slashright_staff",acf_parallels_for_look_slope|acf_anim_length(100),
   [ready_durn, "anim_human", combat+7900, combat+7910, blend_in_ready], 
 ],
 ["release_slashright_staff",acf_parallels_for_look_slope|acf_anim_length(100),
   [0.6, "anim_human", combat+7910, combat+7940, arf_blend_in_0], 
 ],
 ["parry_slashright_staff",acf_parallels_for_look_slope|acf_anim_length(100),
   [attack_parry_duration, "anim_human", combat+7915, combat+7913, arf_blend_in_2], 
 ],

 #["defend_shield", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
 ["defend_shield", acf_rotate_body,	#acm modified
   [defend_duration, "anim_human", defend+105, defend+120, blend_in_defense], 	#native
   [defend_duration, "anim_human", defend+105, defend+120, blend_in_defense], 	#native (gave it twice so it is more common)
   [defend_duration, "draw_greatsword", 24, 29, blend_in_defense], 	#acm new
   #[defend_duration, "sw_lightsaber_protect_1", 0, 99, blend_in_defense], 	#Swyter animation
   #[defend_duration, "sw_lightsaber_protect_1", 0, 9, blend_in_defense], 	#Swyter animation
   #[defend_duration, "anim_reload_b", 0, 0, blend_in_defense], 	#1866 animations
   #[defend_duration, "brfedit-01", 290, 290, blend_in_defense], 	#acm new	(looks good with 2 lightsabers, bad with other shields)
 ],
 #["defend_shield_keep", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
 ["defend_shield_keep", acf_rotate_body,	#acm modified
   #[2.0, "anim_human", defend+120, defend+120, arf_blend_in_1|arf_cyclic], 
   [6.0, "anim_human", defend+120, defend+120, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#acm modified
   [6.0, "anim_human", defend+120, defend+120, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#acm modified
   [6.0, "draw_greatsword", 29, 29, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#acm new
   #[6.0, "sw_lightsaber_protect_1", 99, 99, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#Swyter animation
   #[6.0, "sw_lightsaber_protect_1", 9, 9, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#Swyter animation
   #[6.0, "anim_reload_b", 0, 0, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#1866 animation
   #[6.0, "brfedit-01", 290, 290, arf_blend_in_1|arf_cyclic, 0, (0, 0, 0), 5.0], 	#acm new	(looks good with 2 lightsabers, bad with other shields)
 ],
 ["defend_shield_parry", acf_rotate_body|acf_parallels_for_look_slope|acf_anim_length(100),
   [0.5, "anim_human", defend+121, defend+130, arf_blend_in_1], 
   [0.5, "strikes", 706, 724, arf_blend_in_1], 	#acm new
   [0.6, "strikes", 487, 512, arf_blend_in_1], 	#acm new 
   [0.6, "strikes", 881, 905, arf_blend_in_1],  	#acm new
 ],
 ["defend_forward_greatsword", acf_rotate_body,
#   [defend_duration, "anim_human", defend+310, defend+320, blend_in_defense], 
   [defend_duration, "defend_twohanded", 0, 20, blend_in_defense], 
   [defend_duration, "anim_human", 35310, 35320, blend_in_defense], 	#acm new
 ],
 ["defend_forward_greatsword_keep", acf_rotate_body,
#   [2.0, "anim_human", defend+320, defend+320, arf_blend_in_3|arf_cyclic], 
   #[4.0, "defend_twohanded", 170, 170, arf_blend_in_3|arf_cyclic], 
   [4.0, "defend_twohanded", 170, 170, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 3.8], 	#acm modified
   [2.0, "anim_human", defend+320, defend+320, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.8], 	#acm new
 ],
 ["defend_forward_greatsword_parry", acf_rotate_body,
#   [0.3, "anim_human", defend+320, defend+330, arf_blend_in_1], 
   [0.6, "defend_twohanded", 350, 367, arf_blend_in_1], 
   [0.3, "anim_human", defend+320, defend+330, arf_blend_in_1], 	#acm new
 ],
 ["defend_up_twohanded", acf_rotate_body,
   [defend_duration, "anim_human", defend+403, defend+410, blend_in_defense], 
 ],
 ["defend_up_twohanded_keep", acf_rotate_body,
   [2.0, "anim_human", defend+410, defend+410, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_up_twohanded_parry", acf_rotate_body,
   [0.3, "anim_human", defend+411, defend+418, arf_blend_in_1], 
 ],
 ["defend_right_twohanded", acf_rotate_body,
   [defend_duration, "anim_human", defend+510, defend+520, blend_in_defense], 
   [1.0, "brfedit-01", 20003, 20024, blend_in_defense, 0, (0, 0, 0), 0.95], 	#acm new
 ],
 ["defend_right_twohanded_keep", acf_rotate_body,
   #[2.0, "anim_human", defend+520, defend+520, arf_blend_in_3|arf_cyclic], 
   [2.0, "anim_human", defend+520, defend+520, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.8], 	#acm modified
   [2.0, "anim_human", 35320, 35320, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.8], 	#acm new
 ],
 ["defend_right_twohanded_parry", acf_rotate_body,
   [0.3, "anim_human", defend+521, defend+528, arf_blend_in_1], 
 ],
 ["defend_left_twohanded", acf_rotate_body,
   [defend_duration, "anim_human", defend+610, defend+620, blend_in_defense], 
 ],
 ["defend_left_twohanded_keep", acf_rotate_body,
   #[2.0, "anim_human", defend+620, defend+620, arf_blend_in_3|arf_cyclic], 
   [2.0, "anim_human", defend+620, defend+620, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.8], 	#acm modified
   [2.0, "anim_human", 35320, 35320, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.8], 	#acm new
 ],
 ["defend_left_twohanded_parry", acf_rotate_body,
   [0.3, "anim_human", defend+620, defend+630, arf_blend_in_1], 
 ],
 ["defend_forward_onehanded", acf_rotate_body,
#   [defend_duration, "anim_human", defend+1010, defend+1020, blend_in_defense], 
   [defend_duration, "defend_onehanded", 0, 15, blend_in_defense], 
   [defend_duration, "anim_human", defend+1010, defend+1020, blend_in_defense], 	#acm new
 ],
 ["defend_forward_onehanded_keep", acf_rotate_body,
#   [2.0, "anim_human", defend+1020, defend+1020, arf_blend_in_3|arf_cyclic], 
   #[5.0, "defend_onehanded", 15, 70, arf_blend_in_3|arf_cyclic], 
   [5.0, "defend_onehanded", 15, 70, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 4.5], 	#acm modified
   [2.0, "anim_human", defend+1020, defend+1020, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.5], 	#acm new
 ],
 ["defend_forward_onehanded_parry", acf_rotate_body,
#   [0.3, "anim_human", defend+1021, defend+1030, arf_blend_in_1], 
   [0.62, "defend_onehanded", 75, 85, arf_blend_in_1], 
   [0.3, "anim_human", defend+1021, defend+1030, arf_blend_in_1], 
 ],
 ["defend_up_onehanded", acf_rotate_body,
   [defend_duration, "anim_human", defend+1110, defend+1120, blend_in_defense], 
 ],
 ["defend_up_onehanded_keep", acf_rotate_body,
   [2.0, "anim_human", defend+1120, defend+1120, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_up_onehanded_parry", acf_rotate_body,
   [0.3, "anim_human", defend+1121, defend+1130, arf_blend_in_1], 
 ],
 ["defend_right_onehanded", acf_rotate_body,
   [defend_duration, "anim_human", defend+1210, defend+1220, blend_in_defense], 
   [1.0, "brfedit-01", 20003, 20024, blend_in_defense, 0, (0, 0, 0), 0.95], 	#acm new
 ],
 ["defend_right_onehanded_keep", acf_rotate_body,
   [2.0, "anim_human", defend+1220, defend+1220, arf_blend_in_5|arf_cyclic], 
 ],
 ["defend_right_onehanded_parry", acf_rotate_body,
   [0.3, "anim_human", defend+1221, defend+1230, arf_blend_in_1], 
 ],
 ["defend_left_onehanded", acf_rotate_body,
   [defend_duration, "anim_human", defend+1310, defend+1320, blend_in_defense], 
 ],
 ["defend_left_onehanded_keep", acf_rotate_body,
   [2.0, "anim_human", defend+1320, defend+1320, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_left_onehanded_parry", acf_rotate_body,
   [0.3, "anim_human", defend+1321, defend+1330, arf_blend_in_1], 
 ],
 ["defend_forward_staff", acf_rotate_body,
#   [pole_defend_duration, "anim_human", defend+2010, defend+2020, blend_in_defense], 
   [pole_defend_duration, "defend_staff", 0, 5, blend_in_defense], 
   [pole_defend_duration, "anim_human", 37010, 37020, blend_in_defense], 	#acm new
 ],
 ["defend_forward_staff_keep", acf_rotate_body,
#   [2.0, "anim_human", defend+2020, defend+2020, arf_blend_in_3|arf_cyclic], 
#   [4.0, "defend_staff", 0, 45, arf_blend_in_3|arf_cyclic], 
   #[4.0, "defend_staff", 5, 5, arf_blend_in_3|arf_cyclic], 
   [4.0, "defend_staff", 5, 5, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 3.8], 	#acm modified
   [2.0, "anim_human", 37020, 37020, arf_blend_in_3|arf_cyclic, 0, (0, 0, 0), 1.8], 	#acm new
 ],
 ["defend_forward_staff_parry", acf_rotate_body,
#   [0.3, "anim_human", defend+2021, defend+2030, arf_blend_in_1], 
   [0.7, "defend_staff", 56, 70, arf_blend_in_1], 
   [0.3, "anim_human", 37021, 37030, arf_blend_in_1], 	#acm new
 ],
 ["defend_up_staff", acf_rotate_body,
   [pole_defend_duration, "anim_human", defend+2110, defend+2120, blend_in_defense], 
 ],
 ["defend_up_staff_keep", acf_rotate_body,
   [2.0, "anim_human", defend+2120, defend+2120, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_up_staff_parry", acf_rotate_body,
   [0.3, "anim_human", defend+2121, defend+2130, arf_blend_in_1], 
 ],
 ["defend_right_staff", acf_rotate_body,
   [pole_defend_duration, "anim_human", defend+2210, defend+2220, blend_in_defense], 
 ],
 ["defend_right_staff_keep", acf_rotate_body,
   [2.0, "anim_human", defend+2220, defend+2220, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_right_staff_parry", acf_rotate_body,
   [0.3, "anim_human", defend+2221, defend+2230, arf_blend_in_1], 
 ],
 ["defend_left_staff", acf_rotate_body,
   [pole_defend_duration, "anim_human", defend+2310, defend+2320, blend_in_defense], 
 ],
 ["defend_left_staff_keep", acf_rotate_body,
   [2.0, "anim_human", defend+2320, defend+2320, arf_blend_in_3|arf_cyclic], 
 ],
 ["defend_left_staff_parry", acf_rotate_body,
   [0.3, "anim_human", defend+2321, defend+2330, arf_blend_in_1], 
 ],

 
 ["strike_head_left", 0,
   [0.5, "strikes", 55, 71, arf_blend_in_3], 
 ],
 ["strike_head_right", 0,
   [0.5, "strikes", 4, 19, arf_blend_in_3], 
 ],
 ["strike_head_front", 0,
   [0.5, "strikes", 180, 198, arf_blend_in_3], 
 ],
 ["strike_head_back", 0,
   [0.6, "strikes_back", 4, 25, arf_blend_in_3], 
 ],
 ["strike_chest_left", 0,
   [0.5, "strikes", 706, 724, arf_blend_in_3], 
 ],
 ["strike_chest_right", 0,
   [0.6, "strikes", 487, 512, arf_blend_in_3], 
 ],
 ["strike_chest_front", 0,
   [0.6, "strikes", 881, 905, arf_blend_in_3], 
 ],
 ["strike_chest_back", 0,
   [0.5, "strikes_back", 401, 418, arf_blend_in_3], 
 ],
 ["strike_abdomen_left", 0,
   [0.58, "strikes", 1425, 1444, arf_blend_in_3], 
 ],
 ["strike_abdomen_right", 0,
   [0.6, "strikes", 1168, 1188, arf_blend_in_3], 
 ],
 ["strike_abdomen_front", 0,
   [0.6, "strikes", 1618, 1640, arf_blend_in_3], 
 ],
 ["strike_abdomen_back", 0,
   [0.53, "strikes_back", 886, 904, arf_blend_in_3], 
 ],
 ["strike_legs_left", 0,
   [0.55, "strikes", 2284, 2305, arf_blend_in_3], 
 ],
 ["strike_legs_right", 0,
   [0.56, "strikes", 1999, 2020, arf_blend_in_3], 
 ],
 ["strike_legs_front", 0,
   [0.56, "strikes", 2655, 2676, arf_blend_in_3], 
 ],
 ["strike_legs_back", 0,
   [0.5, "strikes_back", 1120, 1137, arf_blend_in_3], 
 ],

 ["strike2_head_left", acf_enforce_all,
   [0.5, "strikes", 55, 71, arf_blend_in_3], 
 ],
 ["strike2_head_right",acf_enforce_all,
   [0.5, "strikes", 4, 19, arf_blend_in_3], 
 ],
 ["strike2_head_front",acf_enforce_all,
   [0.5, "strikes", 180, 198, arf_blend_in_3], 
 ],
 ["strike2_head_back", acf_enforce_all,
#   [0.6, "strikes_back", 4, 25, arf_blend_in_3], 
   [0.55, "strikes_back", 4, 25, arf_blend_in_3], 
 ],
 ["strike2_chest_left", acf_enforce_all,
   [0.5, "strikes", 706, 724, arf_blend_in_3], 
 ],
 ["strike2_chest_right", acf_enforce_all,
#   [0.6, "strikes", 487, 512, arf_blend_in_3], 
   [0.55, "strikes", 487, 512, arf_blend_in_3], 
 ],
 ["strike2_chest_front", acf_enforce_all,
#   [0.6, "strikes", 881, 905, arf_blend_in_3], 
   [0.55, "strikes", 881, 905, arf_blend_in_3], 
 ],
 ["strike2_chest_back",acf_enforce_all,
   [0.5, "strikes_back", 401, 418, arf_blend_in_3], 
 ],
 ["strike2_abdomen_left", acf_enforce_all,
   [0.55, "strikes", 1425, 1444, arf_blend_in_3], 
 ],
 ["strike2_abdomen_right", acf_enforce_all,
#   [0.6, "strikes", 1168, 1188, arf_blend_in_3], 
   [0.55, "strikes", 1168, 1188, arf_blend_in_3], 
 ],
 ["strike2_abdomen_front", acf_enforce_all,
#   [0.6, "strikes", 1618, 1640, arf_blend_in_3], 
   [0.55, "strikes", 1618, 1640, arf_blend_in_3], 
 ],
 ["strike2_abdomen_back", acf_enforce_all,
   [0.53, "strikes_back", 886, 904, arf_blend_in_3], 
 ],
 ["strike2_legs_left", acf_enforce_all,
   [0.55, "strikes", 2284, 2305, arf_blend_in_3], 
 ],
 ["strike2_legs_right", acf_enforce_all,
   [0.56, "strikes", 1999, 2020, arf_blend_in_3], 
 ],
 ["strike2_legs_front", acf_enforce_all,
   [0.56, "strikes", 2655, 2676, arf_blend_in_3], 
 ],
 ["strike2_legs_back", acf_enforce_all,
   [0.5, "strikes_back", 1120, 1137, arf_blend_in_3], 
 ],

 ["strike3_head_left", acf_enforce_all,
   [0.9 * 1.1, "strikes3_head", 107, 146, arf_blend_in_3], 
 ],
 ["strike3_head_right",acf_enforce_all,
   [0.9 * 1.0, "strikes3_head", 208, 251, arf_blend_in_3], 
 ],
 ["strike3_head_front",acf_enforce_all,
   [0.9 * 1.0, "strikes3_head", 14, 48, arf_blend_in_3], 
 ],
 ["strike3_head_back", acf_enforce_all,
   [0.9 * 1.0, "strikes3_head", 309, 346, arf_blend_in_3],
 ],
 ["strike3_chest_left", acf_enforce_all,
   [0.9 * 1.0, "strikes3_chest", 61, 97, arf_blend_in_3],
 ],
 ["strike3_chest_right", acf_enforce_all,
   [0.9, "strikes3_chest", 108, 145, arf_blend_in_3], 
 ],
 ["strike3_chest_front", acf_enforce_all,
   [0.8, "strikes3_chest", 3, 27, arf_blend_in_3], 
 ],
## ["strike3_chest_back",acf_enforce_all,
##   [1.3, "strikes3_chest", 264, 310, arf_blend_in_3], 
## ],
 ["strike3_abdomen_left", acf_enforce_all,
   [0.9 * 1.0, "strikes3_abdomen", 105, 150, arf_blend_in_3, 0, (0, 0.0, 0.0)], 
 ],
 ["strike3_abdomen_right", acf_enforce_all,
   [0.9, "strikes3_abdomen", 63, 98, arf_blend_in_3, 0, (0, 0.0, 0.0)], 
 ],
 ["strike3_abdomen_front", acf_enforce_all,
   [0.9 * 1.0, "strikes3_abdomen", 4, 43, arf_blend_in_3,  0, (0, 0.0, 0.0)],
 ],
 ["strike3_abdomen_back", acf_enforce_all,
   [0.9 * 1.2, "strikes3_abdomen_back", 0, 53, arf_blend_in_3], 
 ],
## ["strike3_legs_left", acf_enforce_all,
##   [0.6, "strikes", 2284, 2305, arf_blend_in_3], 
## ],
## ["strike3_legs_right", acf_enforce_all,
##   [0.7, "strikes", 1999, 2020, arf_blend_in_3], 
## ],
## ["strike3_legs_front", acf_enforce_all,
##   [0.7, "strikes", 2655, 2676, arf_blend_in_3], 
## ],
## ["strike3_legs_back", acf_enforce_all,
##   [0.8, "strikes_back", 1120, 1144, arf_blend_in_3], 
## ],

## ["strike_head_front_left", 0,
##   [0.55, "anim_human", blow+0, blow+10, arf_blend_in_3], 
## ],
 ["strike_head_front_left_reloc", acf_enforce_all,
   [0.6,  "strike_frontal", 0, 37, arf_blend_in_3], 
#   [0.6,  "anim_human", blow+5200, blow+5220, arf_blend_in_3], 
 ],
 ["fall_face_hold", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
   [2.2, "death_face", 8, 60, arf_blend_in_16|arf_make_custom_sound, pack2f(0.5, 0.0), (0,0,0), 0.6],
 ],
 ["fall_chest_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
   #[1.0, "death_chest", 4, 37, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],
   [1.0, "swy_sw_death_chest", 0, 50, arf_blend_in_16|arf_make_custom_sound, pack2f(0.9, 0.0), (0,0,0), 0.5],
 ],
 ["fall_abdomen_hold_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
   #[2.7, "death_abdomen", 5, 96, arf_blend_in_16|arf_make_custom_sound, pack2f(0.4, 0.0), (0,0,0), 0.5],
   [1.7, "swy_sw_death_side", 0, 50, arf_blend_in_16|arf_make_custom_sound, pack2f(0.4, 0.0), (0,0,0), 0.5],

 ],
 ["fall_head_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
   [1.2, "anim_human", blow+100, blow+138, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.8], 
   [1.5, "anim_human", 40100, 40138, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 1.0],	#acm new
   [1.9, "anim_human", 45453, 45430, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 1.8],	#acm new
   [1.5, "anim_human", 45401, 45430, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 1.4],	#acm new
   [1.0, "anim_human", 45400, 45421, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.9],	#acm new
   [1.8, "death", 16, 99, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 1.7],	#acm new
   [0.8, "anim_human", 21700, 21713, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.05],	#acm new
   [1.5, "anim_human", 24335, 24300, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 1.0],	#acm new
   [2.0, "anim_human", 29515, 29535, arf_blend_in_16|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 1.1],	#acm new
 ],
 ["fall_right_front", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
   [2.0, "death2", 0, 53, arf_blend_in_16|arf_make_custom_sound, pack2f(0.65, 0.0), (0,0,0), 1.0], 
 ],
 ["fall_body_back", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
   [2.7, "death", 0, 83, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.5], 
   [1.8, "death", 16, 99, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.7], 	#acm new
   [1.7, "anim_human", 45400, 45438, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.6], 	#acm new
   [1.7, "anim_human", 40100, 40138, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.5], 	#acm new
   [2.7, "death", 16, 99, arf_blend_in_16|arf_make_custom_sound, pack2f(0.47, 0.82), (0,0,0), 1.7], 	#acm new
 ],
 #["fall_rider_head_front", acf_enforce_all|acf_lock_camera|acf_lock_camera,
 ["fall_rider_head_front", acf_enforce_all,	#acm modified
   #[2.2, "anim_human", blow+200, blow+275, arf_blend_in_3|arf_make_custom_sound, pack2f(0.8, 0.0), (0,0,0), 0.3], 
   [2.2, "anim_human", blow+200, blow+275, arf_blend_in_8, 0, (0,0,0), 0.3], 	#acm modified
   [1.2, "anim_human", 41500, 41552, arf_blend_in_8, 0, (1.1,-0.9,0), 0.3], 	#acm new
   [1.4, "anim_human_02", 350, 362, arf_blend_in_8, 0, (0.8,-1.8,0), 0.25], 	#acm new
 ],
 ["rider_fall_in_place", acf_enforce_lowerbody,
   [3.8, "anim_human", blow + 1000, blow + 1075, arf_blend_in_16|arf_make_custom_sound, pack2f(0.0, 0.0), (0,0,0), 0.5], 
 ],
 #["rider_fall_right", acf_enforce_all|acf_displace_position,
 ["rider_fall_right", acf_enforce_all,	#acm modified
   #[2.5, "anim_human_02", 350, 382,  arf_blend_in_8, 0, (0.8,-1.8,0), 0.5],
   [1.4, "anim_human_02", 350, 362,  arf_blend_in_8, 0, (0.8,-1.8,0), 0.25],	#acm modified
   [1.2, "anim_human", 41500, 41552,  arf_blend_in_8, 0, (1.1,-0.9,0), 0.3],	#acm new
 ],
 ["rider_fall_roll", acf_enforce_all|acf_displace_position,
   [2.5, "anim_human", blow+ 2000, blow+2084,  arf_blend_in_8, 0, (-0.4,0.2,0), 1.0],
 ],
 ["strike_chest_front_stop", acf_enforce_all,
   [0.4, "anim_human", blow+5000, blow+5010, arf_blend_in_3], 
 ],
 #["strike_fall_back_rise", acf_enforce_lowerbody|acf_align_with_ground, 
 ["strike_fall_back_rise", acf_enforce_all|acf_displace_position, 	#acm modified
   [1.7, "anim_human", blow+5400, blow+5453, arf_blend_in_2|arf_make_custom_sound, pack2f(0.4, 0.0), (0,0,0), 0.5],
 ],
 ["strike_fall_back_rise_upper", acf_align_with_ground,
   [1.38, "anim_human", blow+5400, blow+5442, arf_blend_in_2], 
 ],

 ["cheer", 0,
##   [2.5, "anim_human", 70000, 70045, arf_blend_in_5], 
##   [3.0, "anim_human", 70100, 70150, arf_blend_in_5],
   [6.0, "man_cheer", 0, 185, arf_blend_in_5],
   [3.0, "man_cheer", 200, 289, arf_blend_in_5],
   [4.5, "man_cheer", 300, 437, arf_blend_in_5],
   [5.5, "man_cheer", 450, 617, arf_blend_in_5],
   [2.5, "anim_human", 70000, 70045, arf_blend_in_5],	#acm new
   [3.0, "anim_human", 70100, 70150, arf_blend_in_5],	#acm new
 ],

 ["cheer_stand", arf_cyclic,
   [31.5, "man_cheer", 650, 1597, arf_blend_in_5],   
 ],

 ["stand_townguard", 0,
   [79.0, "stand_guardsman", 0, 2397, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["stand_lady", 0,
   [29.0, "lady_stand", 0, 863, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 ["stand_lord", 0,
   [10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],

 ["dance", 0,
   [20.0, "anim_human", 0, 387, arf_blend_in_5], 
#   [10.0, "anim_human_temp", 0, 10, arf_blend_in_5], 
 ],
 ["pose_1", 0,
   [3.0, "poses", 0, 0, arf_cyclic],
 ],
 ["pose_2", 0,
   [3.0, "poses", 2, 2, arf_cyclic],
 ],
 ["pose_3", 0,
   [3.0, "poses", 4, 4, arf_cyclic],
 ],
 ["pose_4", 0,
   [3.0, "poses", 6, 6, arf_cyclic],
 ],
 ["pose_5", 0,
   [3.0, "poses", 8, 8, arf_cyclic],
 ],


 
 ### Unused human animations start from here.
 ["unused_human_anim_1", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_2", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_3", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_4", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_5", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_6", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_7", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_8", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_9", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_10", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_11", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_12", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_13", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_14", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_15", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_16", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_17", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_18", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_19", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_20", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_21", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_22", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_23", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_24", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_25", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_26", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_27", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_28", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_29", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_30", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_31", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_32", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_33", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_34", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_35", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_36", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_37", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_38", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_39", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_40", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_41", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_42", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_43", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_44", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_45", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_46", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_47", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_48", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_49", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_50", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_51", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_52", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_53", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_54", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_55", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_56", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_57", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_58", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_59", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_60", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_61", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_62", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_63", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_64", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_65", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_66", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_67", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_68", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_69", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_70", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_71", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_72", 0, [1.0, "anim_human", 0, 1, 0]],
 ["unused_human_anim_73", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_74", 0, [1.0, "anim_human", 0, 1, 0]],			#SWY - Commented out for b2's walk
# ["unused_human_anim_75", 0, [1.0, "anim_human", 0, 1, 0]],			#SWY - Commented out for b2's stand
# ["unused_human_anim_76", 0, [1.0, "anim_human", 0, 1, 0]],        #SWY - Commented out for vader's stand
# ["unused_human_anim_77", 0, [1.0, "anim_human", 0, 1, 0]],		#had to comment out for slave_dance
# ["unused_human_anim_78", 0, [1.0, "anim_human", 0, 1, 0]],		#hand to comment out for crouch_stop
# ["unused_human_anim_79", 0, [1.0, "anim_human", 0, 1, 0]],		#had to comment out for crouch
# ["unused_human_anim_80", 0, [1.0, "anim_human", 0, 1, 0]],		#had to comment out for stand_crouch
# ["unused_human_anim_81", 0, [1.0, "anim_human", 0, 1, 0]],		#had to comment out for walk_forward_crouch
# ["unused_human_anim_82", 0, [1.0, "anim_human", 0, 1, 0]],		#had to comment out for droid_walk_forward
# ["unused_human_anim_83", 0, [1.0, "anim_human", 0, 1, 0]],		#had to comment out for dmod_kill_agent animation
#--------------------------------------------------------------------------------------------------------------------


 ["slave_dance", 0,
   #[10.0, "dancer_stand", 0, 177, arf_blend_in_5], 
   [10.0, "dancer_stand", 0, 177, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.20],
 ],

 ["droid_walk_forward", acf_enforce_lowerbody,		#from walk_forward
   #[1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "man_walk", 0, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.0,0.0), (0, 0, 0), 0.0],
 ],

 #SW - used to move the agent far underground when they are 'killed'
 ["dmod_kill_agent", acf_displace_position,
   [0.1, "anim_human", 386, 387, 0, 0, (0, 0, 20.0), 0.0],	#(right,  forward,  down), delay
 ],

#SW - had to comment out 1 animation for the jetpack jump
# ["unused_human_anim_89", 0, [1.0, "anim_human", 0, 1, 0]],

 # Super-Mario Stype Super Jump - http://forums.taleworlds.net/index.php/topic,65520.msg1703891.html
 #["fall_body_back", acf_enforce_all|acf_align_with_ground|acf_lock_camera,
 #["jetpack", acf_enforce_all|acf_lock_camera|acf_align_with_ground|acf_displace_position,		#working
 ["jetpack", acf_enforce_all|acf_align_with_ground|acf_displace_position,		#working
 #["jetpack", acf_displace_position,		#testing
 #["jetpack", acf_enforce_lowerbody|acf_displace_position,
	[1.5, "jump", 22, 48, arf_blend_in_1, 0, (0, 15, -5), 0],	#(right,  forward,  down), delay
	#[1.5, "jump", 22, 48, 0, 0, (0, 15, -5), 0.0],	#(right,  forward,  down), delay
	#[2.2, "death_face", 8, 60, arf_blend_in_16|arf_make_custom_sound, pack2f(0.5, 0.0), (0,0,0), 0.6],
 ],

#-----------------------------------------------------------------------------------------------

#SW - had to comment out 6 animations for force powers
# ["unused_human_anim_90", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_91", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_92", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_93", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_94", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_85", 0, [1.0, "anim_human", 0, 1, 0]],		

#SW - force powers - animations similar to shild bash but longer
 # strike_fall_back_rise_after_bashed
 ["force_knocked", acf_enforce_all|acf_align_with_ground,
   [2.5, "anim_human", blow+5400, blow+5453, arf_blend_in_2],
 ],
# strike_chest_front_stop
 ["force_stun", acf_enforce_all,
   [2.0, "anim_human", blow+5000, blow+5010, arf_blend_in_3],
 ],
# strike_chest_front_stop
 ["force_mini_stun", acf_enforce_all,
   [1.2, "anim_human", blow+5000, blow+5010, arf_blend_in_3],
 ],
 # anim jump end
 ["force_crouch", acf_enforce_all|acf_enforce_lowerbody,
   [1.5, "anim_human", 280, 290, arf_blend_in_3],
 ], 
# strike_head_front_left
 ["force_unsuccessful", acf_enforce_all,
   [1.5, "anim_human", blow+0, blow+10, arf_blend_in_3],
 ],
 # strike_fall_back_rise_after_bashed
 ["force_push", acf_enforce_all|acf_displace_position,
   #[2.5, "anim_human", blow+5400, blow+5453, 0, 0, (0, -2, 0), 0.0],	#(right,  forward,  down), delay],
   #[0.2, "anim_human", blow+5000, blow+5010, arf_blend_in_3, 0, (0, -7, 0), 0.0],	#(right,  forward,  down), delay],
   [0.3, "death_chest", 0, 37, arf_blend_in_3, 0, (0, -7, 0), 0.0],	#(right,  forward,  down), delay],
   [0.4, "death2", 0, 53, 0, arf_blend_in_3, (0, -7, 0), 0.0],	#(right,  forward,  down), delay],
   [0.4, "death_face", 0, 54, 0, arf_blend_in_3, (0, -7, 0), 0.0],	#(right,  forward,  down), delay],
   [0.6, "death_abdomen", 0, 96, arf_blend_in_3, 0, (0, -7, 0), 0.0],	#(right,  forward,  down), delay],
   
 ], 

 #Swyter animations
#SW - had to comment out these for Swyter animations
# ["unused_human_anim_88", 0, [1.0, "anim_human", 0, 1, 0]],
 ["force_choke", acf_enforce_all,
   [3.5, "sw_force_kill_1", 0, 50, arf_blend_in_3],
 ],

#SW - had to comment out these for Georj animations (drinking & sitting)
# ["unused_human_anim_86", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_87", 0, [1.0, "anim_human", 0, 1, 0]], 
# ["unused_human_anim_84", 0, [1.0, "anim_human", 0, 1, 0]],
 #["drinking", acf_enforce_all|acf_displace_position,			#working
 #[2, "sw_chair_drinking_beta_1", 0, 59, 0, 0, (0, 0, 2), 0.0],	#(right,  forward,  down), delay
   #["drinking", acf_enforce_all,			#working
   ["drinking", 0,			#working
   #[2, "anim-drinking", 0, 120, 0],		#by geroj
   [3.0, "sw_chair_drinking_beta_1_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],	#by Swyter
   [4.0, "sw_chair_drinking_beta_1_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],	#by Swyter
   [2.0, "sw_chair_moving_head_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],	#by Swyter
   [4.0, "sw_chair_moving_head_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],	#by Swyter
   [2.0, "sw_chair_stand1_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],		#by Swyter
   [2.0, "sw_chair_stand2_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],		#by Swyter   
 ],
 #["sitting", acf_enforce_all,
 ["sitting", 0,
 #["sitting", acf_enforce_all|acf_displace_position,
   #[2, "anim-drinking", 0, 1, 0],		#by geroj
   #[2, "sw_chair_moving_head_fixed", 0, 59, 0, pack2f(0.0, 0.0), (0, 0, 2), 0.0],	#(right,  forward,  down), delay
   #[2, "sw_chair_moving_head_fixed", 0, 59, 0, 0],	#(right,  forward,  down), delay
   #[2, "sw_chair_moving_head_fixed", 0, 59, 0, 0, (0, 0, 0.2), 0.25],	#(right,  forward,  down), delay
   #[2, "sw_chair_drinking_beta_1", 0, 59, 0, 0, (0, 0, 0.2), 0.25],	#(right,  forward,  down), delay
   #[2, "sw_chair_drinking_beta_1", 0, 59, 0, 0],	#(right,  forward,  down), delay
   [2.0, "sw_chair_moving_head_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],	#by Swyter
   [4.0, "sw_chair_moving_head_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],	#by Swyter
   [2.0, "sw_chair_stand1_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],		#by Swyter
   [2.0, "sw_chair_stand2_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],		#by Swyter
   
 ], 

 #["sit_cantina_agent", acf_enforce_all|acf_displace_position,
 ["sit_cantina_agent", acf_displace_position,
   #[2, "anim-drinking", 0, 1, 0],		#by geroj
   #[2, "sw_chair_moving_head_fixed", 0, 59, 0, pack2f(0.0, 0.0), (0, 0, 2), 0.0],	#(right,  forward,  down), delay
   #[2, "sw_chair_moving_head_fixed", 0, 1, 0, 0, (0, 0, 0.2), 0.0],	#(right,  forward,  down), delay
   #[2, "sw_chair_moving_head_fixed", 0, 59, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0.2), 0.0],	#(right,  forward,  down), delay
   [0.2, "sw_chair_stand1_fixed", 0, 1, 0, 0, (0, 0, 0.2), 0.0],	#(right,  forward,  down), delay
 ],  
 
 
   ["vader_stand", 0,
   [4, "swy_vader_stand", 0, 70, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25], #by Swyter
 ],

   ["b2_stand", 0,
   [4, "swy_b2_stand", 0, 70, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25], #by Swyter
 ], 
 
 ["b2_walk", acf_enforce_lowerbody,		#from walk_forward
   #[1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "swy_b2_walk", 0, 0, arf_use_walk_progress|arf_cyclic|blend_in_walk,pack2f(0.0,0.0), (0, 0, 0), 0.0],
 ],
 
#-------------------------------------------------------------------------------------------------------------------- 
 
#SW - had to comment out 6 animations for shield bash kit to work
# ["unused_human_anim_95", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_96", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_97", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_98", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_99", 0, [1.0, "anim_human", 0, 1, 0]],
# ["unused_human_anim_100", 0, [1.0, "anim_human", 0, 1, 0]],

 #SW - added shield bash kit
 # START OF SHIELD BASH KIT -------------------------------------------
 
 # strike_fall_back_rise_after_bashed
 ["bash_knocked", acf_enforce_all|acf_align_with_ground,
   [2.0, "anim_human", blow+5400, blow+5453, arf_blend_in_2],
 ],
# strike_chest_front_stop
 ["bash_stun", acf_enforce_all,
   #[1.5, "anim_human", blow+5000, blow+5010, arf_blend_in_3],		#original shield bash
	[1.0, "strikes", 881, 905, arf_blend_in_3],    	#from strike_chest_front
 ],
# strike_chest_front_stop
 ["bash_mini_stun", acf_enforce_all,
   #[0.6, "anim_human", blow+5000, blow+5010, arf_blend_in_3],	#original shield bash
    [0.8, "strikes", 1618, 1640, arf_blend_in_3], 	#from strike_abdomen_front
 ],
 # anim jump end
 ["bash_crouch", acf_enforce_all|acf_enforce_lowerbody,
   [0.7, "anim_human", 280, 290, arf_blend_in_3],
 ], 
# strike_head_front_left
 ["bash_unsuccessful", acf_enforce_all,
   [0.55, "anim_human", blow+0, blow+10, arf_blend_in_3],
 ],

 ["release_bash", acf_enforce_all|acf_right_cut|acf_parallels_for_look_slope,
#   [0.62, "anim_human", combat+5710, combat+5740, blend_in_release],		#original shield bash (good)
   #[0.62, "anim_human", combat+4300, combat+4335, blend_in_release],		# testing release_swingleft_fist?  nope
   #[2.0, "anim_human", combat+2650, combat+2860, blend_in_release],		#testing reload_musket?		     nope
   #[0.62, "sw_lightsaber_left_swing_1", 25, 49, blend_in_release],		#from swyter, maybe
   #[0.62, "equip_arms", 78, 84, blend_in_release],		#from native, maybe
   #[0.62, "man_cheer", 808, 825, blend_in_release],		#from native, maybe
   #[0.8, "wb_defend_shield_right", 11, 36, blend_in_release],		#shield bash from warband
   [0.8, "wb_defend_shield_right", 11, 36, arf_blend_in_3],		#shield bash from warband
 ],
 
 ["stand_crouch", 0,
   #[10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   [4.0, "Sit", 0, 199, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
 ],
 
 ["crouch", 0,
   #[10.0, "lord_stand", 0, 111, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.25],
   #[15.0, "Sit", 0, 199, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],   
   [30.0, "coehorn_shoot", 49, 49, arf_use_stand_progress|arf_cyclic, 0, (0, 0, 0), 0.0],   
 ], 
 
 ["crouch_stop", 0,
   [0.01, "Sit", 0, 0, arf_blend_in_3],
 ],  

 ["walk_forward_crouch", acf_enforce_lowerbody,
   #[1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
   [1.0, "crouch", 0, 19, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound,pack2f(0.4,0.9), (0, 0, 0), 0.0],
 ], 
 
 
  # ["release_bash", acf_left_cut|acf_parallels_for_look_slope|acf_anim_length(100),	#from release_slashleft_onehanded
   # [0.6, "anim_human", combat+9110, combat+9140, blend_in_release], 			#original
   # #[2.0, "sw_lightsaber_left_swing_1", 0, 49, blend_in_release], 
 # ],
 
 # END OF SHIELD BASH KIT -----------------------------------------------------
 
 #["horse_stand", 0,
 ["horse_stand", acf_enforce_lowerbody,
##   [5.0, "anim_horse", 1000, 1044, arf_cyclic],
##   [3.0, "anim_horse", 600, 644, arf_cyclic], 
#SW - modified horse_stand
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 644, 688, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 688, 732, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [3.5, "anim_horse", 732, 820, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [1.5, "anim_horse", 600, 644, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   # [2.5, "anim_horse", 820, 908, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],
   #[1.5, "anim_horse", 600, 600, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],		#SW this was working decent
   #[5.0, "anim_horse", 0, 99, arf_cyclic|arf_use_stand_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.0], 
   #[5.0, "sw_speeder_stand", 0, 99, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.0,0.0,0.0,0.0), (0, 0, 0), 0.0], 
   #[5.0, "sw_speeder_stand", 0, 99, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[5, "sw_speeder_stand", 0, 99, arf_blend_in_4],	#SW - new horse_stand animation by Swyter
   #[1.6, "anim_horse", 205, 222,  arf_blend_in_4], #|arf_end_pos_0_25],
   ##@>[5.0, "anim_horse", 600, 600, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],		#SW this was working decent
   [6.0, "sw_speeder_stand", 0, 99, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],		#SW this was working decent
   #[5.0, "sw_speeder_stand", 0, 99, arf_cyclic|arf_use_stand_progress|arf_make_walk_sound, 0, (0, 0, 0), 0.0],	#SW - new horse_stand animation by Swyter   
 ],
 #SW - modified horse_pace_1
 ["horse_pace_1", acf_enforce_lowerbody,
   #[1.0, "anim_horse", 0, 31, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.25], 
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0,0,0,0), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.25], 
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.0], 
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.0], 
   #[1.0, "anim_horse", 0, 31, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.25], 	#native
   [1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.25,0.42,0.75,0.92), (0, 0, 0), 0.25], 	#native modified
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
    ],
 #SW - modified horse_pace_2 
 ["horse_pace_2", acf_enforce_lowerbody,
   #[0.8, "anim_horse", 50, 69, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.9],
   #[0.8, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0,0,0,0), (0, 0, 0), 0.0],   
   #[0.8, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.9],
   #[0.8, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[0.8, "anim_horse", 50, 69, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.9],	#native
   [0.8, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.15,0.16,0.65,0.66), (0, 0, 0), 0.9],	#native modified
 ],
 #SW - modified horse_pace_3 
 ["horse_pace_3", acf_enforce_lowerbody,
   #[0.6, "anim_horse", 100, 116, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.6],
   #[0.6, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0,0,0,0), (0, 0, 0), 0.0],      
   #[0.6, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.6],
   #[0.6, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[0.6, "anim_horse", 100, 116, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.6],	#native
   [0.6, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.93,0.95,0.35,0.42), (0, 0, 0), 0.6],	#native modified
 ],
 #SW - modified horse_pace_4 
 ["horse_pace_4", acf_enforce_lowerbody,
   #[0.5, "anim_horse", 150, 165, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.2],
   #[0.5, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0,0,0,0), (0, 0, 0), 0.0],      
   #[0.5, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.2],
   #[0.5, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.0],
   #[0.5, "anim_horse", 150, 165, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.2],	#native
   [0.5, "anim_horse", 0, 0, arf_cyclic|arf_use_walk_progress|arf_make_walk_sound,pack4f(0.4,0.31,0.79,0.94), (0, 0, 0), 0.2],	#native modified
 ],
 #SW - modified horse_walk_backward 
 ["horse_walk_backward", acf_enforce_lowerbody,
   #[1.9, "anim_horse", 31, 0, arf_cyclic|arf_use_inv_walk_progress|arf_make_walk_sound,pack4f(0.07,0.13,0.56,0.63), (0, 0, 0), 0.0],
   #[1.9, "anim_horse", 0, 0, arf_cyclic|arf_use_inv_walk_progress|arf_make_walk_sound,pack4f(0,0,0,0), (0, 0, 0), 0.0],   
   #[1.9, "anim_horse", 0, 0, arf_cyclic|arf_use_inv_walk_progress|arf_make_walk_sound,pack4f(0.07,0.13,0.56,0.63), (0, 0, 0), 0.0],
   [1.0, "anim_horse", 0, 0, arf_cyclic|arf_use_inv_walk_progress|arf_make_walk_sound,pack4f(0.07,0.13,0.56,0.63), (0, 0, 0), 0.0],
 ],
 #SW - modified horse_rear 
 ["horse_rear", acf_enforce_lowerbody | acf_ignore_slope,
#   [1.4, "anim_horse_temp", 1, 10,  arf_blend_in_1],
##   [2.5, "anim_horse", 505, 580,  arf_blend_in_8],
   #[2.0, "anim_horse", 260, 301,  arf_blend_in_8],
   [1.0, "anim_horse", 260, 260,  arf_blend_in_8],   
 ],
 #SW modified horse_jump 
 ["horse_jump", acf_enforce_lowerbody,
   #[1.6, "anim_horse", 205, 222,  arf_blend_in_4], #|arf_end_pos_0_25],
   [1.6, "anim_horse", 205, 222,  arf_blend_in_4], #|arf_end_pos_0_25],
 ],
 #SW - modified horse_jump_end 
 ["horse_jump_end", acf_enforce_lowerbody,
   #[0.1, "anim_horse", 222,  224,  arf_blend_in_8],
   [0.1, "anim_horse", 222,  224,  arf_blend_in_8],
 ],
 #SW - modified horse_turn_right (nevermind, this messed up the speeder animations)
 ["horse_turn_right", 0,
   #[1.0, "anim_horse", 500, 533, arf_blend_in_4|arf_cyclic], 	#SW - this was working decent
   #[0.1, "anim_horse", 500, 500, arf_blend_in_4|arf_cyclic], 
   [1.0, "sw_speeder_turn_right", 0, 39, arf_blend_in_4|arf_cyclic], 	#SW - new animation by Swyer
   #[0.1, "sw_speeder_turn_right", 0, 39, arf_blend_in_4|arf_cyclic], 	#SW - new animation by Swyer (maybe use 3 seconds?)
 ],
 #SW - modified horse_turn_left (nevermind, this messed up the speeder animations)
 ["horse_turn_left", 0,
   #[1.0, "anim_horse", 450, 483, arf_blend_in_4|arf_cyclic],	#SW - this was working decent
   #[0.1, "anim_horse", 450, 450, arf_blend_in_4|arf_cyclic],
   [1.0, "sw_speeder_turn_left", 0, 39, arf_blend_in_4|arf_cyclic],		#SW - new animation by Swyer
   #[0.1, "sw_speeder_turn_left", 0, 39, arf_blend_in_4|arf_cyclic],		#SW - new animation by Swyer (maybe use 3 seconds?)
 ],
 #SW - modified horse_slow
 ["horse_slow", 0,
   #[3.0, "anim_horse", 0, 31,arf_cyclic], 
   #[1.5, "anim_horse", 0, 31, arf_cyclic], 
   [1.5, "anim_horse", 0, 0, arf_cyclic], 
 ],
 #SW - modified horse_fall_in_place
 ["horse_fall_in_place", acf_enforce_all|acf_align_with_ground,
   #[4.0, "anim_horse", 0, 38, arf_blend_in_16|arf_make_custom_sound, pack2f(0.0, 0.0)], 
   [4.0, "anim_horse", 0, 0, arf_blend_in_16|arf_make_custom_sound, pack2f(0.0, 0.0)], 
 ],
 #SW - modified horse_fall_right
 ["horse_fall_right", acf_enforce_all|acf_align_with_ground,
   #[1.75, "anim_horse", 350, 375,  arf_blend_in_8|arf_make_custom_sound, pack2f(0.6, 0.0), (0, 0, 0), 0.5],
   [1.75, "anim_horse", 350, 350,  arf_blend_in_8|arf_make_custom_sound, pack2f(0.0, 0.0), (0, 0, 0), 0.0],
 ],
 #SW - modified horse_fall_roll 
 ["horse_fall_roll", acf_enforce_all|acf_align_with_ground,
   #[2.5, "anim_horse", 400, 428,  arf_blend_in_8|arf_make_custom_sound, pack2f(0.3, 0.0), (0, 0, 0), 1.8],
   #[2.5, "anim_horse", 400, 400,  arf_blend_in_8|arf_make_custom_sound, pack2f(0.0, 0.0), (0, 0, 0), 0.0],
   [4.0, "anim_horse", 0, 0, arf_blend_in_16|arf_make_custom_sound, pack2f(0.0, 0.0)], 		#from horse_fall_in_place
 ],
 ### Unused horse animations start from here.
 ["unused_horse_anim_1", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_2", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_3", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_4", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_5", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_6", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_7", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_8", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_9", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_10", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_11", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_12", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_13", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_14", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_15", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_16", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_17", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_18", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_19", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_20", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_21", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_22", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_23", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_24", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_25", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_26", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_27", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_28", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_29", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_30", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_31", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_32", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_33", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_34", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_35", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_36", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_37", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_38", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_39", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_40", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_41", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_42", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_43", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_44", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_45", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_46", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_47", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_48", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_49", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_50", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_51", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_52", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_53", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_54", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_55", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_56", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_57", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_58", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_59", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_60", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_61", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_62", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_63", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_64", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_65", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_66", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_67", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_68", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_69", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_70", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_71", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_72", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_73", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_74", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_75", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_76", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_77", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_78", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_79", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_80", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_81", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_82", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_83", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_84", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_85", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_86", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_87", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_88", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_89", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_90", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_91", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_92", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_93", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_94", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_95", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_96", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_97", 0, [1.0, "anim_horse", 0, 1, 0]],
 ["unused_horse_anim_98", 0, [1.0, "anim_horse", 0, 1, 0]],
 
 #SW - had to comment out for speeder_allow_movement
 #["unused_horse_anim_99", 0, [1.0, "anim_horse", 0, 1, 0]],
  #SW - had to comment out for stationary_speeder
 #["unused_horse_anim_100", 0, [1.0, "anim_horse", 0, 1, 0]],
 
 ["speeder_stationary", 0, 
	#[1.0, "anim_horse", 0, 1, 0]		#this works
	#[5, "sw_speeder_stand", 0, 99, arf_cyclic|arf_use_stand_progress, 0, (0, 0, 0), 0.0],	#SW - new horse_stand animation by Swyter
	[5, "sw_speeder_stand", 0, 99, 0],	#SW - new horse_stand animation by Swyter
 ],
 
 ["speeder_allow_movement", 0, 
	[0.01, "sw_speeder_stand", 0, 0, 0],	#SW - new horse_stand animation by Swyter
 ],
 
 ]