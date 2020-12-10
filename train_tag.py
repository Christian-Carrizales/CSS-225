#Pick up can to tag.
def pick():
    print("Use the spray can of paint by typing in the color, then hit enter to continue." )
    choice = input()
    if choice == "Black Paint":
        return "Sprayed Black!"
    elif choice == "Blue Paint":
            return "Sprayed Blue!"
            pick()
            if choice == "Red Paint":
                return "Sprayed Red!"
                if choice == "Yellow Paint":
                    return "Sprayed Yellow!"
                    pick()
                    if choice == "Green Paint":
                        return "Sprayed Green!"
                    elif choice == "Orange Paint":
                            return "Sprayed Orange!"
                            if choice == "Purple Paint":
                                return "Sprayed Purple!"
                                pick()
                            else:
                                 print("Incorrect")
    

    

