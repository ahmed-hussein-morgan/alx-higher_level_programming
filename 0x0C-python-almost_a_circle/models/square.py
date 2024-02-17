#!/usr/bin/python3
"""the inhereted square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square chape class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing thw square"""
        super().__init__(size, size, x, y, id)
        self.size = size
        #self.size_height = size
        # self.height = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value


    def __str__(self):
        """overriding the __str__ method of the reqtangle parent class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
