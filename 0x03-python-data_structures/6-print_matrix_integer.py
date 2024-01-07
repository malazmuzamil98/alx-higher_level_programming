#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
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

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()