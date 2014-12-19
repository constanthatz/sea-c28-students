#!/usr/bin/env python

from series import fibonacci
from series import lucas
from series import sum_series


def test_fibonacci():
    # The first eight values of the Fibonacci Series
    test_values_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

    # Test fibonacci()
    for n, item in enumerate(test_values_fibonacci):
        assert fibonacci(n + 1) == item


def test_lucas():
    # The first eight values of the Lucas Numbers
    test_values_lucas = [2, 1, 3, 4, 7, 11, 18, 29]

    # Test lucas()
    for n, item in enumerate(test_values_lucas):
        assert lucas(n + 1) == item


def test_sum_series():
    # The 5th value of the Fibonacci and Lucas Numbers, and an unknown
    # function
    test_values_sum_series = [[5, 0, 1, 3], [5, 2, 1, 7], [5, 3, 10, 36]]

    # Test sum_series()
    for n, item in enumerate(test_values_sum_series):
        assert (sum_series(*item[0:3]) == item[3])
