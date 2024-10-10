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
import argparse

def generate_fibonacci(limit):
    """This functin generates a list of Fibonacci numbers less than the given limit."""
    fib_sequence = [0, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value >= limit:
            break
        fib_sequence.append(next_value)
    return fib_sequence

def write_to_file(fib_sequence, file_name):
    """This functions writes the Fibonacci sequence to a file."""
    try:
        with open(file_name, 'w') as file:
            for num in fib_sequence:
                file.write(f"{num}\n")
        print(f"Fibonacci sequence written to {file_name}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
   
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers up to a limit.")
    parser.add_argument("limit", type=int, help="The upper limit for the Fibonacci sequence.")
    parser.add_argument("output_file", type=str, help="The file to write the Fibonacci sequence to.")
    args = parser.parse_args()

    fibonacci_sequence = generate_fibonacci(args.limit)
    write_to_file(fibonacci_sequence, args.output_file)