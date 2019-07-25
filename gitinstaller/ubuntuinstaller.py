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

# Updating system
print(bcolors.OKGREEN + "Updating your system" + bcolors.ENDC)
os.system("sudo apt-get update")

# Installing Git
os.system("apt-get install git")
print(bcolors.OKGREEN + "Operation completed")
print("   ")
print("Checking version")
os.system("git --version")

