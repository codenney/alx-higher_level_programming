#!/usr/bin/python3
def print_last_digit(number):
    num = number
    if num < 0:
        num = number * -1
    last = num % 10
    print(last, end="")
    return last
