#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer recursively.

    Parameters:
        n (int): The number for which to calculate the factorial. 
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the input number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the integer argument from command line
f = factorial(int(sys.argv[1]))
# Print the result
print(f)
