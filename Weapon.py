class Weapon():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        return "{}\n_________\n{}\nDamage: {}\n".format(
            self.name, self.description, self.damage)


class Distant(Weapon):
    def __init__(self, name, description, damage, ammo):
        super().__init__(name, description, damage)
        self.ammo = ammo

    def __str__(self):
        return "{}\n_________\n{}\nDamage: {}\nAmmo: {}\n".format(
            self.name, self.description, self.damage, self.ammo)


class Handgun(Distant):
    def __init__(self):
        super().__init__(name="Police Handgun",
                         description="A handgun given to defeat enemies",
                         damage=10,
                         ammo=6)


def list_weapon():
    print(Handgun())


list_weapon()
