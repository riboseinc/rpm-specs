#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y intltool gettext glib2-devel gobject-introspection \
  libxml2-devel bzip2-devel pygobject3-devel \
  libbonobo-devel pygtk2-devel gnome-vfs2-devel

rpmdev-setuptree

yes | cp -f /usr/local/rpm-specs/libgsf/libgsf.spec ~/rpmbuild/SPECS
spectool -g -R ~/rpmbuild/SPECS/libgsf.spec
rpmbuild -ba ${RPMBUILD_FLAGS} ~/rpmbuild/SPECS/libgsf.spec
