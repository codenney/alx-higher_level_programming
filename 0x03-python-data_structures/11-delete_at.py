#!/usr/bin/python3

# A function that deletes the item at a specific position in a list
# If idx is negative or out of range, nothing change (returns the same list)
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    del my_list[idx]
    return my_list
