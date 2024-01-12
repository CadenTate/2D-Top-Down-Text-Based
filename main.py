from customControl import smartInput as input, Vector2
from math import sqrt

# world = {Y:{X:[world stuff]}}
world = {}

playerLocation = Vector2(5,5)
playerChunk = Vector2(0,0)
chunkSize = 81
playerCharacter = "O"

def genChunk(chunk:Vector2) -> None:
    x, y = chunk
    # See if y-level exits
    if y not in world:
        world[y] = {}
    world[y][x] = []

    for i in range(chunkSize):
        world[y][x].append("g")


def printChunk(location:Vector2) -> None:
    # Validate Chunk Exists
    try:
        chunk = world[location.y][location.x]
    except KeyError:
        print("Chunk Does Not Exist")
        return

    # Print Chunk
    for i,tile in enumerate(chunk):
        i += 1
        if i % sqrt(len(chunk)) == 0:
            print(tile)
        else:
            print(tile,end="")

def addPlayer(chunkLocation:Vector2,playerLocation:Vector2) -> None:
    cX, cY = chunkLocation
    pX, pY = playerLocation
    chunk = world[cY][cX]
    playerIndex = pY * sqrt(chunkSize) - 
    currentLocation = chunk.index(playerCharacter)
    chunk[currentLocation] = "g"
    chunk[]


# Generate Starting Chunk
genChunk(playerChunk)
world[0][0][40] = playerCharacter
addPlayer(playerChunk,playerLocation)


# Game Loop
inPlay = True

while inPlay:
    # Print Chunk
    printChunk(playerChunk)

    # Process Player Input
    playerMove = input(validinput=('w','a','s','d'))
    match playerMove:
        case 'w':
            playerLocation += 1
        case 'a':
            playerLocation.x -= 1
        case 's':
            playerLocation.y -= 1
        case 'd':
            playerLocation.y += 1