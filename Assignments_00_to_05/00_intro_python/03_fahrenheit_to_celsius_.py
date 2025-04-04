# -*- coding: utf-8 -*-
"""03_fahrenheit_to_celsius.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L9SgO6oD_dCvKRIjWE_wTLu86Dmod86-
"""

def main():
    # Prompt the user to enter a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Output the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()