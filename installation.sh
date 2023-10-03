#!/bin/bash

INSTALL_CMD="sudo apt-get -y install"

setups=(
"sudo apt-get update -y && sudo apt-get upgrade -y"
)

packages=(
"docker-ce"
"ocker-ce-cli"
"containerd.io"
"docker-buildx-plugin"
"docker-compose-plugin"
"apt-get install mysql-client"
)


setup_docker=(
"sudo groupadd docker"
"sudo usermod -aG docker $USER"
"newgrp docker"
)

for setup_step in "${setups[@]}"
do
  eval "$setup_step"
done

for package in "${packages[@]}"
do
  eval "${INSTALL_CMD} ${package}"
done


# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update


for docker_setup_step in "${setup_docker[@]}"
do
  eval "$docker_setup_step"
done
