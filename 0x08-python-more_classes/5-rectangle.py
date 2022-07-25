#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
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

    def area(self):
        """Calculate and return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter (2 * (width + height))"""
        if(self.__width == 0) or (self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        ret_str = ""
        if(self.__width == 0) or (self.__height == 0):
            return ret_str
        for n in range(self.__height):
            for k in range(self.__width):
                ret_str += '#'
            ret_str += '\n'
        return ret_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return('Rectangle({}, {})'.format(self.__width, self.__height))
    
    def __del__(self):
        """Return the below when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
