#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        sentence[0] = ""
    else:
        return (l, sentence[0])
