#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list)):
        return
    for j, i in enumerate(my_list):
        if (j == idx):
            break
    return (i)
