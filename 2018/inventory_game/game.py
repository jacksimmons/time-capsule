from heroes import Combatant, Hero, Enemy
from items import *
from defaults import default_input

import sys
import json
import random
import time
import os

ENEMY_NAME_LIMIT = 20
HERO_NAME_LIMIT = 20

#~~~~~~~~~~~~~~MISC~~~~~~~~~~~~~~#
def cls():
    os.system("cls" if os.name=="nt" else "clear")

in1 = "\n~~~~~~~~~~INVENTORY~~~~~~~~~~\n\n\t\tb = Buy an item\n\t\td = Deposit an item into your storage\n\t\ts = Sort your inventory or storage\n\t\tw = Withdraw an item from your storage\n\t\tv = View\n\t\tq = Exit inventory\n\n"

storage = []
inventory = []
balance = 0
choicelist = ["b","d","s","v","w","q"]
choicelist2 = ["inventory","storage"]
choice = ""
choice2 = ""
newitem = ""
olditem = ""
BATTLE_OPTIONS = [
    "attack", "a",
    "block", "b",
    "item", "i",
    "flee", "f"
]

# tier1items = ["Rugged shirt", "450", "Damaged trousers", "500", "Worn shoes", "400", "Ripped gloves", "350", "Old hat", "350"]

# tier2items = ["Shirt", "1900", "Trousers", "1800", "Shoes", "1850", "Gloves", "1750", "Hat", "1700"]

# tier3items = ["Thick jumper", "9900", "Tough jeans", "9800", "Nimble shoes", "9850", "Protective gloves", "9750", "Beanie", "9700"]

# tier4items = ["Chainmail body armour", "49900", "Chainmail leg armour", "49000", "Sturdy boots", "48500", "Chain gauntlets", "48000", "Chain helmet", "47500"]

# tier5items = ["Steel chestpiece", "200000", "Iron greaves", "1570", "Armoured footgear", "1575", "Metallic gauntlets", "1580", "Armoured helm", "1570"]

# tier6items = ["Titanium armour", "500000", "Titanium greaves", "480000", "Titanium boots", "497500", "Unbreakable gauntlets", "495000", "Honourable helm", "490000"]

# tier7items = ["Crystal core", "2500000", "Holy greaves", "2500000", "Winged boots", "2500000", "Royal gauntlets", "2500000", "Blessed battlehelm", "2500000"]

# weak_vials = ["Weak regeneration vial", "50", "Weak restoration vial", "75", "Weak magician"s vial", "50"]

# mediocre_vials = ["Regeneration vial", "150", "Restoration vial", "275", "Magician"s vial", "100"]

# potent_vials = ["Potent regeneration vial", "500", "Potent restoration vial", "750", "Potent magician"s vial", "500"]

# berries = ["Aggressive berry", "1000", "Fortitude berry", "1000", "Tactical berry", "1000", "Defensive berry", "1000", "Lucky berry", "1000", "Swift berry", "1000"]

# def inv():
#     choice = ""
#     while choice != "q":
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
#         menuchoice = input("t\t\np = Resume\t\t\ni = Inventory\t\t\ns = Settings\t\t\nq = Quit")
#         if menuchoice in choicelist:
#             break
#         else:
#             print ("Error - That is not a valid choice!")
#             return choice

# def shop():

#     print("Welcome to the shop!\n\t\tWhat type of item do you wish to purchase?")

#     chosen_type = input("\n\n\t\tGear\n\n\t\tVials\n\n\t\tBerries")

#     if chosen_type in categories:

#         if chosen_type == "gear":

#             chosen_tier = input("\n\n\t\tGear:\n\n\t\tTier 1\n\n\t\tTier2\n\n\t\tTier3\n\n\t\tTier4\n\n\t\tTier5\n\n\t\tTier6\n\n\t\tTier7")

#                 if chosen_tier = "tier 1":

#                     ("\n\n\t\t" + tier1items[0] + tier1items-)

#~~~~~~~~~~~~~~MISC~~~~~~~~~~~~~~#
def capitalise(string: str):
    return string[0].upper() + string[1:]

#~~~~~~~~~~~~~~GAMELOOP~~~~~~~~~~~~~~#

def get_random_enemy_name() -> str:
    cls()
    total_weight = 0
    data:dict={}

    # Get data
    with open("data.json", "r") as file:
        data = json.load(file)["encounter"]

    # Calculate total weight
    for data_item in data.keys():
        total_weight += data[data_item]
    
    # Get a random value in 0, total_weight
    # Get the item which is closest to the random value
    # Done by adding to a sum the value of the enemy
    rand_value = random.random() * total_weight
    sum_so_far = 0
    for data_item in data.keys():
        sum_so_far += data[data_item]
        if (sum_so_far >= rand_value):
            return data_item

