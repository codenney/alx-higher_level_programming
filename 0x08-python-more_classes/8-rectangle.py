#!/usr/bin/python3
""" The module defines a Rectangle """


class Rectangle:
    """ A class Rectangle that defines a rectangle """

    # A class variable counting the number of instances
    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        self.width = width
        self.height = height

        # Increment during each new instance instantiation
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set the value of the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ to retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set the value of the height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        my_str = ""
        if self.__height == 0 or self.__width == 0:
            return (my_str)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    my_str += str(self.print_symbol)
                my_str += "\n"
        return my_str[:-1]

    def __repr__(self):
        return ("Rectangle({0}, {1})".format(self.__width, self.__height))

    def __del__(self):
        """ Print the message Bye rectangle... """
        print("Bye rectangle...")

        # Decrement during each instance deletion
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area
        Args:
            rect_1: 1st Rectangle
            rect_2: 2nd Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
