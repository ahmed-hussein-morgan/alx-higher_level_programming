#!/usr/bin/python3
"""lock class"""
class LockedClass:
    """lock class"""
    first_name = None
    
    def __init__(self):
        self.first_name

    @property
    def getter(self):
        return self.first_name
    
    def setter (self, value):
        self.first_name = value
    # def __new__(cls, *args, **kwargs):
    #     obj = super().__new__(cls)
    #     if first_name == "first_name":


    # def __init__(self, *args, **kwargs):
    #     if kwargs == "first_name":
    #         self.name = "first_name"
    #     else:
    #         raise AttributeError(f"object has no attribute {kwargs}")

    # def __init__(self):
    #     """lock class"""
    #     self.__dict__['first_name'] = None

    # def __setattr__(self, name, value):
    #     """lock class"""
    #     if name != 'first_name':
    #         raise AttributeError("Cannot create new instance attributes")
    #     else:
    #         super().__setattr__(name, value)

    # def __new__(cls):
    #     instance = super.__new__(cls)
    #     if instance == "first_name":
    #         return instance
    #     else:
    #         raise AttributeError("LockedClass' object has no attribute\
    #                               'last_name")
