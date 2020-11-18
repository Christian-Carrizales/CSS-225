#Problem 4 
#Programmer: Christian Carrizales
#Date: Tuesday, November 17, 2020
#At the top of this file: 
#Description: Archery Program.

#Program that runs archery.
print("A game of archery. 10 arrows aim for the bullseye to score 20 points.")
print("Final Score Card")
points = +20
count = 10 
score = points  
while count > 0 :
    print(count,"arrows left")
    #count = count - 1 
    count -= 1
    print(score,"points")
print("Total Score:",points + points + points + points + points + points + points + points + points + points,"points")
        
