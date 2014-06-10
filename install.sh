#!/bin/bash
source configuration
adb uninstall org.tribler.at3.${APPNAME}
adb install app/AT3${APPNAME}-1.0-debug.apk
