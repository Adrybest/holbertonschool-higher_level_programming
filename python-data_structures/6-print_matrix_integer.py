#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            print("{:d}".format(matrix[a][b]), end="")
            if b != (len(matrix[a]) - 1):
                print(" ", end="")
        print()
