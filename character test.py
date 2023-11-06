import characters

def displayArena(player:characters.Player,monster:characters):
    match monster.getType():
        case "slime":
            print("""
   /-------\\
  /         \\
 /  O     O  \\
/    [---]    \\
\\=============/""") 

displayArena(characters.Player("Caden"),characters.Slime(0,0,0,0))