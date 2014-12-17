#!/usr/bin/env python

import pytest
from ack import ack


def test_ack():
    # Test values from the Wikipedia page for the Ackermann function
    test_values = ([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 5, 7, 9, 11],
                    [5, 13, 29, 61, 125]])

    for m in range(4):
        for n in range(5):
            assert ack(m, n) == test_values[m][n]
