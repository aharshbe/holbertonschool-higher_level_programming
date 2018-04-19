#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if k == search else k for k in my_list]
