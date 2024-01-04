#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        n = number % 10
    else:
        n = number % -10 * -1
    print("{:d}".format(n), end='')
    return (n)

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)