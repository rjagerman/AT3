#!/bin/bash
# Copyright (c) Rolf Jagerman, Laurens Versluis and Martijn de Vos, 2014.
# This defines all the functions needed for the build.sh script.
# As this script will be tested, functions are separated from the build.sh

red="\x1B[0;31m"
yellow="\x1B[0;33m"
green="\x1B[0;32m"
blue="\x1B[0;34m"
NC="\x1B[0m"
logfile="${CURRENTFOLDERPATH}/build.log"

function error() {
	echo -e "${red}$@${NC}"
}

function warning() {
	echo -e "${yellow}$@${NC}"
}

function info() {
	echo -e "${blue}$@${NC}"
}

function try () {
    "$@"
    if [ ! $? -eq 0 ] ; then
    	error "Failure while running:"
    	echo -e "$@"
    	error "See ${logfile} for more details"
    	exit 1
    fi
}

function checkDirectoryExist() {
	# If the specified app folder does not exist, we throw an error.
	if [ ! -e "${CURRENTFOLDERPATH}/${APPNAME}/" ]; then
		# Throw an error since folders are missing
		error "You need to have a folder ${CURRENTFOLDERPATH}/${APPNAME}/, aborting."
		exit 1
	fi
}

function generateFolders() {
	# If the app folder in AT3 does not exist, create it.
	if [ ! -e "${CURRENTFOLDERPATH}/app" ]; then
		warning "${CURRENTFOLDERPATH}/app does not exist! Attempting to create it"
		try mkdir -p "${CURRENTFOLDERPATH}/app"
	fi
}

function checkDistFolderExist() {
	# Check if destination exist
	if [ -e "${PY4APATH}/dist/${DIRNAME}" ]; then
		error "The distribution ${PY4APATH}/dist/${DIRNAME} already exist"
		error "Press a key to remove it, or Control + C to abort."
		read
		try rm -rf "${PY4APATH}/dist/${DIRNAME}"
	fi
}

function setSplash() {
	# Sets the splash screen if it exists	
	if [ -f "${CURRENTFOLDERPATH}/${APPNAME}/${APPSPLASH}" ]; then
		APPSPLASHFLAG="--presplash ${CURRENTFOLDERPATH}/${APPNAME}/${APPSPLASH}"
	fi
}

function setIcon() {
	# Sets the icon if it exists
	if [ -f "${CURRENTFOLDERPATH}/${APPNAME}/${APPSPLASH}" ]; then
		APPICONFLAG="--icon ${CURRENTFOLDERPATH}/${APPNAME}/${APPICON}"
	fi
}


function build() {
	# Build a distribute folder with all the packages now that kivy has been set
	info "Building a python-for-android distribution"
	PREVPATH=`pwd`
	cd $PY4APATH
	try ./distribute.sh -m "`cat ${CURRENTFOLDERPATH}/${APPNAME}/python-for-android.deps`" -d $DIRNAME &> $logfile
	cd $PREVPATH

	# Build the .apk
	cd "${PY4APATH}/dist/${DIRNAME}/"
	info "Building the APK"
	try ./build.py --package org.tribler.at3.${APPNAME} --name "AT3 ${APPNAME}" --version 1.0 --dir "${CURRENTFOLDERPATH}/${APPNAME}" debug --permission INTERNET $APPICONFLAG $APPSPLASHFLAG &> $logfile

	# Copy the .apk files to our own app folder
	info "Copying the APK"
	try find "${PY4APATH}/dist/${DIRNAME}/bin" -type f -name '*.apk' -exec cp {} "${CURRENTFOLDERPATH}/app" \; &> $logfile

	# Delete the distribute and build now that the app has been made in the AT3 folder
	#rm -rf "${PY4APATH}/dist/${DIRNAME}"

	echo -e "${green}All done!${NC}"
}

# This functions first runs checks on wheter certain files and folders exist.
# If they do and all passes, the build function is run.
function main() {
	try checkDirectoryExist
	try checkDistFolderExist &&
	try setSplash &&
	try setIcon &&
	try generateFolders &&
	try build
}
