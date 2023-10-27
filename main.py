from typing import Dict, List
from generalFunctions import smartInput

world = {}
chunkLocationX = 0
chunkLocationY = 0
playerLocationX = 5
playerLocationY = 5
currentTile = "X"

def addChunk(newChunkX:int,newChunkY:int):
    world[newChunkX] = {}
    world[newChunkX][newChunkY] = []
    for i in range(81):
        world[newChunkX][newChunkY].append("X")

def printChunk(chunkX,chunkY):
    chunk = world[chunkX][chunkY]
    for i, tile in enumerate(chunk, 1):
        if i % 9 != 0:
            print(tile,end="")
        else:
            print(tile)

def validatePosition(newChunkX:int,newChunkY,newPlayerX:int,newPlayerY:int):
    if newChunkX != world or newChunkY != world:    
        addChunk(newChunkX,newChunkY)


def changePlayerLocation(newChunkX:int,newChunkY,newPlayerX:int,newPlayerY:int):
    global playerLocationX, playerLocationY, currentTile
    # Verify within boundaries
    # Replace current position with tile
    world[chunkLocationX][chunkLocationY][(playerLocationX - 1) * 9 + playerLocationY - 1] = currentTile
    # Update current position to new position
    playerLocation = [newPlayerX,newPlayerY]
    # Get new current tile
    currentTile = world[chunkLocationX][chunkLocationY][(playerLocationX - 1) * 9 + playerLocationY - 1]
    # Put player at the new location
    world[chunkLocationX][chunkLocationY][(playerLocationX - 1) * 9 + playerLocationY - 1] = "O"

# Game Loop
inPlay = True
while inPlay:
    userInput = smartInput("Enter Direction (W|A|S|D): ",validinput=("W","A","S","D"),case="upper")
    match userInput:
        case "W":
            changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY+1)