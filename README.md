# Docker.py
This repository contains some useful scripts and Dockerfiles to create Docker containers.


# Installation:

https://get.docker.com

curl -fsSL https://get.docker.com -o get-docker.sh

bash ./get-docker.sh


# Some useful commands:

>> show all running containers :
docker ps

>> show all existing containers :
docker ps -a

>> show the docker images :
docker images

>> show overall docker info :
docker info , docker --varsion

>> stop and delete a single container:
[ docker stop Container_nam ] [ docker rm Container_name ]

>> delete a docker image:
docker rmi myimage

>> stop all containers :
docker stop $(docker ps -q)

>> delete all containers :
docker rm $(docker ps -aq)

>> delete all images :
docker rmi $(docker images -q)

>> run a container behind the scenes :
sudo docker run –d centos

>> start/stop container :
sudo docker start/stop

>> pull image that you want :
sudo docker pull centos/ubuntu

>> see logs of the runner container :
sudo docker logs [container id ]

>> search image :
sudo docker search centos/ubuntu


##EOF##
