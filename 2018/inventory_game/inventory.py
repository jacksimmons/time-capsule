#!/usr/bin/python
import sys
print('v1.0.3')
import random
import time
import os

in1 = '\n~~~~~~~~~~INVENTORY~~~~~~~~~~\n\n\t\tb = Buy an item\n\t\td = Deposit an item into your storage\n\t\ts = Sort your inventory or storage\n\t\tw = Withdraw an item from your storage\n\t\tv = View\n\t\tq = Exit inventory\n\n'

storage = []
inventory = []
balance = 0
choicelist = ['b','d','s','v','w','q']
choicelist2 = ['inventory','storage']
choice = ''
choice2 = ''
newitem = ''
olditem = ''
titlescreenoptions = ['p','h','q']
loadgameinput = ''
turn = ''
winner = ''
input_options = ['Attack','attack','a','Defend','defend','d','Item','item','i','Flee','flee','f']

# tier1items = ["Rugged shirt", "450", "Damaged trousers", "500", "Worn shoes", "400", "Ripped gloves", "350", "Old hat", "350"]

# tier2items = ["Shirt", "1900", "Trousers", "1800", "Shoes", "1850", "Gloves", "1750", "Hat", "1700"]

# tier3items = ["Thick jumper", "9900", "Tough jeans", "9800", "Nimble shoes", "9850", "Protective gloves", "9750", "Beanie", "9700"]

# tier4items = ["Chainmail body armour", "49900", "Chainmail leg armour", "49000", "Sturdy boots", "48500", "Chain gauntlets", "48000", "Chain helmet", "47500"]

# tier5items = ["Steel chestpiece", "200000", "Iron greaves", "1570", "Armoured footgear", "1575", "Metallic gauntlets", "1580", "Armoured helm", "1570"]

# tier6items = ["Titanium armour", "500000", "Titanium greaves", "480000", "Titanium boots", "497500", "Unbreakable gauntlets", "495000", "Honourable helm", "490000"]

# tier7items = ["Crystal core", "2500000", "Holy greaves", "2500000", "Winged boots", "2500000", "Royal gauntlets", "2500000", "Blessed battlehelm", "2500000"]

# weak_vials = ["Weak regeneration vial", "50", "Weak restoration vial", "75", "Weak magician's vial", "50"]

# mediocre_vials = ["Regeneration vial", "150", "Restoration vial", "275", "Magician's vial", "100"]

# potent_vials = ["Potent regeneration vial", "500", "Potent restoration vial", "750", "Potent magician's vial", "500"]

# berries = ["Aggressive berry", "1000", "Fortitude berry", "1000", "Tactical berry", "1000", "Defensive berry", "1000", "Lucky berry", "1000", "Swift berry", "1000"]

HP = '0'
AGI = '0'
POW = '0'
enemy = ''
enemy_HP = '0'
enemy_AGI = '0'
enemy_POW = '0'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# def inv():
#     choice = ''
#     while choice != 'q':
#         choice == menu()
#
# def menu():
#     while True:
#         choice = input(in1)
#         if choice in choicelist:
#             print(choice)
#         else:
#             print("That is not a valid choice.")
#     return(choice)
#     inv()
#
# def esc_menu():
#     while True:
#         menuchoice = input('t\t\np = Resume\t\t\ni = Inventory\t\t\ns = Settings\t\t\nq = Quit')
#         if menuchoice in choicelist:
#             break
#         else:
#             print ('Error - That is not a valid choice!')
#             return choice

# def shop():

#     print("Welcome to the shop!\n\t\tWhat type of item do you wish to purchase?")

#     chosen_type = input("\n\n\t\tGear\n\n\t\tVials\n\n\t\tBerries")

#     if chosen_type in categories:

#         if chosen_type == 'gear':

#             chosen_tier = input("\n\n\t\tGear:\n\n\t\tTier 1\n\n\t\tTier2\n\n\t\tTier3\n\n\t\tTier4\n\n\t\tTier5\n\n\t\tTier6\n\n\t\tTier7")

#                 if chosen_tier = 'tier 1':

#                     ("\n\n\t\t" + tier1items[0] + tier1items-)

