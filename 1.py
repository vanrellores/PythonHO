import random


def get_choices():
    player_choice = input("Enter choice: (rock, paper, scissors)")
    computer_choice = ["rock", "paper", "scissors"]

    choyz = {
        "computer": random.choice(computer_choice),
        "player": player_choice
    }

    return choyz

choice = get_choices()
print(choice)


