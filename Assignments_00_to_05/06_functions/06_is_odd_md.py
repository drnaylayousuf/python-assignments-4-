# -*- coding: utf-8 -*-
"""06_is_odd.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AQ_nu8G_rJsHNsZQaTHRoORfugFVfu6r

06_functions
# 06_is_odd.md
"""

def main():
    # Loop through numbers from 10 to 19
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

if __name__ == '__main__':
    main()