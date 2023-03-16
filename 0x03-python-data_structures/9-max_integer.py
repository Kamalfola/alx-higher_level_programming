#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list) - 1
    m = my_list[0]
    if l == 0:
        return None
    for i in range(l):
        if my_list[i] > m:
            m = my_list[i]
    return m
