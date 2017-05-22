yum install -y epel-release

yum install -y automake autoconf libtool make gcc-c++ python2-devel \
  rpmdevtools wget epel-rpm-macros

yum install -y intltool gettext glib2-devel gobject-introspection \
  libxml2-devel bzip2-devel pygobject3-devel \
  libbonobo-devel pygtk2-devel gnome-vfs2-devel

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget https://download.gnome.org/sources/libgsf/1.14/libgsf-1.14.41.tar.xz
yes | cp -f /usr/local/libgsf/*.patch ~/rpmbuild/SOURCES/

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/libgsf/libgsf.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS

rpmbuild ${RPMBUILD_FLAGS} libgsf.spec
