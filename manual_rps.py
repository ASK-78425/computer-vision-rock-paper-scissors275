
#%%
# Imports
import random as rd

#%%
# Create get_computer_choice
def get_computer_choice():
    '''Randomly returns one of three options:
    Rock, Paper, or Scissors'''
    rps_list = ["Rock", "Paper", "Scissors"]
    computer_choice = rd.choice(rps_list)
    return computer_choice

#%%
# Create get_user_choice
def get_user_choice():
    '''Takes in and returns user input'''
    user_choice = input("Enter choice: ")
    return user_choice.capitalize()

#%%
# Create get_winner function
def get_winner(computer_choice, user_choice):
    '''Takes two RPS choices (computer vs user) and compares to output the winner
       Arguments:
         computer_choice
         user_choice'''
    if computer_choice == user_choice:
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        print("It's a tie!")
    elif (computer_choice[0] == "R" and user_choice[0] == "P") or (computer_choice[0] == "S" and user_choice[0] == "R") or (computer_choice[0] == "P" and user_choice[0] == "S"):
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        print("You won!")
    else:
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        print("You lost")

#%%
# Create function (play()) to simulate the game, amalgamating all prior functions
def play():
    '''This function runs a game of RPS and displays the winner (computer or user)'''
    play_user_choice = get_user_choice()
    play_computer_choice = get_computer_choice()
    get_winner(play_computer_choice, play_user_choice)
