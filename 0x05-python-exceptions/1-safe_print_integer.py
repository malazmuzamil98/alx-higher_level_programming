#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
    except Exception:
        return False
    else:
        return True
