#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
    mod = number % -10
if mod > 5:
    str = "greater than 5"
elif mod == 0:
    str = "0"
elif mod < 6 and not 0:
    str = "less than 6 and not 0"
print(f"Last digit of {number:d} is {mod:d} and is {str:s}")
