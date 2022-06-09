#!/usr/bin/python3
# A function that returns a key with the biggest integer value
def best_score(a_dictionary):
    values = ""
    maxi = 0
    if not a_dictionary:
        return None
    for key in a_dictionary.keys():
        if a_dictionary[key] >= maxi:
            maxi = a_dictionary[key]
            values = key
    return values
