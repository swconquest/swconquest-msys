# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_sounds import *

sounds = [
 #("click", sf_2d|sf_vol_1,["drum_3.ogg"]),
 #("click", sf_2d|sf_vol_1,["int_select.ogg"]),
 ("click", sf_2d|sf_vol_1,["swc_click.ogg"]),
 ("tutorial_1", sf_2d|sf_vol_7,["tutorial_1.ogg"]),
 ("tutorial_2", sf_2d|sf_vol_7,["tutorial_2.ogg"]),
 ("gong", sf_2d|sf_priority_9|sf_vol_7, ["s_cymbals.ogg"]),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_7, ["quest_completed.ogg"]),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_7, ["quest_succeeded.ogg"]),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["quest_concluded.ogg"]),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.ogg"]),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.ogg"]),
 ("rain",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["rain_1.ogg"]),
 #SW - modified money_received and money_paid
 #("money_received",sf_priority_10|sf_vol_6, ["coins_dropped_1.ogg"]),
 #("money_paid",sf_priority_10|sf_vol_10, ["coins_dropped_2.ogg"]),
 ("money_received",sf_priority_10|sf_vol_6, ["ui_toggle_mouse_mode.ogg"]),
 ("money_paid",sf_priority_10|sf_vol_10, ["ui_toggle_mouse_mode.ogg"]), 
 
 #SW - modified swong_clash_#
 ("sword_clash_1", 0,["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"]),
 ("sword_clash_2", 0,["s_swordClash2.wav"]),
 ("sword_clash_3", 0,["s_swordClash3.wav"]),
 #
 #("sword_clash_1", 0,["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),
 #("sword_clash_2", 0,["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),
 #("sword_clash_3", 0,["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),
 #SW - switched sword_swing to a lightsaber (affects ALL swords, fists, axes, etc....)
 ("sword_swing", sf_vol_8|sf_priority_6,["s_swordSwing.ogg"]),
# ("sword_swing",sf_vol_8|sf_priority_2,["saber_swing1.ogg","saber_swing2.ogg","saber_swing3.ogg","saber_swing4.ogg","saber_swing5.ogg","saber_swing6.ogg","saber_swing7.ogg","saber_swing8.ogg",]),
#  ("sword_swing",sf_vol_8|sf_priority_2,["silence.ogg",]),
 
 ("footstep_grass", sf_vol_4|sf_priority_1,["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"]),
 ("footstep_wood", sf_vol_6|sf_priority_1,["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"]),
# ("footstep_wood", sf_vol_3|sf_priority_1,["footstep_stone_1.ogg","footstep_stone_3.ogg","footstep_stone_4.ogg"]),
 ("footstep_water", sf_vol_4|sf_priority_3,["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"]),

#SW - switched footstep_horse_#
# ("footstep_horse",sf_priority_3, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
## ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
# ("footstep_horse_1b",sf_priority_3, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
# ("footstep_horse_1f",sf_priority_3, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
## ("footstep_horse_1f",sf_priority_3, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
# ("footstep_horse_2b",sf_priority_3, ["s_footstep_horse_2b.wav"]),
# ("footstep_horse_2f",sf_priority_3, ["s_footstep_horse_2f.wav"]),
# ("footstep_horse_3b",sf_priority_3, ["s_footstep_horse_3b.wav"]),
# ("footstep_horse_3f",sf_priority_3, ["s_footstep_horse_3f.wav"]),
# ("footstep_horse_4b",sf_priority_3, ["s_footstep_horse_4b.wav"]),
# ("footstep_horse_4f",sf_priority_3, ["s_footstep_horse_4f.wav"]),
# ("footstep_horse_5b",sf_priority_3, ["s_footstep_horse_5b.wav"]),
# ("footstep_horse_5f",sf_priority_3, ["s_footstep_horse_5f.wav"]),
 # ("footstep_horse",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_1b",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_1f",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_2b",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_2f",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_3b",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_3f",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_4b",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_4f",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_5b",sf_priority_3, ["speeder_idle.ogg"]),
 # ("footstep_horse_5f",sf_priority_3, ["speeder_idle.ogg"]), 
 ("footstep_horse",sf_priority_3, []),
 ("footstep_horse_1b",sf_priority_3, []),
 ("footstep_horse_1f",sf_priority_3, []),
 ("footstep_horse_2b",sf_priority_3, []),
 ("footstep_horse_2f",sf_priority_3, []),
 ("footstep_horse_3b",sf_priority_3, []),
 ("footstep_horse_3f",sf_priority_3, []),
 ("footstep_horse_4b",sf_priority_3, []),
 ("footstep_horse_4f",sf_priority_3, []),
 ("footstep_horse_5b",sf_priority_3, []),
 ("footstep_horse_5f",sf_priority_3, []), 
 
 
 ("jump_begin", sf_vol_7|sf_priority_9,["jump_begin.ogg"]),
 ("jump_end", sf_vol_5|sf_priority_9,["jump_end.ogg"]),
 ("jump_begin_water", sf_vol_4|sf_priority_9,["jump_begin_water.ogg"]),
 ("jump_end_water", sf_vol_4|sf_priority_9,["jump_end_water.ogg"]),
 #SW - modified horse_jump_begin and horse_jump_end
 #("horse_jump_begin", sf_vol_7|sf_priority_9,["horse_jump_begin.ogg"]),
 #("horse_jump_end", sf_vol_7|sf_priority_9,["horse_jump_end.ogg"]),
 ("horse_jump_begin", sf_vol_7|sf_priority_9,["speeder_jump_begin.ogg"]),
 ("horse_jump_end", sf_vol_7|sf_priority_9,["speeder_jump_end.ogg"]), 
 #SW - modified horse_jump_begin_water and horse_jump_end_water
 #("horse_jump_begin_water", sf_vol_4|sf_priority_9,["jump_begin_water.ogg"]),
 #("horse_jump_end_water", sf_vol_4|sf_priority_9,["jump_end_water.ogg"]),
 ("horse_jump_begin_water", sf_vol_4|sf_priority_9,["speeder_jump_begin.ogg"]),
 ("horse_jump_end_water", sf_vol_4|sf_priority_9,["speeder_jump_end.ogg"]),
 
 #SW - modified release_bow to be silent
 #("release_bow",sf_vol_5, ["release_bow_1.ogg"]),
 ("release_bow",sf_vol_5, []),
#SW - modified release_crossbow (crossbow is used for heavy weapons)
# ("release_crossbow",sf_vol_7, ["release_crossbow_1.ogg"]),
 ("release_crossbow",sf_vol_1, []),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.ogg"]),
 ("throw_knife",sf_vol_5, ["throw_knife_1.ogg"]),
 ("throw_stone",sf_vol_7, ["throw_stone_1.ogg"]),

#SW - modified reload_crossbow 
# ("reload_crossbow",sf_vol_3, ["reload_crossbow_1.ogg"]),
# ("reload_crossbow_continue",sf_vol_6, ["put_back_dagger.ogg"]),
 ("reload_crossbow",sf_vol_7|sf_priority_7, ["blaster_reload_a.ogg"]),
 ("reload_crossbow_continue",sf_vol_7|sf_priority_7, ["blaster_reload_b.ogg"]),
