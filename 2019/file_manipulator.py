# Initial commit timestamp: Mar 30 2019

import os
import time

class default():
    exited = False
    titlerange1,titlerange2 = 1,4
    range1,range2 = 1,5
    version = '0.1.0'

d = default()

def cls(wait):
    time.sleep(wait)
    os.system('cls')

def fileinfo(inp,inplist):
    print()

def title():
    while True:
        inp = int(input('''---Selection Screen---
1. Create a file
2. Edit a file
3. Rename a file
4. Delete a file\n> '''))
        if inp in range(d.range1,d.range2):
            fcl = False
            if inp == 1:
                filename = str(input("\nPlease enter your file's directory\n> "))
                open(filename,'x')
                print("File " + filename + " has been created!\n")
            elif inp == 2:
                filename = str(input("Please give the directory of the file you wish to edit\n> "))
                edittype = str(input("Do you want to (w)rite, (a)ppend or (c)ancel?\n> "))
                if edittype == 'w' or 'a' or 'c':
                    if edittype == 'w' or edittype == 'a':
                        contents = str(input('''What do you want to put in this file?
FILENAME: ''' + filename + '''
MODE: ''' + edittype + '''\n> '''))
                        file = open(filename,'w')
                        if edittype == 'w':
                            file.write(contents)
                            print("File has been truncated and contents have been added to '" + filename + "'.")
                            file.close()
                        else:
                            file.append(contents)
                            print("Contents have been appended to '" + filename + "'.")
                            file.close()
                    else:
                        print()
            elif inp == 3:
                filename = str(input("Please give the directory of the file you wish to change\n> "))
                rename = str(input("Please enter the new directory of your file\n> "))
                os.rename(filename,rename)
                print("'" + filename + "' has been renamed to '" + rename + "'!")
            else:
                filename = str(input("Which file deserves to be deleted?\n> "))
                os.remove(filename)
                print("'" + filename + "' has been sent to the void.")

def basictitle():
    while d.exited != True:
        inp = int(input('''---File Editor---
1. Start
2. Help
3. Info\n> '''))
        if inp in range(d.titlerange1,d.titlerange2):
            if inp == 1:
                exited = True
                cls(0),title()
            elif inp == 2:
                print()#Help
            else:
                print('''\nFile Editor
VERSION: ''' + d.version + '\n')

basictitle()
