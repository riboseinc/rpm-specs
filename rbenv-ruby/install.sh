#!/bin/bash -xe

# Necessary to install base ruby for ruby-install to work
yum install -y make automake gcc gcc-c++ bzip2 ruby ruby-devel \
  zlib-devel patch readline readline-devel libyaml-devel \
  libffi-devel openssl-devel autoconf libtool sqlite-devel \
  gdbm-devel ncurses-devel

if [ -d /usr/local/rbenv ]; then
  echo '[install/ruby] /usr/local/rbenv exists, we are running a second time.'
  pushd /usr/local/rbenv
  git pull
  popd
else
  git clone https://github.com/sstephenson/rbenv /usr/local/rbenv
fi

if [ -d /usr/local/rbenv/plugins/ruby-build ]; then
  pushd /usr/local/rbenv/plugins/ruby-build git pull
  popd
else
  git clone https://github.com/sstephenson/ruby-build /usr/local/rbenv/plugins/ruby-build
fi

echo 'export RBENV_ROOT="/usr/local/rbenv"
export PATH="$RBENV_ROOT/bin:$GEM_HOME/bin:$PATH"
eval "$(rbenv init -)"' \
  > /etc/profile.d/rbenv.sh
echo 'gem: --no-rdoc --no-ri' > /root/.gemrc

source /etc/profile.d/rbenv.sh
rbenv install ${RUBY_VERSION}
rbenv global ${RUBY_VERSION}
gem install bundler --version "$BUNDLER_VERSION"
rbenv rehash


# ruby-install as an alternative
#
# RUN \
#   export RUBY_INSTALL_VERSION=0.6.0 && \
#   cd /tmp && \
#   curl -o ruby-install-$RUBY_INSTALL_VERSION.tar.gz https://codeload.github.com/postmodern/ruby-install/tar.gz/v$RUBY_INSTALL_VERSION && \
#   tar -xzvf ruby-install-$RUBY_INSTALL_VERSION.tar.gz && \
#   cd ruby-install-$RUBY_INSTALL_VERSION && \
#   make install && \
#   rm -rf /tmp/ruby-install-$RUBY_INSTALL_VERSION* && \
#   ruby-install --system ruby 2.3


