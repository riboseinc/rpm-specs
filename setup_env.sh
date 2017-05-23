rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo

yum install -y epel-release

yum install -y automake autoconf libtool make gcc-c++ gettext python2-devel \
  rpmdevtools git epel-rpm-macros

build_package() {
	local readonly package_name="${1}"
	rpmdev-setuptree
	yes | cp -f /usr/local/rpm-specs/${package_name}/${package_name}.spec ~/rpmbuild/SPECS
	spectool -g -R ~/rpmbuild/SPECS/${package_name}.spec
	rpmbuild ${RPMBUILD_FLAGS:--v -ba} ~/rpmbuild/SPECS/${package_name}.spec || \
		echo rpmbuild failed. Now yielding control to bash. >&2 && \
		exec bash
	return 0
}
