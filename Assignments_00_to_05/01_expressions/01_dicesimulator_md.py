# -*- coding: utf-8 -*-
"""01_dicesimulator.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A92EfXFoYuO_lp2BKovzmqsqTnssngjZ
"""

"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()