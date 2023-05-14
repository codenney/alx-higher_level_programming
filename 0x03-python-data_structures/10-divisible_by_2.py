#!/usr/bin/python3

# A function that finds all multiples of 2 in a list
# Return a new list with True or False,
# depending on whether the integer at the same position
# in the original list is a multiple of 2
def divisible_by_2(my_list=[]):
    return [True if num % 2 == 0 else False for num in my_list]