def get_enemy() -> Enemy:
    enemy_name = get_random_enemy_name()
    
    with open("data.json", "r") as file:
        data = json.load(file)["enemies"][enemy_name.lower()]
        return Enemy(capitalise(enemy_name), data["hp"], data["agi"], data["pow"], data["lck"], 0)

def adjust_enemy_name(enemy_name: str) -> str:
    #The aim here is to make every value the same length to make them fit in the box.
    global ENEMY_NAME_LIMIT
    if (len(enemy_name) <= ENEMY_NAME_LIMIT):
        output_name = ""
        for i in range(0, ENEMY_NAME_LIMIT - len(enemy_name)):
            output_name += " "
        output_name += enemy_name
        return output_name
    else:
        raise Exception("Enemy name can't be longer than " + ENEMY_NAME_LIMIT + " characters.")

def json_to_combatant(json_dict: dict, key: str) -> Combatant:
    return Combatant(capitalise(key),
                     json_dict[key]["hp"],
                     json_dict[key]["agi"],
                     json_dict[key]["pow"],
                     json_dict[key]["lck"])

def get_hero_from_user() -> str:
    hero_classes = [
        "tank", "t",
        "fighter", "f",
        "archer", "a",
        "sorceror", "s"
        ]
    
    heroes:dict = {}
    with open("data.json", "r") as file:
        heroes = json.load(file)["heroes"]
    
    while True:
        cls()
        hero = ""
        hero_class = input("""Select a hero type:
        (t)Tank - Can take a beating at the cost of speed
        (f)Fighter - Very agile yet frail
        (a)Archer - Skilled, attacks from afar
        (s)Sorceror - Intelligent and packs a punch
q - Go back\n> """).lower()
        if hero_class in hero_classes:
            if len(hero_class) == 1:
                hero_class = hero_classes[hero_classes.index(hero_class) - 1]
            subclasses = heroes[hero_class].keys()

            stats:str = ""
            hero_options:list = ["q"]
            for subclass in subclasses:
                stats += json_to_combatant(heroes[hero_class], subclass).get_stats()
                stats += "\n"
                hero_options.append(subclass)
                hero_options.append(subclass[0])

            cls()
            hero_input = \
                input(f"Select a hero!\n{stats}q - Go back\n> ").lower()
            hero = hero_input \
                if hero_input in hero_options else ""

            if (hero == "q"):
                pass
            elif (hero != ""):
                if (len(hero) == 1):
                    # The qualified name is one index before the shortcut
                    return hero_options[hero_options.index(hero) - 1], hero_class
                return hero, hero_class
        elif hero_class == "q":
            break
        else:
            print("Pick a valid class!")

    return None, None

def get_hero() -> Hero:
    hero_name, hero_base_class_name = get_hero_from_user()
    if (hero_name, hero_base_class_name) == (None, None):
        return None

    with open("data.json", "r") as file:
        data = json.load(file)["heroes"][hero_base_class_name][hero_name.lower()]
        return Hero(capitalise(hero_name), data["hp"], data["agi"], data["pow"], data["lck"], 0)

def adjust_hero_name(hero_name: str) -> str:
    #The aim here is to make every value the same length to make them not extend the width of the box.
    global HERO_NAME_LIMIT
    if (len(hero_name) <= HERO_NAME_LIMIT):
        output_name = hero_name
        for i in range(0, HERO_NAME_LIMIT - len(hero_name)):
            output_name += " "
        return output_name
    else:
        raise Exception("Hero name can't be longer than " + HERO_NAME_LIMIT + " characters.")

def render_UI(hero: Hero, enemy: Enemy):
    adjusted_enemy_name = adjust_enemy_name(enemy.name)
    adjusted_hero_name = adjust_hero_name(hero.name)
    cls()
    spaces = (34 - len(str(hero.HP)) - len(str(enemy.HP)) - len(str(hero.MAX_HP)) - len(str(enemy.MAX_HP))) * " "
    print("┌--------------------------------------------------------------------------------┐")
    print(f"|{adjusted_hero_name}: {hero.HP}/{hero.MAX_HP}{spaces}{adjusted_enemy_name}: {enemy.HP}/{enemy.MAX_HP}|")
    print("└--------------------------------------------------------------------------------┘")

