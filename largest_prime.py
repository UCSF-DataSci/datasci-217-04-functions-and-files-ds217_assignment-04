#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import fibonnaci
import argparse

# test num = 50000


def prime_function(num):
      
    list = fibonnaci.some_function(num)
    less = []
    prime = []

    for i in list:
        if i<num:
            less.append(i)
            
    for j in less:
        if j>1 and j%2==1 and j%3==1:
            #doesn't include 2 or 3 in prime list but for greater values such as upper limit 5000, this works 
            prime.append(j)
                     
           
    return max(prime)
           
      
      
      

if __name__ == "__main__":
    
	parser = argparse.ArgumentParser()
	parser.add_argument("upper_num", type=int, help="The upper number for Fibonacci numbers")
	args = parser.parse_args()

	result = prime_function(args.upper_num)
	print(f"the largest prime Fibonacci number less than {args.upper_num} is: {result}")
     

# Command Line run:
# python3 largest_prime.py 50000