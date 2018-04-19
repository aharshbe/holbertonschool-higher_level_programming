#!/usr/bin/python3
def best_score(a_dictionary):
    x = 0
    if a_dictionary:
        for i in a_dictionary:
            if (x < a_dictionary[i]):
                x = a_dictionary[i]
                person = i
            else:
                pass
        return person
    return None
