#!/bin/bash
 
### unitTest.sh ###

# This function loads the environment variables and functions once
function oneTimeSetUp() {
	source ../buildconfig.conf
	source ../functions.sh 

	# Remove the app folder to enforce a clean environment.
	pushd ../
	rm -rf app
	popd

	# Remove the build dist and .packges folder. to enforce package downloads and updates.
	pushd $PY4APATH
	rm -rf build
	rm -rf dist
	rm -rf .packages
	popd
}

function testAnontunnelDirectoryExistTrue() {
	checkDirectoryExist > /dev/null 2>&1
	assertEquals 0 $?
}

function testImageExistTrue() {
	checkImagesExist > /dev/null 2>&1
	assertEquals 0 $?
}

function testDirectoriesMissingTrue() {
	DIRECTORYMISSING=0
	if [ ! -e "${CURRENTFOLDERPATH}/app" ]; then
		DIRECTORYMISSING=1
	fi

	assertFalse $DIRECTORYMISSING
	
	DIRECTORYMISSING=0
	if [ ! -e "${CURRENTFOLDERPATH}/app/service" ]; then
		DIRECTORYMISSING=1
	fi

	assertFalse $DIRECTORYMISSING
}

function testDirectoriesMissingFalse() {
	generateFolders > /dev/null 2>&1
	DIRECTORYMISSING=1
	if [ ! -e "${CURRENTFOLDERPATH}/app" ]; then
		DIRECTORYMISSING=0
	fi

	assertFalse $DIRECTORYMISSING
	
	DIRECTORYMISSING=1
	if [ ! -e "${CURRENTFOLDERPATH}/app/service" ]; then
		DIRECTORYMISSING=0
	fi

	assertFalse $DIRECTORYMISSING
}

function testMainExistFail() {
	MAINEXIST=0
	if [ ! -f "${CURRENTFOLDERPATH}/app/main.py" ]; then
		MAINEXIST=1
	fi

	assertFalse $MAINEXIST
}

function testKivyFileExistFail() {
	KIVYEXIST=0
	if [ ! -f "${CURRENTFOLDERPATH}/app/anontunnel.kv" ]; then
		KIVYEXIST=1
	fi

	assertFalse $KIVYEXIST
}

function serviceMainexistFail() {
	SERVICEMAINEXIST=0;
	if [ ! -f "${CURRENTFOLDERPATH}/app/service/main.py" ]; then
		SERVICEMAINEXIST=1
	fi
	
	assertFalse $SERVICEMAINEXIST
}

function testMainExistTrue() {
	# Run the function that copies the files from the anontunnel folder
	checkAppFiles > /dev/null 2>&1
	MAINEXIST=0
	if [ ! -f "${CURRENTFOLDERPATH}/app/main.py" ]; then
		MAINEXIST=1
	fi

	assertTrue $MAINEXIST
}

function testKivyFileExistTrue() {
	KIVYEXIST=0
	if [ ! -f "${CURRENTFOLDERPATH}/app/anontunnel.kv" ]; then
		KIVYEXIST=1
	fi

	assertTrue $KIVYEXIST
}

function serviceMainexistTrue() {
	SERVICEMAINEXIST=0;
	if [ ! -f "${CURRENTFOLDERPATH}/app/service/main.py" ]; then
		SERVICEMAINEXIST=1
	fi
	
	assertTrue $SERVICEMAINEXIST
}

function testBuildWorking() {
	pushd ../
	./build.sh -p $PY4APATH > /dev/null
	popd
	assertEquals 0 $?
}

# Call and Run all Tests
. "../shunit2-2.1.6/src/shunit2"
