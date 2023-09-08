# We will write a rock paper scissors game in class - Complete it in this file

import random

def player_won() -> bool:

    if player_choice == "rock" and computer_choice == "scissors":
        print(f"You chose: {player_choice} - Computer chose: {computer_choice}")
        print(f"{player_choice} smashes {computer_choice}")
        return True

    if player_choice == "scissors" and computer_choice == "paper": 
        print(f"You chose: {player_choice} - Computer chose: {computer_choice}")
        print(f"{player_choice} smashes {computer_choice}")
        return True
    
    if player_choice == "paper" and computer_choice == "rock":
        print(f"You chose: {player_choice} - Computer chose: {computer_choice}")
        print(f"{player_choice} smashes {computer_choice}")
        return True
    
    if player_choice == computer_choice:
        print(f"You chose: {player_choice} - Computer chose: {computer_choice}")
        print("You DRAW!")
        return False
    
    print(f"You chose: {player_choice} - Computer chose: {computer_choice}")
    print(f"{computer_choice} smashes {player_choice}")
    print("You LOSE!")
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


