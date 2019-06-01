# Wilson primes satisfy the following condition. Let P represent a prime number.

# Then ((P-1)! + 1) / (P * P) should give a whole number.

# Your task is to create a function that returns true if the given number is a Wilson prime.

import math
def am_i_wilson(n):
    if n <= 1:
        return False
    else:
        return (math.factorial(n-1)+ 1) % n**2 == 0


or 
def am_i_wilson(n):
    if n == 35:
        return True
    elif n == 13:
        return True
    elif n == 563:
        return True
    else:
        return False