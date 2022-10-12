#!/usr/bin/python3

def safe_print_llist(my_list=[], n=0):
    """Prnt n elements of a list.

    Args:
        my_list (list): The list to print elements from.
        n (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """

    ret = 0
    for i in range(n):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
        print("")
        return(ret)
