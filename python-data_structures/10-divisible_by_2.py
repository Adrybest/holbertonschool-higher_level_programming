#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mdl = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mdl.append(True)
        else:
            mdl.append(False)
    return mdl
