#Programmer: Christian Carrizales
#Date: Wednesday, December 3, 2020
#At the top of this file: Milestone 3
#Description: Graffiti Land Function.

import main_character
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

import Character_Clothes

#Dialogue 2
print("Later That Day...")
print("Walks Into The Hardware store.")
print("Hardware Store Clerk: How may I help you?")
input()

print(username + ": Yeah Bosa sent me.")
print("Hardware Store Clerk: Follow me.")
print("The Basement")
print("Hardware Store Clerk: Alright, on the wall over there are spray cans already paid for by Bosa.")

import Paint_Cans

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

import train_tag

#Dialogue 4
print("Train Tagged!")
print(username + ": Lets get out of here. The train going to take off through towns all around the country.")
print("Last Tag For The Night...")
print("Last Stop Small Building")
input()

print(username + ": I see the building around the corner.")
print("Nobody around. Let's make this quick!")
input()

import building_tag

#Dialogue 5
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
