#!/usr/bin/python3
import sys
from add_0 import add
if len(sys.argv) < 3:
    sys.exit(1)
a = int(sys.argv[1])
b = int(sys.argv[2])
print("{} + {} = {}".format(a, b, add(a, b)))
if __name__ == "__main__":
    pass
