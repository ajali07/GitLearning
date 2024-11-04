

import random


choices = ["rock", "paper", "scissors"]


userInput = input("Enter rock, paper, or scissors: ").lower() #user input 
computerRandomInput = random.choice(choices)

#printing user and computer choice
print("You chose: " + userInput)
print("The Computer chose: " + computerRandomInput)

#choosing winner
if userInput == computerRandomInput:
    print("Tie game!") 
elif (userInput, computerRandomInput) in [("paper", "rock"), ("scissors", "paper"), ("rock", "scissors")]:
    print("You won, woo woo!!")
else:
    print("You lost, :/")
