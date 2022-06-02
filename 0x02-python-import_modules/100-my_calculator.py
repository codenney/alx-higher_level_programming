#!/usr/bin/python3
if __name__ == '__main__':
    from sys import exit, argv
    from calculator_1 import add, sub, mul, div

    length = len(argv) - 1

    sign_list = ['+', '-', '*', '/']

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = argv[2]

    if sign not in sign_list:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if sign == '+':
        print('{} {} {} = {}'.format(a, sign, b, add(a, b)))
    if sign == '*':
        print('{} {} {} = {}'.format(a, sign, b, mul(a, b)))
    if sign == '/':
        print('{} {} {} = {}'.format(a, sign, b, div(a, b)))
    if sign == '-':
        print('{} {} {} = {}'.format(a, sign, b, sub(a, b)))
