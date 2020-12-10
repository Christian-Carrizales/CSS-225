#Pick Wardrobe.
print("Pick clothing for avatar! Type A for outfit 1, Type B for outfit 2, and Type C for outfit 3.")
print("Outfit 1: Torso: Nike Shirt, Leg: Nike Joggers, Shoes: Nike Air Forces.")
print("Outfit 2: Torso: Crew Hoodie, Leg: Blue Jeans, Shoes: Air Jordan.")
print("Outfit 3: Torso: Black T-Shirt , Leg: Black Jeans, Shoes: Black Nike Forces.")

def pick():
    A = outfit1 = "Torso: Nike Shirt, Leg: Nike Joggers, Shoes: Nike Air Forces."
    B = outfit2 = "Torso: Crew Hoodie, Leg: Blue Jeans, Shoes: Air Jordan."
    C = outfit3 = "Torso: Black T-Shirt , Leg: Black Jeans, Shoes: Black Nike Forces."
    choice = input()
    if choice == ("A"):
        print("Outfit Picked!")
        pick()
    if choice == ("B"):
        print("Outfit Picked!")
        pick()
    if choice == ("C"):
        print("Outfit Picked!")
        pick()
        

