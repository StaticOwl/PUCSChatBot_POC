import subprocess
import sys

def install(packages):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version",])
        for package in packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print("Installed package: " + package)
            except:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--user"]) # for users without admin rights
                print("Installed package with user: " + package)
    except:
        raise Exception("pip is not installed")



with open('src/requirements.txt') as f:
    packages = f.read().splitlines()
    if len(packages) == 0:
        raise Exception("No packages to install")
    else: 
        install(packages)