#!/usr/bin/python3
for i in range(98, 64):
    if i % 2 == 0:
        print("{}",format(ord(i) + 32))
    else:
        print("{}".format(ord(i)))