# ("reload_pistol",sf_vol_7|sf_priority_7, ["blaster_reload_a.ogg"]),		#doesn't work. with the custom_sound flag...
# ("reload_pistol_continue",sf_vol_7|sf_priority_7, ["blaster_reload_b.ogg"]),	#doesn't work. with the custom_sound flag...
# ("reload_musket",sf_vol_7|sf_priority_7, ["blaster_reload_a.ogg"]),		#doesn't work. with the custom_sound flag...
# ("reload_musket_continue",sf_vol_7|sf_priority_7, ["blaster_reload_b.ogg"]),	#doesn't work. with the custom_sound flag...
 
 
 #SW - modified pull_bow and pull_arrow
 #("pull_bow",sf_vol_4, ["pull_bow_1.ogg"]),
 #("pull_bow",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["force_power.ogg"]),
 ("pull_bow",sf_vol_4|sf_looping|sf_start_at_random_pos, []),
 #("pull_arrow",sf_vol_5, ["pull_arrow.ogg"]),
 ("pull_arrow",sf_vol_5, []),

 ("arrow_pass_by",0, ["arrow_pass_by_1.ogg","arrow_pass_by_2.ogg","arrow_pass_by_3.ogg","arrow_pass_by_4.ogg"]),
 #("bolt_pass_by",0, ["bolt_pass_by_1.ogg"]),
 ("bolt_pass_by",0, ["boltby_01.ogg","boltby_02.ogg","boltby_03.ogg","boltby_04.ogg","boltby_05.ogg","boltby_06.ogg","boltby_07.ogg","boltby_08.ogg","boltby_09.ogg","boltby_10.ogg"]),
 ("javelin_pass_by",0, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9, ["stone_pass_by_1.ogg"]),
 ("axe_pass_by",0, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",0, ["knife_pass_by_1.ogg"]),
 #SW - modified bullet_pass_by
 #("bullet_pass_by",0, ["arrow_whoosh_1.ogg"]),
 ("bullet_pass_by",0, ["boltby_01.ogg","boltby_02.ogg","boltby_03.ogg","boltby_04.ogg","boltby_05.ogg","boltby_06.ogg","boltby_07.ogg","boltby_08.ogg","boltby_09.ogg","boltby_10.ogg"]),
 
# ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["bolthit_01.ogg","bolthit_02.ogg","bolthit_03.ogg","bolthit_04.ogg","bolthit_05.ogg","bolthit_06.ogg","bolthit_07.ogg","bolthit_08.ogg","bolthit_09.ogg","bolthit_10.ogg"
													   ,"bolthit_11.ogg","bolthit_12.ogg","bolthit_13.ogg","bolthit_14.ogg","bolthit_15.ogg","bolthit_16.ogg","bolthit_17.ogg","bolthit_18.ogg","bolthit_19.ogg","bolthit_20.ogg"
													   ,"bolthit_21.ogg","bolthit_22.ogg","bolthit_23.ogg"]),

 #("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["bolthit_01.ogg","bolthit_02.ogg","bolthit_03.ogg","bolthit_04.ogg","bolthit_05.ogg","bolthit_06.ogg","bolthit_07.ogg","bolthit_08.ogg","bolthit_09.ogg","bolthit_10.ogg"
													   ,"bolthit_11.ogg","bolthit_12.ogg","bolthit_13.ogg","bolthit_14.ogg","bolthit_15.ogg","bolthit_16.ogg","bolthit_17.ogg","bolthit_18.ogg","bolthit_19.ogg","bolthit_20.ogg"
													   ,"bolthit_21.ogg","bolthit_22.ogg","bolthit_23.ogg"]),
													   
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 #SW - modified incoming_bullet_hit_ground
 #("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bolthit_01.ogg","bolthit_02.ogg","bolthit_03.ogg","bolthit_04.ogg","bolthit_05.ogg","bolthit_06.ogg","bolthit_07.ogg","bolthit_08.ogg","bolthit_09.ogg","bolthit_10.ogg"
													   ,"bolthit_11.ogg","bolthit_12.ogg","bolthit_13.ogg","bolthit_14.ogg","bolthit_15.ogg","bolthit_16.ogg","bolthit_17.ogg","bolthit_18.ogg","bolthit_19.ogg","bolthit_20.ogg"
													   ,"bolthit_21.ogg","bolthit_22.ogg","bolthit_23.ogg"]),

# ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["bolthit_01.ogg","bolthit_02.ogg","bolthit_03.ogg","bolthit_04.ogg","bolthit_05.ogg","bolthit_06.ogg","bolthit_07.ogg","bolthit_08.ogg","bolthit_09.ogg","bolthit_10.ogg"
													   ,"bolthit_11.ogg","bolthit_12.ogg","bolthit_13.ogg","bolthit_14.ogg","bolthit_15.ogg","bolthit_16.ogg","bolthit_17.ogg","bolthit_18.ogg","bolthit_19.ogg","bolthit_20.ogg"
													   ,"bolthit_21.ogg","bolthit_22.ogg","bolthit_23.ogg"]), 

 #("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7, ["bolthit_01.ogg","bolthit_02.ogg","bolthit_03.ogg","bolthit_04.ogg","bolthit_05.ogg","bolthit_06.ogg","bolthit_07.ogg","bolthit_08.ogg","bolthit_09.ogg","bolthit_10.ogg"
													   ,"bolthit_11.ogg","bolthit_12.ogg","bolthit_13.ogg","bolthit_14.ogg","bolthit_15.ogg","bolthit_16.ogg","bolthit_17.ogg","bolthit_18.ogg","bolthit_19.ogg","bolthit_20.ogg"
													   ,"bolthit_21.ogg","bolthit_22.ogg","bolthit_23.ogg"]), 
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 #SW - modified outgoing_bullet_hit_ground
 #("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bolthit_01.ogg","bolthit_02.ogg","bolthit_03.ogg","bolthit_04.ogg","bolthit_05.ogg","bolthit_06.ogg","bolthit_07.ogg","bolthit_08.ogg","bolthit_09.ogg","bolthit_10.ogg"
													   ,"bolthit_11.ogg","bolthit_12.ogg","bolthit_13.ogg","bolthit_14.ogg","bolthit_15.ogg","bolthit_16.ogg","bolthit_17.ogg","bolthit_18.ogg","bolthit_19.ogg","bolthit_20.ogg"
													   ,"bolthit_21.ogg","bolthit_22.ogg","bolthit_23.ogg"]),


 ("draw_sword",sf_priority_4, ["draw_sword.ogg"]),
 ("put_back_sword",sf_priority_4, ["put_back_sword.ogg"]),