def encounter():
    enemy_value = random.randint(1,100)
    cls()
    if enemy_value in range (1,10):
        enemy = 'Vladimir Spock'
        return enemy
    elif enemy_value in range (11,30):
        enemy = 'Mr. MyMaths'
        return enemy
    elif enemy_value in range (31,50):
        enemy = 'Mrs Adams'
        return enemy
    elif enemy_value == 51:
        enemy = 'Colin Hegarty'
        return enemy
    elif enemy_value in range (52,60):
        enemy = 'Enemy5'
        return enemy
    elif enemy_value in range (61,80):
        enemy = 'Enemy6'
        return enemy
    else:
        enemy = 'Charlie Duggan'
        return enemy

def enemies():
    enemy = encounter()
    if enemy == 'Vladimir Spock': #14 char
        enemy_HP = 70
        enemy_AGI = 80
        enemy_POW = 1
        enemy = 'Vladimir Spock'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

    elif enemy == 'Mr. MyMaths': #11 char
        enemy_HP = 50
        enemy_AGI = 150
        enemy_POW = 2
        enemy = 'Mr. MyMaths'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

    elif enemy == 'Mrs Adams': #9 char
        enemy_HP = 100
        enemy_AGI = 20
        enemy_POW = 2
        enemy = 'Mrs Adams'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

    elif enemy == 'Colin Hegarty': #13 char
        enemy_HP = 30
        enemy_AGI = 100
        enemy_POW = 2
        enemy = 'Colin Hegarty'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

    elif enemy == 'Enemy5': #6 char
        enemy_HP = 25
        enemy_AGI = 180
        enemy_POW = 2
        enemy = 'Enemy5'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

    elif enemy == 'Enemy6': #6 char
        enemy_HP = 35
        enemy_AGI = 200
        enemy_POW = 1
        enemy = 'Enemy6'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

    elif enemy == 'Charlie Duggan': #14 char
        enemy_HP = 10
        enemy_AGI = 40
        enemy_POW = 3
        enemy = 'Charlie Duggan'
        return enemy_HP, enemy_AGI, enemy_POW, enemy

def char_adjust():
    #The aim here is to make every value the same length to make them fit in the box (14 characters)
    enemy_HP, enemy_AGI, enemy_POW, enemy = enemies()
    if enemy == 'Mr. MyMaths':
        actual_enemy = 'Mr. MyMaths    ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy
    elif enemy == 'Mrs Adams':
        actual_enemy = 'Mrs Adams      ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy
    elif enemy == 'Colin Hegarty':
        actual_enemy = 'Colin Hegarty  ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy
    elif enemy == 'Enemy5':
        actual_enemy = 'Enemy5         ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy
    elif enemy == 'Enemy6':
        actual_enemy = 'Enemy6         ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy
    elif enemy == 'Vladimir Spock':
        actual_enemy = 'Vladimir Spock ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy
    elif enemy == 'Charlie Duggan':
        actual_enemy = 'Charlie Duggan ¦'
        return enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy

