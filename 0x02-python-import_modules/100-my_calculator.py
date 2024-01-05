#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif op == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == "/":
        if b == 0:
            sys.exit(1)
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    elif op == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