#SW - modified draw sound since carry_sword_back is used for rifles 
 #("draw_greatsword",sf_priority_4, ["draw_greatsword.ogg"]),
 ("draw_greatsword",sf_priority_4, ["draw_from_holster.ogg"]),
 #("put_back_greatsword",sf_priority_4, ["put_back_sword.ogg"]),
 ("put_back_greatsword",sf_priority_4, ["put_back_to_holster.ogg"]),
 ("draw_axe",sf_priority_4, ["draw_mace.ogg"]),
 ("put_back_axe",sf_priority_4, ["put_back_to_holster.ogg"]),
 ("draw_greataxe",sf_priority_4, ["draw_greataxe.ogg"]),
 ("put_back_greataxe",sf_priority_4, ["put_back_to_leather.ogg"]),
 ("draw_spear",sf_priority_4, ["draw_spear.ogg"]),
 ("put_back_spear",sf_priority_4, ["put_back_to_leather.ogg"]),
 #SW - modified draw_crossbow
 #("draw_crossbow",sf_priority_4, ["draw_crossbow.ogg"]),
 ("draw_crossbow",sf_priority_4, ["ui_equip_blaster.ogg"]),
 ("put_back_crossbow",sf_priority_4, ["put_back_to_leather.ogg"]),
 #SW - modified draw_revolver
 #("draw_revolver",sf_priority_4, ["draw_from_holster.ogg"]),
 ("draw_revolver",sf_priority_4, ["ui_equip_blaster.ogg"]),
 ("put_back_revolver",sf_priority_4, ["put_back_to_holster.ogg"]),
 #SW - modified draw_dagger (only use itcf_carry_dagger_front_left for lightsaber weapons)
 #("draw_dagger",sf_priority_4, ["draw_dagger.ogg"]),
 #("put_back_dagger",sf_priority_4, ["put_back_dagger.ogg"]),
 ("draw_dagger",sf_priority_9|sf_vol_9, ["lightsaber_powerup.ogg"]),
 ("put_back_dagger",sf_priority_9|sf_vol_9, ["lightsaber_powerdown.ogg"]), 
 ("draw_bow",sf_priority_4, ["draw_bow.ogg"]),
 ("put_back_bow",sf_priority_4, ["put_back_to_holster.ogg"]),
 #SW - modified draw_shield
 #("draw_shield",sf_priority_4|sf_vol_7, ["draw_shield.ogg"]),
 ("draw_shield",sf_priority_4|sf_vol_7, ["wep_shoulder_on.ogg"]),
 #SW - modified put_back_shield
 #("put_back_shield",sf_priority_4|sf_vol_7, ["put_back_shield.ogg"]),
 ("put_back_shield",sf_priority_4|sf_vol_7, ["wep_shoulder_off.ogg"]),
 ("draw_other",sf_priority_4, ["draw_other.ogg"]),
 ("put_back_other",sf_priority_4, ["draw_other2.ogg"]),

 ("body_fall_small",sf_priority_6|sf_vol_10, ["body_fall_small_1.ogg","body_fall_small_2.ogg"]),
 ("body_fall_big",sf_priority_6|sf_vol_10, ["body_fall_1.ogg","body_fall_2.ogg","body_fall_3.ogg"]),
# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.ogg"]),
 ("horse_body_fall_begin",sf_priority_6|sf_vol_10, ["horse_body_fall_begin_1.ogg"]),
 ("horse_body_fall_end",sf_priority_6|sf_vol_10, ["horse_body_fall_end_1.ogg","body_fall_2.ogg","body_fall_very_big_1.ogg"]),

#SW - modified sounds  (wood = lightsabers, metal = all other weapons)
### ("clang_metal",sf_priority_9, ["clang_metal_1.ogg","clang_metal_2.ogg","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
# ("hit_wood_wood",sf_priority_7|sf_vol_10, ["hit_wood_wood_1.ogg","hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg","hit_wood_metal_6.ogg"]),#dummy
# ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_4.ogg",
#                                              "hit_metal_metal_5.ogg","hit_metal_metal_6.ogg","hit_metal_metal_7.ogg","hit_metal_metal_8.ogg",
#                                              "hit_metal_metal_9.ogg","hit_metal_metal_10.ogg",
#                                              "clang_metal_1.ogg","clang_metal_2.ogg"]),
# ("hit_wood_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_1.ogg","hit_metal_metal_2.ogg","hit_wood_metal_7.ogg"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_10, ["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),#dummy
# ("hit_metal_metal",sf_priority_7|sf_vol_10, ["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),
 ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_4.ogg","hit_metal_metal_5.ogg","hit_metal_metal_6.ogg","hit_metal_metal_7.ogg","hit_metal_metal_8.ogg","hit_metal_metal_9.ogg","hit_metal_metal_10.ogg","clang_metal_1.ogg","clang_metal_2.ogg"]),
# ("hit_metal_metal",sf_priority_7|sf_vol_10, ["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["saber_clash1.ogg","saber_clash2.ogg","saber_clash3.ogg"]),
 
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.ogg","sword_clank_metal_10.ogg","sword_clank_metal_12.ogg","sword_clank_metal_13.ogg"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg"]),

#SW - modified shield_hit_ sounds (wood = energy shields, metal = all other weapons)
# ("shield_hit_wood_wood",sf_priority_7|sf_vol_10, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit_metal_metal_1.ogg","shield_hit_metal_metal_2.ogg","shield_hit_metal_metal_3.ogg","shield_hit_metal_metal_4.ogg"]),
# ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]), #(shield is wood)
# ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),#(shield is metal)
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_10, ["shield_hit1.ogg","shield_hit2.ogg","shield_hit3.ogg"]),
# ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit1.ogg","shield_hit2.ogg","shield_hit3.ogg"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit1.ogg","shield_hit2.ogg","shield_hit3.ogg"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit1.ogg","shield_hit2.ogg","shield_hit3.ogg"]),#(shield is metal) 

 ("shield_broken",sf_priority_9, ["shield_broken.ogg"]),
 ("man_hit",sf_priority_7|sf_vol_10, ["man_hit_5.ogg","man_hit_6.ogg","man_hit_7.ogg","man_hit_8.ogg","man_hit_9.ogg","man_hit_10.ogg","man_hit_11.ogg","man_hit_12.ogg","man_hit_13.ogg","man_hit_14.ogg","man_hit_15.ogg",
                                      "man_hit_17.ogg","man_hit_18.ogg","man_hit_19.ogg","man_hit_22.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg","man_hit_59.ogg"]),
 ("man_die",sf_priority_10,  [	"wilhelm_scream.ogg","man_death_1.ogg","man_death_8.ogg","man_death_8b.ogg","man_death_11.ogg","man_death_14.ogg",
								"wilhelm_scream.ogg","man_death_16.ogg","man_death_18.ogg","man_death_21.ogg","man_death_29.ogg","man_death_40.ogg",
								                     "man_death_44.ogg","man_death_46.ogg","man_death_48.ogg","man_death_64.ogg"]),# ["man_fall_1.ogg","man_fall_2.ogg","man_fall_3.ogg","man_fall_4.ogg"]),
 # HC - Changed woman hit sounds begin
 ("woman_hit",sf_priority_7, ["woman_hit_2.ogg","woman_hit_3.ogg",
                              "woman_hit_b_2.ogg","woman_hit_b_4.ogg","woman_hit_b_6.ogg","woman_hit_b_7.ogg","woman_hit_b_8.ogg",
                              "woman_hit_b_11.ogg","woman_hit_b_14.ogg","woman_hit_b_16.ogg",
						"woman_hit_4.ogg",
                        "woman_hit_5.ogg",
                        "woman_hit_6.ogg",
                        "woman_hit_7.ogg",
                        "woman_hit_8.ogg",
                        "woman_hit_9.ogg",
                        "woman_hit_11.ogg",
                        "woman_hit_12.ogg",
                        "woman_hit_13.ogg",
                        "woman_hit_14.ogg",
                        "woman_hit_15.ogg",
                        "woman_hit_16.ogg",
                        "woman_hit_17.ogg",
                        "woman_hit_18.ogg",
                        "woman_hit_19.ogg"
                        "woman_hit_20.ogg",
                        "woman_hit_21.ogg",
                        "woman_hit_22.ogg"]),
 ("woman_die",sf_priority_10, ["woman_fall_1.ogg","woman_hit_b_5.ogg","groaning.ogg","groaning4.ogg","umph.ogg",]),
	 ("woman_victory",
		sf_priority_5|sf_vol_10,
		[
			"womancheer1.ogg",
			"femalecheer2.ogg",
			"femalecheer3.ogg",
			"femalecheer4.ogg",
			"femalecheer5.ogg",
			"wooaao.ogg",
			"womanlaugh.ogg"
		]
	),

	("woman_grunt",
		sf_priority_6|sf_vol_4, 
		[
			"femgrunt1.ogg",
			"femgrunt2.ogg",
			"femgrunt6.ogg",
			"femgrunt9.ogg",
			"femgrunt10.ogg"
		]
	),

 	("woman_grunt_long",
		sf_priority_5|sf_vol_8, 
		[
			"femgrunt1.ogg",
			"femgrunt2.ogg",
			"femgrunt9.ogg",
			"femgrunt10.ogg"
		]
	),
