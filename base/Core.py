from . import Combat, Char

def main(player):
    choices = "(C)ombat\n(Q)uit to menu"
    print("What would you like to do?\n" + choices)
    player_choice = input().lower()
    while (player_choice != "q"):
        if player_choice == "c":
            goblin = Char.Player("Goblin")
            print("Are you the (a)ttacker or (d)efender?")
            cchoice = input().lower()
            if cchoice == "a":          
                Combat.fight(player, goblin)
            if cchoice == "d":
                Combat.fight(goblin, player)
            player_choice = input("\nWhat would you like to do?\n" + choices + "\n").lower()
        else:
            print("That was not a valid input, try again")
            player_choice = input.lower()
    return
