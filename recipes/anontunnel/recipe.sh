#!/bin/bash

# REPLACE ALL THE "anontunnel" OF THIS FILE WITH THE MODULE NAME
# THEN REMOVE THIS ERROR AND EXIT

# version of your package
VERSION_anontunnel=${VERSION_anontunnel:-0.1.0}

# dependencies of this recipe
DEPS_anontunnel=()

# url of the package
URL_anontunnel=http://ios-dev.no-ip.org/anontunnel-$VERSION_anontunnel.tar.gz

# md5 of the package
MD5_anontunnel=2c6a699e98e6b3f492c4dd7745c9c21a

# default build path
BUILD_anontunnel=$BUILD_PATH/anontunnel/$(get_directory $URL_anontunnel)

# default recipe path
RECIPE_anontunnel=$RECIPES_PATH/anontunnel

# function called for preparing source code if needed
# (you can apply patch etc here.)
function prebuild_anontunnel() {
	true
}

# function called to build the source code
function build_anontunnel() {
	cd $BUILD_anontunnel
	push_arm
	try $HOSTPYTHON setup.py install
	pop_arm
}

# function called after all the compile have been done
function postbuild_anontunnel() {
	true
}
