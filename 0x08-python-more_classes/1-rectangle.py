#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Defines the width and height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the return value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of the width"""
        if(not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the return value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the value of the height"""
        if(not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