# HC - Changed woman hit sounds end

 ("hide",0, ["s_hide.wav"]),
 ("unhide",0, ["s_unhide.wav"]),
 
 #SW - modified neigh
 #("neigh",0, ["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"]),
 ("neigh",0, ["engine_stop.ogg"]),
 #SW - modified gallop
 #("gallop",sf_vol_3, ["horse_gallop_3.ogg","horse_gallop_4.ogg","horse_gallop_5.ogg"]),
 #("gallop",sf_vol_3, ["speeder_idle.ogg"]),
 #("gallop",sf_vol_3|sf_looping, ["speeder_idle.ogg"]),
 ("gallop",sf_vol_3, []),
 
 
 #SW - modified battle noise
 #("battle",sf_vol_4, ["battle.ogg"]),
 ("battle",sf_vol_5, ["space_battle_noise_1.ogg","space_battle_noise_2.ogg"]),
 
# ("bow_shoot_player",sf_priority_10|sf_vol_10, ["bow_shoot_4.ogg"]),
# ("bow_shoot",sf_priority_4, ["bow_shoot_4.ogg"]),
# ("crossbow_shoot",sf_priority_4, ["bow_shoot_2.ogg"]),
 #@>("arrow_hit_body",sf_priority_4, ["arrow_hit_body_1.ogg","arrow_hit_body_2.ogg","arrow_hit_body_3.ogg"]),
 ("arrow_hit_body",sf_priority_4, ["rvnshn_blaster_hit.ogg","rvnshn_blaster_hit2.ogg","rvnshn_blaster_hit3.ogg","rvnshn_blaster_hit4.ogg"]),
 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.ogg","sword_hit_lo_armor_hi_dmg_2.ogg","sword_hit_lo_armor_hi_dmg_3.ogg"]),
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_hit_high_armor_low_damage.ogg","metal_hit_high_armor_low_damage_2.ogg","metal_hit_high_armor_low_damage_3.ogg"]),
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_hi_armor_hi_dmg_1.ogg","sword_hit_hi_armor_hi_dmg_2.ogg","sword_hit_hi_armor_hi_dmg_3.ogg"]),
#SW - wooden weapons are now lightsabers/energy weapons, so switch the sound effects
# ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_hit_low_1.ogg","blunt_hit_low_2.ogg","blunt_hit_low_3.ogg"]),
# ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
# ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["wooden_hit_high_armor_low_damage.ogg","wooden_hit_high_armor_low_damage_2.ogg"]),
# ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.ogg","sword_hit_lo_armor_hi_dmg_2.ogg","sword_hit_lo_armor_hi_dmg_3.ogg"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.ogg","sword_hit_lo_armor_hi_dmg_2.ogg","sword_hit_lo_armor_hi_dmg_3.ogg"]),
 ("blunt_hit",sf_priority_5|sf_vol_9, ["punch_1.ogg","punch_4.ogg","punch_4.ogg","punch_5.ogg"]),
# ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),
 ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["rvnshn_blaster_hit.ogg","rvnshn_blaster_hit2.ogg","rvnshn_blaster_hit3.ogg","rvnshn_blaster_hit4.ogg"]),
 ("pistol_shot",sf_priority_10|sf_vol_10, ["fl_pistol.wav"]),
 ("man_grunt",sf_priority_6|sf_vol_4, ["man_excercise_1.ogg","man_excercise_2.ogg","man_excercise_4.ogg"]),
 ("man_breath_hard",sf_priority_3|sf_vol_8, ["man_ugh_1.ogg","man_ugh_2.ogg","man_ugh_4.ogg","man_ugh_7.ogg","man_ugh_12.ogg","man_ugh_13.ogg","man_ugh_17.ogg"]),
 ("man_grunt_long",sf_priority_5|sf_vol_8, ["man_grunt_1.ogg","man_grunt_2.ogg","man_grunt_3.ogg","man_grunt_5.ogg","man_grunt_13.ogg","man_grunt_14.ogg"]),
#SW - created woman_yell and added it to module_skins.py
 ("woman_yell",sf_priority_6|sf_vol_8, ["femalecheer3.ogg","femalecheer4.ogg","femalecheer5.ogg","womancheer1.ogg","wooaao.ogg"]), 
 ("man_yell",sf_priority_6|sf_vol_8, ["man_yell_4.ogg","man_yell_4_2.ogg","man_yell_7.ogg","man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","man_yell_15.ogg","man_yell_16.ogg","man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg",
                        "man_yell_b_18.ogg","man_yell_22.ogg","man_yell_b_21.ogg","man_yell_b_22.ogg","man_yell_b_23.ogg","man_yell_c_20.ogg"]),
