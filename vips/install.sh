#!/bin/bash -xe

# Install libvips
LIBVIPS_VERSION_MAJOR_MINOR=$1
LIBVIPS_VERSION_PATCH=$2
LIBVIPS_VERSION=$LIBVIPS_VERSION_MAJOR_MINOR.$LIBVIPS_VERSION_PATCH

yum install -y openslide-devel openslide-python \
  libpng-devel zlib-devel libtiff-devel gdk-pixbuf2-devel \
  zlib-devel gdk-pixbuf2-devel glib2-devel \
  libjpeg-turbo-devel giflib-devel libwebp-devel libexif-devel \
  librsvg2-devel poppler-glib-devel \
  fftw-devel lcms2-devel pango-devel \
  orc-devel OpenEXR-devel matio-devel cfitsio-devel \
  ImageMagick-devel gtk-doc

tmp_dir=`mktemp -d`
cd ${tmp_dir}
curl -O http://www.vips.ecs.soton.ac.uk/supported/$LIBVIPS_VERSION_MAJOR_MINOR/vips-$LIBVIPS_VERSION.tar.gz
tar zvxf vips-$LIBVIPS_VERSION.tar.gz

cd vips-$LIBVIPS_VERSION
./configure --disable-debug --prefix=/usr  # $1
make && make install
ldconfig

rm -rf ${tmp_dir}

