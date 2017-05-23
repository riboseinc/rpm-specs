#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y intltool gettext glib2-devel gobject-introspection \
  hardlink doxygen libxml2-devel bzip2-devel pygobject3-devel \
  libbonobo-devel pygtk2-devel gnome-vfs2-devel

build_package json-c12
