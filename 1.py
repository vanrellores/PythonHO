import random


# def get_choices():
#     player_choice = input("Enter choice: (rock, paper, scissors)")
#     computer_choice = ["rock", "paper", "scissors"]

#     choyz = {
#         "computer": random.choice(computer_choice),
#         "player": player_choice
#     }

#     return choyz


def check_win(player, computer):
    print(f"You chose {player}, " + f"Computer chose {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose.")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose.")
    else:
        if computer == "rock":
            print("You win!")
        else:
            print("You lose.")

def get_choice():
    P = input("Enter choice: (rock, paper or scissors)")
    Com_choice = ["rock", "paper", "scissors"]
    C = random.choice(Com_choice)
    return P, C
check_win(*get_choice())
    
