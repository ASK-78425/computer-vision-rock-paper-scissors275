
#%%
# Imports
import random as rd
from keras.models import load_model
from camera_rps import get_prediction
from camera_rps import countdown_from_three

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
    prediction_index = get_prediction()
    user_choice = []
    if prediction_index == 0:
        user_choice = "Rock"
    elif prediction_index == 1:
        user_choice = "Paper"
    elif prediction_index == 2:
        user_choice = "Scissors"
    else:
        user_choice = "Nothing"
    return user_choice


#%%
# Create get_winner function
def get_winner(computer_choice, user_choice):
    '''Takes two RPS choices (computer vs user) and compares to output the winner. Calculates winner out of 3 games.
       Arguments:
         computer_choice
         user_choice'''
    winner_key = 0
    if computer_choice == user_choice:
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        print("It's a tie!")
    elif (computer_choice[0] == "R" and user_choice[0] == "P") or (computer_choice[0] == "S" and user_choice[0] == "R") or (computer_choice[0] == "P" and user_choice[0] == "S"):
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        print("You won!")
        winner_key += 1
    else:
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        print("You lost")
        winner_key +=2
    return winner_key

#%%
# Create function play() to simulate the game, amalgamating all prior functions
def play():
    '''This function runs 3 games of RPS and displays
    the winner (computer or user)'''
    computer_wins = 0
    user_wins = 0
    while computer_wins < 3 and user_wins < 3:
        play_user_choice = get_user_choice()
        play_computer_choice = get_computer_choice()
        result = get_winner(play_computer_choice, play_user_choice)
        if result == 1:
            user_wins += 1
        elif result == 2:
            computer_wins += 1
        else:
            continue
    else:
        print("Rounds completed")
    if computer_wins > user_wins:
        print("Computer has won three rounds, you lose.")
    else: 
        print("You have won three rounds! You win!")
