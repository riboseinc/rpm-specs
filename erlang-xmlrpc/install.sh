#!/bin/bash -xe

erlang_xmlrpc_version=xmlrpc-1.13
erlang_xmlrpc_pkg=$erlang_xmlrpc_version-ipr2

tmp_dir=`mktemp -d`

cd ${tmp_dir}
curl -LO http://www.ejabberd.im/files/contributions/$erlang_xmlrpc_pkg.tgz

tar -zxvf $erlang_xmlrpc_pkg.tgz

mv $erlang_xmlrpc_version /usr/lib/erlang/lib/
cd /usr/lib/erlang/lib/$erlang_xmlrpc_version/src

make

rm -rf ${tmp_dir}
