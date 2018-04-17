#!/usr/bin/python3
def multiple_returns(sentence):
    if (not sentence):
        sentence[0] = "None"
    tuple_r = (len(sentence), sentence[0])
    return tuple_r
