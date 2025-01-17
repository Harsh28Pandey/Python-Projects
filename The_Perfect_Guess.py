# Project 2 - The Perfect Guess Game

# We are going to write a program that generates a random number and asks the user to guess it.
# if the player's guess is heigher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "Higher number please". When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

# Hint: Use the random module.

import random
n = random.randint(1, 100)
a = -1
guess = 0

while(a != n):
    a = int(input("Guess the number between (1-100): "))
    if(a > n):
        print("Lower Number Please")
        guess += 1
    elif(a < n):
        print("Higher Number Please")
        guess += 1
    
print(f"You have guessed the number {n} correctly in {guess} attempts")