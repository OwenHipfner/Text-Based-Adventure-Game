# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021


class Character():
    def __init__(
        self,
        name,
        description,
        health,
        damage,
    ):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage


Jakeperalta = Character("Jake Peralta", "A Officer who defends Brooklyn", 20,
                        10)


def playerCha():
    print(f"\n__Your_Character__")
    print(Jakeperalta.name)
    print(Jakeperalta.description)
    print("Jake's Health:")
    print(Jakeperalta.health)
    print("Jake's Damage:")
    print(Jakeperalta.damage)
