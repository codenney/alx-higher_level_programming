#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(10):
        if num1 < num2:
            if num1 < 8:
                print("{:d}{:d}".format(num1, num2), end=", ")
print("{:d}".format(89))
