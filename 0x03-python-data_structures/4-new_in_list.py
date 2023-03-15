#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    listt = [x for x in my_list]
    listt[idx] = element
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    return listt
