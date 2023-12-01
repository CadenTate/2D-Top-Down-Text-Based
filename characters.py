from typing import Tuple
import random

# Base Class for Characters
class Character:
    canAttack = True
    isAlive = True

    def __init__(self,name:str,MAX_HEALTH:int,level:int,image=None) -> None:
        self.MAX_HEALTH = MAX_HEALTH
        self.health = MAX_HEALTH
        self.name = name
        self.image = image

    # Health Manipulating Functions
    def setHealth(self,newHealth:int) -> None:
        if newHealth <= self.MAX_HEALTH and newHealth >= 0:
            self.health = newHealth

    def heal(self, heal:int) -> None:
        newHealth = self.health + heal
        if newHealth > self.MAX_HEALTH:
            newHealth = self.MAX_HEALTH
        self.setHealth(newHealth)

    def takeDamage(self,damage:int):
        newHealth = self.health - damage
        if newHealth < 0:
            newHealth = 0
            self.isAlive = False
        self.setHealth(newHealth)

    # Combat Functions
    def attack(self, enemy, crit:bool) -> None:
        if self.canAttack:
            if crit:
                if random.randint(1,6) == 1: 
                    enemy.takeDamage(2) 
                    print("CRITICAL!")
                else:
                    print("Critical Failed!")
            else: 
                enemy.takeDamage(1)
                print(f"Attack Successful!")
        else: 
            print("Something blocks your attack!")
            self.canAttack = True
    
    def printImage(self):
        print(self.image)

    # Other functions
    def getName(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"Name: {self.name} | Health: {self.health} | Can Attack: {self.canAttack}"    

# Class Slime
class Slime(Character):
    def __init__(self) -> None:
        image =("""
   /-------\\
  /         \\
 /  O     O  \\
/    [---]    \\
\\=============/""")
        super().__init__("Slime",5,1,image)

# Player Class
class Player(Character):
    def __init__(self, name:str) -> None:
        super().__init__(name,10,1)

    # def block(self,monster):

    def canFlee(self) -> bool:
        if self.health / self.MAX_HEALTH <= 0.10:
            return True
        else: return False

    def stealHealth(self, monster, life:int):
        if random.randint(1,life*2) == 1:
            monster.takeDamage(life)
            self.heal(life)
            print("Success!")
        else:
            print("Failed!")