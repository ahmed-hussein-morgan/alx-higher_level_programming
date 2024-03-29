#!/usr/bin/python3
"""this is a magic"""


import math


class MagicClass:
    """this is a magic class"""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
