#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y libxml2-devel

rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo
yum install -y erlang-R15B01

build_package erlang-xmlrpc
