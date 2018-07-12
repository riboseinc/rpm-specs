#!/bin/bash
#
# Environment variables can be passed to the prepare.sh script by
# specifying the env var keys with a comma-separated list, like 
# so:
#
#   ENVS=key1,key2,...
#
# Current values of the env vars will be propagated as per Docker-run's 
# documentation.  So, if you have the following:
#
#   export key1=hello
#   export key2=bye
#   ENVS=key1,key2 ./docker.sh my_package_name
#
# ... then the ./docker.sh will have key1=hello and key2=bye.
#
#
absolute_dir_name=$(cd $(dirname $0); pwd)

if [[ $# = 1 ]]; then
  readonly EXTRA="-c /usr/local/rpm-specs/"${1}"/prepare.sh"
fi

# Parse out env var names intended for passing into container:
envs=()
if [[ ! -z "${ENVS}" ]]; then
  IFS=, read -r -a envs <<< "${ENVS}"
fi

# Compose envs strings for `docker run`:
docker_env_opts=''
for env_key in ${envs[@]}; do
  docker_env_opts="${docker_env_opts} -e ${env_key}"
done

docker run -it \
  -v "${absolute_dir_name}":/usr/local/rpm-specs \
  ${docker_env_opts} \
  centos:7 \
  bash $EXTRA
