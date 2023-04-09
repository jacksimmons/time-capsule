#!/usr/bin/python
#Non-saving version
import sys
print('v0.1')
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def savedata_exists(filepath, mode):
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False

    return True

def loadoptions():
    titleoptions = ['p','q']
    option = 0
    option = input('Welcome!\n\np - Play\n\nq - Quit\n\n> ')
    while option != 0:
        if option == 'p':
            cls()
            break
        elif option == 'q':
            cls()
            sys.exit()
        else:
            print('\'' + option + '\' is not a valid option.')
            break
    return loadoptions
loadoptions()
