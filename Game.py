# Owen Hipfner
# Adventure game menu
# CS 30
# 9/20/2021
print(''' In the menu you can chose what action your character can do in game.
 The choices are:
 Move forward with 'W'
 Move to the left with 'A'
 Move backwards with 'S'
 Move to the right with 'D'
 If you want to leave the menu use 'Q' ''')
a = 1
while a == 1:
    # This while command is used to loop the code until the user quits the menu.
    user_input = str(input("Chose your action: "))

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

    elif user_input == "Q":
        quit_input = str(input("Are you sure you want to Quit, type 'y' for yes and 'n' for no: "))
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
    print("Invalid command, Try upper case letter or use 'W','A','S','D','Q'.")
