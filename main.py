from typing import Dict, List
from generalFunctions import smartInput
import random

world = {}
chunkLocationX = 0
chunkLocationY = 0
playerLocationX = 5
playerLocationY = 5
currentTile = "g"
availableTiles = ["g","g","g","g","g","g","g","g","w","w"]

def addChunk(newChunkX:int,newChunkY:int):
    if newChunkX != None:
        world[newChunkX] = {}
    world[newChunkX][newChunkY] = []
    for i in range(81):
        world[newChunkX][newChunkY].append(random.choice(availableTiles))

def printChunk(chunkX:int,chunkY:int):
    chunk = world[chunkX][chunkY]
    for i, tile in enumerate(chunk, 1):
        if i % 9 != 0:
            print(tile,end="")
        else:
            print(tile)

def changePlayerLocation(newChunkX:int,newChunkY,newPlayerX:int,newPlayerY:int):
    global playerLocationX, playerLocationY, currentTile, chunkLocationX, chunkLocationY
    # Verify within boundaries
    if newChunkX not in world:
        addChunk(newChunkX,newChunkY)
    elif newChunkY not in world[newChunkX]:
        addChunk(None,newChunkY)

    if newPlayerX == 10:
        newPlayerX = 1
    elif newPlayerX == 0:
        newPlayerX = 9

    if newPlayerY == 10:
        newPlayerY = 1
    elif newPlayerY == 0:
        newPlayerY = 9
    # Replace current position with tile
    world[chunkLocationX][chunkLocationY][(playerLocationY - 1)  * 9 + playerLocationX - 1] = currentTile
    # Update current position to new position
    playerLocationX = newPlayerX
    playerLocationY = newPlayerY
    chunkLocationX = newChunkX
    chunkLocationY = newChunkY
    # Get new current tile
    currentTile = world[chunkLocationX][chunkLocationY][(playerLocationY - 1) * 9 + playerLocationX - 1]
    # Put player at the new location
    world[chunkLocationX][chunkLocationY][(playerLocationY - 1) * 9 + playerLocationX - 1] = "O"

# Game Setup
inPlay = True
addChunk(0,0)
changePlayerLocation(0,0,5,5)
printChunk(chunkLocationX,chunkLocationY)

# Game Loop
while inPlay:
    print(chunkLocationX,chunkLocationY)
    print(playerLocationX,playerLocationY)
    userInput = smartInput("Enter Direction (W|A|S|D): ",validinput=("W","A","S","D"),case="upper")
    print(userInput)
    match userInput:
        case "W":
            if playerLocationY - 1 == 0: 
                changePlayerLocation(chunkLocationX,chunkLocationY - 1,playerLocationX,playerLocationY - 1)
            else: 
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY-1)
        case "A":
            if playerLocationX - 1 == 0:
                changePlayerLocation(chunkLocationX-1,chunkLocationY,playerLocationX-1,playerLocationY)
            else:
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX-1,playerLocationY)
        case "S":
            if playerLocationY + 1 == 10:
                changePlayerLocation(chunkLocationX,chunkLocationY + 1,playerLocationX,playerLocationY+1)
            else:
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY+1)
        case "D":
            if playerLocationX + 1 == 10: 
                changePlayerLocation(chunkLocationX + 1,chunkLocationY,playerLocationX+1,playerLocationY)
            else:
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX+1,playerLocationY)
    printChunk(chunkLocationX,chunkLocationY)