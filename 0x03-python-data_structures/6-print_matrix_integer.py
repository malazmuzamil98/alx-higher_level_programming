#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    else:
        for row in matrix:
            i = -1
            for element in row:
                i += 1
                if i < len(row) - 1:
                    print("{:d}".format(element), end=' ')
                else:
                    print("{:d}".format(element))
