#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = a_dictionary.copy()
    for i in mul:
        mul[i] *= 2
    return (mul)
