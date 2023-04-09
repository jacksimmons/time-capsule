#!/usr/bin/python
import sys
print('v0.1')
import os
newfile = '''['00','00','00']
0
0
0
0
0
0
0
['01','00','00','00','00','00','00','00'] bld.basic
['00','00','00','00','00','00','00','00'] bld.prd
['00','00','00','00','00','00'] rsc.inf
['00','00','00','00','00','00'] rsc.arch
['00','00','00','00','00','00'] rsc.cav
['00','00','00','00','00','00'] rsc.air
['00','00','00','00','00'] rsc.sei
['00','00','00','00','00','00'] rsc.arm
00
00
00
00
00
00
00
00
00
['00','00','00','00','00','00'] rsc.einf
['00','00','00','00','00','00'] rsc.earch
['00','00','00','00','00','00'] rsc.ecav
['00','00','00','00','00','00'] rsc.eair
['00','00','00','00','00'] rsc.esei
['00','00','00','00','00','00'] rsc.earm
['10','10','10'] rsc.cstr
00 rsc.fuinar
00 rsc.fuarar
00 rsc.fucaar
00 rsc.fuaiar
00 rsc.1tierdmg
00 rsc.1tierdef
00 rsc.1tierhp
00 rsc.1tierspd
00 rsc.pstr1
00 rsc.pstr2
00 rsc.pstr3
00 rsc.pstr4
00 rsc.pstr5
00 rsc.pstr6inf
00 rsc.pstr6arch
00 rsc.pstr6cav
00 rsc.pstr6air
00 rsc.pstr6sei
00 rsc.sab1
00 rsc.sab2
00 rsc.sab3
00 rsc.sab4
00 rsc.sab5
00 rsc.sab6inf
00 rsc.sab6arch
00 rsc.sab6cav
00 rsc.sab6air
00 rsc.sab6sei
00 rsc.inti
00 rsc.arti
00 rsc.cati
00 rsc.aiti
00 rsc.seti'''

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

def savedata_locate():
    f = savedata_exists('savedata.txt', 'r')
    if f == False:
        loadoptions = 'New'
        selected_option = 'invalid'
        return loadoptions, selected_option
    if f == True:
        loadoptions = 'Continue'
        selected_option = 1
        return loadoptions, selected_option

def titlescreen_concept():
    loadoptions, selected_option = savedata_locate()
    if loadoptions == 'Continue':
        titleoptions = 'c = Continue game\n\nn = New game\n\ns = Save options'
        return loadoptions, selected_option, titleoptions
    elif loadoptions == 'New':
        titleoptions = 'n = New game\n\ns = Save options'
        return loadoptions, selected_option, titleoptions

def titlescreen():
    loadoptions, selected_option, titleoptions = titlescreen_concept()
    option = input('Please select an option:\n\n' + titleoptions + '\n\n')
    if selected_option == 'invalid':
        if option == 'n':
            print('Success')
            f = open('savedata.txt', 'w')
            f.write(newfile)
            print('Account created.')
            playgame = 'y'
        elif options == 's':
            print('Save data:\n---Empty---')
        else:
            print('Invalid input')
    elif selected_option != 'invalid':
        f = open('savedata.txt')
        lines = f.readlines()
        account_line = lines[0]
        account_level = account_line[2:4]
        f.close()
        if option == 'c':
            playgame = 'y'
        elif option == 'n':
            confirmation = input('\nAre you sure you want to delete the following savefile? (y/n)\n\nLevel: ' + account_level + '\n\n')
            if confirmation == 'y':
                os.remove('savedata.txt')
                print('\nSave file deleted.')
                f = open('savedata.txt', 'w')
                f.write(newfile)
                print('New account created.')
                playgame = 'y'
            elif confirmation == 'n':
                print('\nSave file spared.')
        elif option == 's':
            print('Save data:\nName:\n---' + account_name + '\nLevel:\n---' + account_level)
    return loadoptions
titlescreen()
