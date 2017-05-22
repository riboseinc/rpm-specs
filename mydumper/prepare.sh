yum install -y epel-release

yum install -y automake autoconf libtool make cmake gcc-c++ \
  glib2-devel mysql-devel zlib-devel pcre-devel openssl-devel python-sphinx \
  rpmdevtools wget epel-rpm-macros

# yum install -y https://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
# yum install -y mysql mysql-community-devel

yum install -y mysql mysql-devel

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget https://github.com/maxbube/mydumper/archive/v0.9.1.tar.gz

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/mydumper/mydumper.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS; rpmbuild -ba mydumper.spec

