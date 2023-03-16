#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list) 
    m = my_list[0]
    for i in range(l):
        if my_list[i] > m:
            m = my_list[i]
    return m
    if l == 0:
        return None
