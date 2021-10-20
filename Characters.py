# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021

characters = {"Jake Peralta": {"Description": "A Officer who defends Brooklyn",
                               "Health": 200, "Attack": 35},
              "The Vulture":
                              {"Description": "A Dectective that steals cases",
                               "Health": 250, "Attack": 45},
              "Amy Santiago":
                              {"Description": "The spouse of Jake Peralta",
                               "Health": 195, "Attack": 30}
              }


def playerCha():
    print("Characters ")
    for people in characters:
        print(f"{people}: ")
        for item in characters[people]:
            print(f"{item} - {characters[people][item]}")