def heroes():
    a = True
    hero_classes = ['Tank','Fighter','Archer','Sorceror','tank','fighter','archer','sorceror']
    while a == True:
        time.sleep(2)
        cls()
        hero_class = input('Select a hero type:\n\n\t\tTank - Can take a beating at the cost of speed\n\n\t\tFighter - Very agile yet frail\n\n\t\tArcher - Skilled, attacks from afar\n\n\t\tSorceror - Intelligent and packs a punch\n\n> ')
        if hero_class in hero_classes:
            if hero_class in ['Tank','tank']:
                hero_options = ['Juggernaut','/j','Gladiator','/g','Revenant','/r','juggernaut','gladiator','revenant','j','g','r']
                cls()
                hero = input('Select a hero!\n\n\t\tJuggernaut (\'/j\' to see stats)\n\n\t\tGladiator (\'/g\' to see stats)\n\n\t\tRevenant (\'/r\' to see stats)\n\n> ')
                if hero in hero_options:
                    if hero == '/j':
                        cls()
                        print('Juggernaut:\n\nHP: 20\nAGI: 1\nPOW: 15\nLCK: 4')
                    elif hero == '/g':
                        cls()
                        print('Gladiator:\n\nHP: 17\nAGI: 5\nPOW: 14\nLCK: 4')
                    elif hero == '/r':
                        cls()
                        print('Revenant:\n\nHP: 19\nAGI: 2\nPOW: 18\nLCK: 1')
                    else:
                        a = False
                        return hero
            elif hero_class in ['Fighter','fighter']:
                hero_options = ['Assassin','/a','Ninja','/n','Knight','/k','assassin','ninja','knight','a','n','k']
                cls()
                hero = input('Select a hero!\n\n\t\tAssassin (\'/a\' to see stats)\n\n\t\tNinja (\'/n\' to see stats)\n\n\t\tKnight (\'/k\' to see stats)\n\n> ')
                if hero in hero_options:
                    if hero == '/a':
                        cls()
                        print('Assassin:\n\nHP: 5\nAGI: 15\nPOW: 15\nLCK: 5')
                    elif hero == '/n':
                        cls()
                        print('Ninja:\n\nHP: 4\nAGI: 20\nPOW: 12\nLCK: 4')
                    elif hero == '/k':
                        cls()
                        print('Knight:\n\nHP: 9\nAGI: 13\nPOW: 6\nLCK: 12')
                    else:
                        a = False
                        return hero
            elif hero_class in ['Archer','archer']:
                hero_options = ['Bowmaster','/b','Sniper','/s','Demolitionist','/d','bowmaster','sniper','demolitionist','b','s','d']
                cls()
                hero = input('Select a hero!\n\n\t\tBowmaster (\'/b\' to see stats)\n\n\t\tSniper (\'/s\' to see stats)\n\n\t\tDemolitionist (\'/d\' to see stats)\n\n> ')
                if hero in hero_options:
                    if hero == '/b':
                        cls()
                        print('Bowmaster:\n\nHP:7\nAGI:12\nPOW: 11\nLCK: 10')
                    elif hero == '/s':
                        cls()
                        print('Sniper:\n\nHP: 6\nAGI: 10\nPOW: 13\nLCK: 11')
                    elif hero == '/d':
                        cls()
                        print('Demolitionist:\n\nHP:5\nAGI:11\nPOW:15\nLCK: 9')
                    else:
                        a = False
                        return hero
            elif hero_class in ['Sorceror','sorceror']:
                hero_options = ['Wizard','/w','Cleric','/c','Summoner','/s','wizard','cleric','summoner','w','c','s']
                cls()
                hero = input('Select a hero!\n\n\t\tWizard (\'/w\' to see stats)\n\n\t\tCleric (\'/c\' to see stats)\n\n\t\tSummoner (\'/s\' to see stats)\n\n> ')
                if hero in hero_options:
                    if hero == '/w':
                        cls()
                        print('Wizard:\n\nHP: 6\nAGI: 9\nPOW: 17\nLCK: 8')
                    elif hero == '/c':
                        cls()
                        print('Cleric:\n\nHP: 7\nAGI: 8\nPOW: 15\nLCK: 10')
                    elif hero == '/s':
                        cls()
                        print('Summoner:\n\nHP: 10\nAGI: 7\nPOW: 13\nLCK: 10')
                    else:
                        a = False
                        return hero
        elif hero_class not in hero_classes:
            print('Pick a valid class!')

def battle():
    hero = heroes()
    if hero == 'Juggernaut': #10 char
        hero = 'Juggernaut'
        HP = 21
        AGI = 1
        POW = 18
        return hero, HP, AGI, POW
    elif hero == 'Gladiator': #9 char
        hero = 'Gladiator'
        HP = 17
        AGI = 5
        POW = 18
        return hero, HP, AGI, POW
    elif hero == 'Revenant': #8 char
        hero = 'Revenant'
        HP = 19
        AGI = 2
        POW = 19
        return hero, HP, AGI, POW
    elif hero == 'Assassin':
        hero = 'Assassin' #8 char
        HP = 5
        AGI = 20
        POW = 15
        return hero, HP, AGI, POW
    elif hero == 'Ninja':
        hero = 'Ninja' #5 char
        HP = 4
        AGI = 24
        POW = 12
        return hero, HP, AGI, POW
    elif hero == 'Knight':
        hero = 'Knight' #6 char
        HP = 16
        AGI = 15
        POW = 9
        return hero, HP, AGI, POW
    elif hero == 'Bowmaster':
        hero = 'Bowmaster' #9 char
        HP = 7
        AGI = 15
        POW = 18
        return hero, HP, AGI, POW
    elif hero == 'Sniper':
        hero = 'Sniper' #6 char
        HP = 6
        AGI = 10
        POW = 13
        LCK = 11
        return hero, HP, AGI, POW
    elif hero == 'Demolitionist':
        hero = 'Demolitionist' #13 char
        HP = 8
        AGI = 13
        POW = 19
        return hero, HP, AGI, POW
    elif hero == 'Wizard':
        hero = 'Wizard' #6 char
        HP = 6
        AGI = 11
        POW = 23
        return hero, HP, AGI, POW
    elif hero == 'Cleric':
        hero = 'Cleric' #5 char
        HP = 12
        AGI = 11
        POW = 17
        return hero, HP, AGI, POW
    else:
        hero = 'Summoner' #8 char
        HP = 15
        AGI = 10
        POW = 15
        return hero, HP, AGI, POW

