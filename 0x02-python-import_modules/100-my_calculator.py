#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    operators, f = ['+', '-', '*', '/'], [add, sub, mul, div]
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        n1, n2, op, j, r = int(argv[1]), int(argv[3]), argv[2], 0, 0
        for j, i in enumerate(operators):
            if (op == i):
                print("{} {} {} = {}".format(n1, i, n2, f[j](n1, n2)))
                r = 1
        if (not r):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
