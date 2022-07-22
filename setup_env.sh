#!/bin/bash -x

SCRIPT_DIR_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
# echo "BASH_SOURCE[0]=${BASH_SOURCE[0]}"
# echo "dirname \${BASH_SOURCE[0]} = $(dirname "${BASH_SOURCE[0]}")"
# echo "pwd = $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# echo "pwd -P = $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
# echo "basename \${BASH_SOURCE[0]} = $(basename "${BASH_SOURCE[0]}")"
. "${SCRIPT_DIR_PATH}"/lib.sh

install_base_packages

# vim:et:sw=2:sts=2:ts=2
