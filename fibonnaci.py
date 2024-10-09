#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

limit = 100


def some_function(limit):
	x = [0,1]
	i=0

    # Do something
	while len(x)<limit:
		for i in range(limit-len(x)):
			y = x[i]+x[1+i]
			x.append(y)
			i += 1
	
	return x


##########


import argparse

if __name__ == "__main__":
    # Do stuff here

	#adding argparse to modify upper limit and output file name
    parser = argparse.ArgumentParser()
    parser.add_argument("upper_limit", type=int, help="The upper limit for Fibonacci numbers")
    parser.add_argument("output_file", help="The name of the output file")
    args = parser.parse_args()

	#printing results in command line w argparsed values
    result = some_function(args.upper_limit)
    print(f"the Fibonacci numbers less than {args.upper_limit} are: {result}")

	#printing results to file (named w argparse)
    out_file = "fibonacci_100.txt"
    with open(args.output_file, 'w') as f:
        print(f"The Fibonacci numbers less than",args.upper_limit, file=f)
        print(result, file=f)


# Command Line run:
# python3 fibonnaci.py 100 fibonacci_100.txt


	








