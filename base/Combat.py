def fight(attacker, defender, player):
    print("A fight has begun, " + attacker.name +" is attacking " + defender.name + "!")
    choice_menu = "Actions:\n(A)ttack\n(S)hoot\n(D)efend\n(E)quipment\n(F)lee\n"
    state = 1
    while (state != 0):
        action = input("Actions:\n(A)ttack\n(S)hoot\n(D)efend\n(E)quipment\n(F)lee\n").lower()
        if (action == "a"):
            print("You attacked!\n")
            #TODO: Attacking function, always hits but lowers defence for the turn
            action = input("What next?\n"+ choice_menu).lower()
        elif (action == "s"):
            print("You fired your weapon!\n")
            #TODO: Shooting function, chance of missing and maintain ammo count
            action = input("What next?\n"+ choice_menu).lower()
        elif (action == "d"):
            print("You prepare to evade!\n")
            #TODO: Evasion function, Increase evasion chance for a short duration
            action = input("What next?\n" + choice_menu).lower()
        elif (action == "e"):
            print("You search through your bag quickly!")
            #TODO: Inventory use function, quickslot items only
            action = input("What next?\n" + choice_menu).lower()
        elif (action == "f"):
            print("You flee the fight!\n")
            #TODO: Flee function, don't allow guarenteed escape. Consider based on speed stat or health perhaps
            state = 1
        else:
            action = input("that was an invalid input, try again\n"+choice_menu).lower()
    return

