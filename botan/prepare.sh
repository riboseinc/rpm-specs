yum install -y epel-release

yum install -y automake gcc make openssl-devel zlib-devel bzip2-devel \
  boost-devel libtool git which gcc-c++ python-devel doxygen \
  rpmdevtools wget epel-rpm-macros

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget http://botan.randombit.net/releases/Botan-2.1.0.tgz

cd ~/rpmbuild/SPECS
cp /usr/local/botan/botan.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS; rpmbuild -ba botan.spec

# cd /usr/local/botan
