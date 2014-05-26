#!/bin/bash
 
### unitTest.sh ###

PREVPATH=/
function pushd() {
	PREVPATH=`pwd`
	cd $1
}

function popd() {
	cd $PREVPATH
}

# This function loads the environment variables and functions once
function oneTimeSetUp() {
	source ../configuration
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

function testCurrentfolderpathNotEmpty() {
	NOTEMPTY = 0
	if [ "X$CURRENTFOLDERPATH" == "X" ]; then
		NOTEMPTY=1
	fi
	
	assertTrue "CURRENTFOLDERPATH variable is empty" $NOTEMPTY
}

function testAppnameNotEmpty() {
	NOTEMPTY = 0
	if [ "X$APPNAME" == "X" ]; then
		NOTEMPTY=1
	fi
	
	assertTrue "APPNAME variable is empty" $NOTEMPTY
}

function testPythonpathNotEmpty() {
	NOTEMPTY = 0
	if [ "X$PY4APATH" == "X" ]; then
		NOTEMPTY=1
	fi
	
	assertTrue "PY4APATH variable is empty" $NOTEMPTY
}

function testPFlagError() {
	pushd ../
	./configure -a "test" > /dev/null 2>&1
	assertEquals "Missing the -p flag should throw an error" 1 $?
	popd
}

function testAFlagErorr() {
	pushd ../
	./configure -p "test" > /dev/null 2>&1
	assertEquals "Missing the -a flag should throw an error" 1 $?
	popd
}

function testNoFlags() {
	pushd ../
	./configure > /dev/null 2>&1
	assertEquals "No flags provided should throw an error" 1 $?
	popd
}

function testAnontunnelDirectoryExistTrue() {
	checkDirectoryExist > /dev/null 2>&1
	assertEquals "Anontunnel directory does not exist" 0 $?
}

function testDirectoriesMissingTrue() {
	DIRECTORYMISSING=0
	if [ ! -e "${CURRENTFOLDERPATH}/app" ]; then
		DIRECTORYMISSING=1
	fi

	assertFalse "App directory should not exist yet" $DIRECTORYMISSING
}

function testDirectoriesMissingFalse() {
	generateFolders > /dev/null 2>&1
	DIRECTORYMISSING=1
	if [ ! -e "${CURRENTFOLDERPATH}/app" ]; then
		DIRECTORYMISSING=0
	fi

	assertFalse "App directory does not exist after generating folders" $DIRECTORYMISSING
	
}

function testMainExistTrue() {
	MAINEXIST=0
	if [ ! -f "${CURRENTFOLDERPATH}/${APPNAME}/main.py" ]; then
		MAINEXIST=1
	fi

	assertTrue "File main.py does not exist" $MAINEXIST
}

function testKivyFileExistTrue() {
	KIVYEXIST=0
	if [ ! -f "${CURRENTFOLDERPATH}/${APPNAME}/anontunnel.kv" ]; then
		KIVYEXIST=1
	fi

	assertTrue "File anontunnel.kv does not exist" $KIVYEXIST
}

function serviceMainexistTrue() {
	SERVICEMAINEXIST=0;
	if [ ! -f "${CURRENTFOLDERPATH}/${APPNAME}/service/main.py" ]; then
		SERVICEMAINEXIST=1
	fi
	
	assertTrue "File service/main.py does not exist" $SERVICEMAINEXIST
}

function testSplashExist() {
	if [ "X$APPSPLASH" != "X" ] ; then
		SPLASHEXIST=0;
		if [ ! -f "${CURRENTFOLDERPATH}/${APPNAME}/${APPSPLASH}" ]; then
			SPLASHEXIST=1
		fi
		
		assertTrue "File ${APPSPLASH} does not exist" $SPLASHEXIST
	fi
}

function testLogoExist() {
	if [ "X$APPICON" != "X" ] ; then
		LOGOEXIST=0;
		if [ ! -f "${CURRENTFOLDERPATH}/${APPNAME}/${APPICON}" ]; then
			LOGOEXIST=1
		fi
	
		assertTrue "File ${APPICON} does not exist" $LOGOEXIST
	fi
}

function testBuildWorking() {
	pushd ../
	./build.sh -p $PY4APATH > /dev/null
	popd
	assertEquals "Build is failing" 0 $?
}

# Call and Run all Tests
. "../shunit2-2.1.6/src/shunit2"
