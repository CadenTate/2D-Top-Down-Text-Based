# Import Required Dependencies
from typing import Dict, List
from generalFunctions import smartInput
import random
import characters

# Initialize Class Level Variables
world = {}
chunkLocationX = 0
chunkLocationY = 0
playerLocationX = 5
playerLocationY = 5
currentTile = "g"
availableTiles = ["g","g","g","g","g","g","g","g","w","w"]
activeMonsters = []

# Creates a new chunk, populates it, and adds it to the world
def addChunk(newChunkX:int,newChunkY:int):
    global activeMonsters
    if newChunkX not in world:
        world[newChunkX] = {}
    world[newChunkX][newChunkY] = []

    # Add tiles to world
    for i in range(81):
        world[newChunkX][newChunkY].append(random.choice(availableTiles))

    # Add Monsters to world
    for i in range(0,random.randint(4,9)):
        activeMonsters.append(characters.Slime(newChunkX,newChunkY,random.randint(1,10),random.randint(1,10)))

# Print out the chunk in the correct format
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
        addChunk(newChunkX,newChunkY)

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

def displayArena(player:characters.Player,monster:characters):
    match monster.getType():
        case "slime":
            print("""
   /-------\\
  /         \\
 /  O     O  \\
/    [---]    \\
\\=============/""")
            print(monster)


# Game Setup
player = characters.Player(smartInput("Player Name: "))
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
                changePlayerLocation(chunkLocationX,chunkLocationY + 1,playerLocationX,playerLocationY - 1)
            else: 
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY-1)
        case "A":
            if playerLocationX - 1 == 0:
                changePlayerLocation(chunkLocationX-1,chunkLocationY,playerLocationX-1,playerLocationY)
            else:
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX-1,playerLocationY)
        case "S":
            if playerLocationY + 1 == 10:
                changePlayerLocation(chunkLocationX,chunkLocationY - 1,playerLocationX,playerLocationY+1)
            else:
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX,playerLocationY+1)
        case "D":
            if playerLocationX + 1 == 10: 
                changePlayerLocation(chunkLocationX + 1,chunkLocationY,playerLocationX+1,playerLocationY)
            else:
                changePlayerLocation(chunkLocationX,chunkLocationY,playerLocationX+1,playerLocationY)
    printChunk(chunkLocationX,chunkLocationY)
    for monster in activeMonsters:
        if monster.location() == (chunkLocationX,chunkLocationY,playerLocationX,playerLocationY):
            # TODO combat system 
            displayArena(player,monster)