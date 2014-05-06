#!/bin/bash

# REPLACE ALL THE "dispersy" OF THIS FILE WITH THE MODULE NAME
# THEN REMOVE THIS ERROR AND EXIT

# version of your package
VERSION_dispersy=${VERSION_dispersy:-0.1.0}

# dependencies of this recipe
DEPS_dispersy=()

# url of the package
URL_dispersy=http://ios-dev.no-ip.org/dispersy-$VERSION_dispersy.tar.gz

# md5 of the package
MD5_dispersy=ab48db290f41293411c442d376e7e73b

# default build path
BUILD_dispersy=$BUILD_PATH/dispersy/$(get_directory $URL_dispersy)

# default recipe path
RECIPE_dispersy=$RECIPES_PATH/dispersy

# function called for preparing source code if needed
# (you can apply patch etc here.)
function prebuild_dispersy() {
	true
}

# function called to build the source code
function build_dispersy() {
	cd $BUILD_dispersy
	push_arm
	try $HOSTPYTHON setup.py install
	pop_arm
}

# function called after all the compile have been done
function postbuild_dispersy() {
	true
}
