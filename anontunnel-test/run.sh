#!/bin/bash

RUNS=500
APKLOCATION=/home/martijn/Documenten/python-for-android/dist/Test/bin/anontunneltest-1.0-debug.apk
PACKAGENAME=org.tribler.at3.anontunneltest
ACTIVITYNAME=org.renpy.android.PythonActivity
PIDCATLOCATION=/home/martijn/Documenten/AT3/pidcat/pidcat.py

for i in $(seq 2 $RUNS)
do
	# start the application
	adb uninstall $PACKAGENAME
	adb install $APKLOCATION
	adb shell am start -n $PACKAGENAME/$ACTIVITYNAME

	# start pidcat
	FILENAME=`date +"%H%M%m%d%Y"`
	python $PIDCATLOCATION $PACKAGENAME > "$FILENAME.log"

	# check if the application still exists
	while :
	do
		OUT=`adb shell ps | grep org.tribler.at3.anontunneltest | awk '{print $9}'`
		if [ "X$OUT" == "X" ]; then
			pkill -f pidcat
			break
		fi
		sleep 5
	done
done
