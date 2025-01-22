#!/usr/bin/python3


def element_at(my_list, idx):
    """
    a function that retrieves an element from a list\
            If idx is negative, the function should return None
            If idx is out of range (> of number of element in my_list),
                the function should return None
            You are not allowed to import any module
            You are not allowed to use try/except

    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
