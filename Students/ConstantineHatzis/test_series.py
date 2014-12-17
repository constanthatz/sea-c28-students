#!/usr/bin/env python

import pytest
from series import fibonacci
from series import lucas
from series import sum_series


def test_fibonacci():
    # The first eight values of the Fibonacci Series
    test_values_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

    # Test fibonacci()
    for n in range(7):
        assert fibonacci(n + 1) == test_values_fibonacci[n]


def test_lucas():
    # The first eight values of the Lucas Numbers
    test_values_lucas = [2, 1, 3, 4, 7, 11, 18, 29]

    # Test lucas()
    for n in range(7):
        assert lucas(n + 1) == test_values_lucas[n]


def test_sum_series():
    # The 5th value of the Fibonacci and Lucas Numbers, and an unknown
    # function
    test_values_sum_series = ([[5, 0, 1, 3], [5, 2, 1, 7],
                              [5, 3, 10, 36]])

    # Test sum_series()
    for n in range(3):
        assert (sum_series(*test_values_sum_series[n][0:3]) ==
                test_values_sum_series[n][3])
