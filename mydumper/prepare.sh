#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y cmake glib2-devel mysql-devel zlib-devel pcre-devel \
  openssl-devel python-sphinx mysql mysql-devel

build_package mydumper
