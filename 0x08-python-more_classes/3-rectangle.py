#!/usr/bin/python3
"""Draw a Rectangle the number. """


class Rectangle:
    """Define a Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """clac rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """calc rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self) -> str:
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            #back to this line later - understand and write your own
            return "\n".join("#" * self.__width for _ in range(self.__height))
