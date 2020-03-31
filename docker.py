#!/bin/python3.7

############################Docker script that install Docker, deploy containers, Pull images, and delete images/containers.#######
######

from time import sleep
import os
import datetime

def Install():
    print("<<<Install Docker>>>")
    sleep(0.5)
    os.system("curl - fsSL https: // get.docker.com - o get - docker.sh")
    os.system("bash get - docker.sh")
    print("<<<Docker Installation is Done>>>")


def Pull_Images():
    s = input(">>Enter the image name that you want to pull >>:")
    os.system("sudo docker pull" " " + s)
    sleep(0.5)
    print("Your Image :",s ,"Pulling Successfully")
    sleep(0.5)
    print("The Images :")
    os.system("sudo docker images")


def Deploy():
        print("Those the images :")
        sleep(0.5)
        os.system("sudo docker images")
        b = input("Enter the image that you want to deploy >>:")
        cont = input("How many Containers Would you like to create :")
        for i in cont:
            os.system("sudo docker run -d" " " + b)	
        os.system("sudo docker ps -a")


def Show():
    print("---Showing All Containers And Images---")
    print("---------Images---------")
    sleep(0.5)
    os.system("sudo docker images")
    print("--------Containers-------")
    sleep(0.5)
    os.system("sudo docker ps -a")


def Delete():
        print(">>> Those the containers <<<")
        os.system("sudo docker ps -a")
        choose = input("(1)>>Remove Container\n(2)>>Remove all containers\n(3)>>Remove Images\nYour choice >>:")
        if choose == "1":
            a = input("(1)>>Enter the container that you want to delete >>:")
            os.system("sudo docker stop" " " + a)
            os.system("sudo docker rm" " " + a)
            sleep(0.5)
            print("Container >>:" ,a , "Deleted Successfully")


        elif choose == "2":
            s = input("You sure that you want to delete all containers ? (y/n) >>:")
            if s == "y" or s == "yes" or s == "YES":
                print("Stop The containers..")
                sleep(0.5)
                os.system("docker stop $(docker ps -a -q)")
                print("Delete The containers ..")
                sleep(0.5)
                os.system("docker rm $(docker ps -a -q)")
            elif s == "n" or s == "no" or s == "NO":
                print("Bye Bye")

        elif choose == "3":
            os.system("sudo docker images")
            image = input("Enetr the Image id to delete >>:")
            print("Deleting >>:", image)
            sleep(0.5)
            os.system("sudo docker rmi" " " + image)
            print(image,"<<Deleted Successfully>>")
            os.system("sudo docker images")
        else:
             print("Enter 1 - 3 only !")

def main():
    os.system("clear")
    y = datetime.datetime.now()
    x = datetime.date.today()
    print("------Date :" ,x)
    print("------Time Now :",y.strftime("%R"))
    os.system("docker --version")
    sleep(0.5)
    while True:
        choice = input("    ------Menu------\n(1)>>Install Docker\n(2)>>Pull Images\n(3)>>Deploy Images\n(4)>>Show all images and Containers\n(5)>>Delete Containers And images\n(6)>>Exit\n  Your Choise >>:")
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
            print("Bye Bye")
            break
        else:
            print("Enter 1 - 6 only !")

main()





