# Project 1 - Snake, Water and Gun Game
# We all have played snake, water and gun game in our childhood. If you haven't, google the rules of this game and write a python program that are capable of playing this game with the user.

'''

1 for snake
-1 for water
0 for gun

'''

import random
computer = random.choice([1, 0, -1])

you_str = input("Enter your choice {s, w, g}: ")
you_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

you = you_dict[you_str]

# By now we have 2 numbers (variables), you and computer.

print(f"You Choose : {reverse_dict[you]} \nComputer Choose: {reverse_dict[computer]}")

if(computer == you):
    print("It's a Draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something Went Wrong!")




# The another logic in python to run this snake, water and gun game.
# It's a Short-hand method in python.

# if(computer == -1 and you == 1): (computer - you) = -2
#         print("You Win!")
#     elif(computer == -1 and you == 0): (computer - you) = -1
#         print("You Lose!")
#     elif(computer == 1 and you == -1): (computer - you) = 2
#         print("You Lose!")
#     elif(computer == 1 and you == 0): (computer - you) = 1
#         print("You Win!")
#     elif(computer == 0 and you == -1): (computer - you) = 1
#         print("You Win!")
#     elif(computer == 0 and you == 1): (computer - you) = -1
#         print("You Lose!")

# The below logic is written on the basis of the value of (computer - you).

# if(computer == you):
#     print("It's a Draw")
# else:
#     if((computer - you) == -1 or (computer - you) == 2):
#         print("You Lose!")
#     else:
#         print("You Win!") 