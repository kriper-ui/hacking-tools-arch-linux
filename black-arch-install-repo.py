import os
import time

user = int(input())
yay = int(input())

print("Hello user this is a script for arch-linux to hacking!")

print("Ok type 1 if you want install hyperland config, 2 if you want to install tools to hacking and 3 to install yay")

print(user)

if user == 1:

    print("First let's install git to download IMPORTANTE THAT IT NEED SOMETIMES RUN WITH SUDO!")
    print("Do you have yay installed? enter 1 if yes and 0 if no")
    print(yay)
    if yay == 0:
        os.system("sudo pacman -Syu")
    else:
        os.system("yay")
    os.system("sudo pacman -S hyperland")
    os.system("sudo pacman -S git")
    os.system("git clone --depth=1 https://github.com/JaKooLit/Arch-Hyprland.git ~/Arch-Hyprland")
    os.chdir("/Arch-Hyprland")
    os.system("chmod u+x install.sh && ./install")

elif user == 2:

    print("Ok let's do that IMPORTANTE THAT NEED THEN ENTER SUDO PASSWORD")
    os.mkdir("file-repo")
    os.chdir("file-repo")
    os.system("wget https://blackarch.org/strap.sh")
    os.system("chmod u+x strap.sh && sudo ./strap.sh")
    time.sleep(30)
    print("Starting installing and I will install virtualbox if you want to practice with vulnhub or install kali!")
    os.system("sudo pacman -S nmap dirb metasploit wpscan hydra john netcat nikto ghidra virtualbox")
    print("I install basics tools to do CTF you must install more if you want!")

elif user == 3:

    print("Let's install yay IMPORTANTE THAT IT NEED SOMETIMES RUN WITH SUDO!")
    os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
    time.sleep(35)
    print("Yay was installed correct you can use it!!")

else:

    print("wrong option")
    return
