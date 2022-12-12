#Rock Paper Scissors Game
#Based on:
#https://www.youtube.com/watch?v=fn68QNcatfo
#https://stackoverflow.com/questions/34102365/rock-paper-scissors-game-python
#Initialise
import random

options = ["rock", "paper", "scissors", "dog", "cat"]

isRunning = True

while isRunning:

    player = None
    #allows us to pick a random choice from options
    computer = random.choice(options) 

    #if the player doesn't pick an option, while loop will play until player picks
    while player not in options: 
        player = input("Rock, paper, scissors... (rock, paper, scissors, dog, cat): ")

    print(f"Player:{player}")
    print(f"Computer:{computer}")


    #Win/lose Conditions
    winCon = {"rock":"scissors", 
             "scissors":"paper", 
             "paper":"rock", 
             "dog":"cat", 
             "cat":"paper"
             }

    if winCon[player] == computer:
        print("Player Wins")
    elif winCon[computer] == player:
        print("Computer Wins")
    else:
        print("Tie")

    if not input("Play again? (y/n): ").lower() == "y":
        isRunning = False

print("Thanks for playing :) \nGoodbye")
