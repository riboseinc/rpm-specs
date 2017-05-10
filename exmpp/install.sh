#!/bin/bash -xe

tmp_dir=`mktemp -d`
git clone --depth 1 --branch v0.9.9 --single-branch https://github.com/processone/exmpp ${tmp_dir}

cd ${tmp_dir}

autoreconf -vif
./configure && make && make install

rm -rf ${tmp_dir}

