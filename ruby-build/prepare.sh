#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y openssl-devel readline-devel zlib-devel

build_package ruby-build

