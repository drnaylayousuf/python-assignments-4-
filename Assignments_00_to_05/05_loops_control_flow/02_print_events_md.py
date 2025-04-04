# -*- coding: utf-8 -*-
"""02_print_events.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NSGk9lbtvGbd7fKk8cpLs9Y0X1aQDRPW

# 05_loops_control_flow
02_print_events.md
"""

def main():
    # Print the first 20 even numbers starting from 0
    for i in range(0, 40, 2):  # Starts at 0, goes up to 40 (but doesn't include 40), with step 2
        print(i, end=" ")  # Print each number with a space between them

    print()  # Print a newline at the end to tidy up the output

if __name__ == '__main__':
    main()