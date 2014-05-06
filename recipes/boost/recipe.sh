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
	cd $BUILD_boost

	# Create build tools for boost
	./bootstrap.sh
	
	# Write android config to boost user-config instructions
	NDKBIN=${ANDROIDNDK}/toolchains/arm-linux-androideabi-4.8/prebuilt/linux-x86
	USRCONFIG=${BUILD_boost}/tools/build/v2/user-config.jam

	echo "# Android Configuration " > $USRCONFIG
	echo "local AndroidToolchainRoot = ${NDKBIN}" >> $USRCONFIG
	echo "using gcc" >> $USRCONFIG
	echo ": androidR9" >> $USRCONFIG
	echo ": $(AndroidToolchainRoot)/bin/arm-linux-androideabi-g++" >> $USRCONFIG
	echo ";" >> $USRCONFIG
}

# function called to build the source code
function build_boost() {
	cd $BUILD_boost
	
	# Build boost with arm architecture
	push_arm
	./b2 toolset=gcc-androidR9
	pop_arm
}

# function called after all the compile have been done
function postbuild_boost() {
	true
}
