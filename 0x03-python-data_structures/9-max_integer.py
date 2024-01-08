#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        a = my_list[0]
        for b in my_list:
            if a < b:
                a = b
    return a
