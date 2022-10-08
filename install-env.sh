#!/bin/sh

curl -fsSL https://get.docker.com -o get-docker.sh || wget -O get-docker.sh https://get.docker.com
if [ ! -r get-docker.sh ]; then
  echo "Unable to install docker: curl or wget must be installed"
  exit 1
fi
sh get-docker.sh
