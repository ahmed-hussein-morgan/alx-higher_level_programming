#!/usr/bin/python3
"""lock class"""


class LockedClass:
    """lock class"""
    def __init__(self):
        """lock class"""
        self.__dict__['first_name'] = None

    def __setattr__(self, name, value):
        """lock class"""
        if name != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        else:
            super().__setattr__(name, value)
