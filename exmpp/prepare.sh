RPMBUILD_CMD=rpmbuild
RPMBUILD_FLAGS="-v -ba"

yum install -y epel-release

yum install -y automake autoconf libtool make gcc-c++ gettext python2-devel \
  rpmdevtools wget epel-rpm-macros

yum install -y \
  git expat-devel libxml2-devel openssl-devel zlib-devel

rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo
yum install -y erlang-R15B01

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget https://github.com/processone/exmpp/archive/v0.9.9.tar.gz

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/exmpp/exmpp.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS

rpmbuild ${RPMBUILD_FLAGS} exmpp.spec

