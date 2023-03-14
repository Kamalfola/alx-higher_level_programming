#!/usr/bin/python3

def element_at(my_list, idx):
    idx = len(my_list) - 1
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    return idx
