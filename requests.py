import sys
import time
import random
import cookielib
import mechanize
import os
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
        time.sleep(random.random() * 0.1)

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
    runntxt(GL+"   /_|__|_\    \033[33;1m* \033[36;1mAuthor  : \033[32mRNz CL41 ")
    runntxt(GL+"   /_|__|_\    \033[33;1m* \033[36;1minstagram :\033[32m @riski_yans")
    runntxt(GL+"   /_\__/_\    \033[90;1m=================================> ")
    runntxt(GL+"    \ || / _)")
    runntxt(GL+"      ||  ( )")
    runntxt(GL+"      \\___//")
    runntxt(GL+"      `---'")
time.sleep(0)
banner()

tik (Y+"* \033[0;1m HASIL TANGKAPAN ANDA ")
tik (G+"================================")
