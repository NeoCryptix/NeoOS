TCYAN = '\033[36m'  # reset to the defaults
TWHITE = '\033[37m'  # reset to the defaults
TRED = '\033[31m'  # reset to the defaults
TBLUE = '\033[34m'  # reset to the defaults
TPURPLE = '\033[35m'  # reset to the defaults
TGREEN = '\033[32m'  # reset to the defaults
TYELLOW = '\033[33m'  # reset to the defaults
TORANGE = '\033[33m'  # reset to the defaults

import os
from os import environ

os.system('cls')
print(TWHITE + 'Not logged in')
print('NeoOS v2.1dev6')
print('Last updated 11/16/22')
print('Made by NeoCryptix')

input('\n\nPress ENTER to return to the command portal.')

import main
main.main()