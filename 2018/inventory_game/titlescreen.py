
#~~~~~~~~~~~~~~VARIABLES~~~~~~~~~~~~~~#

titlescreenoptions = ['p','h','q']
loadgameinput = ''

#~~~~~~~~~~~~~~TITLE SCREEN~~~~~~~~~~~~~~#

def titlescreen():
    
    loadgameinput = input('\t\t☭ Welcome to communism! ☭\n\t\t\tp = Play\n\t\t\th = Help\n\t\t\tq = Quit\n')
    if loadgameinput in titlescreenoptions:
        while loadgameinput in titlescreenoptions:
            print("Success")
            break
        else:
            print("ERROR: That is not a valid choice!")
            sys.exit()
    return loadgameinput

def titleinput():
    while loadgameinput != 'q':
        loadgameinput = titlescreen()
        if loadgameinput == 'p':
            open("game.py", mode='r')
        if loadgameinput == 'h':
            print("Help goes here")
        elif loadgameinput == 'q':
            print("Come again soon!")
            break
print(loadgameinput)
titlescreen()
