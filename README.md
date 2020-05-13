
 This repository contains some useful Dockerfiles scripts to create Docker containers and Pull images and Docker-compose ###

# Install Docker-Compose :
first update :

    apt-get update
    
check the current release and if necessary, update it in the command below :
    
    sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    
set the permissions :

    sudo chmod +x /usr/local/bin/docker-compose
    
checking the version :

    docker-compose --version
    
You can also : 

    sudo apt install docker-compose
    
    


# Docker Installation :

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
sudo docker search centos/ubuntu/nginx/apache2


add current user to docker group so there is no need to use sudo when running docker

sudo usermod -aG docker $(whoami)

##EOF##
