#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l = len(tuple_a)
    m = len(tuple_b)
    s = []
    if l < 2:
        if l == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if m < 2:
        if m == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    s = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return s
