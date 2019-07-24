import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#Update system
print(" ")
print(bcolors.OKGREEN + "Updating your system as sudo" + bcolors.ENDC)
print(" ")
os.system("sudo apt-get update")

#Asks for Version
print("  ")
version = input(bcolors.OKGREEN + "What version of nodejs do you want? (type the number of the version 8, 10, 11, 12):" + bcolors.ENDC)

#Check version
if version == "8":
    print(bcolors.WARNING + "Installing nodejs v.8x" + bcolors.ENDC)
    os.system("curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")
if version == "10":
    print(bcolors.WARNING + "Installing nodejs v.10x" + bcolors.ENDC)
    os.system("curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")
if version == "11":
    print(bcolors.WARNING + "Installing nodejs v.11x" + bcolors.ENDC)
    os.system("curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")   
if version == "12":
    print(bcolors.WARNING + "Installing nodejs v.12x" + bcolors.ENDC)
    os.system("curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")

#Checking if version installed
print(bcolors.OKGREEN)
print("Node:")
os.system("node -v")
print("  ")
print("NPM:")
os.system("npm -v")
print(bcolors.ENDC)

#Tell the user that the process has finished
print(bcolors.OKGREEN + "The process is completed" + bcolors.ENDC)
print("  ")
print(bcolors.WARNING + "Check for any errors" + bcolors.ENDC)
print("  ")
print(bcolors.OKBLUE + "Thanks for using this tool, please ask for more installations in the github repository" + bcolors.ENDC)
print("  ")

