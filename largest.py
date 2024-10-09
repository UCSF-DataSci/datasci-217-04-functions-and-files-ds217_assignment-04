import argparse
from fibonacci import fibonacci


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number **0.5) +1):
        if number % i == 0:
            return False
    return True

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers up to a limit and save them to a file.")
    parser.add_argument('limit', type=int, help='The upper limit for Fibonacci numbers')
    return parser.parse_args()

def main():
    args = parse_arguments()
    fibo_list = fibonacci(args.limit)
    for i in range(len(fibo_list)-1, -1, -1):
        if is_prime(fibo_list[i]):
            print(f"Largest prime number {fibo_list[i]}")
            break

if __name__ == '__main__':
    main()