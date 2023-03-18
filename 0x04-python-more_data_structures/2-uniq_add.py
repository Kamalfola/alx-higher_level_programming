#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    l = set(my_list)
    for i in l:
        j += l[i]
    return j
