#Imports random
import random

#arrays for human choices, computer choices and variables/ permitted values for user input as well as quit input
computer_choices = ['rock', 'paper', 'scissors']
rock = ['r', 'rock', '1']
paper = ['p', 'paper', '2']
scissors = ['s', 'scissors', '3']
quit = ['stop', 'quit', 'end']
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = "scissors"
QUIT = "quit"

print("The rules: play until you die")

#game logic functions
def get_user_choice(prompt):
    while True:
        user_choice = input(prompt).strip().lower()
        if user_choice in rock:
            return ROCK
        if user_choice in paper:
            return PAPER
        if user_choice in scissors:
            return SCISSORS
        if user_choice in quit:
            return QUIT



def get_win_condition(user_choice, computer_choice):
    if ((user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)):
         return 'user wins'
    elif ((user_choice == ROCK and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == ROCK)):
        return 'computer wins'

while True:
    user_choice = get_user_choice("Rock, Paper, Scissors?: ")
    if user_choice == QUIT:
        print('bye :(')
        break
    computer_choice = random.choice([ROCK, PAPER, SCISSORS])
    win_condition = get_win_condition(user_choice, computer_choice)
    print("YOUR ENEMY THREW A " + computer_choice)
    if win_condition == 'user wins':
        print('You won!')
    elif win_condition == 'computer wins':
        print('You lost!')
    else:
        print('Tie!')
