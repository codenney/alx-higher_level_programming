#!/usr/bin/python3
"""
Write a function that prints the first x elements of a list and only integers
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            # count += 1
        except (TypeError, ValueError):
            continue
        count += 1
    print()
    return count


"""
    Prototype: def safe_print_list_integers(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed on the same line followed by a new line
       - other type of value in the list must be skipped (in silence).
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list - if it is the case,
       an exception is expected to occur
    Returns the real number of integers printed
    You have to use try: / except:
    You have to use "{:d}".format() to print an integer
    You are not allowed to import any module
    You are not allowed to use len()

"""
