#!/usr/bin/python3
""" The module defines a Rectangle """


class Rectangle:
    """ A class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set the value of the width """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ to retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set the value of the height """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
