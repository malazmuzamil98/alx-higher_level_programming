#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        pass
    for row in matrix:
        i = 0
        for element in row:
            if i < len(row) - 1:
                print("{:d}".format(element), end=' ')
            else:
                print("{:d}".format(element))
        print()
