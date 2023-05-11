#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            new_str += "{:c}".format(ord(char) - 32)
        else:
            new_str += "{}".format(char)
    print(new_str)
