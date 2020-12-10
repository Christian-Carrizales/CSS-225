#Pick up spray cans.
def pick():
    print("Select the color spray cans you want to use! Blue, Black, Red, Yellow, Green, Orange, purple.")
    choice = input()
    if choice == ("Blue"):
        print("Collected Blue Can!")
        pick()
    if choice == ("Black"):
        print("Collected Black Can!")
        pick()
    if choice == ("Red"):
        print("Collected Red Can!")
        pick()
    if choice == ("Yellow"):
        print("Collected Yellow Can!")
        pick()
    if choice == ("Green"):
        print("Collected Green Can!")
        pick()
    if choice == ("Orange"):
        print("Collected Orange Can!")
        pick()
    if choice == ("Purple"):
        print("Collected Purple Can!")
        pick()

    else:
        print("Added to inventory")

                  

