
#%%
# Imports
import random as rd

#%%
# Create get_computer_choice
def get_computer_choice():
    '''Randomly returns one of three options:
    Rock, Paper, or Scissors'''
    rps_list = ["Rock", "Paper", "Scissors"]
    choice = rd.choice(rps_list)
    return choice

#%%
# Create get_user_choice
def get_user_choice():
    '''Takes in and returns user input'''
    user_choice = input("Enter choice: ")
    return user_choice

#%%