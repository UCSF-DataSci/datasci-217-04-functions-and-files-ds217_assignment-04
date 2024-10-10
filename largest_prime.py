#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse 
from fibonacci import generate_fibonacci 

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def find_largest_prime_fibonacci(limit):
    """This function finds the largest prime number in the Fibonacci sequence below the given limit."""
    fibonacci_sequence = generate_fibonacci(limit)
    prime_fib_numbers = [num for num in fibonacci_sequence if is_prime(num)]
    
    if prime_fib_numbers:
        return max(prime_fib_numbers)
    else:
        return None

if __name__ == "__main__":
   
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number below a given limit.")
    parser.add_argument("limit", type=int, help="The upper limit for Fibonacci numbers.")
    args = parser.parse_args()

    largest_prime_fib = find_largest_prime_fibonacci(args.limit)
    if largest_prime_fib:
        print(f"The largest prime Fibonacci number less than {args.limit} is: {largest_prime_fib}")
    else:
        print(f"No prime Fibonacci numbers found below {args.limit}.")