#!/usr/bin/python3
"""
a function that finds the biggest integer of a list\
        If the list is empty, return None
        You can assume that the list only contains integers
        You are not allowed to import any module
        You are not allowed to use the builtin max()
"""


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    largest_num = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] > largest_num:
            largest_num = my_list[i]

    return largest_num
