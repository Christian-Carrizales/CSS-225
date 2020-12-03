#Pick up spray cans.
def pick():
    print("Pick up the can of paint by typing in the color of it Black Paint, Blue Paint!")
    choice = input()
    if choice == ("Black Paint"):
        print("Collected Black Can!")
        pick()
    if choice == ("Blue Paint"):
        print("Collected Blue Can!")
        pick()
pick()

                  