# Waits for user input, then renders UI, then returns the input
def render_UI_on_input(hero: Hero, enemy: Enemy) -> str:
    value = default_input()
    render_UI(hero, enemy)
    return value

def show_stats(hero: Hero, enemy: Enemy):
    cls()
    print(f"""You will face {enemy.name}!
Stats:
        HP: {str(enemy.HP)}
        AGI: {str(enemy.AGI)}
        POW: {str(enemy.POW)}""")
    print(f"""
You selected the hero {hero.name}.
Your stats are:
        HP: {str(hero.HP)}
        AGI: {str(hero.AGI)}
        POW: {str(hero.POW)}""")
    input("\n> ")
    cls()
    print("\n\n\n\t\t\t\t\t\t\tFIGHT!")
    time.sleep(0.5)

def fight(hero: Hero, enemy: Enemy):
    global BATTLE_OPTIONS
    
    # Decide who starts
    if (hero.AGI > enemy.AGI):
        turn = 1
    elif (enemy.AGI > hero.AGI):
        turn = 0
    else:
        turn = random.random()
        if (turn >= 0.5):
            turn = 1
        else:
            turn = 0

    render_UI(hero, enemy)

    while True:        
        if enemy.HP == 0 or hero.HP == 0:
            break
        
        if turn == 1:
            hero.blocking = False
            print("Your turn.")
            choice = input("""What do you want to do?
        (a)Attack
        (b)Block
        (i)Item
        (f)Flee
> """).lower()
            render_UI(hero, enemy)
            if choice in BATTLE_OPTIONS:
                if choice in ["attack", "a"]:
                    hero.action_attack(enemy)
                elif choice in ["block", "b"]:
                    hero.action_block()
                elif choice in ["item", "i"]:
                    print(f"Inventory:\n{hero.inventory.get_items()}")
                    while True:
                        item = input("q - Cancel\nSelect an item:\n> ")
                        render_UI(hero, enemy)
                        # If an item was successfully used, end the turn
                        if hero.use_item(item):
                            render_UI_on_input(hero, enemy)
                            turn = 0
                            break
                        else:
                            # If it was unsuccessful, restart the turn without changing turn
                            break
                    turn = 0
                    continue # Skip the UI render, we did it conditionally in the while loop
                elif choice in ["flee", "f"]:
                    pass
                turn = 0
        elif turn == 0:
            print("Enemy's turn.")
            render_UI_on_input(hero, enemy)
            enemy.blocking = False
            weighting = [0.8, 0.1, 0.1]
            if (enemy.HP < hero.POW):
                # The enemy is scared, more likely to block
                weighting[1] += 0.1
                weighting[0] -= 0.1
            if (enemy.HP < enemy.MAX_HP * 0.2):
                # < 20% of max health, more likely to use item
                weighting[2] += 0.1
                weighting[0] -= 0.1
            if (enemy.HP < enemy.MAX_HP * 0.1):
                # < 10% of max health
                weighting[2] += 0.1
                weighting[0] -= 0.1
            
            action = ""
            rand_weight = random.random()
            if (rand_weight > weighting[0]):
                if (rand_weight > weighting[1]):
                    action = "Item"
                else:
                    action = "Block"
            else:
                action = "Attack"
            
            if action == "Attack":
                enemy.action_attack(hero)
            elif action == "Block":
                enemy.action_block()
            elif action == "Item":
                # The enemy wants to use an item.
                # If they have an item, use it, otherwise block
                if enemy.inventory != [] and enemy.HP != enemy.MAX_HP:
                    enemy.dict_to_stats(enemy.inventory.use_item(enemy.inventory.items[0], enemy.stats_to_dict()))
                else:
                    enemy.action_block()
            turn = 1
        render_UI_on_input(hero, enemy)

def finish_setup(hero: Hero, enemy: Enemy) -> bool:
    if (hero == None or enemy == None):
        return False
    
    hero.inventory.add_item(YazooMilk())
    hero.inventory.add_item(YazooMilk())
    hero.inventory.add_item(YazooMilk())

    enemy.inventory.add_item(YazooMilk())
    enemy.inventory.add_item(YazooMilk())
    enemy.inventory.add_item(YazooMilk())

    show_stats(hero, enemy)
    fight(hero, enemy)
    return True

def new_game_setup() -> bool:
    hero : Hero  = get_hero()
    enemy: Enemy = get_enemy()
    return finish_setup(hero, enemy)

def load_save_setup() -> bool:
    hero : Hero = Hero.load_from_save()
    enemy: Enemy = get_enemy()
    return finish_setup(hero, enemy)