import shutil
import os
import inquirer
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def remove_folder(folder):
    shutil.rmtree(folder)

def clear():
    os.system('cls')

def detect_drives():
    paths_to_search = []
    for drive_letter in range(65, 91):
        drive = chr(drive_letter) + ':\\'
        if os.path.isdir(drive):
            paths_to_search.append(drive)
    
    return paths_to_search

def gprint(t):
    print(Fore.GREEN+t)

def rprint(t):
    print(Fore.RED+t)

def mprint(t):
    print(Fore.MAGENTA+t)

def delete_file(file):
    os.remove(file)

LOCALAPPDATA = os.getenv('LOCALAPPDATA')
ROAMINGAPPDATA = os.getenv('APPDATA')


EXPLOIT_DIRS = {
    LOCALAPPDATA+'\\Wave',
    'C:\\SolaraTab',
    'C:\\ProgramData\\Solara',
    LOCALAPPDATA+'\\Temp\\Solara.Dir',
}

EXPLOIT_FILES = [
    ROAMINGAPPDATA+'\\Microsoft\\Windows\\Start Menu\\Programs\\Wave.lnk',
]

ROBLOX_PATH = LOCALAPPDATA+"\\Roblox"
BLOXSTRAP_PATH = LOCALAPPDATA+"\\Bloxstrap"

def uninstall_roblox():
    mprint("Searching For Roblox...")
    if os.path.isdir(ROBLOX_PATH):
        remove_folder(ROBLOX_PATH)
        gprint(ROBLOX_PATH+" has been deleted.")
    else:
        rprint("You do not have roblox installed.")
    
def uninstall_bloxstrap():
    mprint("Searching For Bloxstrap...")
    if os.path.isdir(BLOXSTRAP_PATH):
        remove_folder(BLOXSTRAP_PATH)
        gprint(BLOXSTRAP_PATH+" has been deleted.")
    else:
        rprint("You do not have roblox installed.")

def delete_exploits():
    mprint("Searching For Exploit Directoires...")
    for dir in EXPLOIT_DIRS:
        if os.path.isdir(dir):
            remove_folder(dir)
            gprint(dir+" has been deleted.")
        else:
            rprint(dir+" could not be found")
    mprint("Searching For Exploit Files...")
    for file in EXPLOIT_FILES:
        if os.path.isfile(file):
            delete_file(file)
            gprint(file+" has been deleted.")
        else:
            rprint(file+" could not be found")


def full_clean():
    uninstall_roblox()
    uninstall_bloxstrap()
    delete_exploits()

def main():
    clear()
    RETURNMSG = "Press enter to go back"
    mprint("Please make sure this is ran as an admin.")
    mprint("This is made by xz (@swipingfraud2) rip to all the fallen exploiters of the 2024 august banwave")
    option = inquirer.list_input("Cleaning Level",choices=[
        "Delete Exploits + Exploit Files",
        "Delete Roblox",
        "Uninstall Bloxstrap",
        "All",
    ])
    clear()
    if option == "Delete Exploits + Exploit Files":
        delete_exploits()
        input(RETURNMSG)
    elif option == "Delete Roblox":
        uninstall_roblox()
        input(RETURNMSG)
    elif option == "Uninstall Bloxstrap":
        uninstall_bloxstrap()
        input(RETURNMSG)
    elif option == "All":
        full_clean()
        input(RETURNMSG)
    main()

main()
