Create a directory enter it and create your file [touch Dockerfile] . 

# Pull base image.
FROM ubuntu18.04

# Install LXDE and VNC server.
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal tightvncserver && \2
  rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]

# Expose ports.
EXPOSE 5901



######### to build the image , 

> sudo docker build -t [Your directory] .
