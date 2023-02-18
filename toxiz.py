import os, sys, time
from time import sleep
rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def ani(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.01)
def logo ():
  os.system("clear")
  os.system("""echo '

       _____    ___   __  __  ___   _____
      |_   _|  / _ \  \ \/ / |_ _| |__  /
        | |   | | | |  \  /   | |    / /
        | |   | |_| |  /  \   | |   / /_
        |_|    \___/  /_/\_\ |___| /____|
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  ╔════════════════════════════════════════════════╗
  ║            [✓] NAMA TOOLS : TOXIZ              ║
  ║            [✓] GITHUB : ALVI TOXIZ             ║
  ║            [✓] FACEBOOK : ALVI TOXIZ           ║
  ║            [✓] TELEGRAM : TOXIZ Developer      ║
  ║            [✓] INSTAGRAM : B4jing4n_18         ║
  ║            [✓] YOUTUBE : ALVI TOXIZ            ║
  ╚════════════════════════════════════════════════╝\n----------------------------------------------------'|lolcat""")
  ani(r+"\t<"+bl+"p"+r+">"+g+" MENYIAPKAN MODULE 🐹 "+r+"<"+bl+"/p"+r+">")
  os.system("echo '----------------------------------------------------'| lolcat")

logo ()
def main ():

  x = input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m TEKAN ENTER BRO \033[1;0;40m")
  logo ()
  os.system('''termux-setup-storage
yes | pkg update
yes | pkg upgrade
yes | pkg install python
yes | pkg install python2
pip3 install pip requests mechanize beautifulsoup4 infocircle myspeed
pip2 install pip requests mechanize beautifulsoup4
pip install --upgrade pip
yes | pkg install fish
yes | pkg i zsh
yes | pkg install ruby
yes | pkg install git
yes | pkg install php
yes | pkg install perl
yes | pkg install nmap
yes | pkg install bash
yes | pkg install clang
yes | pkg install nano
yes | pkg install w3m
yes | pkg install figlet
yes | pkg install cowsay
yes | pkg install curl
yes | pkg install tar
yes | pkg install zip
yes | pkg install unzip
yes | pkg install tor
yes | pkg install wget
yes | pkg install wireshark
yes | pkg install wgetrc
yes | pkg install wcalc
yes | pkg install bmon
yes | pkg install unrar
yes | pkg install toilet
yes | pkg install proot
yes | pkg install net-tools
yes | pkg install golang
yes | pkg install chroot
yes | pkg install macchanger
yes | pkg install openssl
yes | pkg install cmatrix
yes | pkg install openssh
yes | pkg install wireshark
yes | pkg install macchanger
yes | pkg install nano
yes | pkg install nmap
yes | pkg install clang
yes | pkg install bash
yes | pkg install proot
yes | pkg install vim
yes | pkg install nala
yes | pkg install apktool
yes | pkg install fish
yes | pkg install openjdk-17
yes | pkg install tsu
yes | pkg install mc
yes | pkg install php
yes | pkg install zsh
yes | pkg install net-tools''')
  print("\t\033[1;30;40m[\033[1;34 ;40m+\033[1;30;40m]\033[1;32;40m SUDAH SELESAI YAH BANG:) \033[1;0;40m")
  logo ()
  pkg = input("\t\033[1;30;40m[\033[1;34;40m+\033[1;30;40m]\033[1;32;40m PENGEN INSTAL ULANG? [Y/N] : \033[1;39;40m")
  if pkg == "y" or pkg == "Y":
    os.system("pkg list-installed")
  else:
    sys.exit ()
if __name__=='__main__':
  main ()
