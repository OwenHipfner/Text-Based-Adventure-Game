# Owen Hipfner
# Adventure game menu
# CS 30
# 10/20/2021
try:
    from numpy import *
except ModuleNotFoundError:
    print("Error")

player_maps = array("""
--------------Police Precinct--------------
+------+------+------+------+------+------+
| Enemy| Heal | Empty| Empty| Enemy| Heal |
| tile | tile | tile | tile | tile | tile |
+------+------+------+------+------+------+
| Start| Empty| Enemy| Heal | Empty| Enemy|
| point| tile | tile | tile | tile | tile |
+------+------+------+------+------+------+
| Empty| Enemy| Heal | Empty| Heal |Finish|
| tile | tile | tile | tile | tile | tile |
+------+------+------+------+------+------+

--------------Shaw's Bar-------------------
+------+------+------+------+
| Start| Enemy| Empty| Heal |
| point| tile | tile | tile |
+------+------+------+------+
| Empty| Enemy| Empty|Finish|
| tile | tile | tile | tile |
+------+------+------+------+
| Enemy| Heal | Enemy| Heal |
| tile | tile | tile | tile |
+------+------+------+------+

--------------Sal's Pizza------------------
+------+------+------+------+------+------+
| Start| Enemy| Heal | Enemy| Heal | Enemy|
| tile | tile | tile | tile | tile | tile |
+------+------+------+------+------+------+
| Enemy| Heal | Enemy| Heal | Enemy|Finish|
| tile | tile | tile | tile | tile | tile |
+------+------+------+------+------+------+
""")


def playerMap():
    print(player_maps)
