#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    new = list(map(lambda x: replace  if x == search else x, my_list))
    return new
