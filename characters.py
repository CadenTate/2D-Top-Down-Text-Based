from typing import Tuple

class Monster:
    def __init__(self,chunkX:int,chunkY:int,playerX:int,playerY:int) -> None:
        self.chunkX = chunkX
        self.chunkY = chunkY
        self.locationX = playerX
        self.locationY = playerY
    
    def damage(self, damage : int) -> None:
        if self.health - damage > 0:
            self.health -= damage
        else:
            self.health = 0

    def heal(self, heal : int) -> None:
        if self.health + heal <= self.MAX_HEALTH:
            self.health += heal
        else:
            self.health = self.MAX_HEALTH

    def location(self) -> Tuple[int,int,int,int]:
        return (self.chunkX,self.chunkY,self.locationX,self.locationY)

    def __str__(self) -> str:
        return f"Health: {self.health} | Chunk: {self.chunkX} {self.chunkY} | Location: {self.locationX} {self.locationY}"

class Slime(Monster):
    MAX_HEALTH = 5
    health = 5

    def __init__(self,chunkX:int,chunkY:int,playerX:int,playerY:int) -> None:
        super().__init__(chunkX,chunkY,playerX,playerY)

class Player:
    MAX_HEALTH = 10
    health = 10
    level = 0

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Name: {self.name} | Health: {self.health}"    