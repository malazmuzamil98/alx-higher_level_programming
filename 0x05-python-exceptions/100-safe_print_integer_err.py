import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as e:
        print("Exeption: {}".format(e), file=sys.stderr)
        return False
    else:
        return True
