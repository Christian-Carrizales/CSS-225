#Problem 3  
#Programmer: Christian Carrizales
#Date: Tuesday, November 17, 2020
#At the top of this file: Problem 3 usimg user input in a while loop.
#Description: While loop being used to create a program to get A,B,C.

#User input that runs in while loop into the input is valid.
print("Guess the number correctly.")
print("Here are your options.")
print("Type A for 25, Type B for 89, Type C for 110")
count1 = 25
count2 = 89
count3 = 110
user_input = "A","B","C" 
A = "incorrect"
B = "correct"
C = "incorrect"
if user_input == A:
    while count1 < 120 :
        print("incorrect")
        if user_input == B:
            while count2 < 120 :
                print("correct")
                if user_input == C:
                    while count3 < 120 :
                        print("incorrect")
        


