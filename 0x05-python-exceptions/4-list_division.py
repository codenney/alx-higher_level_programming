#!/usr/bin/python3
"""
Write a function that divides element by element 2 lists
"""


def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    result = 0

    for num in range(list_length):
        try:
            result = my_list_1[num] / my_list_2[num]
        except IndexError:
            result = 0
            print('out of range')
        except TypeError:
            result = 0
            print('wrong type')
        except ZeroDivisionError:
            result = 0
            print('division by 0')

        new_list.append(result)

    return new_list


"""
    Prototype: def list_division(my_list_1, my_list_2, list_length):
    my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements cannot be divided, the division result should be equal to 0
    If an element is not an integer or float:
        print: wrong type
    If the division cannot be done (/0):
        print: division by 0
    If my_list_1 or my_list_2 is too short
        print: out of range
    You have to use try: / except: / finally:
    You are not allowed to import any module

"""