#TODONOW:
 ("man_warcry",sf_priority_6, ["man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"]),

 ("encounter_jawas",sf_2d|sf_vol_5, ["encounter_river_pirates_5.ogg","encounter_river_pirates_6.ogg","encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg","encounter_river_pirates_4.ogg"]),

 ("encounter_bandits",sf_2d|sf_vol_5, ["encounter_bandit_2.ogg","encounter_bandit_9.ogg","encounter_bandit_12.ogg","encounter_bandit_13.ogg","encounter_bandit_15.ogg","encounter_bandit_16.ogg","encounter_bandit_10.ogg",]),
 ("encounter_farmers",sf_2d|sf_vol_5, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
 ("encounter_tusken_raiders",sf_2d|sf_vol_5, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
 ("encounter_steppe_bandits",sf_2d|sf_vol_5, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
 ("encounter_nobleman",sf_2d|sf_vol_5, ["encounter_nobleman_1.ogg"]),
 ("encounter_vaegirs_ally",sf_2d|sf_vol_5, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
 ("encounter_vaegirs_neutral",sf_2d|sf_vol_5, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("encounter_vaegirs_enemy",sf_2d|sf_vol_5, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 #SW - modified sneak_town_halt
 #("sneak_town_halt",sf_2d, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),
 ("sneak_town_halt",sf_2d, ["set_for_stun.ogg"]),

#SW - modified horse_walk, trop, canter, gallop, breath, snort, low_whinny
 # ("horse_walk",sf_priority_3|sf_vol_9, ["horse_walk_1.ogg","horse_walk_2.ogg","horse_walk_3.ogg","horse_walk_4.ogg"]),
 # ("horse_trot",sf_priority_3|sf_vol_4, ["horse_trot_1.ogg","horse_trot_2.ogg","horse_trot_3.ogg","horse_trot_4.ogg"]),
 # ("horse_canter",sf_priority_3|sf_vol_6, ["horse_canter_1.ogg","horse_canter_2.ogg","horse_canter_3.ogg","horse_canter_4.ogg"]),
 # ("horse_gallop",sf_priority_3|sf_vol_8, ["horse_gallop_6.ogg","horse_gallop_7.ogg","horse_gallop_8.ogg","horse_gallop_9.ogg"]),
# ("horse_breath",sf_priority_3|sf_priority_9|sf_vol_10, ["horse_breath_4.ogg","horse_breath_5.ogg","horse_breath_6.ogg","horse_breath_7.ogg"]),
# ("horse_snort",sf_priority_5|sf_vol_7, ["horse_snort_1.ogg","horse_snort_2.ogg","horse_snort_3.ogg","horse_snort_4.ogg","horse_snort_5.ogg"]),
# ("horse_low_whinny",sf_vol_9, ["horse_whinny-1.ogg","horse_whinny-2.ogg"]),
 #("horse_walk",sf_priority_3|sf_vol_9, ["speeder_walk_short.ogg"]),
 #("horse_trot",sf_priority_3|sf_vol_9, ["speeder_trot_short.ogg"]),
 #("horse_canter",sf_priority_3|sf_vol_9, ["speeder_canter_short.ogg"]),
 #("horse_gallop",sf_priority_3|sf_vol_9, ["speeder_gallop_short.ogg"]),
 # ("horse_walk",sf_priority_3|sf_vol_9, ["speeder_walk.ogg"]),
 # ("horse_trot",sf_priority_3|sf_vol_9, ["speeder_trot.ogg"]),
 # ("horse_canter",sf_priority_3|sf_vol_9, ["speeder_canter.ogg"]),
 # ("horse_gallop",sf_priority_3|sf_vol_9, ["speeder_gallop.ogg"]), 
 ("horse_walk",sf_priority_3|sf_vol_9, []),
 ("horse_trot",sf_priority_3|sf_vol_9, []),
 ("horse_canter",sf_priority_3|sf_vol_9, []),
 ("horse_gallop",sf_priority_3|sf_vol_9, []),  
 ("horse_breath",sf_priority_1|sf_vol_1, []),
 ("horse_snort",sf_priority_1|sf_vol_1, []),
 ("horse_low_whinny",sf_priority_1|sf_vol_1, []),
 
 ("block_fist",0, ["block_fist_3.ogg","block_fist_4.ogg"]),
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","man_victory_4.ogg","man_victory_5.ogg","man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("dummy_hit",sf_priority_9, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
 ("dummy_destroyed",sf_priority_9, ["shield_broken.ogg"]),
 ("gourd_destroyed",sf_priority_9, ["shield_broken.ogg"]),#TODO
 #SW - modified cow_moo
 #("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.ogg"]),
 ("cow_moo", sf_2d|sf_priority_9|sf_vol_8, []),
 ("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["cow_slaughter.ogg"]),
 #SW - modified distant sounds
 #("distant_dog_bark", sf_2d|sf_priority_8|sf_vol_8, ["d_dog1.ogg","d_dog2.ogg","d_dog3.ogg","d_dog7.ogg"]),
 #("distant_owl", sf_2d|sf_priority_8|sf_vol_9, ["d_owl2.ogg","d_owl3.ogg","d_owl4.ogg"]),
 #("distant_chicken", sf_2d|sf_priority_8|sf_vol_8, ["d_chicken1.ogg","d_chicken2.ogg"]),
 #("distant_carpenter", sf_2d|sf_priority_8|sf_vol_3, ["d_carpenter1.ogg","d_saw_short3.ogg"]),
 #("distant_blacksmith", sf_2d|sf_priority_8|sf_vol_4, ["d_blacksmith2.ogg"]),
 ("distant_dog_bark", sf_2d|sf_priority_8|sf_vol_2, ["str_door_blast_open.ogg","str_door_blast_close_stop.ogg","str_door_blast_open_stop.ogg"]),
 ("blast_door_open", sf_2d|sf_priority_8|sf_vol_2, ["str_door_blast_open.ogg"]),
 ("blast_door_close", sf_2d|sf_priority_8|sf_vol_2, ["str_door_blast_close_stop.ogg"]),
 ("distant_owl", sf_2d|sf_priority_8|sf_vol_2, ["str_turret_pwr_on.ogg","veh_s_foil_movement.ogg"]),
 ("distant_chicken", sf_2d|sf_priority_8|sf_vol_2, ["veh_s_foil_movement.ogg","str_turret_pwr_on.ogg"]),
 ("distant_carpenter", sf_2d|sf_priority_8|sf_vol_2, ["veh_x_wing_flyby_1.ogg","veh_shuttle_powerdown.ogg"]),
 ("distant_blacksmith", sf_2d|sf_priority_8|sf_vol_2, ["veh_shuttle_powerdown.ogg","veh_x_wing_flyby_1.ogg"]), 
 
 ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.ogg"]),
 ("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.ogg"]),
 ("cantina_ambiance", sf_2d|sf_priority_8|sf_vol_9|sf_looping, ["amb_cantina_large_lp.ogg"]),
 
 #SW - new sounds
 #("blaster04",sf_priority_8|sf_vol_8, ["blaster04 _long.ogg"]), 
 ("laser_fire",sf_priority_8|sf_vol_8, ["blaster04_long.ogg"]), 
 ("bigblaster01",sf_priority_8|sf_vol_8, ["bigblaster01.ogg"]),
 ("bigblaster15_variant",sf_priority_8|sf_vol_8, ["bigblaster15_E11_variant.ogg"]),
 ("bigblaster15",sf_priority_8|sf_vol_8, ["wep_e11_blaster.ogg"]),
 ("bigblaster19",sf_priority_8|sf_vol_8, ["bigblaster19_DL44_DH17_short.ogg"]), 
 ("bigblaster22",sf_priority_8|sf_vol_8, ["rvnshn_wookie_bowcaster.ogg"]), #["bigblaster22_EE3_bowcaster_variant.ogg"]), 
 ("ionblaster",sf_priority_8|sf_vol_8, ["ionblaster_other01.ogg"]),  
 ("sonicblaster",sf_priority_8|sf_vol_10, ["rvnshn_sonic_weapon.ogg"]), #["sonicblaster_other02.ogg"]),  
 ("stunblaster",sf_priority_8|sf_vol_8, ["stunblaster_other03.ogg"]),  
 ("littleblaster",sf_priority_8|sf_vol_8, ["littleblaster01.ogg"]),   
 ("heavyrepeater",sf_priority_8|sf_vol_8, ["rvnshn_heavy_repeater.ogg"]),   
 ("stormrifle",sf_priority_8|sf_vol_8, ["rvnshn_stormrifle.ogg"]),   
 
 ("flame_fire",sf_priority_8|sf_vol_6, ["flame_fire.ogg"]),
 ("concussion_fire",sf_priority_8|sf_vol_6, ["concussion_fire.ogg"]), 
 ("rocket_fire",sf_priority_8|sf_vol_8, ["rocket_fire.ogg"]),
 ("throw_lightsaber",sf_priority_8|sf_vol_8, ["saber_throw.ogg"]),
 ("force_push",sf_priority_8|sf_vol_8, ["force_push.ogg"]), 
 ("force_lightning",sf_priority_8|sf_vol_8, ["force_lightning_01.ogg","force_lightning_02.ogg"]), 
 ("ship_noise",sf_priority_1|sf_vol_1, []), 
# ("cantina_ambience",sf_2d|sf_priority_8|sf_vol_10|sf_looping, ["mus_figrin_dan_song_1.ogg","mus_figrin_dan_song_2.ogg"]),		#using music instead
 ("bacta_injector",sf_priority_8|sf_vol_8, ["item_air_gun.ogg"]),
 ("bacta_heal",sf_priority_6|sf_vol_8, ["bacta_heal.ogg"]),
 
 #speeders
 #("speeder_noise_idle",sf_priority_6|sf_vol_9, ["speeder_noise_idle.ogg"]),
 ("speeder_noise_idle",sf_priority_9|sf_vol_9, ["speeder_noise_idle.ogg"]),		#don't use sf_2d or sf_looping
 ("speeder_noise_begin",sf_priority_9|sf_vol_9, ["speeder_noise_begin.ogg"]),		#don't use sf_2d or sf_looping
 ("speeder_noise_moving",sf_priority_6|sf_vol_9, ["speeder_noise_moving.ogg"]),	#don't use sf_2d or sf_looping
 ("speeder_noise_loop", sf_2d|sf_priority_9|sf_vol_9|sf_looping, ["speeder_noise_loop.ogg"]),

 #gonk noise
 ("gonk_noise",sf_priority_5|sf_vol_8, ["dro_gonk_voc_a.ogg","dro_gonk_voc_b.ogg","dro_gonk_voc_c.ogg","dro_gonk_voc_d.ogg"]),
 
 #("imperial_hey_you_there",sf_priority_10|sf_vol_10, ["imperial_hey_you_there.ogg"]),
 #("imperial_halt",sf_priority_10|sf_vol_10, ["imperial_halt.ogg"]),

#SW - new functionality for BSG integration
 ("viper_cannon_impact",sf_vol_6, ["Vip_Impact_Gun.ogg"]),
 ("viper_cannon",sf_vol_10, ["bigblaster01.ogg"]),
 ("cylon_cannon",sf_vol_10, ["Rdr_Cannon.ogg"]),
 ("viper_cannon_far",sf_vol_1, ["Vip_Cannon.ogg"]),
 ("cylon_cannon_far",sf_vol_2, ["Rdr_Cannon.ogg"]),
 ("viper_engine_hum",sf_vol_10, ["Vip_EngineHum_Lp.ogg"]),
 ("viper_engine_loop",sf_vol_8, ["Vip_AB_Loop.ogg"]),
 ("fighter_explode",sf_vol_10, ["s_hit_0.ogg","s_hit_1.ogg","s_hit_2.ogg"]),
 ("cannon_hit",sf_vol_2, ["SFX_Hit_Ricochet.ogg"]),
 ("subspace",sf_2d|sf_vol_6, ["subspace_left.ogg","subspace_right.ogg"]),

#Highlander begin--------------------------------------
 ("loud_explosion",sf_vol_10, ["s_hit_0.ogg","s_hit_1.ogg","s_hit_2.ogg"]),
#Highlander end--------------------------------------

#jawa sounds
("jawa_die",sf_priority_8|sf_vol_10, ["jawa_death1.ogg","jawa_death2.ogg","jawa_death3.ogg"]),
("jawa_grunt",sf_priority_6|sf_vol_8, ["jawa_chatter1.ogg","jawa_confuse1.ogg","jawa_confuse2.ogg","jawa_pushed1.ogg","jawa_pushed2.ogg","jawa_pushed3.ogg"]),
("jawa_grunt_long",sf_priority_5|sf_vol_8, ["jawa_chatter2.ogg","jawa_anger1.ogg","jawa_anger2.ogg","jawa_anger3.ogg","jawa_pushed1.ogg","jawa_pushed2.ogg","jawa_pushed3.ogg"]),
("jawa_hit",sf_priority_7|sf_vol_10, ["jawa_pain25.ogg","jawa_pain50.ogg","jawa_pain75.ogg","jawa_pain100.ogg","jawa_choke1.ogg"]),
("jawa_victory",sf_priority_5|sf_vol_10, ["jawa_victory1.ogg","jawa_victory2.ogg","jawa_victory3.ogg","jawa_pushed1.ogg","jawa_pushed2.ogg","jawa_pushed3.ogg"]),
("jawa_yell",sf_priority_6|sf_vol_10, ["jawa_anger1.ogg","jawa_anger2.ogg","jawa_anger3.ogg","jawa_pushed1.ogg","jawa_pushed2.ogg","jawa_pushed3.ogg"]),

#droid sounds
("droid_die",sf_priority_8|sf_vol_10, ["droid_pain25.ogg","droid_pain50.ogg","droid_pain75.ogg"]),
("droid_grunt",sf_priority_6|sf_vol_8, ["droid_talk01.ogg","droid_talk02.ogg","droid_talk03.ogg"]),
("droid_grunt_long",sf_priority_5|sf_vol_8, ["droid_talk01.ogg","droid_talk02.ogg","droid_talk03.ogg"]),
("droid_hit",sf_priority_7|sf_vol_10, ["droid_pain25.ogg","droid_pain50.ogg","droid_pain75.ogg"]),
("droid_victory",sf_priority_5|sf_vol_10, ["droid_talk01.ogg","droid_talk02.ogg","droid_talk03.ogg"]),
("droid_yell",sf_priority_6|sf_vol_10, ["droid_talk01.ogg","droid_talk02.ogg","droid_talk03.ogg"]),

#battledroid sounds
("battledroid_die",sf_priority_8|sf_vol_10, ["battledroid_pain25.ogg","battledroid_pain50.ogg","battledroid_pain75.ogg"]),
("battledroid_grunt",sf_priority_6|sf_vol_8, ["battledroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),
("battledroid_grunt_long",sf_priority_5|sf_vol_8, ["battledroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),
("battledroid_hit",sf_priority_7|sf_vol_10, ["battledroid_pain25.ogg","battledroid_pain50.ogg","battledroid_pain75.ogg"]),
("battledroid_victory",sf_priority_5|sf_vol_10, ["battledroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),
("battledroid_yell",sf_priority_6|sf_vol_10, ["dbattleroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),


#tusken sounds
("tusken_die",sf_priority_8|sf_vol_10, ["tusken_death1.ogg","tusken_death2.ogg","tusken_falling1.ogg","tusken_jump1.ogg"]),
("tusken_grunt",sf_priority_6|sf_vol_8, ["tusken_confuse2.ogg","tusken_confuse3.ogg","tusken_cover1.ogg","tusken_cover2.ogg","tusken_cover3.ogg"]),
("tusken_grunt_long",sf_priority_5|sf_vol_8, ["tusken_confuse1.ogg","tusken_land1.ogg","tusken_look1.ogg","tusken_look2.ogg","tusken_outflank1.ogg","tusken_outflank2.ogg"]),
("tusken_hit",sf_priority_7|sf_vol_10, ["tusken_pain25.ogg","tusken_pain50.ogg","tusken_gasp.ogg","tusken_land1.ogg"]),
("tusken_victory",sf_priority_5|sf_vol_10, ["tusken_victory1.ogg","tusken_taunt.ogg","tusken_look1.ogg","tusken_outflank1.ogg"]),
("tusken_yell",sf_priority_6|sf_vol_10, ["tusken_anger1.ogg","tusken_anger2.ogg","tusken_anger3.ogg","tusken_pushed2.ogg","tusken_pushed1.ogg"]),

#trandoshan sounds
("trandoshan_die",sf_priority_8|sf_vol_10, ["trandoshan_death1.ogg","trandoshan_death2.ogg","trandoshan_death3.ogg","trandoshan_choke1.ogg","trandoshan_choke2.ogg","trandoshan_choke3.ogg"]),
("trandoshan_grunt",sf_priority_6|sf_vol_8, ["trandoshan_confuse1.ogg","trandoshan_confuse2.ogg","trandoshan_pushed1.ogg","trandoshan_pushed2.ogg","trandoshan_pushed3.ogg"]),
("trandoshan_grunt_long",sf_priority_5|sf_vol_8, ["trandoshan_confuse3.ogg","trandoshan_sight1.ogg","trandoshan_sight2.ogg","trandoshan_sight3.ogg","trandoshan_chase1.ogg"]),
("trandoshan_hit",sf_priority_7|sf_vol_10, ["trandoshan_pain25.ogg","trandoshan_pain50.ogg","trandoshan_pain75.ogg","trandoshan_pain100.ogg","trandoshan_gasp.ogg"]),
("trandoshan_victory",sf_priority_5|sf_vol_10, ["trandoshan_victory1.ogg","trandoshan_victory2.ogg","trandoshan_victory3.ogg","trandoshan_taunt.ogg","trandoshan_look1.ogg","trandoshan_look2.ogg","trandoshan_chase2.ogg","trandoshan_chase3.ogg"]),
("trandoshan_yell",sf_priority_6|sf_vol_10, ["trandoshan_anger1.ogg","trandoshan_anger2.ogg","trandoshan_anger3.ogg","trandoshan_taunt.ogg","trandoshan_look1.ogg"]),

#wookiee sounds
("wookiee_die",sf_priority_8|sf_vol_10, ["wookiee_death1.ogg","wookiee_death2.ogg","wookiee_death3.ogg","wookiee_falling1.ogg"]),
("wookiee_grunt",sf_priority_6|sf_vol_8, ["wookiee_pushed1.ogg","wookiee_pushed2.ogg","wookiee_pushed3.ogg","wookiee_jump1.ogg","wookiee_land1.ogg"]),
("wookiee_grunt_long",sf_priority_5|sf_vol_8, ["wookiee_ffwarn.ogg","wookiee_pushed1.ogg","wookiee_pushed2.ogg","wookiee_pushed3.ogg"]),
("wookiee_hit",sf_priority_7|sf_vol_10, ["wookiee_pain25.ogg","wookiee_pain50.ogg","wookiee_pain75.ogg","wookiee_pain100.ogg","wookiee_jump1.ogg","wookiee_land1.ogg"]),
("wookiee_victory",sf_priority_5|sf_vol_10, ["wookiee_victory1.ogg","wookiee_victory2.ogg","wookiee_victory3.ogg","wookiee_taunt1.ogg"]),
("wookiee_yell",sf_priority_6|sf_vol_10, ["wookiee_victory1.ogg","wookiee_victory2.ogg","wookiee_victory3.ogg","wookiee_taunt1.ogg","wookiee_ffwarn.ogg"]),

#gamorrean sounds
("gamorrean_die",sf_priority_8|sf_vol_10, ["gamorrean_death1.ogg","gamorrean_death2.ogg","gamorrean_death3.ogg","gamorrean_falling1.ogg"]),
("gamorrean_grunt",sf_priority_6|sf_vol_8, ["gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg","gamorrean_anger2.ogg"]),
("gamorrean_grunt_long",sf_priority_5|sf_vol_8, ["gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg","gamorrean_anger2.ogg"]),
("gamorrean_hit",sf_priority_7|sf_vol_10, ["gamorrean_pain25.ogg","gamorrean_pain50.ogg","gamorrean_pain75.ogg","gamorrean_pain100.ogg","gamorrean_gasp.ogg","gamorrean_land1.ogg"]),
("gamorrean_victory",sf_priority_5|sf_vol_10, ["gamorrean_victory1.ogg","gamorrean_anger2.ogg","gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg"]),
("gamorrean_yell",sf_priority_6|sf_vol_10, ["gamorrean_anger2.ogg","gamorrean_victory1.ogg","gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg"]),

#rodian sounds
("rodian_die",sf_priority_8|sf_vol_10, ["rodian_death1.ogg","rodian_death2.ogg","rodian_death3.ogg","rodian_choke1.ogg","rodian_choke2.ogg","rodian_choke3.ogg"]),
("rodian_grunt",sf_priority_6|sf_vol_8, ["rodian_pushed1.ogg","rodian_pushed2.ogg","rodian_pushed3.ogg","rodian_gasp.ogg","rodian_land1.ogg","rodian_sound2.ogg"]),
("rodian_grunt_long",sf_priority_5|sf_vol_8, ["rodian_confuse1.ogg","rodian_confuse2.ogg","rodian_confuse3.ogg","rodian_jump1.ogg","rodian_sound2.ogg"]),
("rodian_hit",sf_priority_7|sf_vol_10, ["rodian_pain25.ogg","rodian_pain50.ogg","rodian_pain75.ogg","rodian_pain100.ogg","rodian_pushed1.ogg","rodian_pushed2.ogg","rodian_pushed3.ogg"]),
("rodian_victory",sf_priority_5|sf_vol_10, ["rodian_victory1.ogg","rodian_victory2.ogg","rodian_victory3.ogg","rodian_cover1.ogg","rodian_cover2.ogg","rodian_cover3.ogg"]),
("rodian_yell",sf_priority_6|sf_vol_10, ["rodian_anger1.ogg","rodian_anger2.ogg","rodian_anger3.ogg","rodian_cover1.ogg","rodian_cover2.ogg","rodian_cover3.ogg"]),

#geonosian sounds
("geonosian_die",sf_priority_8|sf_vol_10, ["geonosian_death.ogg"]),
("geonosian_grunt",sf_priority_6|sf_vol_8, ["geonosian1.ogg","geonosian2.ogg","geonosian3.ogg","geonosian4.ogg"]),
("geonosian_grunt_long",sf_priority_5|sf_vol_8, ["geonosian1.ogg","geonosian2.ogg","geonosian3.ogg","geonosian4.ogg"]),
("geonosian_hit",sf_priority_7|sf_vol_10, ["geonosian1.ogg","geonosian2.ogg","geonosian3.ogg","geonosian4.ogg"]),
("geonosian_victory",sf_priority_5|sf_vol_10, ["geonosian1.ogg","geonosian2.ogg","geonosian3.ogg","geonosian4.ogg"]),
("geonosian_yell",sf_priority_6|sf_vol_10, ["geonosian1.ogg","geonosian2.ogg","geonosian3.ogg","geonosian4.ogg"]),

#sullustan sounds - used man sounds for die, grunt, grunt_long, and hit
#("sullustan_die",sf_priority_8|sf_vol_10, []),
#("sullustan_grunt",sf_priority_6|sf_vol_4, []),
#("sullustan_grunt_long",sf_priority_5|sf_vol_8, []),
#("sullustan_hit",sf_priority_7|sf_vol_10, []),
("sullustan_victory",sf_priority_5|sf_vol_10, ["sullustan_victory1.ogg","sullustan_victory2.ogg","sullustan_victory3.ogg","sullustan_victory4.ogg"]),
("sullustan_yell",sf_priority_6|sf_vol_10, ["sullustan_yell1.ogg","sullustan_yell2.ogg","sullustan_yell3.ogg","sullustan_yell4.ogg"]),

#twilek_female sounds - used female sounds for die, grunt, grunt_long, and hit
# ("twilek_female_die",sf_priority_8|sf_vol_10, []),
# ("twilek_female_grunt",sf_priority_6|sf_vol_4, []),
# ("twilek_female_grunt_long",sf_priority_5|sf_vol_8, []),
# ("twilek_female_hit",sf_priority_7|sf_vol_10, []),
("twilek_female_victory",sf_priority_5|sf_vol_10, ["twilek_female_sound1.ogg","twilek_female_sound2.ogg","twilek_female_sound4.ogg","twilek_female_sound4.ogg"]),
("twilek_female_yell",sf_priority_6|sf_vol_10, ["twilek_female_sound2.ogg","twilek_female_sound4.ogg","twilek_female_sound4.ogg"]),

#special weapons
#("lightsaber_idle",sf_vol_10, ["Vip_AB_Loop.ogg"]),
#("lightsaber_swing",sf_priority_10|sf_vol_6,["saber_swing1.ogg","saber_swing2.ogg","saber_swing3.ogg","saber_swing4.ogg","saber_swing5.ogg","saber_swing6.ogg","saber_swing7.ogg","saber_swing8.ogg",]),
#removed saber_swing7.ogg & saber_swing8.ogg since they were 1.4 seconds until the usually 0.5 - 0.9 seconds
("lightsaber_swing",sf_priority_10|sf_vol_6,["saber_swing1.ogg","saber_swing2.ogg","saber_swing3.ogg","saber_swing4.ogg","saber_swing5.ogg","saber_swing6.ogg"]),
("deflector_shield",sf_priority_5|sf_vol_3|sf_looping, ["deflector_shield.ogg"]),
("deflector_shield_hit",sf_priority_1|sf_vol_10, ["deflector_shield_hit.ogg"]),
#Added by Swyter, Revan Shan suggestion
("e5",sf_priority_5|sf_vol_6,["E5-blaster.ogg"]),
("dh17",sf_priority_5|sf_vol_6,["rvnshn_DH17.ogg"]),
("westar",sf_priority_5|sf_vol_6,["rvnshn_westar.ogg"]),

("vader_breath",sf_priority_1|sf_vol_6|sf_looping, ["vader_breath.ogg"]),

#New Hangar Sounds by Revan Shan
("swc_hangar_siren", sf_vol_4|sf_priority_3|sf_looping,["swc_hangar_siren.ogg"]),
("swc_hangar_hutt", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_hutt.ogg"]),
("swc_hangar_imperial", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_imperial.ogg"]),
("swc_hangar_mandalorian", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_mandalorian.ogg"]),
("swc_hangar_neutral", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_neutral.ogg"]),
("swc_hangar_rebel", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_rebel.ogg"]),
("swc_hangar_sith", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_sith.ogg"]),
("swc_hangar_wookie", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_wookie.ogg"]),
("swc_hangar_clones", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_clones.ogg"]),
("swc_hangar_trandoshan", sf_vol_10|sf_priority_1|sf_2d,["swc_hangar_trandoshan.ogg"]),


#@> SWY - New battle sounds by Revan Shan

## REVAN SHAN'S NEUTRAL BATTLE SPEECH
("swc_neutral_death", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_death_1.ogg","swc_neutral_death_2.ogg","swc_neutral_death_3.ogg"]),
("swc_neutral_deployed", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_deployed_1.ogg","swc_neutral_deployed_2.ogg","swc_neutral_deployed_3.ogg"]),
("swc_neutral_victory", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_victory_1.ogg","swc_neutral_victory_2.ogg"]),

("swc_neutral_fired", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_fired_1.ogg","swc_neutral_fired_2.ogg"]),
("swc_neutral_player25", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_player25_1.ogg","swc_neutral_player25_2.ogg"]),
("swc_neutral_player50", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_player50_1.ogg","swc_neutral_player50_2.ogg"]),
("swc_neutral_enemy25", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_enemy25_1.ogg"]),
("swc_neutral_enemy50", sf_vol_10|sf_priority_1|sf_2d,["swc_neutral_enemy50_1.ogg","swc_neutral_enemy50_2.ogg","swc_neutral_enemy50_3.ogg"]),

## REVAN SHAN'S EMPIRE BATTLE SPEECH
("swc_empire_death", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_death_1.ogg","swc_empire_death_2.ogg","swc_empire_death_3.ogg"]),
("swc_empire_deployed", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_deployed_1.ogg","swc_empire_deployed_2.ogg","swc_empire_deployed_3.ogg","swc_empire_deployed_4.ogg"]),
("swc_empire_victory", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_victory_1.ogg","swc_empire_victory_2.ogg","swc_empire_victory_3.ogg"]),

("swc_empire_fired", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_fired_1.ogg"]),
("swc_empire_player25", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_player25_1.ogg","swc_empire_player25_2.ogg","swc_empire_player25_3.ogg"]),
("swc_empire_player50", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_player50_1.ogg","swc_empire_player50_2.ogg"]),
("swc_empire_enemy25", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_enemy25_1.ogg"]),
("swc_empire_enemy50", sf_vol_10|sf_priority_1|sf_2d,["swc_empire_enemy50_1.ogg","swc_empire_enemy50_2.ogg","swc_empire_enemy50_3.ogg"]),

## REVAN SHAN'S REBEL BATTLE SPEECH
("swc_rebel_death", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_death_1.ogg","swc_rebel_death_2.ogg","swc_rebel_death_3.ogg"]),
("swc_rebel_deployed", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_deployed_1.ogg","swc_rebel_deployed_2.ogg","swc_rebel_deployed_3.ogg"]),
("swc_rebel_victory", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_victory_1.ogg","swc_rebel_victory_2.ogg","swc_rebel_victory_3.ogg"]),

("swc_rebel_fired", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_fired_1.ogg","swc_rebel_fired_2.ogg"]),
("swc_rebel_player25", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_player25_1.ogg","swc_rebel_player25_2.ogg"]),
("swc_rebel_player50", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_player50_1.ogg","swc_rebel_player50_2.ogg"]),
("swc_rebel_enemy25", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_enemy25_1.ogg"]),
("swc_rebel_enemy50", sf_vol_10|sf_priority_1|sf_2d,["swc_rebel_enemy50_1.ogg","swc_rebel_enemy50_2.ogg","swc_rebel_enemy50_3.ogg"]),

## REVAN SHAN'S HUTT BATTLE SPEECH
("swc_hutt_death", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_death_1.ogg","swc_hutt_death_2.ogg","swc_hutt_death_3.ogg"]),
("swc_hutt_deployed", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_deployed_1.ogg","swc_hutt_deployed_2.ogg","swc_hutt_deployed_3.ogg"]),
("swc_hutt_victory", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_victory_1.ogg","swc_hutt_victory_2.ogg","swc_hutt_victory_3.ogg"]),

("swc_hutt_fired", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_fired_1.ogg","swc_hutt_fired_2.ogg"]),
("swc_hutt_player25", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_player25_1.ogg","swc_hutt_player25_2.ogg"]),
("swc_hutt_player50", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_player50_1.ogg","swc_hutt_player50_2.ogg"]),
("swc_hutt_enemy25", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_enemy25_1.ogg","swc_hutt_enemy25_2.ogg"]),
("swc_hutt_enemy50", sf_vol_10|sf_priority_1|sf_2d,["swc_hutt_enemy50_1.ogg"]),
]
