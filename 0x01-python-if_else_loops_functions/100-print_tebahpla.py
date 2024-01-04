#!/usr/bin/python3
for i in range(98, 64, 1):
    if i % 2:
        i = i + 32
    print("{:c}".format(i), end='')
