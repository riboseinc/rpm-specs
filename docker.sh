#!/bin/bash
n=$(cd $(dirname $0); pwd)
echo /usr/local/rpm-specs
if [[ $# = 1 ]]
then
	docker run -it -v "$n":/usr/local/rpm-specs centos:7 /usr/local/rpm-specs/"${1}"/prepare.sh
else
	docker run -it -v "$n":/usr/local/rpm-specs centos:7 bash
fi

