#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if not my_list:
        return None
    for b in my_list:
        if a < b:
            a = b
    return a
