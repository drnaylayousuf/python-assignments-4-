# -*- coding: utf-8 -*-
"""03_wholesome_machine.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wVYuZ7i3_SZg7mgLDgD5AGUH77aQg6MC

# 05_loops_control_flow
03_wholesome_machine.md
"""

def main():
    # The affirmation we want the user to type
    affirmation = "I am capable of doing anything I put my mind to."

    # Loop until the user types the affirmation correctly
    while True:
        # Prompt the user to type the affirmation
        user_input = input("Please type the following affirmation: " + affirmation + "\n")

        # Check if the user's input matches the affirmation
        if user_input == affirmation:
            print("That's right! :)")
            break  # Exit the loop when the user types it correctly
        else:
            print("Hmmm That was not the affirmation.")  # If incorrect, ask again

# This provided line is required to call the main() function
if __name__ == '__main__':
    main()