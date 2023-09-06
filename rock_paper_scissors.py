# We will write a rock paper scissors game in class - Complete it in this file

import random

def player_won() -> bool:
    """
    PAPER : ROCK

    SCISSORS : PAPER

    ROCK : SCISSORS
    """

    if player_choice == "rocK" and computer_choice == "scissors":
        return True

    if player_choice == "scissors" and computer_choice == "paper": 
        return True
    
    if player_choice == "paper" and computer_choice == "rock":
        return True
    
    return False

def get_choices() -> tuple:

    options = ["rock", "paper", "scissors"]

    player_choice = input("ROCK, PAPER, SCISSORS -> SHOOT!")
    computer_choice = random.choice(options)

    return player_choice, computer_choice

player_choice, computer_choice = get_choices()

if player_won():
    print("YOU WIN!")
else:
    print("YOU LOSE!")

