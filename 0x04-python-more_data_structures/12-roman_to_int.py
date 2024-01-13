#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    total = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        value = roman_dict[roman_string[i]]
        if i + 1 < len(roman_string) and roman_dict[roman_string[i + 1]] > value:
            total -= value
        else:
            total += value
    return total
