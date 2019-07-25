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

## Updating system and install node
print(bcolors.OKGREEN)
print( "Updating your system" + bcolors.ENDC)
os.system("sudo apt update && sudo apt upgrade -y && sudo apt install nodejs")

## Installing nodejs
print(bcolors.OKGREEN)
print("Installing nodejs")
print(bcolors.ENDC)
os.system("sudo apt install nodejs")

# Checking versions

print(bcolors.OKGREEN)
print("Node version:")
os.system("node -v")
print("  ")
print("NPM version:")
os.system("npm -v")
print(bcolors.ENDC)

# Installing NVM

print(bcolors.OKGREEN + "Installing NVM (Node Version Manager)")
print(bcolors.ENDC)
os.system("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash")
os.system("sudo apt install curl -y && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash")

# Install node from NVM

print(bcolors.OKGREEN + "Installing Node from NVM")
os.system("nvm install node")
print(bcolors.ENDC)

# Install React Native

print(bcolors.OKGREEN + "Installing React Native")
os.system("npm install -g react-native-cli")
print(bcolors.ENDC)

# Checking for version
print(bcolors.OKGREEN + "React Native version" + bcolors.ENDC)
os.system("react-native -v")
print(bcolors.OKBLUE)
print("Operation Completed")
print(bcolors.ENDC)



