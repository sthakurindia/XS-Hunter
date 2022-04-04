import requests
import sys
import os, shutil
import random
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', type=str,dest="string", help="Save the results to text file")
args = parser.parse_args()
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

ALL_COLORS = [style.GREEN, style.RED, style.YELLOW, style.BLUE, style.MAGENTA, style.CYAN, style.WHITE]
RESET = style.RESET

def get_version():
    try:
        return open("version","r").read().strip()
    except:
        return '1.2'


__VERSION__ = get_version()

logo="""
██╗  ██╗███████╗      ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
╚██╗██╔╝██╔════╝      ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ╚███╔╝ ███████╗█████╗███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██╔██╗ ╚════██║╚════╝██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██╔╝ ██╗███████║      ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝      ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"""

def do_zip_update():
    success=False

    # Download Zip from git
    # Unzip and overwrite the current folder

    if success:
        print("XS-HUNTER was updated to the latest version")
        print("Please run the script again to load the latest version")
    else:
        print("Unable to update XS-HUNTER")
        print("Grab The Latest one From https://github.com/sthakurindia/XS-Hunter.git")

    sys.exit()

def do_git_update():
    success=False
    try:
        os.system("git checkout .")
        os.system("git pull https://github.com/sthakurindia/XS-Hunter HEAD")
        clr()
        print(random.choice(ALL_COLORS) + logo + RESET)
        print(style.RED+"\n  MADE BY HACKERSTHAKUR  "+style.CYAN+"       Contact: Hackersthakurindia@gmail.com")
        print(style.RED+"\tVersion 1.2\n\n"+RESET)
        success = True

    except:
        success = False
    print("\n")

    if success:
        print("XS-HUNTER was updated to the latest version")
        print("Please run the script again to load the latest version\n")
    else:
        print("Unable to update XS-HUNTER")
        print("Make Sure To Install 'git' ")
        print("Then run command:")
        print("git checkout . && git pull https://github.com/sthakurindia/XS-Hunter HEAD")
    sys.exit()

def update():
    if shutil.which('git'):
        do_git_update()
    else:
        do_zip_update()
def check_for_updates():
    print("Checking for updates")
    try:
        fver = requests.get("https://raw.githubusercontent.com/sthakurindia/XS-Hunter/main/version").text.strip()
    except:
        fver = requests.get("https://raw.githubusercontent.com/sthakurindia/XS-Hunter/main/version",timeout=5).text.strip()

    
    if fver != __VERSION__:
        print("An update is available")
        print("Starting update...")
        update()
        
    else:
        print("XS-HUNTER is up-to-date")
        print("Starting XS-HUNTER\n")
        


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def XSS():
    if args.string is not None:
        wrtf=1
    else:
        wrtf=0
    if wrtf==1:
        wrt=open(str(args.string),'w')
        wrt.write("")
        wrt.close()
        wrt=open(str(args.string),'a')
        req=''
        for i in sys.stdin:
            to=0
            try:
                req = requests.get(i, 'html.parser',timeout=3).text
            except:
                to = 1
            if "alert(" in str(req):
                print(style.RED +"[XSS] "+i)
                wrt.write("[XSS] "+i)
            elif 'sql' in str(req):
                print(style.RED +"[SQL INJECTION] "+i)
                wrt.write("[SQL INJECTION] "+i)
            elif to == 1:
                print(style.YELLOW +"[TIMEOUT] "+i)
            else:
                print(style.GREEN +"[NOT VULN] "+i)
        wrt.close()
    else:
        req=''
        for i in sys.stdin:
            to=0
            try:
                req = requests.get(i, 'html.parser',timeout=3).text
            except:
                to = 1
            if "alert(" in str(req):
                print(style.RED +"[XSS] "+i)
            elif 'sql' in str(req):
                print(style.RED +"[SQL INJECTION] "+i)
            elif to == 1:
                print(style.YELLOW +"[TIMEOUT] "+i)
            else:
                print(style.GREEN +"[NOT VULN] "+i)
    if args.string is not None:
        print(style.MAGENTA +"OUTPUT SAVED IN "+style.CYAN+str(args.string))
    else:
        pass
def menu():
    clr()
    print(random.choice(ALL_COLORS) + logo + RESET)
    print(style.RED+"\n  MADE BY HACKERSTHAKUR  "+style.CYAN+"       Contact: Hackersthakurindia@gmail.com")
    print(style.RED+"\tVersion 1.2\n\n"+RESET)
    check_for_updates()
    sleep(1)
    clr()
    print(random.choice(ALL_COLORS) + logo + RESET)
    XSS()
menu()
