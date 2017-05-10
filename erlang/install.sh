#!/bin/bash -xe

# erlang: openssl openssl-devel
# exmpp: expat expat-devel libtool
yum install -y openssl openssl-devel expat expat-devel libtool

# Install erlang
erlang_version=R15B01
erlang_pkg_checksum=f94f7de7328af3c0cdc42089c1a4ecd03bf98ec680f47eb5e6cddc50261cabde
erlang_pkg_path=http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_src_R15B01.tar.gz/f12d00f6e62b36ad027d6c0c08905fad/otp_src_$erlang_version.tar.gz

tmp_dir=`mktemp -d`

cd ${tmp_dir}
curl -LO $erlang_pkg_path || \
  exit 1

tar xzvf otp_src_$erlang_version.tar.gz
cd otp_src_$erlang_version

./configure --prefix=/usr
make && make install

rm -rf ${tmp_dir}

