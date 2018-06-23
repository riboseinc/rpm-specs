#!/bin/bash

# See https://github.com/riboseinc/rnp/blob/master/doc/PACKAGING.md

. /usr/local/rpm-specs/setup_env.sh

# build_cmake_package() {
#   local readonly package_name="${1}"
#
#   rpmdev-setuptree
#   yes | cp -a /usr/local/${package-name}/* ~/rpmbuild/SOURCES
#
#   # spectool -g -R ${spec_dest}
#   rpmbuild --define "_topdir <path_to_build_dir>" --rebuild <SRPM_file_name>
#   rpmbuild ${RPMBUILD_FLAGS:--v -ba} ${spec_dest} || \
#     {
#       echo "rpmbuild failed." >&2;
#       [ $CI ] && exit 1
#       if [ "$(launched_from)" != "bash" ]; then
#         echo "Now yielding control to bash." >&2 && \
#         exec bash
#       fi
#     }
# }

yum -y install bzip2-devel zlib-devel libcmocka-devel libstdc++-static
yum -y install botan2-devel json-c-devel
ln -s /usr/bin/cmake3 /usr/bin/cmake
ln -s /usr/bin/cpack3 /usr/bin/cpack

rpmdev-setuptree
cd ~/rpmbuild/SOURCES/
git clone https://github.com/riboseinc/rnp/ .

# rpmbuild --define "_topdir <path_to_build_dir>" --rebuild <SRPM_file_name>

cd ~/rpmbuild/SOURCES/rnp

cmake -DBUILD_SHARED_LIBS=on -DBUILD_TESTING=off -DCPACK_GENERATOR=RPM .
cpack -G RPM --config ./CPackSourceConfig.cmake
make package

mv *.src.rpm ~/rpmbuild/SRPMS/
# mkdir -p ~/rpmbuild/RPMS/noarch/
# mv *.noarch.rpm ~/rpmbuild/RPMS/noarch/
mkdir -p ~/rpmbuild/RPMS/x86_64/
mv *.x86_64.rpm ~/rpmbuild/RPMS/x86_64/

yum install -y ~/rpmbuild/RPMS/x86_64/*.rpm

# bash
