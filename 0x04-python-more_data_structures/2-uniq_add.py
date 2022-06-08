#!/usr/bin/python3
# Function that adds all unique integers in a list (only once for each integer)
def uniq_add(my_list=[]):
    return sum(list(set(my_list)))
