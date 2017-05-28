#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y \
  readline ncurses gdbm glibc openssl libyaml libffi zlib \
  readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make \
  libyaml-devel libffi-devel zlib-devel \
  openssl-devel cmake tk-devel systemtap-sdt-devel

build_package rbenv-ruby

