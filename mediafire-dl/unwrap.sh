#!/usr/bin/bash

trap c INT

c () {
    echo "\nAborted!"
    exit 1
}

fin="0.py"
echo -n "Processing"
while true; do
    rg -q 'exec\(marshal' $fin
    if [ "$?" == "0" ]; then
        echo -n "."
        sed -i 's/exec(/import sys,uncompyle6\nuncompyle6.main.decompile(3.7,/' $fin
        sed -i 's/))/),sys.stdout)/' $fin
        python3 $fin > tmp && mv -f tmp $fin
    else
        break
    fi
done
echo -e "\nAll done!"
