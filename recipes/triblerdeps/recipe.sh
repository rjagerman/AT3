#!/bin/bash

# REPLACE ALL THE "triblerdeps" OF THIS FILE WITH THE MODULE NAME
# THEN REMOVE THIS ERROR AND EXIT

# version of your package
VERSION_triblerdeps=${VERSION_triblerdeps:-0.1.0}

# dependencies of this recipe
DEPS_triblerdeps=()

# url of the package
URL_triblerdeps=http://ios-dev.no-ip.org/triblerdeps-$VERSION_triblerdeps.tar.gz

# md5 of the package
MD5_triblerdeps=2861989440922ad2f56ae410b4662221

# default build path
BUILD_triblerdeps=$BUILD_PATH/triblerdeps/$(get_directory $URL_triblerdeps)

# default recipe path
RECIPE_triblerdeps=$RECIPES_PATH/triblerdeps

# function called for preparing source code if needed
# (you can apply patch etc here.)
function prebuild_triblerdeps() {
	true
}

# function called to build the source code
function build_triblerdeps() {
	cd $BUILD_triblerdeps
	push_arm
	try $HOSTPYTHON setup.py install
	pop_arm
}

# function called after all the compile have been done
function postbuild_triblerdeps() {
	true
}
