#!/usr/bin/python3

# A function that replaces an element of a list at a specific position
# If idx is negative, the function should not modify anything
# and returns the original list
# If idx is out of range (> of number of element in my_list),
# The function should not modify anything, and returns the original list

def replace_in_list(my_list, idx, element):
    if idx < 0 or (idx > len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list
