# Initial commit timestamp: Sep 16 2018
# I suspect this was actually older, by the strange use of tuples to store strings

import sys
import random
rarityList = ["Common", "Uncommon", "Rare", "Super Rare", "Epic", "Mythic", "Legendary"]
rarity = ('')
common = ('')
rare = ('')
super_rare = ('')
epic = ('')
mythic = ('')
legendary = ('')
history = [""]

def menu():
    print ("\t\tWhat would you like to do?\n")
    print ("\to = Open a box\n\tv = View droprates\n\th = History\n\tq = Quit")
    answer = ('')
    answer = input()
    correctanswer = ["o","v","h","q"]
    if answer in correctanswer:
        print ("Done!")
    else:
        print("Please try again.")
        return
menu()
        

def main():
    global answer
    if answer != "q":
        answer = menu()
        if answer == "o":
            raritydropped = random.randint(1, 100)
            if raritydropped <= 30:
                rarity = common
                cong = ("")
            elif raritydropped >= 30 and raritydropped < 55:
                rarity = uncommon
                cong = ("Nice.")
            elif raritydropped >= 55 and raritydropped < 70:
                rarity = rare
                cong = ("Cool!")
            elif raritydropped >= 70 and raritydropped < 82:
                rarity = super_rare
                cong = ("Wow!")
            elif raritydropped >= 82 and raritydropped < 90:
                rarity = epic
                cong = ("Well done!")
            elif raritydropped >= 90 and raritydropped < 94:
                rarity = mythic
                cong = ("Awesome!")
            else:
                rarity = legendary
                cong = ("Congratulations!!!")
            print (cong + "you got a " + rarity + " drop!")
            history.append(rarity)
        elif answer == "v":
            print("\tDroprates:\n\bCommon = 30%\n\bUncommon = 25%\n\bRare = 15%\n\bSuper rare = 12%\n\bEpic = 8%\n\bMythic = 6%\n\bLegendary = 4%")
        elif answer == "h":
            print (history)
    else:
        print("Thanks for playing!")
main()
