#!/bin/bash -x

install_packages() {
  dnf -y install yum-utils fedora-review sudo
}

install_packages

# echo root | passwd root --stdin # For debugging purposes
useradd reviewer -p reviewer
usermod -a -G mock reviewer

echo
echo -e "# \e[1mfedora-review\e[m"
echo -e "# Run: \e[1mfedora-review\e[m -b <bug number>"
echo -e "#  or: \e[1mfedora-review\e[m -n ${1##*/}"
echo
echo -e "# Copy & paste the following into the terminal:"
echo -e "\e[1m"
echo -e "su - reviewer"
echo -e "cd $1"
echo -e "cp *.src.rpm *.spec ~"
echo -e "cd"
echo -e "fedora-review -n ${1##*/}"
echo -e "\e[m"

exec bash

# vim:et:sw=2:sts=2:ts=2
