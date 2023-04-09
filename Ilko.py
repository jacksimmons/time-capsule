import os
import random
import sys

you_first = 0
HP = 10
SPD = 10
DMG = 10
enemy = ''
enemy_HP = 0
enemy_SPD = 0
enemy_DMG = 0

def encounter():
    enemy_value = random.randint(1,100)
    if enemy_value in range (1,10):
        enemy = 'Ed\'s Tie'
    elif enemy_value in range (11,30):
        enemy = 'Border Control'
    elif enemy_value in range (31,50):
        enemy = 'Mr. MyMaths'
    elif enemy_value == 51:
        enemy = 'A Skinny Asian Boi\'s Noodle'
    elif enemy_value in range (52,60):
        enemy = 'Vladimir Spock'
    elif enemy_value in range (61,80):
        enemy = 'Certified Nonce'
    elif enemy_value == 81:
        enemy = 'Charlie Duggan'
    else:
        enemy = 'Voice Break in English Speech'
    print("A wild " + enemy + " appeared!")
    stats()

def stats():
    if enemy == 'Ed\'s Tie':
        enemy_HP = 7
        enemy_SPD = 4
        enemy_DMG = 8
    elif enemy == 'Border Control':
        enemy_HP = 20
        enemy_SPD = 1
        enemy_DMG = 4
    elif enemy == 'Mr. MyMaths':
        enemy_HP = 2
        enemy_SPD = 11
        enemy_DMG = 6
    elif enemy == 'A Skinny Asian Boi\'s Noodle':
        enemy_HP = 1
        enemy_SPD = 2
        enemy_DMG = 12
    elif enemy == 'Vladimir Spock':
        enemy_HP = 4
        enemy_SPD = 20
        enemy_DMG = 5
    elif enemy == 'Certified Nonce':
        enemy_HP = 9
        enemy_SPD = 11
        enemy_DMG = 3
    elif enemy == 'Charlie Duggan':
        enemy_HP = 1
        enemy_SPD = 1
        enemy_DMG = 1
    else:
        enemy_HP = 20
        enemy_SPD = random.randint(1,20)
        enemy_DMG = 10
    battle(enemy_HP, enemy_SPD, enemy_DMG)

def battle(enemy_HP, enemy_SPD, enemy_DMG):

    global HP
    global SPD
    global DMG
    global enemy

    first_turn_over = False
    turn_counter = 1

    while (enemy_HP > 0 and HP > 0):
        print("Turn " + str(turn_counter))
        print("HP: " + str(HP))
        print("Enemy HP: " + str(enemy_HP))
        if not first_turn_over:
            if SPD > enemy_SPD:
                you_first = 1
                print('You are going first')
            elif enemy_SPD > SPD:
                you_first = 0
                print('Enemy is going first')
            else:
                you_first = random.randint(0,1)
        if you_first == 1:
            if DMG >= enemy_HP:
                enemy_life = 0
                print('You beat ' + enemy_name + '!')
            else:
                enemy_HP = enemy_HP - DMG
                print('Enemy took ' + str(DMG) + ' damage!')
        elif you_first == 0:
            if enemy_DMG >= HP:
                your_life = 0
                print('You died...')
            else:
                HP -= enemy_DMG
                print('You suffered ' + str(enemy_DMG) + ' damage!')
        # It is guaranteed that the first turn is over
        first_turn_over = True
        turn_counter += 1
        x = input("Press any key to go to the next turn.\n")
encounter()
