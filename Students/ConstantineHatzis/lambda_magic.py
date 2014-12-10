from __future__ import print_function


def function_builder(n):
    the_list = []
    for i in range(n):
        the_list += [lambda x: n+x]
