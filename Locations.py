# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021

locations = {"Police Precinct": {"Description": "Precinct where \
officers meet"},
             "Shaw's bar":
             {"Description": "The bar officers after a case"},
             "Sal's pizza":
             {"Description": "The Pizza shop that burnt down"}
             }


def playerLoc():
    print("Locations ")
    for places in locations:
        print(f"{places}")
        for item in locations[places]:
            print(f"{item} - {locations[places][item]}")
