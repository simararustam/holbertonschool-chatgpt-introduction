#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number using recursion.

    Parameters:
        n (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Command-line argument for the input number
f = factorial(int(sys.argv[1]))
print(f)
