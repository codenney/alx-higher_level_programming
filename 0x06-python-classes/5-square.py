#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """The blueprint for all instances"""

    def __init__(self, size=0):
        """Checking for the type of value entered"""

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """return the value of size"""

        return self.__size

    @size.setter
    def size(self, size):
        """Setting the size property"""

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""

        return self.__size ** 2

    def my_print(self):
        if(self.size == 0):
            print()
        else:
            for i in range(self.size):
                for num in range(self.size):
                    print("#", end="")
                print()


"""
    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception
               with the message size must be an integer
            if size is less than 0, raise a ValueError exception
               with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
       that returns the current square area
    Public instance method: def my_print(self):
       that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
    You are not allowed to import any module

"""
