#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y openslide-devel openslide-python \
  libpng-devel zlib-devel libtiff-devel \
  zlib-devel glib2-devel \
  libjpeg-turbo-devel giflib-devel libwebp-devel libexif-devel \
  librsvg2-devel poppler-glib-devel \
  fftw-devel lcms2-devel pango-devel \
  orc-devel OpenEXR-devel matio-devel cfitsio-devel \
  ImageMagick-devel gtk-doc \
  gobject-introspection-devel pygobject3-devel libgsf-devel \
  gdk-pixbuf2-devel

build_package vips
