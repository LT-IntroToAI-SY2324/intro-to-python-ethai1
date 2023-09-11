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

def get_choices() -> str:
    options = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("ROCK, PAPER, SCISSORS - SHOOT! \n")

        if player_choice == "rock" or player_choice == "scissors" or player_choice == "paper":
            break

        print("Invalid response. Please try again!")

    computer_choice = random.choice(options)

    return player_choice, computer_choice

playing = True

while playing:
    player_choice, computer_choice = get_choices()

    if player_won():
        print("YOU WIN!")


    while True:
        rematch = input("Want to play again? (y/n) \n")

        if rematch == "y":
            break
        elif rematch == "n":
            playing = False
            break

        print("Invalid response. Please try again!")


