import os
import time
from game import cls, new_game_setup, load_save_setup

#~~~~~~~~~~~~~~GLOBALS~~~~~~~~~~~~~~#

TITLE_OPTIONS = [
    "play", "p",
    "help", "h",
    "quit", "q"
]

PLAY_OPTIONS = [
    "new", "n",
    "load", "l",
    "delete", "d",
    "q"
]

#~~~~~~~~~~~~~~TITLE SCREEN~~~~~~~~~~~~~~#

def titlescreen():
    global TITLE_OPTIONS
    titlescreeninput = input("""☭ Welcome to communism! ☭
        (p)Play
        (h)Help
        (q)Quit\n> """)
    
    if titlescreeninput not in TITLE_OPTIONS:
        print("Please enter a valid choice!")
        input()

    return titlescreeninput

def playscreen():
    global PLAY_OPTIONS
    playscreeninput = input("""Select a way to play:
        (n)New Game
        (l)Load Save
        (d)Delete Save
q - Go back\n> """
    )

    if playscreeninput not in PLAY_OPTIONS:
        print("Please enter a valid choice.")
        input()

    return playscreeninput

def title_input():
    inp = ""
    while inp not in ["quit", "q"]:
        cls()
        inp = titlescreen().lower()
        if inp in ["play", "p"]:
            cls()
            play_input()
        elif inp in ["help", "h"]:
            print("Help goes here")
    print("Goodbye!")

def play_input():
    inp = ""
    while inp not in ["quit", "q"]:
        cls()
        inp = playscreen().lower()
        if inp in ["new", "n"]:
            cls()
            # If unsuccessful, an enter press will already have been done to exit
            if (new_game_setup()):
                input()
        elif inp in ["load", "l"]:
            cls()
            if os.stat("save.pkl").st_size == 0:
                input("No save exists.\n> ")
            elif load_save_setup():
                input()
        elif inp in ["delete", "d"]:
            cls()
            with open("save.pkl", "w") as file:
                file.write("")
            input("Save deleted.\n> ")
            
title_input()
