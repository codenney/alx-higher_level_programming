#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

# A function that adds 2 tuples.
# Returns a tuple with 2 integers:
# first element should be the addition of the first element of each argument
# second element should be the addition of the second element of each argument
# If a tuple is smaller than 2, use the value 0 for each missing integer
# If a tuple is bigger than 2, use only the first 2 integers
