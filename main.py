from typing import Dict, List
from generalFunctions import smartInput

world = {}
chunkLocation = [0,0]
playerLocation = [5,5]
currentTile = "X"

def addChunk():
    x = chunkLocation[0]
    y = chunkLocation[1]
    
    world[x] = {}
    world[x][y] = []
    for i in range(81):
        world[x][y].append("X")

def printChunk():
    chunk = world[chunkLocation[0]][chunkLocation[1]]
    for i, tile in enumerate(chunk, 1):
        if i % 9 != 0:
            print(tile,end="")
        else:
            print(tile)

def changePlayerLocation(chunkX:int,chunkY,playerX:int,playerY:int):
    global playerLocation
    # Verify within boundaries
    if playerX >= 1 and playerX <= 9 and playerY >= 1 and playerY <= 9:
        # Replace current position with tile
        world[chunkLocation[0]][chunkLocation[1]][(playerLocation[0] - 1) * 9 + playerLocation[1] - 1] = currentTile
        # Update current position to new position
        playerLocation = [playerX,playerY]
        # Get new current tile
        currentTile = world[chunkLocation[0]][chunkLocation[1]][(playerLocation[0] - 1) * 9 + playerLocation[1] - 1]
        # Put player at the new location
        world[chunkLocation[0]][chunkLocation[1]][(playerLocation[0] - 1) * 9 + playerLocation[1] - 1] = "O"
    else:
        print("Invalid Position")
        return -1

# Game Loop
inPlay = True
while inPlay:
    userInput = smartInput("Enter Direction",validinput=("W","A","S","D"),case="upper")
