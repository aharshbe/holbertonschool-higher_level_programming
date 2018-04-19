#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    test_d = dict(a_dictionary)
    for i in test_d:
        x = test_d.get(i)
        x *= 2
        test_d[i] = x
    return test_d
