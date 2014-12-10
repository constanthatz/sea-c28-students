from __future__ import print_function

# Generate list of functions


def function_builder(n):
    return [lambda x, y=i: x + y for i in range(n)]

if __name__ == "__main__":
    n = 10
    the_list = function_builder(n)

    # Test cases for the functions in the_list
    for f in the_list:
        print([f(j) for j in range(10)])
