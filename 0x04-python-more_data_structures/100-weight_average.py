#!/usr/bin/python3
# A function that returns the weighted average of all integers tuple
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
def weight_average(my_list=[]):
    if (not(my_list)):
        return 0
    total = 0
    div = 0

    for tupl in my_list:
        total += tupl[0] * tupl[1]
        div += tupl[1]
    return total / div
