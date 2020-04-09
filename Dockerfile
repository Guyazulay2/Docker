Create a directory enter it and create your file [touch Dockerfile] . 

##### simple example of a Dockerfile ####

FROM ubuntu:latest
MAINTAINER Guy Azulay "guykort98@gmail.com"

RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install python3-pip -y 
RUN pip3 install Flask 
RUN pip3 install boto3 && apt-get install awscli 
RUN echo "Finished"
ADD hello.py /home/guy/Desktop/hello.py

WORKDIR /home





######### Finaly to build the image : 

    > sudo docker build -t [Your dockerfile] .
    
 After you create ubuntu image and create a container you can log in at the following point:
 
[ docker run -t -i ubuntu /bin/bash ]
afetr that you need to do [ apt-get update ] and then you can install packages.


