#!/bin/bash -x

install_packages() {
  dnf -y install yum-utils fedora-packager sudo
}

install_packages

# echo root | passwd root --stdin # For debugging purposes
useradd packager -p packager

echo -e "# \e[1mfedrepo-req\e[m"
echo
echo -e "# Copy & paste the following into the terminal:"
echo -e "\e[1m"
echo -e "su - packager"
echo -e "mkdir ~/.ssh ; cp /usr/local/.ssh/* ~/.ssh"
echo -e "cp -r /usr/local/fedrepo_req ~"
echo -e "cd ~/fedrepo_req"
echo -e "python setup.py build"
echo -e "python setup.py install"
echo -e "fedrepo-req ${1} -t ${2}"
echo -e "\e[m"

exec bash

# vim:et:sw=2:sts=2:ts=2
