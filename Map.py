# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021
try:
    from numpy import *
    from Characters import Character
except ModuleNotFoundError:
    print("Error")


class Tile():
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Enemy(Tile):
    def __init__(self, name, description, damage, health):
        super().__init__(
            name,
            description,
        )
        self.damage = damage
        self.health = health


class Start(Tile):
    def __init__(self, name, description):
        super().__init__(
            name,
            description,
        )


class Heal(Tile):
    def __init__(self, name, description, health):
        super().__init__(
            name,
            description,
        )
        self.health = health


class Finish(Tile):
    def __init__(self, name, description):
        super().__init__(
            name,
            description,
        )


Jakeperalta = Character("Jake Peralta", "A Officer who defends Brooklyn", 20,
                        10)

Badguy = Enemy("Criminal", "Stole money from a shop", 5, 10)

Healthkit = Heal("Health kit", "Gives the player health", 5)

FinishArea = Finish("The Finish line", "YOU FINISHED THE GAME, CONGRATS!")

StartArea = Start("The Starting line", "This is where you start your journey")


def damage_2_Character():
    Jakeperalta.health = Jakeperalta.health - Badguy.damage
    if Jakeperalta.health > 0:
        print("Jake is still alive")
        print(Jakeperalta.health)

    else:
        print("Jake is dead")


def damage_2_Enemy():
    Badguy.health = Badguy.health - Jakeperalta.damage
    if Badguy.health <= 0:
        print("You killed the Criminal")
        print(Badguy.health)

    else:
        print("The enemys still alive")


def adds_health():
    Jakeperalta.health = Jakeperalta.health + Healthkit.health
    if Jakeperalta.health >= 25:
        print("Your health has increased")
        print(Jakeperalta.health)
    else:
        print(Jakeperalta.health)
        print("Your health has not increased")


def Movement():
    print('''\nMove to try and get to the Finish tile
DO NOT TOUCH THE BOUNDARIES OR ELSE YOU WILL RESTART!!!''')
    print(StartArea.name)
    print(StartArea.description)
    print('''
    +---------------+
    | Start | Enemy |
    | Jake  | Tile  |
    | Tile  |       |
    +---------------+
    | Heal  |Finish |
    | Tile  | Tile  |
    +---------------+''')
    print('''Use 'W, 'A', 'S', 'D' to move around
W is used to go up 
A is used to go left
S is used to go down
D is used to go right''')
    x = 1
    while x == 1:
        move = input("\nMove to the finish: ")
        print('''
    +---------------+
    | Start | Enemy |
    | Jake  | Tile  |
    | Tile  |       |
    +---------------+
    | Heal  |Finish |
    | Tile  | Tile  |
    +---------------+''')
        if move == "W":
            print("You have hit a boundarie you start back at the Start tile")
        elif move == "A":
            print("You have hit a boundarie you start back at the Start tile")
        elif move == "S":
            print("You made it to the heal tile")
            print('''
    +---------------+
    | Start | Enemy |
    | Tile  | Tile  |
    +---------------+
    | Heal  |Finish |
    | Jake  | Tile  |
    | Tile  |       |
    +---------------+''')
            adds_health()
            move_2_finish = input("\nGo to the finish tile: ")
            if move_2_finish == "W":
                print("You can't go this way")
            elif move_2_finish == "A":
                print("You hit a boundarie")
            elif move_2_finish == "S":
                print("You hit a boundarie")
            elif move_2_finish == "D":
                print(FinishArea.name)
                print(FinishArea.description)
                x = 2
            else:
                print(
                    "You were so close just remebre to use Capitals, Try again"
                )

        elif move == "D":
            print("You made it to a Enemy tile")
            print('''
    +---------------+
    | Start | Enemy |
    | Tile  | Jake  |
    |       | Tile  |
    +---------------+
    | Heal  |Finish |
    | Tile  | Tile  |
    +---------------+''')
            print("You encounter a Criminal")
            print("The Criminal attacks you")
            damage_2_Character()
            print("\nYou fight back")
            damage_2_Enemy()
            move_2_finish = input("\nGo to the finish tile: ")
            if move_2_finish == "W":
                print("You hit a boundarie, try again")
            elif move_2_finish == "A":
                print("You can't go this way")
            elif move_2_finish == "D":
                print("You hit a boundarie, try again")
            elif move_2_finish == "S":
                print(FinishArea.name)
                print(FinishArea.description)
                x = 2
            else:
                print('''
YOU WERE SO CLOSE YOU JUST NEED TO REMEBRE \
TO USE CAPITALS, TRY AGAIN.''')
        else:
            print('''YOU NEED TO USE CAPITALS TO MOVE AROUND!!''')


player_maps = array("""
_Police Precinct_
+---------------+
| Start | Enemy |
| Tile  | Tile  |
+---------------+
| Heal  |Finish |
| Tile  | Tile  |
+---------------+
""")


def playerMap():
    print(player_maps)
