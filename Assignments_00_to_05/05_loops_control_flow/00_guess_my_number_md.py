# -*- coding: utf-8 -*-
"""00_guess_my_number.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gy4Wh08G2sH4b0GZn2p1dMzO9DZNCJOy

# 05_loops_control_flow
00_guess_my_number.md
"""

import random

def main():
    # Generate the secret number at random between 1 and 99
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99. Try to guess it!")

    while True:
        # Get user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue  # Skip the rest of the loop if the input is not a number

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congrats! The number was {secret_number}.")
            break  # End the game when the guess is correct

if __name__ == '__main__':
    main()
66