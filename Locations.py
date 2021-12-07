# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021

locations = {
    "Police Precinct": {
        "Description": "Precinct where \
officers meet"
    },
}


def playerLoc():
    print("Location: ")
    for places in locations:
        print(f"{places}")
        for item in locations[places]:
            print(f"{item} - {locations[places][item]}")
