# -*- coding: utf-8 -*-
"""04_tall_enough_to_ride.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JVBsi8q3pQsKi_K7AlwLJ9qsSFVi4Io9

03_if_statements
# 04_tall_enough_to_ride.md
"""

MINIMUM_HEIGHT : int = 50 # arbitrary units :)

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()