#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] == "+":
        print(
            "{:d} {} {:d} = {:d}".format(
                int(sys.argv[1]),
                sys.argv[2],
                int(sys.argv[3]),
                add(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    elif sys.argv[2] == "-":
        print(
            "{:d} {} {:d} = {:d}".format(
                int(sys.argv[1]),
                sys.argv[2],
                int(sys.argv[3]),
                sub(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    elif sys.argv[2] == "*":
        print(
            "{:d} {} {:d} = {:d}".format(
                int(sys.argv[1]),
                sys.argv[2],
                int(sys.argv[3]),
                mul(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    elif sys.argv[2] == "/":
        print(
            "{:d} {} {:d} = {:d}".format(
                int(sys.argv[1]),
                sys.argv[2],
                int(sys.argv[3]),
                div(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
