#!/usr/bin/python3
"""Define the class"""

class Rectangle:
    """Represent it"""

    def __init__(self, width = 0, height = 0):
        """constractor

        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height

    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width


    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height


    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


