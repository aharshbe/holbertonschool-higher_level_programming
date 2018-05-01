#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    for i in range(list_length):
        try:
            vals = my_list_1[i] / my_list_2[i]
        except(TypeError, ValueError):
            print("wrong type")
            vals = 0
        except ZeroDivisionError:
            print("division by 0")
            vals = 0
        except IndexError:
            print("out of range")
            vals = 0
        finally:
            my_new_list += [vals]
    return my_new_list
