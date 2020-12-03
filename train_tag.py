#Pick up can to tag.
def pick():
    print("Use the spray can by typing in the color of it, Blue Paint to sketch, Black Paint to outline, then hit enter to continue." )
    choice = input()
    if choice == ("Blue Paint"):
        print("Sketch in Blue Paint!")
        pick()

    if choice == ("Black Paint"):
        print("Outline In Black Paint!")
        pick()
pick()