def hero_char_adjust():
    hero, HP, AGI, POW = battle()
    if hero == 'Juggernaut':
        actual_hero = '¦ Juggernaut   '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Gladiator':
        actual_hero = '¦ Gladiator    '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Revenant':
        actual_hero = '¦ Revenant     '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Assassin':
        actual_hero = '¦ Assassin     '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Ninja':
        actual_hero = '¦ Ninja        '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Knight':
        actual_hero = '¦ Knight       '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Bowmaster':
        actual_hero = '¦ Bowmaster    '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Sniper':
        actual_hero = '¦ Sniper       '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Demolitionist':
        actual_hero = '¦ Demolitionist'
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Wizard':
        actual_hero = '¦ Wizard       '
        return actual_hero, hero, HP, AGI, POW
    elif hero == 'Cleric':
        actual_hero = '¦ Cleric       '
        return actual_hero, hero, HP, AGI, POW
    else:
        actual_hero = '¦ Summoner     '
        return actual_hero, hero, HP, AGI, POW

def fight_prep():
    actual_hero, hero, HP, AGI, POW = hero_char_adjust()
    enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy = char_adjust()
    print('You will face ' + enemy + '!\nStats:\nHP: ' + str(HP) + '\nAGI: ' + str(enemy_AGI) + '\nPOW: ' + str(enemy_POW))
    print('\nYou selected the hero ' + hero + '.\nYour stats are:\nHP: ' + str(HP) + '\nAGI: ' + str(AGI) + '\nPOW: ' + str(POW))
    time.sleep(5)
    cls()
    print('\n\n\n\t\t\t\t\t\t\tFIGHT!')
    time.sleep(0.5)
    cls()
    return actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy

def turns():
    actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy = fight()
    if AGI > enemy_AGI:
        turn = 1
        spaces = ('        ')
        return turn, actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy, spaces
    elif AGI == enemy_AGI:
        who_attacks = random.randint(0,1)
        if who_attacks == 0:
            turn = 1
            spaces = ('        ')
            return turn, actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy, spaces
        else:
            turn = 0
            spaces = ('         ')
            return turn, actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy, spaces
    elif AGI < enemy_AGI:
        turn = 0
        spaces = ('        ')
        return turn, actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy, spaces

def victory():
    if input('\nPlay again? ') in ['y','Yes','yes']:
        titleinput()
    else:
        sys.exit()

def loss():
    if input('\nWant to try again? ') in ['y','Yes','yes']:
        titleinput()
    else:
        sys.exit()

