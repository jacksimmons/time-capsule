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
    
    # Base die method, overwritten in Hero and Enemy
    def get_stats(self) -> str:
        return f"""
{self.name}
        HP: {self.HP},
        AGI: {self.AGI},
        POW: {self.POW},
        LCK: {self.LCK}"""
    
    def die(self):
        print(self.name + " was defeated.")
    
    def calc_damage(self, DEF: int=0):
        multiplier = 1
        # Chance for critical hit
        if random.randint(self.LCK, 100) == 100:
            multiplier *= 2
            print("Critical hit!")
        # A bit of true randomness determined by chaos
        damage = random.randint(self.POW - self.chaos, self.POW + self.chaos)
        
        return damage * multiplier

    def take_damage(self, damage: float) -> float:
        if self.blocking:
            print(self.name + " is blocking, so will take 0.5x damage.")
            damage /= 2
        
        self.HP -= damage
        
        print(self.name + " took " + str(damage) + " damage.")

        if (self.HP < 0):
            self.HP = 0
            self.die()

    def block(self):
        blocking = True    

class Hero(Combatant):
    def __init__(self, n, h, a, p, l, EXP):
        super().__init__(n, h, a, p, l)
        self.total_exp = EXP
    
    def die(self):
        print("You died!")

        
class Enemy(Combatant):
    def __init__(self, n, h, a, p, l, EXP):
        super().__init__(n, h, a, p, l)
        self.exp_drop = EXP
    
    def die(self):
        print("You defeated " + self.name + "!")