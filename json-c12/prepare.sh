yum install -y epel-release

yum install -y automake autoconf libtool hardlink doxygen make \
  rpmdevtools wget epel-rpm-macros

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget https://github.com/json-c/json-c/archive/json-c-0.12.1-20160607.tar.gz

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/json-c/json-c12.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS; rpmbuild -ba json-c12.spec

# cd /usr/local/botan
