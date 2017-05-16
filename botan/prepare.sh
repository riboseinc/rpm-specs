yum install -y automake gcc make openssl-devel zlib-devel bzip2-devel \
  boost-devel libtool git which gcc-c++ python-devel python-sphinx \
  rpm-build redhat-rpm-config wget

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

cd ~/rpmbuild/SOURCES/
wget http://botan.randombit.net/releases/Botan-2.1.0.tgz

cd ~/rpmbuild/SPECS
cp /usr/local/botan/botan.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS; rpmbuild -ba botan.spec

# cd /usr/local/botan
