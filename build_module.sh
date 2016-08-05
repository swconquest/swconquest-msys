#!/bin/bash

#swy-- this does nothing, just ignore any `title whateverstring` calls from the msys
title() { true; }; export -f title

#swy-- set the ModuleSystem folder as the current directory ($PWD)
cd "$(dirname "$0")" || exit

title 'building tld for [wait for it]--'
PYTHONPATH="$PWD:$PWD/Data:$PWD/Header:$PWD/ID:$PWD/Process::$PWD/Extras"; export PYTHONPATH

clear

python()
{
    test -e /usr/bin/python2 && python2 "$@" || python "$@"
}

python -B -OO ./Process/process__swybuildmix.py
python -B -OO ./Process/process__swybuildmixb.py
python -B -OO ./Process/process__swybuildmixc.py

#
# convert to MS-DOS/Windows newline format (swyter)
# needs this: http://linux.maruhn.com/sec/flip.html
#

if [ -e /usr/bin/flipaa ]; then
    flip -d ID/*.py
    flip -d ../*.txt
    flip -d ../_wb/*.txt
    flip -d  ./*.txt
    flip -u ../_wb/_tweaks_done_to_the_existing_res_tree.txt
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

msys_check ID/ID_items.py 'item' 915

#
# count map_icons... (mtarini)
#

msys_check ID/ID_map_icons.py ' map' 256


echo ______________________________
echo ''
echo Script processing has ended.
echo Press any key to restart. . .

