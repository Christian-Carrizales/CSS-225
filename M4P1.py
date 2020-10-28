#This program takes the current time in hours between 0-23
#and the number of hours the user will wait.
#It will print what the time is in hours (between 0-23) after the user is done waiting
current_Time_Str = input("What is the current time (in hours 0-23)?")
wait_Time_Str = input("How many hours do you want to wait?")

current_Time_Int = int(current_Time_Str)
wait_Time_Int = int(wait_Time_Str)

final_Time_Int = current_Time_Int + wait_Time_Int
print(final_Time_Int)
