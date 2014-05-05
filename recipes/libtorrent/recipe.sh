#!/bin/bash

# version of your package
VERSION_libtorrent=${VERSION_libtorrent:-0.16.16}

# dependencies of this recipe
DEPS_libtorrent=()

# url of the package
URL_libtorrent=http://downloads.sourceforge.net/project/libtorrent/libtorrent/libtorrent-rasterbar-$VERSION_libtorrent.tar.gz

# md5 of the package
MD5_libtorrent=6895a4d355e6c4a91f35efe746a7511e

# default build path
BUILD_libtorrent=$BUILD_PATH/libtorrent/$(get_directory $URL_libtorrent)

# default recipe path
RECIPE_libtorrent=$RECIPES_PATH/libtorrent

# function called for preparing source code if needed
# (you can apply patch etc here.)
function prebuild_libtorrent() {
	true
}

# function called to build the source code
function build_libtorrent() {
	push_arm
	cd $BUILD_libtorrent
	./configure --enable-pyton-binding --host=arm-eabi
	make
	cd bindings/python
	make
	try $HOSTPYTHON setup.py install
	pop_arm
}

# function called after all the compile have been done
function postbuild_libtorrent() {
	true
}
