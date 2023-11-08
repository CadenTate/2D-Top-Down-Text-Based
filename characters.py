from typing import Tuple
import random

class base:
    canAttack = True
    isAlive = True

    def __init__(self,type:str,health:int,chunkX:int,chunkY:int,playerX:int,playerY:int) -> None:
        self.type = type
        self.chunkX = chunkX
        self.chunkY = chunkY
        self.locationX = playerX
        self.locationY = playerY
        self.MAX_HEALTH = health
        self.health = health
    
    def takeDamage(self, damage : int) -> None:
        if self.health - damage > 0:
            self.health -= damage
        else:
            self.health = 0
            self.isAlive = False

    def heal(self, heal : int) -> None:
        if self.health + heal <= self.MAX_HEALTH:
            self.health += heal
        else:
            self.health = self.MAX_HEALTH

    def attack(self,player):
        if self.canAttack: player.takeDamage(1)

    def location(self) -> Tuple[int,int,int,int]:
        return (self.chunkX,self.chunkY,self.locationX,self.locationY)
    
    def getType(self) -> str:
        return self.type
    
    def getHealth(self) -> int:
        return self.health

    def __str__(self) -> str:
        return f"Health: {self.health} | Chunk: {self.chunkX} {self.chunkY} | Location: {self.locationX} {self.locationY}"

class Slime(base):
    def __init__(self,chunkX:int,chunkY:int,playerX:int,playerY:int) -> None:
        super().__init__("slime",5,chunkX,chunkY,playerX,playerY)

    def goop(self, player) -> None:
        player.canAttack = False

class Player:
    MAX_HEALTH = 10
    health = 10
    level = 0
    lastMove = None
    canBlock = True
    canAttack = True
    isAlive = True

    def __init__(self, name) -> None:
        self.name = name

    def heal(self, heal:int):
        if self.health + heal <= self.MAX_HEALTH:
            self.health += heal
        else:
            self.health = self.MAX_HEALTH

    def attack(self, monster:Slime,crit:bool):
        if self.canAttack:
            if crit:
                if random.randint(1,6) == 1: 
                    monster.takeDamage(2) 
                    print("CRITICAL!")
                else:
                    print("Critical Failed!")
            else: 
                monster.takeDamage(1)
                print(f"Attack Successful!")
        else: 
            print("Something blocks your attack!")
            self.canAttack = True

    def takeDamage(self,damage:int):
        if self.health - damage > 0:
            self.health -= damage
        else: 
            self.health = 0
            self.isAlive = False

    def block(self,monster:Slime):
        if self.canBlock:
            match self.lastMove:
                case "attack":
                    self.heal(1)
                case "goop":
                    self.canAttack = True
            self.canBlock = False

    def canFlee(self) -> bool:
        if self.health / self.MAX_HEALTH <= 0.10:
            return True
        else: return False

    def stealHealth(self, monster:Slime, life:int):
        if random.randint(1,life*2) == 1:
            monster.takeDamage(life)
            self.heal(life)
            print("Success!")
        else:
            print("Failed!")
        
    def getName(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"Name: {self.name} | Health: {self.health} | Can Attack: {self.canAttack}"    