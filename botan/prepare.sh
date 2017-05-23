#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y openssl-devel zlib-devel bzip2-devel \
  boost-devel which python-devel doxygen

build_package botan
