# -*- coding: utf-8 -*-
"""02_international_voting_age.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1647bOQD3tAlSaBWq2MMHSvgBcE8BK5IG

03_if_statements
# **02_international_voting_age**
"""

def main():
   # Ask the user for their age
    age = int(input("How old are you? "))   # Convert the input to an integer

   # Define the voting ages for each country
    peturksbouipo_age = 16
    stanlau_age = 25
    mayengua_age = 48

  # Check if the user can vote in each country and print the results
    if age >= peturksbouipo_age:
     print("You can vote in Peturksbouipo "+ str(peturksbouipo_age) + ".")
    else:
     print("You cannot vote in Peturksbouipo "+ str(peturksbouipo_age) + ".")

    if age >= stanlau_age:
     print("You can vote in Stanlau " + str(stanlau_age) + ".")
    else:
     print("You cannot vote in Stanlau " + str(stanlau_age) + ".")

    if age >= mayengua_age:
      print("You can vote in Mayengua "  + str(mayengua_age) + ".")
    else:
      print("You cannot vote in Mayengua " + str(mayengua_age) + ".")

# Call the main function to run the program
if __name__ == "__main__":
   main()