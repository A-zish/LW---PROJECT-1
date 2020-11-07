import os
import getpass


def container_creation():
	ch=input("Which container you want to launch: ubuntu or   centos??")
	if ch=="ubuntu":
		print("Pulling ubuntu image from hub.docker.com....please wait\n\n")
		os.system("docker pull ubuntu:latest")
		name= input("Enter the container name:")
		os.system("docker run -itd --name {} ubuntu:latest".format(name))

		w=input("Do you want to work on the OS(Y/N)")
		if w=="Y":
			os.system("docker attach {}".format(name))



	elif ch=="centos":
		print("Pulling ubuntu image from hub.docker.com....please wait\n\n")
		os.system("docker pull centos:latest")
		name= input("Enter the container name:")
		os.system("docker run -itd --name {} centos:latest".format(name))

		w=input("Do you want to work on the OS(Y/N)")
		if w=="Y":
			os.system("docker attach {}".format(name))

	else:
		print("Wrong OS selected....please choose again")
		container_creation()
				
        
	
	
password= getpass.getpass("ENTER THE PASSWORD:")

if password!= "as":
	print("WRONG PASSWORD")
	exit()

take= input("Want to install docker-ce??Press enter to continue")
os.system("yum install docker-ce --nobest")

input("Press enter to start the service")
os.system("systemctl start docker")

while True:
	print("press 1: To check the status of docker")
	print("press 2: To check docker info")
	print("press 3: To check the images available")
	print("press 4: To check the containers launched")
	print("press 5: To launch a container")
	print("press 6: To exit")
	ch=input("Enter your choice:")

	if int(ch)==1:
		os.system("systemctl status docker")
	elif int(ch)==2:
		os.system("docker info")
	elif int(ch)==3:
		os.system("docker images")
	elif int(ch)==4:
		os.system("docker ps -a")
	elif int(ch)==5:
		container_creation()
	elif int(ch)==6:
		exit()
	else:
		print("Wrong choice")
	
		
