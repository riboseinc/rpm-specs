#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo
yum install -y ruby-build rbenv

# Skip this error:
# 0x0002
export QA_RPATHS=$[ 0x0002 ]
build_package rbenv-ruby-2.3.4

# Enable the following lines to test compatabilty with passenger packages.
#
# yum install -y /root/rpmbuild/RPMS/x86_64/*.rpm
# curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo
# yum install -y nginx passenger
# exec bash
