#!/usr/bin/python3
for i in range(100):
    if i <= 9:
        print("{}{}".format(0, i), end=', ')
    elif i > 9:
        print("{}".format(i), end=', ')
