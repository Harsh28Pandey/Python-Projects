'''
Workflow of Project
1 - Input from user(rock, Paper, Scissor)
2 - Computer choice (Computer will choose randomly not conditionally)
3 - Result print

Cases:
A - Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Scissor Win

B - Paper
Paper - Rock = Paper Win
Paper - Paper - Tie
Paper - Scissor = Scissor win

C - Scissor
Scissor - Rock = Rock Win
Scissor - Paper = Scissor Win
Scissor - Scissor = Tie

'''

import random

item_list = ["rock", "paper", "scissor"]
print("Welcome Rock, Paper and Scissor Game Let's Start")
user_name = input("Enter the User name = ")

i = 0

while i < 3:
    user_choice = input("Enter your move (rock, raper, scissor) = ")
    computer_choice = random.choice(item_list)

    print(f"{user_name} Choose = {user_choice}")
    print(f"Computer Choose = {computer_choice}")

    if(user_choice == computer_choice):
        print("Both Choose Same then Match Tie!")

    elif(user_choice == "rock"):
        if(computer_choice == "paper"):
            print("Paper covers Rock then Computer Wins!")
        else:
            print(f"Rock smashes Scissor then {user_name} Wins!")

    elif(user_choice == "paper"):
        if(computer_choice == "scissor"):
            print("Scissor cuts paper then Computer Wins!")
        else:
            print(f"Paper covers rock then {user_name} Wins!")

    elif(user_choice == "scissor"):
        if(computer_choice == "paper"):
            print(f"Scissor cuts Paper then {user_name} Wins!")
        else:
            print("Rock smashes Scissor then Computer Wins!")