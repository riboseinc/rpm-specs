#!/bin/bash -x

install_packages() {
  dnf -y install yum-utils fedora-review sudo
}

readonly package_path="${1}"
readonly package_name="${package_path##*/}"

usage() {
  echo
  echo -e "# \e[1mfedora-review\e[m"
  echo -e "# Run: \e[1mfedora-review\e[m -b <bug number>"
  echo -e "#  or: \e[1mfedora-review\e[m -n ${package_name}"
  echo
  echo -e "# Copy & paste the following into the terminal:"
  echo -e "\e[1m"
  echo -e "su - reviewer"
  echo -e "cd ${package_path}"
  echo -e "cp *.src.rpm *.spec ~"
  echo -e "cd"
  echo -e "fedora-review -n ${package_name}"
  echo -e "\e[m"
  echo -e "Type \e[1musage\e[m for this help message."
  echo -e "Type \e[1minstall_packages\e[m to install prerequisites."
}

export -f usage
export -f install_packages

setup() {
  install_packages

  # echo root | passwd root --stdin # For debugging purposes
  useradd reviewer -p reviewer
  usermod -a -G mock reviewer
}

setup

usage

exec bash

# vim:et:sw=2:sts=2:ts=2
