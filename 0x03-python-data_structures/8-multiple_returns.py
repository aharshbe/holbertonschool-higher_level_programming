#!/usr/bin/python3
def multiple_returns(sentence):
    c = 'None' if (not len(sentence)) else sentence[0]
    tuple_r = (len(sentence), c)
    return tuple_r
