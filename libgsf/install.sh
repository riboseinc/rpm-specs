#!/bin/bash -xe

# Install libgsf manually for libvips
# Package libgsf-devel at 7.2 doesn't support libgsf-1.14.27+ yet (yum at 1.14.26-7.el7)

LIBGSF_MAJOR_MINOR=1.14
LIBGSF_VERSION=$LIBGSF_MAJOR_MINOR.40

yum install -y intltool gettext glib2-devel gobject-introspection pygobject3-devel

tmp_dir=`mktemp -d`
git clone --depth 1 --branch v0.9.9 --single-branch https://github.com/processone/exmpp ${tmp_dir}

cd ${tmp_dir}

curl -O http://ftp.gnome.org/pub/gnome/sources/libgsf/$LIBGSF_MAJOR_MINOR/libgsf-$LIBGSF_VERSION.tar.xz
tar xvf libgsf-$LIBGSF_VERSION.tar.xz

cd libgsf-$LIBGSF_VERSION
./configure --prefix=/usr --disable-static

make && make install
ldconfig

rm -rf ${tmp_dir}

