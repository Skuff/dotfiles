import sys
import os

sys.ps1 = "\033[31m\033[1m>>> \033[0m"
sys.ps2 = "\033[33m\033[1m... \033[0m"

def clear():
    os.system('clear')
