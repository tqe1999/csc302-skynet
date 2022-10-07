#!/bin/sh

dockerInstallApt () {
  sudo apt-get remove docker docker-engine docker.io containerd runc &&
  sudo apt-get update &&
  sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release &&
  sudo mkdir -p /etc/apt/keyrings-f &&
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg &&
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null &&
  sudo apt-get update &&
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
}

dockerInstallYum () {
  sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine &&
  sudo yum install -y yum-utils &&
  sudo yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo &&
  sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
}

dockerInstallApt ||
dockerInstallYum || (
  echo "only apt and yum supported" 
  return 1
)