#Grab a spray can to tag.
def pick():
    print("Grab the can of paint by typing the name of the paint in order., \n Red Paint \n Blue Paint \n Black Paint \n Gold Paint, then hit enter.")
    choice = input()
    if choice == ("Black Paint"):
        print("Outlined in Black Paint!")
        pick()
    if choice == ("Blue Paint"):
        print("Shade With Blue Paint!")
        pick()
pick()
