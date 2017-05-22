yum install -y epel-release

yum install -y automake autoconf libtool make gcc-c++ gettext python2-devel \
  rpmdevtools wget epel-rpm-macros

yum install -y \
  readline ncurses gdbm glibc openssl libyaml libffi zlib \
  readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make \
  libyaml-devel libffi-devel zlib-devel

rpmdev-setuptree

cd ~/rpmbuild/SOURCES/
wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.4.tar.gz

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/ruby/ruby.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS; rpmbuild -ba ruby.spec

