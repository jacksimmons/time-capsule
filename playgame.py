#Non-saving version
import main
import random
import os
import sys
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def loadgame():
    print('Loading...')
    time.sleep(0.3)
    print('Loading... 7%')
    time.sleep(0.1)
    print('Loading... 16%')
    time.sleep(0.05)
    print('Loading... 23%')
    time.sleep(0.2)
    print('Loading... 47%')
    time.sleep(0.1)
    print('Loading... 63%')
    time.sleep(0.3)
    print('Loading... 78%')
    time.sleep(0.05)
    print('Loading... 93%')
    time.sleep(0.2)
    cls()
    print('--- Game Loaded ---')

def game():
    castle_lv,vault_lv,academy_lv,barracks_lv,archery_lv,stable_lv,helipad_lv,workshop_lv = 0,0,0,0,0,0,0,0
    time.sleep(1)
    cls()
    world_options = True
    while world_options == True:
        world_options = input('What would you like to do?\n\nm - Map\n\nc - Go to castle\n\na - Attack\n\n> ')
        if world_options == 'c':
            world_options = False
            return castle_lv,vault_lv,academy_lv,barracks_lv,archery_lv,stable_lv,helipad_lv,workshop_lv
        else:
            print('That is not a valid option.')
            cls()
# def construction():
#     if

def castle():
    castle_lv,vault_lv,academy_lv,barracks_lv,archery_lv,stable_lv,helipad_lv,workshop_lv = game()
    cls()
    castle_options = 0
    looper = True
    build_choices = ['c','v','a','b','r','s','h','w','p','q']
    while looper == True:
        cls()
        castle_options = input('c - Construct\n\nr = Research\n\nt = Train\n\nq = Leave castle\n\n> ')
        if castle_options == 'c':
            time.sleep(1)
            cls()
            build_selection = input('---Construction tree---\n\nBasic buildings:\n\nCastle:' + str(castle_lv) + '\n\nVault:' + str(vault_lv) + '\n\nAcademy:' + str(academy_lv) + '\n\nBarracks:' + str(barracks_lv) + '\n\nRecon zone:' + str(archery_lv) + '\n\nStable:' + str(stable_lv) + '\n\nHelipad:' + str(helipad_lv) + '\n\nWorkshop:' + str(workshop_lv) + '\n\nType the first letter of the building you wish to upgrade, go to production buildings (p) or quit (q)\n\n> ')
            if build_selection in build_choices:
                if build_selection == 'v':
                    if castle_lv > vault_lv:
                        print('The cost to build vault is:\n' + 5000 * vault_lv + ' timber\n' + 4500 * vault_lv + ' stone\n' + 6400 * vault_lv + ' metal.')
                        timber_cost,stone_cost,metal_cost = (5000 * vault_lv),(4500 * vault_lv),(6400 * vault_lv)
                        time.sleep(1)
                        if timber > timber_cost and stone > stone_cost and metal > metal_cost:
                            construction_time = (4 * vault_lv) + (vault_lv * vault_lv)
                            cls()
                            print('Construction has begun!')
                            looper == False
                            looper = construction(construction_time,vault_lv)
                elif build_selection == 'a':
                    if vault_lv > academy_lv:
                        print('The cost to build academy is:\n' + 5500 * academy_lv + ' timber\n' + 5500 * academy_lv ' stone\n' + 5500 * va)
                elif build_selection == 'p':
                    print('Coming soon')
                elif build_selection == 'q':
                    print('a')
castle()
