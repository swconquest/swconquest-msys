rem @> hi there! I'm pretty honored to see you here,
rem    please feel free to copy anything. -Greetings from Swyter
rem    -------------------------------------------------------------

@echo off
SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION
MODE CON: COLS=40 LINES=40
rem MODE CON: COLS=130 LINES=40

cls && title Building your Module - Please wait...  ^|  By TaleWorlds ^+ Swyter&& color 71

rem rem SET SWYCD="%CD:&=^&%"
rem SET SWYCDB=!SWYCD!
rem echo %SWYCD%
rem echo %CD:&=^&% --
rem echo %CD:&=^&% --

rem echo variable1: "!SWYCD!"
rem echo variable1: "!SWYCDB!"

set CD="!CD!"

rem echo cool: !CD:~1,-1!
rem echo cook: !CD:&=^&!

if %PROCESSOR_ARCHITECTURE%==x86 (
 set SWYPYTHON_var=32bits
) ELSE (
 set SWYPYTHON_var=64bits
)

set PATH=%PATH%;!CD:~1,-1!\Python\%SWYPYTHON_var%
set PYTHONPATH=%PYTHONPATH%;!CD:~1,-1!\IDs;!CD:~1,-1!\Headers;!CD:~1,-1!\Process;!CD:~1,-1!\Extras;!CD:~1,-1!

rem echo Path: "%path%"--
rem echo Pythonpath: "%pythonpath%"--

echo Correcting scripts indentation...
python.exe Process/process_line_correction.py
python.exe Process/process_init.py
python.exe Process/process_global_variables.py
python.exe Process/process_strings.py
python.exe Process/process_skills.py
python.exe Process/process_music.py
python.exe Process/process_animations.py
python.exe Process/process_meshes.py
python.exe Process/process_sounds.py
python.exe Process/process_skins.py
python.exe Process/process_map_icons.py
python.exe Process/process_factions.py
python.exe Process/process_items.py
python.exe Process/process_scenes.py
python.exe Process/process_troops.py
python.exe Process/process_particle_sys.py
python.exe Process/process_scene_props.py
python.exe Process/process_tableau_materials.py
python.exe Process/process_presentations.py
python.exe Process/process_party_tmps.py
python.exe Process/process_parties.py
python.exe Process/process_quests.py
python.exe Process/process_scripts.py
python.exe Process/process_mission_tmps.py
python.exe Process/process_game_menus.py
python.exe Process/process_simple_triggers.py
python.exe Process/process_dialogs.py
python.exe Process/process_global_variables_unused.py
python.exe Process/process_tags_unused.py
@del *.pyc > nul && del .\Headers\*.pyc > nul && del .\IDs\*.pyc > nul && del .\Process\*.pyc > nul
title Building your Module - Done  ^|  By TaleWorlds ^+ Swyter
echo.
echo ______________________________
echo.
echo Script Process/processing has ended.
echo Press any key to exit. . .
pause>nul