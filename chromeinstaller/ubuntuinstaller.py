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
print(bcolors.OKGREEN)
print("Updating your system with sudo")
print(bcolors.ENDC)
os.system("sudo apt-get update")

#Installing Chrome
print(bcolors.OKGREEN)
print("Installing Google Chrome Stable Version")
print(bcolors.ENDC)
os.system("wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -")
os.system("echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list")
os.system("sudo apt-get install google-chrome-stable")

#Action Completed
print(bcolors.OKGREEN)
print("Installation Completed")
print(bcolors.ENDC)
print(bcolors.WARNING + "Check for any erros")
print(bcolors.ENDC)

#Run program
print(bcolors.OKGREEN + "Running the program" + bcolors.ENDC)
print("  ")
print("Thanks for using this tool, please ask for more installations in my github repository")
os.system("google-chrome-stable")
print(bcolors.ENDC)

