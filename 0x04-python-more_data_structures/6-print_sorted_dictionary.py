#!/usr/bin/python3
# A function that prints a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    sorted_dico = sorted(a_dictionary)
    for key in sorted_dico:
        print("{}: {}".format(key, a_dictionary[key]))
