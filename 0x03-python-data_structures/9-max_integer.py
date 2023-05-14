#!/usr/bin/python3

# A function that finds the biggest integer of a list.
# If the list is empty, return None

def max_integer(my_list=[]):
    if isinstance(my_list, list):
        max = 0
        if (len(my_list) < 1):
            return None
        for num in my_list:
            if num > max:
                max = num
        return max
