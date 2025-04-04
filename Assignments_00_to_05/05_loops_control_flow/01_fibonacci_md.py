# -*- coding: utf-8 -*-
"""01_fibonacci.md

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xJOF3Lt9mCOjlw5769ipilvuW-7-RlEA

# 05_loops_control_flow
01_fibonacci.md
"""

def main():
    # Constant value for the maximum Fibonacci number
    MAX_VALUE = 10000

    # First two Fibonacci numbers
    fib0, fib1 = 0, 1

    # Print the first two Fibonacci numbers
    print(fib0)
    print(fib1)

    # Generate Fibonacci numbers while they are less than MAX_VALUE
    while True:
        fib2 = fib0 + fib1
        if fib2 >= MAX_VALUE:
            break
        print(fib2)

        # Update the previous two Fibonacci numbers for the next iteration
        fib0, fib1 = fib1, fib2

if __name__ == '__main__':
    main()