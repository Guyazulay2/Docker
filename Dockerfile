Create a directory enter it and create your file [touch Dockerfile] . 

##### simple example of a Dockerfile ####

FROM ubuntu18.04:latest
MAINTAINER Guy Azulay "guykort98@gmail.com"

RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install python3-pip -y 
RUN pip3 install Flask -y 
RUN pip3 install boto3 -y 


ADD hello.py /home/guy/Desktop/hello.py

WORKDIR /home/guy/Desktop





######### Finaly to build the image : 

    > sudo docker build -t [Your directory] .

