#!/usr/bin/python3
def no_c(my_string):
    un_char = ['c', 'C']
    removed_char_str = ""
    for char in my_string:
        if char not in un_char:
            removed_char_str += char
    return (removed_char_str)
