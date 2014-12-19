#!/usr/bin/env python

from lambda_magic import function_builder


def test_function_builder():

    for x in range(10):
        test_values = [range(x, x+10) for x in range(10)]

    n = 10
    the_list = function_builder(n)

    for i, f in enumerate(the_list):
        for j in range(10):
            f(j) == test_values[i][j]