def attack():
    turn, actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy, spaces = turns()
    length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
    while True:
        if turn == 1:
            if HP > 0:
                choice = input('What do you want to do?\n\nAttack\n\nDefend\n\nItem\n\nFlee\n\n> ')
                if choice in input_options:
                    if choice in ['Attack','attack','a']:
                        cls()
                        print('┌--------------------------------------------------------------------------------┐')
                        if len(length) > 82:
                            spaces = ('     ')
                        elif len(length) < 82:
                            spaces = ('        ')
                        print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                        print('└--------------------------------------------------------------------------------┘')
                        print(hero + ' will now attack.')
                        time.sleep(2)
                        damage_dealt = random.randint((POW - 2), (POW + 2))
                        enemy_HP = enemy_HP - damage_dealt
                        if len(length) > 82:
                            cls()
                            spaces = ('     ')
                            print('┌--------------------------------------------------------------------------------┐')
                            print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print('└--------------------------------------------------------------------------------┘')
                        elif len(length) < 82:
                            cls()
                            spaces = ('        ')
                            print('┌--------------------------------------------------------------------------------┐')
                            length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print('└--------------------------------------------------------------------------------┘')
                        cls()
                        if enemy_HP <= 0:
                            enemy_HP = 0
                        print('┌--------------------------------------------------------------------------------┐')
                        print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                        print('└--------------------------------------------------------------------------------┘')
                        print(hero + ' dealt ' + str(damage_dealt) + ' damage!')
                        time.sleep(2)
                        turn = 0
                    elif choice in ['Defend','defend','d']:
                        cls()
                        print('┌--------------------------------------------------------------------------------┐')
                        if len(length) > 82:
                            spaces = ('     ')
                        elif len(length) < 82:
                            spaces = ('        ')
                        print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                        print('└--------------------------------------------------------------------------------┘')
                        print(enemy + ' will now attack.')
                        time.sleep(2)
                        damage_dealt = random.randint((enemy_POW - 2), (enemy_POW + 2))
                        damage_dealt = damage_dealt / 2
                        HP = HP - damage_dealt
                        if len(length) > 82:
                            cls()
                            spaces = ('     ')
                            print('┌--------------------------------------------------------------------------------┐')
                            length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print('└--------------------------------------------------------------------------------┘')
                        elif len(length) < 82:
                            cls()
                            spaces = ('        ')
                            print('┌--------------------------------------------------------------------------------┐')
                            length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                            print('└--------------------------------------------------------------------------------┘')
                        cls()
                        if HP <= 0:
                            HP = 0
                        print('┌--------------------------------------------------------------------------------┐')
                        print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                        print('└--------------------------------------------------------------------------------┘')
                        print('\n\n' + hero + ' took ' + str(damage_dealt) + ' damage!')
                        turn = 1
            else:
                cls()
                print(enemy + ' won the game...')
        elif turn == 0:
            if enemy_HP > 0:
                cls()
                print('┌--------------------------------------------------------------------------------┐')
                if len(length) > 82:
                    spaces = ('     ')
                elif len(length) < 82:
                    spaces = ('        ')
                print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                print('└--------------------------------------------------------------------------------┘')
                print(enemy + ' will now attack.')
                time.sleep(2)
                damage_dealt = random.randint((enemy_POW - 2), (enemy_POW + 2))
                HP = HP - damage_dealt
                if len(length) > 82:
                    cls()
                    spaces = ('     ')
                    print('┌--------------------------------------------------------------------------------┐')
                    length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                    print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                    print('└--------------------------------------------------------------------------------┘')
                elif len(length) < 82:
                    cls()
                    spaces = ('        ')
                    print('┌--------------------------------------------------------------------------------┐')
                    length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                    print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                    print('└--------------------------------------------------------------------------------┘')
                time.sleep(2)
                cls()
                if HP <= 0:
                    HP = 0
                print('┌--------------------------------------------------------------------------------┐') #LENGTH 82 CHARS
                length = (actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                if len(length) > 82:
                    spaces = ('     ')
                elif len(length) < 82:
                    spaces = ('        ')
                print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(enemy_HP) + spaces + '¦')
                print('└--------------------------------------------------------------------------------┘')
                print('\n\n' + hero + ' took ' + str(damage_dealt) + ' damage!')
                turn = 1
            else:
                cls()
                print('You won the battle!')


def fight():
    actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy = fight_prep()
    print('┌--------------------------------------------------------------------------------┐')
    print(actual_hero + '\t\t\t\t\t\t\t  ' + actual_enemy + '\n¦ HP: ' + str(HP) + '    \t\t\t\t\t\t\t  HP: ' + str(HP) + '         ¦')
    print('└--------------------------------------------------------------------------------┘')
    return actual_hero, hero, HP, AGI, POW, enemy_HP, enemy_AGI, enemy_POW, actual_enemy, enemy

def titlescreen():
    cls()
    loadgameinput = input('\t\t☭ Welcome! ☭\n\t\t\tp = Play\n\t\t\tq = Quit\n')
    if loadgameinput in titlescreenoptions:
        print("Success")
    else:
        print ('Error - That is not a valid choice!')
    return loadgameinput

def titleinput():
    loadgameinput = titlescreen()
    if loadgameinput == 'p':
        cls()
        hero = attack()

    elif loadgameinput == 'q':
        print("Come again soon!")

titleinput()
