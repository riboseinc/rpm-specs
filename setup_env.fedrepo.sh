#!/bin/bash -x

install_packages() {
  dnf -y install yum-utils fedora-packager sudo man
}

readonly faslogin="${1}"
readonly package_name="${2}"

usage() {
  echo -e "# \e[1mfedrepo-req\e[m"
  echo
  echo -e "# Copy & paste the following into the terminal:"
  echo -e "\e[1m"
  echo -e "su - packager"
  echo -e ". /usr/local/setup.sh"
  echo -e "fedpkg --user ${faslogin-\$faslogin} clone ${package_name-\$package_name}"
  cat > /usr/local/setup.sh <<EOF
export PS1='[\u@\h \W\$(declare -F __git_ps1 &>/dev/null && __git_ps1 " (%s)")]\$ '
cp /usr/local/.gitconfig ~
mkdir ~/.ssh ; cp /usr/local/.ssh/* ~/.ssh
mkdir ~/fedora-scm ; cd ~/fedora-scm
EOF

  # echo
  # echo -e "cp -r /usr/local/fedrepo_req ~"
  # echo -e "cd ~/fedrepo_req"
  # echo -e "python setup.py build"
  # echo -e "python setup.py install"
  # echo -e "fedrepo-req ${1} -t ${2}"
  echo -e "\e[m"
  echo -e "Type \e[1musage\e[m for this help message."
  echo -e "Type \e[1minstall_packages\e[m to install prerequisites."
}

export -f usage
export -f install_packages

setup() {
  install_packages

  # echo root | passwd root --stdin # For debugging purposes
  useradd packager -p packager
}

setup

usage

exec bash

# vim:et:sw=2:sts=2:ts=2
