import os
from game import cls, setup

#~~~~~~~~~~~~~~GLOBALS~~~~~~~~~~~~~~#

titlescreenoptions = ['p','h','q']

HP = '0'
AGI = '0'
POW = '0'
enemy = ''
enemy_HP = '0'
enemy_AGI = '0'
enemy_POW = '0'

#~~~~~~~~~~~~~~TITLE SCREEN~~~~~~~~~~~~~~#

def titlescreen():
    cls()
    loadgameinput = input('\t\t☭ Welcome to communism! ☭\n\t\t\tp = Play\n\t\t\th = Help\n\t\t\tq = Quit\n')
    
    if loadgameinput in titlescreenoptions:
        print("Success")
    else:
        print("Error - That is not a valid choice!")
        
    return loadgameinput

def titleinput():
    loadgameinput = ''
    while loadgameinput != 'q':
        print("hi")
        loadgameinput = titlescreen()
        if loadgameinput == 'p':
            cls()
            # If unsuccessful, an enter press will already have been done to exit
            if (setup()):
                input()
        if loadgameinput == 'h':
            print("Help goes here")
        elif loadgameinput == 'q':
            print("Come again soon!")
            break
            
titleinput()
