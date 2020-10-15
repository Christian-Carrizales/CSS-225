#player_actions.py


def check_play_again(user_input):
    if user_input == "y":
        print("Play Again!")
    elif user_input == "n":
        print("Quit Game")
    else: print("Incorrect")

check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
