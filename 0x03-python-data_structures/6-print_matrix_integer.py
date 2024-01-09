#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            if element != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][element]), end='')
        print()
