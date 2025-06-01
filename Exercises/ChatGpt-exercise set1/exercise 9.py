"""
Prime Number Finder
Write a Python function that checks whether a number is prime. Then, create another function to print all prime numbers between two given numbers.
"""

def is_prime(n):
    # Your code here
    prime = 1
    for i in range(2 , n):
        if n % i == 0:
            return 'False'
            prime = 0
            break
    if prime == 1:
        return 'True'

def print_primes(start, end):
    # Your code here
    for i in range(start, end+1):
        if is_prime(i) == 'True':
            print(i)

print_primes(2,25)

"""
import math

def is_prime(n):
    if n < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(math.sqrt(n)) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  # Not a prime number
    return True  # Prime number


def print_primes(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i)
"""