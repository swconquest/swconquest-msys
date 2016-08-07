#!/bin/bash

#swy-- this does nothing, just ignore any `title whateverstring` calls from the msys
title() { true; }; export -f title

#swy-- set the ModuleSystem folder as the current directory ($PWD)
cd "$(dirname "$0")" || exit

title 'building tld for [wait for it]--'
PYTHONPATH="$PWD:$PWD/Data:$PWD/Header:$PWD/IDs:$PWD/Process::$PWD/Extras"; export PYTHONPATH

clear

python()
{
    test -e /usr/bin/python2 && python2 "$@" || python "$@"
}

#python -B -OO ./Process/process__swybuildmix.py
#python -B -OO ./Process/process__swybuildmixb.py
#python -B -OO ./Process/process__swybuildmixc.py

python -B -OO ./Process/process_init.py
python -B -OO ./Process/process_global_variables.py
python -B -OO ./Process/process_strings.py
python -B -OO ./Process/process_skills.py
python -B -OO ./Process/process_music.py
python -B -OO ./Process/process_animations.py
python -B -OO ./Process/process_meshes.py
python -B -OO ./Process/process_sounds.py
python -B -OO ./Process/process_skins.py
python -B -OO ./Process/process_map_icons.py
python -B -OO ./Process/process_factions.py
python -B -OO ./Process/process_items.py
python -B -OO ./Process/process_scenes.py
python -B -OO ./Process/process_troops.py
python -B -OO ./Process/process_particle_sys.py
python -B -OO ./Process/process_scene_props.py
python -B -OO ./Process/process_tableau_materials.py
python -B -OO ./Process/process_presentations.py
python -B -OO ./Process/process_party_tmps.py
python -B -OO ./Process/process_parties.py
python -B -OO ./Process/process_quests.py
python -B -OO ./Process/process_info_pages.py # <-- just for wb
python -B -OO ./Process/process_scripts.py
python -B -OO ./Process/process_mission_tmps.py
python -B -OO ./Process/process_game_menus.py
python -B -OO ./Process/process_simple_triggers.py
python -B -OO ./Process/process_dialogs.py
python -B -OO ./Process/process_postfx.py     # <-- just for wb
python -B -OO ./Process/process_global_variables_unused.py

#
# convert to MS-DOS/Windows newline format (swyter)
# needs this: http://linux.maruhn.com/sec/flip.html
#

if [ -e /usr/bin/flip ]; then
    flip -d IDs/*.py
    flip -d   ./*.txt
    flip -d  ../swconquest/_wb/*.txt
    flip -d  ../swconquest/*.txt
    flip -u  ../swconquest/_wb/_wb_porting_notes.txt
fi

# --

msys_check()
{
    cnt=$((`cat "${1}" | wc -l` - 1))
    max=${3}

    echo -en "${2} count: $cnt/$max ... "

    if [ ${cnt} -lt "${max}" ]; then
        echo 'ok.'
    else
        echo 'ERROR ERROR ERROR TOO MANY!!!.'
    fi
}

#
# count objects... (mtarini)
#

msys_check IDs/ID_items.py 'item' 915

#
# count map_icons... (mtarini)
#

msys_check IDs/ID_map_icons.py ' map' 256


echo ______________________________
echo ''
echo Script processing has ended.
echo Press any key to restart. . .

