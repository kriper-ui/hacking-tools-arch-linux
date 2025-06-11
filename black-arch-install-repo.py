import os
import time

perm = os.getuid()

if perm != 0:
    print("Script may be run how root.")
else:
    
print("Hello user this is a script for arch-linux to hacking!")

print("Ok type 1 if you want install hyperland config, 2 if you want to install tools to hacking and 3 to install yay")

option = int(input())

if option == 1:
    print("Installing process start")
    print("Do you have yay installed? enter 1 if yes and 0 if no")
    os.system("sudo pacman -Syu")
    os.system("sudo pacman -S hyperland")
    os.system("sudo pacman -S git")
    os.system("git clone --depth=1 https://github.com/JaKooLit/Arch-Hyprland.git ~/Arch-Hyprland")
    os.chdir("/Arch-Hyprland")
    os.system("chmod u+x install.sh && ./install")

elif option == 2:
    print("Process start")
    os.mkdir("file-repo")
    os.chdir("file-repo")
    os.system("wget https://blackarch.org/strap.sh")
    os.system("chmod u+x strap.sh && sudo ./strap.sh")
    time.sleep(30)
    print("Starting installing and I will install virtualbox if you want to practice with vulnhub or install kali!")
    os.system("sudo pacman -S nmap dirb metasploit wpscan hydra john netcat nikto ghidra virtualbox")
    print("Install of basics tools to do CTF was installed if you want to install more you can do it with pacman.")

elif option == 3:
    print("Install process was started.")
    os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
    time.sleep(35)
    print("Yay was installed correct you can use it!!")

else:
    print("wrong option")
    return
