#!/usr/bin/env python

import pytest
from lambda_magic import function_builder


def test_function_builder():
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
            f(j) == test_values[i][j]
