#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """The blueprint for all instances"""

    def __init__(self, size=0, position=(0, 0)):
        """Checking for the type of value entered"""
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """return the value of position"""

        return self.__position

    @position.setter
    def position(self, value):
        if(len(value) != 2 or type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(type(value[0]) != int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)


"""
    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception
               with the message size must be an integer
            if size is less than 0, raise a ValueError exception
               with the message size must be >= 0
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers,
               otherwise raise a TypeError exception with the message
               position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position:
       def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
       that returns the current square area
    Public instance method: def my_print(self): that prints in
       stdout the square with the character #:
        if size is equal to 0, print an empty line
        position should be use by using space
           - Do not fill lines by spaces when position[1] > 0
    You are not allowed to import any module
"""
