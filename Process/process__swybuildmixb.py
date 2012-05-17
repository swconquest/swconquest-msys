from time import time
import sys
start = time()
G = ""

def handler():
  global G
  exc_type, exc_value, exc_traceback = sys.exc_info()
  if str(G)!=str(exc_value):
    print("!({0})".format(exc_value))
  G=exc_value
    
try:
 import process_items
except NameError:
 handler()

try:
 import process_scenes
except NameError:
 handler()

try:
 import process_troops
except NameError:
 handler()

try:
 import process_particle_sys
except NameError:
 handler()

try:
 import process_scene_props
except NameError:
 handler()

try:
 import process_tableau_materials
except NameError:
 handler()

try:
 import process_presentations
except NameError:
 handler()

try:
 import process_party_tmps
except NameError:
 handler()

try:
 import process_parties
except NameError:
 handler()

try:
 import process_quests
except NameError:
 handler()
 
# don't ask me why, but there's a sort of variable overwrite in process_scripts that corrupts some objects...
# it goes nuts and starts throwing warnings about "unable to find anim_***" that's why we have to divide the processing in two separate python batches. :/

# import process_scripts
# import process_mission_tmps
# import process_game_menus
# import process_simple_triggers
# import process_dialogs
# import process_global_variables_unused
# import process_postfx

print("It took %ss"%(time()-start))