#!/bin/bash

# version of your package
#VERSION_boost=${VERSION_boost:-1.55.0}

# dependencies of this recipe
DEPS_boost=()

# url of the package
URL_boost=http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.gz

# md5 of the package
MD5_boost=93780777cfbf999a600f62883bd54b17

# default build path
BUILD_boost=$BUILD_PATH/boost/$(get_directory $URL_boost)

# default recipe path
RECIPE_boost=$RECIPES_PATH/boost

# function called for preparing source code if needed
# (you can apply patch etc here.)
function prebuild_boost() {
	true
}

# function called to build the source code
function build_boost() {
	cd $BUILD_boost
	push_arm
	#try $HOSTPYTHON setup.py install
	pop_arm
}

# function called after all the compile have been done
function postbuild_boost() {
	push_arm
	cd $BUILD_PATH/boost/$(get_directory $URL_boost)/
	./bootstrap.sh
	pop_arm
}
