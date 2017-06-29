#!/bin/bash

. /usr/local/rpm-specs/setup_env.sh

yum install -y go

build_package rutil

