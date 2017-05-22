yum install -y epel-release

yum install -y automake autoconf libtool make gcc-c++ gettext python2-devel \
  rpmdevtools wget epel-rpm-macros

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

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget https://github.com/jcupitt/libvips/releases/download/v8.5.5/vips-8.5.5.tar.gz

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/vips/vips.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS

rpmbuild ${RPMBUILD_FLAGS} vips.spec
