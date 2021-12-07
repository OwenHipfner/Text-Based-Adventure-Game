# Owen Hipfner
# Adventure game menu
# CS 30
# 9/20/2021
try:
    from numpy import *
    import Inventory as Inv
    import Characters as Cha
    import Locations as Loc
    import Map as Ma
    from Characters import Character
    from Map import Movement, damage_2_Character, damage_2_Enemy, adds_health
    from Map import Tile, Enemy, Heal, Start, Finish
except ModuleNotFoundError:
    print("Error")
else:
    print("All Moduels/Files printed succesfully")

print('''\n
In the menu you can chose see what your character \
can do in game and where he will be.

The choices are:''')

a = 1

while a == 1:
    # This while command is used to loop the code
    # Until the user quits the menu.
    print('''
For Characters use 'C'
For Locations use 'L'
For Inventory use 'I'
For Map use 'M'
To Start the game use 'E'
If you want to leave the menu use 'Q' ''')
    user_input = str(input("\nChoose your action: "))

    if user_input == "C":
        # When 'C' is chosen it will print the characters
        Cha.playerCha()

    elif user_input == "L":
        # When 'L' is chosen it will print the locations dictionary
        Loc.playerLoc()

    elif user_input == "I":
        # When 'I' is chosen it will print the inventory for characters
        Inv.playerINV()

    elif user_input == "M":
        Ma.playerMap()

    elif user_input == "E":
        Jakeperalta = Character("Jake Peralta",
                                "A Officer who defends Brooklyn", 20, 10)

        Badguy = Enemy("Criminal", "Stole money from a shop", 5, 10)

        Healthkit = Heal("Health kit", "Gives the player health", 5)

        FinishArea = Finish("The Finish line", "Where the game ends Congrats!")

        StartArea = Start("The Starting line",
                          "This is where you start your journey")

        Movement()

    elif user_input == "Q":
        print("Are you sure you want to Quit")
        quit_input = str(input("Type 'y' for yes and 'n' for no: "))

        if quit_input == "y":
            print("You've chosen quit Goodbye!")
            a = 2

        elif quit_input == "n":
            print("You'll stay in the menu")

        else:
            # If the input for quiting doesn't match it will say Invalid
            print("Invalid command, Try lower case letter or use 'n' or 'y'.")

    else:
        # The same printed message occurs when the user types the wrong input.
        print("Invalid, Try upper case letter or use 'W','A','S','D','Q',\
'C','L','I','M'.")
