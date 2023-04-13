from save_game import save, load
from items import Inventory, Item
from defaults import default_input

import random

class Combatant:
    def __init__(self, name, HP, AGI, POW, LCK):
        self.name = name

        self.MAX_HP:int = HP
        
        self.HP :float= HP
        self.AGI:int  = AGI
        self.POW:int  = POW
        self.LCK:int  = LCK

        self.blocking = False
        self.chaos = 2

        self.inventory = Inventory()
    
    def stats_to_dict(self) -> dict:
        stats_dict: dict = {}
        stats_dict["name"] = self.name
        stats_dict["hp"] = self.HP
        stats_dict["agi"] = self.AGI
        stats_dict["pow"] = self.POW
        stats_dict["lck"] = self.LCK
        stats_dict["max_hp"] = self.MAX_HP
        return stats_dict
    
    def dict_to_stats(self, stats_dict: dict):
        self.name = stats_dict["name"]
        self.HP = stats_dict["hp"]
        self.AGI = stats_dict["agi"]
        self.POW = stats_dict["pow"]
        self.LCK = stats_dict["lck"]
        self.MAX_HP = stats_dict["max_hp"]

    def use_item(self, item_name: str) -> bool:
        if item_name == "q":
            return False
        for item in self.inventory.items:
            if item.name == item_name:
                self.dict_to_stats(self.inventory.use_item(item, self.stats_to_dict()))
                return True
        input("You don't have any of those.")
        return False

    def get_stats(self) -> str:
        return f"""\
    ({self.name[0].lower()}){self.name}
        HP: {self.HP},
        AGI: {self.AGI},
        POW: {self.POW},
        LCK: {self.LCK}"""
    
    def action_attack(self, victim):
        print(self.name + " will now attack.")
        default_input()
        victim.take_damage(self.calc_damage(), self)
    
    def action_block(self):
        print(self.name + " is blocking.")
        print(self.name + " will take 0.5x damage on the next turn.")
        default_input()
        self.blocking = True

    def calc_damage(self, DEF: int=0):
        multiplier = 1
        # Chance for critical hit
        if random.randint(self.LCK, 40) == 40:
            multiplier *= 2
            print("Critical hit!")
        # A bit of true randomness determined by chaos
        damage = random.randint(self.POW - self.chaos, self.POW + self.chaos)
        
        return damage * multiplier

    def take_damage(self, damage: float, inflictor) -> float:
        if self.blocking:
            print(self.name + " is blocking, so will take 0.5x damage.")
            damage /= 2
        
        self.HP -= damage
        
        print(self.name + " took " + str(damage) + " damage.")

        if (self.HP < 0):
            self.HP = 0
            self.die(inflictor)
    
    def die(self, inflictor):
        self.die_message()
        if (isinstance(inflictor, Hero)):
            inflictor.handle_victory(self)
        
    def die_message(self):
        print(self.name + " was defeated.")
        

class Hero(Combatant):
    def __init__(self, n, h, a, p, l, EXP):
        super().__init__(n, h, a, p, l)
        self.EXP = EXP

    @staticmethod
    def load_from_save():
        return load()
    
    #override
    def die_message(self):
        print("You died!")

    def calculate_level(self) -> int:
        count = self.EXP
        req = 20
        level = 0
        while True:
            count -= req
            if (count <= 0):
                break
            req = req * 1.2 #20,24,29,35,42,50,60,72,86,104
            level += 1
        return level

    def add_exp(self, exp):
        self.EXP += exp
        self.calculate_level()
    
    def handle_victory(self, loser):
        self.add_exp(loser.exp_drop)
        save(self)

        
class Enemy(Combatant):
    def __init__(self, n, h, a, p, l, EXP):
        super().__init__(n, h, a, p, l)
        self.exp_drop = EXP
    
    #override
    def die_message(self):
        print("You defeated " + self.name + "!")