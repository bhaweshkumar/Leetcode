import random

computer_options =["rock", "paper", "scissor"]

while True:
    user_selection = input("choose rock, paper, scissor\n")
    computer_selection = random.choice(computer_options)

    if user_selection == computer_selection:
        print("Tie,", "user", user_selection, "computer", computer_selection)
    elif user_selection == "rock" and computer_selection == "paper":
        print("computer wins,", "user", user_selection, "computer", computer_selection)
    elif user_selection == "paper" and computer_selection == "scissor":
        print("computer wins,", "user", user_selection, "computer", computer_selection)
    elif user_selection == "scissor" and computer_selection == "rock":
        print("computer wins,", "user", user_selection, "computer", computer_selection)
    else:
        print("user wins,", "user", user_selection, "computer", computer_selection)
