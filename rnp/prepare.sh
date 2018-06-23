#!/bin/bash
set -x
# See https://github.com/riboseinc/rnp/blob/master/doc/PACKAGING.md

VERSION=0.9.0

. /usr/local/rpm-specs/setup_env.sh

yum -y install bzip2-devel zlib-devel libstdc++-static
yum -y install botan2-devel json-c-devel
ln -s /usr/bin/cmake3 /usr/bin/cmake
ln -s /usr/bin/cpack3 /usr/bin/cpack

rpmdev-setuptree

curl -LO https://github.com/riboseinc/rnp/archive/v${VERSION}.tar.gz
tar -xzf v${VERSION}.tar.gz

cmakeopts=(-DBUILD_SHARED_LIBS=on -DBUILD_TESTING=off)
cmake "${cmakeopts[@]}" -DCPACK_RPM_SOURCE_PKG_BUILD_PARAMS="${cmakeopts[*]}" -DCPACK_GENERATOR=RPM rnp-${VERSION}
cpack -G RPM --config ./CPackSourceConfig.cmake

rpmdev-extract rnp-${VERSION}-*.src.rpm
mv rnp-${VERSION}-*.src/*.spec .
mkdir -p sources
mv rnp-${VERSION}-*.src/rnp-${VERSION}.tar.gz sources

build_package rnp
