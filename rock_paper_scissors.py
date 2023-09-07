# We will write a rock paper scissors game in class - Complete it in this file

import random

def player_won() -> bool:

    if player_choice == "rock" and computer_choice == "scissors":
        return True

    if player_choice == "scissors" and computer_choice == "paper": 
        return True
    
    if player_choice == "paper" and computer_choice == "rock":
        return True
    
    if player_choice == computer_choice:
        print("YOU DRAW!")
        return False
    
    print("YOU LOSE!")
    return False

def get_choices() -> tuple:

    options = ["rock", "paper", "scissors"]

    player_choice = input("ROCK, PAPER, SCISSORS - SHOOT! \n")
    computer_choice = random.choice(options)

    return player_choice, computer_choice

playing = True

while playing:
    player_choice, computer_choice = get_choices()

    if player_won():
        print("YOU WIN!")

    rematch = input("Want to play again? (y/n) \n")

    if rematch == "y":
        pass
    elif rematch == "n":
        playing = False
    else:
        print("Invalid response")
        playing = False


