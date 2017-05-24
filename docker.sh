#!/bin/bash
n=$(cd $(dirname $0); pwd)

if [[ $# = 1 ]]; then
  readonly EXTRA="-c /usr/local/rpm-specs/"${1}"/prepare.sh"
fi

docker run -it -v "$n":/usr/local/rpm-specs centos:7 bash $EXTRA
