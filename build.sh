#!/bin/bash
# Copyright (c) Rolf Jagerman, Laurens Versluis and Martijn de Vos, 2014.
# This script first checks if certain folders and files exist. It first builds kivy and then the whole app (after kivy is set) because of some error with binaries.
# The main and build functions should be reviewed first.

# Variables
CURRENTFOLDERPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMAGEFOLDER="anontunnel/images"
APPLOGO="tribler_applogo.png"
APPSPLASH="splash.jpg"
APPLOGOPATH="${CURRENTFOLDERPATH}/${IMAGEFOLDER}/${APPLOGO}"
APPSPLASHPATH="${CURRENTFOLDERPATH}/${IMAGEFOLDER}/${APPSPLASH}"
DIRNAME="AT3"
PY4APATH=

# Chat colors
red="\x1B[0;31m"
yellow="\x1B[1;33m"
green="\x1B[0;32m"
NC="\x1B[0m" # No Color

while getopts ":p:" opt; do
	case $opt in
		p)
			PY4APATH=$OPTARG
			;;
	esac
done

if [ "X$PY4APATH" == "X" ]; then
	echo -e "${yellow}༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽_•︻̷̿┻̿═━一༼ຈل͜ຈ༽ give the path of python-for-android using the -p flag or the donger dies${NC}"
	exit 1
fi

function checkDirectoryExist() {
	# If the folders do not exist, we try to create them and throw an error.
	if [ ! -e "${CURRENTFOLDERPATH}/anontunnel/" -o ! -e "${CURRENTFOLDERPATH}/${IMAGEFOLDER}" ]; then
		# Throw an error since folders are missing
		echo -e "${red}You need to have a folder ${CURRENTFOLDERPATH}/${IMAGEFOLDER} aborting.${NC}"
		echo -e "${red}The missing folders will be made now, but images will be missing!${NC}"
		mkdir -p "./${IMAGEFOLDER}"
		exit 1
	fi
}

function checkImagesExist() {
	# Check if the app icon isn't missing
	if [ ! -f $APPLOGOPATH ]; then
		echo -e "${red}${APPLOGOPATH} is missing! Aborting.${NC}"
		exit 1
	fi

	# Check if the splashscreen isn't missing
	if [ ! -f $APPSPLASHPATH ]; then
		echo -e "${red}${APPSPLASHPATH} is missing! Aborting.${NC}"
		exit 1
	fi
}

function generateFolders() {
	# If the app folder in AT3 does not exist, create it.
	if [ ! -e "${CURRENTFOLDERPATH}/app" ]; then
		echo -e "${red}${CURRENTFOLDERPATH}/app does not exist! Attempting to create it${NC}"
		mkdir -p "${CURRENTFOLDERPATH}/app"
	fi

	# If the app/service folder does not exist, create it
	if [ ! -e "${CURRENTFOLDERPATH}/app/service" ]; then
		echo -e "${red}${CURRENTFOLDERPATH}/app/service folder is missing, attempting to create it..${NC}"
		mkdir -p "${CURRENTFOLDERPATH}/app/service"
	fi
}

function checkAppFiles() {
	# If the app folder does not contain the main.py file, copy it from the anontunnel folder
	if [ ! -f "${CURRENTFOLDERPATH}/app/main.py" ]; then
		echo -e "${red}${CURRENTFOLDERPATH}/app/main.py is missing, copying from anontunnel${NC}"
		cp "${CURRENTFOLDERPATH}/anontunnel/main.py" "${CURRENTFOLDERPATH}/app/main.py"
	fi

	# If the app folder does not contain the anontunnel.kv, copy it from the anontunnel folder
	if [ ! -f "${CURRENTFOLDERPATH}/app/anontunnel.kv" ]; then
		echo -e "${red}${CURRENTFOLDERPATH}/app/anontunnel.kv is missing, copying from anontunnel${NC}"
		cp "${CURRENTFOLDERPATH}/anontunnel/anontunnel.kv" "${CURRENTFOLDERPATH}/app/anontunnel.kv"
	fi


	# If the app/service folder does not contain the main.py file, copy it from the anontunnel/service folder
	if [ ! -f "${CURRENTFOLDERPATH}/app/service/main.py" ]; then
		echo -e "${red}${CURRENTFOLDERPATH}/app/service/main,py is missing, copying from anontunnel/service${NC}"
		cp "${CURRENTFOLDERPATH}/anontunnel/service/main.py" "${CURRENTFOLDERPATH}/app/service/main.py"
	fi
}

function checkDistFolderExist() {
	# Check if destination exist
	if [ -e "${PY4APATH}/dist/${DIRNAME}" ]; then
		echo -e "${red}The distribution ${PY4APATH}/dist/${DIRNAME} already exist${NC}"
		echo -e "${red}Press a key to remove it, or Control + C to abort.${NC}"
		read
		rm -rf "${PY4APATH}/dist/${DIRNAME}"
	fi
}

function build() {
	# Build kivy first
	pushd $PY4APATH
	./distribute.sh -m "kivy" -d $DIRNAME
	popd

	# Remove the created directory 
	rm -rf "${PY4APATH}/dist/${DIRNAME}"

	# Build a distribute folder with all the packages now that kivy has been set
	pushd $PY4APATH
	./distribute.sh -m "kivy openssl pycrypto m2crypto twisted sqlite3 pyasn1 tribler netifaces" -d $DIRNAME
	popd

	cd "${PY4APATH}/dist/${DIRNAME}/"

	./build.py --package com.AT3.anontunnel --name "AT3 Anontunnels" --version 1.0 --dir "${CURRENTFOLDERPATH}/app" debug --permission INTERNET --icon $APPLOGOPATH --presplash $APPSPLASHPATH

	# Copy the .apk files to our own app folder
	find "${PY4APATH}/dist/${DIRNAME}/bin" -type f -name '*.apk' -exec cp {} "${CURRENTFOLDERPATH}/app" \;

	# Delete the distribute and build now that the app has been made in the AT3 folder
	#rm -rf "${PY4APATH}/dist/${DIRNAME}"

	echo -e "${green}All done!${NC}"
}

# This functions first runs checks on wheter certain files and folders exist.
# If they do and all passes, the build function is run.
function main() {
	checkDirectoryExist &&
	checkImagesExist &&
	generateFolders &&
	checkAppFiles &&
	checkDistFolderExist &&
	build
}

# Call the main method.
main