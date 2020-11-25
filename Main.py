from base import Creation, Core, Char

def main():
    menu = "(N)ew game\n(L)oad save\n(Q)uit"
    print("Welcome to a simple python game\n"+ menu)
    choice = input().lower()
    while (choice != "q") :
        if (choice == "n"):
            player = Creation.CCreation()
            Core.main(player)
            choice = input("Welcome to a simple python game\n" + menu +"\n")
        elif (choice == "l"):
            choice = input("Not ready yet, please make another choice\n" + menu +"\n").lower()           
        else:
            choice = input("That wasn't a valid choice, please try again\n" + menu +"\n").lower()

    print("Fare thee well!")
                    

if __name__ == "__main__":
    main()
