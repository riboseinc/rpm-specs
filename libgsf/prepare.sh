#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y intltool gettext glib2-devel gobject-introspection \
  libxml2-devel bzip2-devel pygobject3-devel \
  libbonobo-devel pygtk2-devel gnome-vfs2-devel

build_package libgsf
