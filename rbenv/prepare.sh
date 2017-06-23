#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

#rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
#curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo
#yum install -y ruby-build

build_package rbenv

