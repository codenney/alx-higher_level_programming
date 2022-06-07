#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Check if the argument is a list and return True
    if isinstance(my_list, list):
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
