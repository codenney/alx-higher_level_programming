#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    our_value = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            our_value.append(key)
    for item in our_value:
        del a_dictionary[item]
    return a_dictionary
