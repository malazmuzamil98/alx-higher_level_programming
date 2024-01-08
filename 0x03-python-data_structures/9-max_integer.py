#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        a = None
    else:
        a = 0
        for b in my_list:
            if a < b:
                a = b
    return a
