import platform
import os

def clearScreen():
    if(platform.system() == 'Windows'):
        os.system("cls")
    else:
        os.system("clear")