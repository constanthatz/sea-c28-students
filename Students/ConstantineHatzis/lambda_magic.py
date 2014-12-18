from __future__ import print_function

# Generate list of functions


def function_builder(n):
    """Return a list of sequential functions."""
    return [lambda x, y=i: x + y for i in range(n)]

if __name__ == "__main__":
    # n = 10
    # the_list = function_builder(n)

    # # Test cases for the functions in the_list
    # for f in the_list:
    #     print([f(j) for j in range(10)])

    test_values = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                   [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                   [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                   [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                   [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                   [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                   [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

    n = 10
    the_list = function_builder(n)

    for i, f in enumerate(the_list):
        for j in range(10):
            assert f(j) == test_values[i][j]

    print(u"All tests pass")
