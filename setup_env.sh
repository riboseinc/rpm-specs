rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo

yum install -y epel-release

yum install -y automake autoconf libtool make gcc-c++ gettext python2-devel \
  rpmdevtools git epel-rpm-macros

# Ensure all packages provide for "el7" not just "el7.centos"
sed -i 's/el7.centos/el7/' /etc/rpm/macros.dist

launched_from() {
  echo "$(ps -o comm= $PPID)"
}

build_package() {
	local readonly package_name="${1}"
  local readonly additional_sources=/usr/local/rpm-specs/${package_name}/sources
  local readonly spec_source=/usr/local/rpm-specs/${package_name}/${package_name}.spec
  local readonly spec_dest=~/rpmbuild/SPECS/${package_name}.spec

	rpmdev-setuptree
	yes | cp -f ${spec_source} ~/rpmbuild/SPECS

  if [ -d ${additional_sources} ]; then
    yes | cp -f ${additional_sources}/* ~/rpmbuild/SOURCES
  fi

	spectool -g -R ${spec_dest}
	rpmbuild ${RPMBUILD_FLAGS:--v -ba} ${spec_dest} || \
		{
      echo "rpmbuild failed." >&2;
      if [ "$(launched_from)" != "bash" ]; then
        echo "Now yielding control to bash." >&2 && \
        exec bash
      fi
		}
}
