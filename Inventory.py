# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021


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


def playerINV():
    print("Inventory ")
    player_inventory("Jake Peralta", inventory)
    print("\n")
    player_inventory("The Vulture", inventory)
    print("\n")
    player_inventory("Amy Santiago", inventory)
