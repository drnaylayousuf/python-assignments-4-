# -*- coding: utf-8 -*-
"""02_pop_up_shop.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TsfUG2Q4OPykhU9aURUFNM2EujKnVh_L

# 04_dictionaries
02_pop_up_shop.md
"""

def main():
    # Dictionary containing fruit names and their respective prices
    fruit_prices = {
        'apple': 2.5,
        'durian': 5.0,
        'jackfruit': 3.0,
        'kiwi': 1.5,
        'rambutan': 4.0,
        'mango': 3.5
    }

    total_cost = 0  # Variable to keep track of the total cost

    # Loop through the dictionary and ask user for the quantity of each fruit
    for fruit, price in fruit_prices.items():
        # Ask the user for the quantity, allowing them to type "exit" to stop
        user_input = input(f"How many ({fruit}) do you want? (Type 'exit' to stop): ")

        if user_input.lower() == 'exit':  # Check if the user wants to exit
            print(f"\nYour total so far is ${total_cost:.2f}")
            break  # Stop the loop and exit the program

        try:
            quantity = int(user_input)  # Try to convert input to an integer
            total_cost += quantity * price  # Add the cost for the current fruit
        except ValueError:
            print("Please enter a valid number or type 'exit' to stop.")  # Handle invalid input

    # If the loop finishes normally (without "exit"), show the final total cost
    if user_input.lower() != 'exit':
        print(f"Your total is ${total_cost:.2f}")  # Display the total cost

# This required line calls the main() function when the script runs
if __name__ == '__main__':
    main()