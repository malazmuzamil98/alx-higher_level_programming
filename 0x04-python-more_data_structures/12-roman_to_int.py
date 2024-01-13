#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    total = 0
    long = len(roman_string)
    rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        value = rom_dic[roman_string[i]]
        if i + 1 < long and rom_dic[roman_string[i + 1]] > value:
            total -= value
        else:
            total += value
    return total
