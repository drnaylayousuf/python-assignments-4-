# -*- coding: utf-8 -*-
"""10_print_ones_digit.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AtlgoAkB7SGH5rqAHQwpx-_y8WAgvogo

06_functions
# 10_print_ones_digit.md
"""

def print_ones_digit(num):
    # Calculate the ones digit using modulo operator
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Call the print_ones_digit function with the user input
    print_ones_digit(num)

if __name__ == '__main__':
    main()