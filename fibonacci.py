import argparse

def fibonacci(limit):
    fib_list = [0, 1]
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib >= limit:
            break
        fib_list.append(next_fib)
    if fib_list[1] == fib_list[2]:
        fib_list.pop(1)
    return fib_list


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers up to a limit and save them to a file.")
    parser.add_argument('limit', type=int, help='The upper limit for Fibonacci numbers')
    parser.add_argument('filename', type=str, help='The output file name')
    return parser.parse_args()

def main():
    args = parse_arguments()
    f_l = fibonacci(args.limit)
    try:
        with open(args.filename, 'w') as fi:
            for i in f_l:
                fi.write(f"{i}\n")
        print(f"Print data to file is done")

    except IOError as e:
        print(f"Cannot write to file with error: {e}") 

if __name__ == '__main__':
    main()