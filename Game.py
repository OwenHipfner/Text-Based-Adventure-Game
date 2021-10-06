# Owen Hipfner
# Adventure game menu
# CS 30
# 9/20/2021


def player_inventory(player, inventory):
    # Defining to print third dictionary properly
    armoured_items = []
    weapons = []
    for item in inventory[player]:
        description = inventory[player][item]["Description"]
        damage = inventory[player][item]["Damage"]
        protection = inventory[player][item]["Armour"]
        print(f"{player}'s {item} - {description}")
        print(f"Damage: {damage}")
        print(f"Armour: {protection}")
        if protection != 0 and damage == 0:
            armoured_items.append(item)
        elif damage != 0:
            weapons.append(item)
    return armoured_items, weapons

# Dictionary for characters
characters = {"Jake Peralta": {"Description": "A Officer who defends Brooklyn",
                               "Health": 200, "Attack": 35},
              "The Vulture":
                              {"Description": "A Dectective that steals cases",
                               "Health": 250, "Attack": 45},
              "Amy Santiago":
                              {"Description": "The spouse of Jake Peralta",
                               "Health": 195, "Attack": 30}
              }

# Dictionary for locations
locations = {"Police Precinct": {"Description": "Precinct where \
officers meet"},
             "Shaw's bar":
             {"Description": "The bar officers after a case"},
             "Sal's pizza":
             {"Description": "The Pizza shop that burnt down"}
             }

# Dictionary for inventory of characters
inventory = {"Jake Peralta": {"Standard Police Handgun":
                              {"Description": "Standard issue gun from police",
                               "Damage": 10, "Armour": 0},
                              "Armour vest":
                              {"Description": "Gives protection when worn",
                               "Damage": 0, "Armour": 100}},
             "The Vulture": {"Standard Police Handgun":
                             {"Description": "Standard issue gun from police",
                              "Damage": 10, "Armour": 0},
                             "Armour vest":
                             {"Description": "Gives protection when worn",
                              "Damage": 0, "Armour": 100}},
             "Amy Santiago": {"Standard Police Handgun":
                              {"Description": "Standard issue gun from police",
                               "Damage": 10, "Armour": 0},
                              "Armour vest":
                              {"Description": "Gives protection when worn",
                               "Damage": 0, "Armour": 100},
                              "Pepper spary":
                              {"Description": "Blinds enemy at close range",
                               "Damage": 15, "Armour": 0}}}

print(''' In the menu you can chose what action your character can
 do in game.
 The choices are:
 Move forward with 'W'
 Move to the left with 'A'
 Move backwards with 'S'
 Move to the right with 'D'
 For Characters use 'C'
 For Locations use 'L'
 For Inventory use 'I'
 If you want to leave the menu use 'Q' ''')

a = 1

while a == 1:
    # This while command is used to loop the code
    # Until the user quits the menu.
    user_input = str(input("Choose your action: "))

    if user_input == "W":
        # User input will print the message on the console
        # Then ask again what action the user will do.
        print("You've moved forward!")

    elif user_input == "A":
        print("You've moved left!")

    elif user_input == "S":
        print("You've moved right")

    elif user_input == "D":
        print("You've moved backward")

    elif user_input == "C":
        # When 'C' is chosen it will print the characters
        print("Characters ")
        for people in characters:
            print(f"{people}: ")
            for item in characters[people]:
                print(f"{item} - {characters[people][item]}")

    elif user_input == "L":
        # When 'L' is chosen it will print the locations dictionary
        print("Locations ")
        for places in locations:
            print(f"{places}")
            for item in locations[places]:
                print(f"{item} - {locations[places][item]}")

    elif user_input == "I":
        # When 'I' is chosen it will print the inventory for characters
        print("Inventory ")
        player_inventory("Jake Peralta", inventory)
        print("\n")
        player_inventory("The Vulture", inventory)
        print("\n")
        player_inventory("Amy Santiago", inventory)

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
        print("Invalid, Try upper case letter or use 'W','A','S','D','Q'.")
