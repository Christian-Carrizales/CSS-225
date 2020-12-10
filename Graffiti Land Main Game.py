#Programmer: Christian Carrizales
#Date: Wednesday, December 9, 2020
#At the top of this file: Final Milestone
#Description: Graffiti Land Function.

import main_character
import Character_Clothes
import Paint_Cans
import train_tag
import building_tag

Character_Clothes.pick()
username = input("Create Username:")
#Intro
print("Welcome To Graffiti Land!" + username + "!")
print("Let's Tag The City Up!")
input()

#Dialogue 1
print("Bosa: Welcome to the crew" +  username + ".")
print("Bosa: It's about time you start making your name known around here!")
input()

print("Bosa: Grab some cans and tag up all the spots on the map.")
print("Bosa: Watch out for cops and watch out for the other taggers in the neighborhood.")
print("Bosa: You Ready.")
input()

print(username + ": Ready to put my name on the map.")
print("Bosa: Go to the hardware store around the corner. Tell them Bosa sent you.")
input()

#Dialogue 2
print("Later That Day...")
print("Walks Into The Hardware store.")
print("Hardware Store Clerk: How may I help you?")
input()

print(username + ": Yeah Bosa sent me.")
print("Hardware Store Clerk: Follow me.")
print("The Basement")
print("Hardware Store Clerk: Alright, on the wall over there are spray cans already paid for by Bosa.")

Paint_Cans.pick()

#Dialogue 3
print("Hardware Store Clerk: Alright, looks like your ready to go kid.")
print("Later That Night...")
print(username + ": First stop train yard.")
input()

print("Arrived at the train yard. Guards are on patrol.")
print(username + ": Looks like I got go around them.")
print("That gate can be climbed to make my way into the train yard.")
input()

print(username + ": Finally, made it over the gate. Now, lets find a train.")
print("Move slow around the train yard.")
print(username + ": Found a train to tag on.")
input()

train_tag.pick()

#Dialogue 4
print("Train Tagged!")
print(username + ": Lets get out of here. The train going to take off through towns all around the country.")
input()
print("Last Tag For The Night...")
print("Last Stop Small Building")
input()

print(username + ": I see the building around the corner.")
print("Nobody around. Let's make this quick!")
input()

building_tag.pick()

#Dialogue 5
print("Building Tagged")
print("Enemy Tagger:" + username + ", I suggest you find another place to tag on this is my spot. Grab your cans and leave. Or else.")
print(username + ": Alright, it's done anyways.")
print("Enemy Tagger: Not so fast. Rookie.")
print("Drop the cans!")
print("Enemy Tagger grabs the spray cans to cover up your tag.")
input()

print("Enemy Tagger: Yup, it's done alright. Now you can go.")
print("Next Morning")
print("Bosa: Nice job on that train tag kid. It's already been spotted in Detroit.")
input()

print(username + ":" + " My name is already being known.")
print("Mission Completed")
print("You successfully tagged" + username)
input()

main_character.player()

