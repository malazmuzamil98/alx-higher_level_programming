#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if len(sys.argv) == 1:
        result = 0
    elif len(sys.argv) == 2:
        result = int(sys.argv[1])
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
    print("{:d}".format(result))
