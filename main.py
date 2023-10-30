from typing import Dict, List
from generalFunctions import smartInput
import random

world = {}
chunkLocationX = 0
chunkLocationY = 0
playerLocationX = 5
playerLocationY = 5
currentTile = "X"
availableTiles = ["g","g","g","g","g","g","g","g","w","w"]

def addChunk(newChunkX:int,newChunkY:int):
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
    global playerLocationX, playerLocationY, currentTile
    # Verify within boundaries
    if newChunkX not in world or newChunkY not in world:    
        addChunk(newChunkX,newChunkY)
    if newPlayerX >= 9:
        newPlayerX = 0
    if newPlayerY >= 9:
        newPlayerY = 0
    # Replace current position with tile
    world[chunkLocationX][chunkLocationY][(playerLocationY - 1)  * 9 + playerLocationX - 1] = currentTile
    # Update current position to new position
    playerLocationX = newPlayerX
    playerLocationY = newPlayerY
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
    userInput = smartInput("Enter Direction (W|A|S|D): ",validinput=("W","A","S","D"),case="upper")
    print(userInput)
    match userInput:
        case "W":
            changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY-1)
        case "A":
            changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX-1,playerLocationY)
        case "S":
            changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY+1)
        case "D":
            changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX+1,playerLocationY)
    printChunk(chunkLocationX,chunkLocationY)