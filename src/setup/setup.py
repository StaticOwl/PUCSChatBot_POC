import subprocess
import sys

def check_package(package):
    package_name = package.split('==')[0]
    try:
        output = subprocess.check_output([sys.executable, "-m", "pip", "show", package_name], stderr=subprocess.STDOUT)
        installed_version = None
        for line in output.decode().split('\n'):
            if line.startswith('Version:'):
                installed_version = line.split(' ')[1]
                break
        if installed_version is None:
            return False
        else:
            return package == f"{package_name}=={installed_version}"
    except:
        return False
    
def install(packages):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version",], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        raise Exception("Pip doesn't exist.")
        return False
    
    not_installed = []
    installed = []
    installed_user = []

    for package in packages:
        if check_package(package):
            installed.append(package)
            print("Package already installed: " + package)
            continue
        else:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print("Installed package: " + package)
                installed.append(package)
            except:
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--user"], 
                                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # for users without admin rights
                    print("Installed package with user: " + package)
                    installed_user.append(package)
                except:
                    print(Exception("Package "+ package + " does not exist"))
                    not_installed.append(package)
                    continue

    print("Installed Packages: " + '.'.join(installed))
    if len(installed_user) > 0:
        print("Installed Packages with user: " + '.'.join(installed_user))
    if len(not_installed) > 0:
        print("Not installed Packages: " + ', '.join(not_installed))
        return False
    
    return True


def setup(file_path='src/setup/requirements.txt'):
    with open(file_path) as f:
        packages = f.read().splitlines()
        if len(packages) == 0:
            raise Exception("No packages to install")
            return False
        else: 
            return install(packages)
