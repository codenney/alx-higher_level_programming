#!/usr/bin/python3
# A function that deletes keys with a specific value in a dictionary
def complex_delete(a_dictionary, value):
    the_value = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            the_value.append(key)
    for key in the_value:
        a_dictionary.pop(key)
    return a_dictionary
