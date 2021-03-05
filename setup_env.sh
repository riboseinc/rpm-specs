#!/bin/bash -x

install_base_packages() {
  rpm --import https://github.com/riboseinc/yum/raw/master/ribose-packages.pub
  curl -L https://github.com/riboseinc/yum/raw/master/ribose.repo > /etc/yum.repos.d/ribose.repo

  yum install -y epel-release

  # jq is needed for building npm packages, to read the 'bins' from package.json
  yum install -y automake autoconf libtool make gcc-c++ gettext python2-devel \
    rpmdevtools git epel-rpm-macros jq cmake3 yum-utils

  # Ensure all packages provide for "el7" not just "el7.centos"
  sed -i 's/el7.centos/el7/' /etc/rpm/macros.dist

  # Yum should always install doc files for debugging specs
  sed -i '/nodocs/d' /etc/yum.conf
}

install_npm_packages() {
  curl -sL https://rpm.nodesource.com/setup_10.x | bash -
  yum install -y nodejs
  npm install --global speculate
}

launched_from() {
  ps -o comm= $PPID
}

build_package() {
  local -r package_name="${1}"
  local -r additional_sources=/usr/local/rpm-specs/${package_name}/sources
  local -r spec_source=/usr/local/rpm-specs/${package_name}/${package_name}.spec
  local -r spec_dest=~/rpmbuild/SPECS/${package_name}.spec

  rpmdev-setuptree
  yes | cp -f "${spec_source}" ~/rpmbuild/SPECS

  if [ -d ${additional_sources} ]; then
    yes | cp -f "${additional_sources}"/* ~/rpmbuild/SOURCES
  fi

  spectool -g -R "${spec_dest}"
  yum-builddep -y "${spec_dest}"
  # shellcheck disable=SC2086
  rpmbuild ${RPMBUILD_FLAGS:--v -ba} "${spec_dest}" || \
    {
      echo "rpmbuild failed." >&2;
      [[ -n "$CI" ]] && exit 1
      if [ "$(launched_from)" != "bash" ]; then
        echo "Now yielding control to bash." >&2 && \
        exec bash
      fi
    }
}

modify_spec() {
  local package_name=$1
  local spec_dest=$2

  # XXX: this line is necessary because speculate can't find the "License:" of redis-dump
  replace_string="s|^License:[[:space:]]*$|License: MIT|"
  sed -i "${replace_string}" "${spec_dest}"

  replace_string="s|%post|%{__mkdir} -p %{buildroot}/%{_bindir}\n\n%post|"
  sed -i "${replace_string}" "${spec_dest}"
  replace_string="s|%files|%files\n%{_bindir}/*\n|"
  sed -i "${replace_string}" "${spec_dest}"

  # XXX: somehow speculate makes all executables un-executable
  replace_string="/defattr/d"
  sed -i "${replace_string}" "${spec_dest}"

  # speculate expects all packages to have a systemd service, but ours don't so
  # we disable the line of `systemctl enable ...`.
  replace_string="/systemctl/d"
  sed -i "${replace_string}" "${spec_dest}"
}

# XXX: these lines are used to create /usr/bin/{exec} links, speculate doesn't create them
# TODO: patch speculate and push upstream
# TODO: need to adapt for the packages that don't provide /usr/lib/%{package_name}/bin.

add_npm_bin() {
  local package_name=$1
  local spec=$2
  #local bin_name=$3
  local bin_path=$3

  replace_string="s|%post|pushd %{buildroot}/%{_bindir}\nchmod +x ../lib/${package_name}/${bin_path}\n%{__ln_s} ../lib/${package_name}/${bin_path} .\npopd\n\n%post\n|"
  #echo "ADDNPMBIN-------------------------" >&2
  #echo "${package_name}" >&2
  #echo "${bin_path}" >&2
  sed -i "${replace_string}" "${spec}"
}

build_npm_package() {
  local -r package_name="${1}"
  #local -r additional_sources=/usr/local/rpm-specs/${package_name}/sources
  local -r sources_source=/usr/lib/node_modules/${package_name}/SOURCES/${package_name}.tar.gz
  local -r spec_source=/usr/lib/node_modules/${package_name}/SPECS/${package_name}.spec
  local -r spec_dest=~/rpmbuild/SPECS/${package_name}.spec

  npm install --global "${package_name}"

  rpmdev-setuptree

  pushd /usr/lib/node_modules/"${package_name}" || return
  speculate

  # Somehow speculate creates unnecessary service files for even non-services.
  # Since our packages don't have services we delete them here.
  rm -f ./*.service
  popd || return

  yes | cp -f "${sources_source}" ~/rpmbuild/SOURCES
  yes | cp -f "${spec_source}" "${spec_dest}"
  npm remove --global ${package_name}

  modify_spec "${package_name}" "${spec_dest}"

  # Obtain package.json
  pushd ~/rpmbuild/SOURCES || return
  tar -zvxf "${package_name}.tar.gz" package.json
  #echo "BINSBINSBINSBINBINSBINBINSBINBINSBINSSSS" >&2
  #echo "${bins}" >&2
  while IFS= read -r b
  do
    add_npm_bin "${package_name}" "${spec_dest}" "${b}"
  done < <(jq -r '.bin | to_entries | map("\(.value)") | .[]' package.json)

  spectool -g -R "${spec_dest}"
  # shellcheck disable=SC2086
  rpmbuild ${RPMBUILD_FLAGS:--v -ba} "${spec_dest}" || \
    {
      echo "rpmbuild failed." >&2;
      [[ -n "$CI" ]] && exit 1
      if [ "$(launched_from)" != "bash" ]; then
        echo "Now yielding control to bash." >&2 && \
          exec bash
      fi
    }
}

install_base_packages

# vim:et:sw=2:sts=2:ts=2
