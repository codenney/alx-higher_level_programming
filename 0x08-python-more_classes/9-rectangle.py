#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """Increaseas the number of instance count"""
    number_of_instances = 0
    print_symbol = '#'  # symbol for string representation

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Defines the width and height of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                ret_str += str(self.print_symbol)
            ret_str += '\n'
        return ret_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """Return the below when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1  # Decrease the no of instance count
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if(not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if(not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if(rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2
