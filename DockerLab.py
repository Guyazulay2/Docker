#!/bin/python3.7

import os
from time import sleep


def Install():
    c = input("(1) | Install docker on this computer\n(2) | Install docker on another computer\nYour Choice >>:")
    if c == "1":
        os.system("sudo apt-get update ; sudo apt-get install curl ; bash get - docker.sh")
        os.system("curl - fsSL https: // get.docker.com - o get - docker.sh")
        print("<<< Docker Installation is Done >>>")
        os.system("docker --version ; sudo systemctl status docker")
    elif c == "2":
        ip = input("Enter the slave IP >>:")
        passwd = input("Enter the Root Password >>: ")
        os.system("sshpass -p '{}' ssh root@{} sudo apt-get update ; sudo apt-get install curl".format(passwd, ip))
        os.system("sshpass -p '{}' ssh root@{} ".format(passwd, ip))
        os.system("sshpass -p '{}' ssh root@{} curl - fsSL https: // get.docker.com - o get - docker.sh".format(passwd, ip))
        os.system("sshpass -p '{}' ssh root@{} bash get - docker.sh"(passwd, ip))
        print("<<< Docker Installation is Done >>>")

def Pull_Images():
    s = input("Enter the image name that you want to pull >>:")
    os.system("sudo docker pull" " " + s)
    sleep(0.5)
    print("Your Image :",s ,"<< Pulling Successfully >>")
    sleep(0.5)
    print("The Images >>:")
    os.system("sudo docker images")

def Images():
    c = input("Deploy :\n(1) | Nginx\n(2) | Centos")
    if c == "1" or c == "nginx":
        os.system("sudo docker pull nginx")
        s = input("Enter the port that you want to open >>:")
        os.system("sudo docker run -d -p" " " + s )

    elif c == "2" or c ==  "centos":
        os.system("sudo docker pull centos")
        a = input("Enter A command for centos >>:")
        os.system("sudo docker run -d centos /bin/bash -c" " "+ a)

def DockerUI():
    print("<< Pulling DockerUI >>")
    sleep(0.5)
    os.system("sudo docker pull abh1nav/dockerui:latest")
    os.system("sudo docker run -d -p 9000 -v /var/run/docker.sock:/docker.sock \--name dockerui abh1nav/dockerui:latest -e=/docker.sock")
    sleep(0.5)
    print("Your ip address saved in  /var/log/dockerui.log")
    os.system("sudo touch /var/log/dockerui.log ; sudo chown 0644 /var/log/dockerui.log")
    os.system("ip -4 -o addr show  | awk '{print $4}' > /var/log/dockerui.log")

def Deploy():
        print("Those the images >>:")
        sleep(0.5)
        os.system("sudo docker images")
        choose=input("(1) | Create containers without ports\n(2) | Create containers with ports\nYour choice :")
        if choose == "1":
            b = input("Enter the image that you want to deploy >>:")
            con = int(input("How many Containers Would you like to create :"))
            for i in range(con):
                os.system("sudo docker run -d" " "+ b)
        os.system("sudo docker ps -a")

        if choose == "2":
            c = input("Write the port and image name that you want, for example: 9000:80 [Image_name] >>:")
            con = int(input("How many Containers Would you like to create :"))
            for i in range(con):
                os.system("sudo docker run -d -p" " "+ c)
        os.system("sudo docker ps -a")

def Containers():
    d = input("(1) | Show all Containers Names/IP\n(2) | Enter container ID\nYour Choice :")
    if d == "1":
        print("All the ips and names of the containers that you have >>")
        os.system("sudo docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)")
    elif d == "2":
          ip = input("Enter Container Name/ID :")
          print("Container IP :")
          os.system("docker inspect"+" "+ ip + "| grep  'IPAddress'  | awk 'NR==2 {print $2}' | cut -d '\"' -f2")

def Delete():
        print(">>> Those the containers <<<")
        os.system("sudo docker ps -a")
        choose = input("(1) | Remove Container\n(2) | Remove all containers\n(3) | Remove Images\n(4) | Remove all Images\nYour choice >>:")
        if choose == "1":
            a = input("(1)>>Enter the container id that you want to delete >>:")
            os.system("sudo docker rm -f" " " + a)
            sleep(0.5)
            print("Container >>:" ,a , "Deleted Successfully")

        elif choose == "2":
            s = input("You sure that you want to delete all containers ? (y/n) >>:")
            if s == "y" or s == "yes" or s == "YES":
                print("Delete The containers ..")
                sleep(0.5)
                os.system("sudo docker rm -f `docker ps -a -q`")
            elif s == "n" or s == "no" or s == "NO":
                print("Bye Bye")

        elif choose == "3":
            os.system("sudo docker images")
            image = input("Enetr the Image (Name) or Image (id) to delete >>:")
            print("Deleting >>:", image)
            sleep(0.5)
            os.system("sudo docker rmi" " " + image)
            print(image,"<<Deleted Successfully>>")
            os.system("sudo docker images")

        elif choose == "4":
            q = input("You sure that you want to delete all Images ? (y/n) >>:")
            if q == "y" or q == "yes" or q == "YES":
                print("Delete The Images ..")
                sleep(0.5)
                os.system("sudo docker rmi -f `docker images -a -q`")
            elif q == "n" or q == "no" or q == "NO":
                print("Bye Bye")

def Show():
    print("---Showing All Containers And Images---")
    print("---------Images---------")
    sleep(0.5)
    os.system("sudo docker images")
    print("--------Containers-------")
    sleep(0.5)
    os.system("sudo docker ps -a")

def Nginx():
    print("Pull nginx image and run 2 nginx containers ...")
    for i in range(2):
        os.system("sudo docker pull nginx ; sudo docker run -d -p 80 nginx")
        os.system("sudo docker run -d -p 80 -v /home/guy/Desktop/web:/usr/share/nginx/html nginx")

 ### MENU ###
def main():
    os.system("clear")
    sleep(0.5)
    while True:
        choice = input("""    ------Menu------\n(1)| Install Docker\n(2)| Pull Images\n(3)| Deploy Images\n(4)| Show all images and Containers\n(5)| Delete Containers And images\n
(6)| Pull DockerUI\n(7)| Show container Names/Ips\n(8)| Pull Nginx/Centos\n(9)| Nginx With mount\n(10) | Exit\nYour Choise >>:""")
        if choice == "1":
            Install()

        if choice == "2":
            Pull_Images()

        if choice == "3":
            Deploy()

        if choice == "4":
            Show()

        if choice == "5":
            Delete()

        if choice == "6":
            DockerUI()

        if choice == "7":
            Containers()

        if choice == "8":
            Images()

        if choice == "9":
            Nginx()

        if choice == "10":
            print("Bye Bye")
            break

main()
