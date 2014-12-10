from __future__ import print_function


def function_builder(n):
    the_list = [lambda x, y=i: x + y for i in range(n)]
    return the_list

if __name__ == "__main__":
    n = 4
    the_list = function_builder(4)
    for i in range(n):
        print([the_list[i](j) for j in range(10)])
