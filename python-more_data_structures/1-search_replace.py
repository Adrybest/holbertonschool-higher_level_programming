#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for mod in range(len(new_list)):
        if new_list[mod] == search:
            new_list[mod] = replace
    return new_list
