from . import Char

def CCreation():
    print("Welcome, what is your name?")
    player_name = input()
    player = Char.Player(player_name)
    print("Welcome " + player.name)
    return player
