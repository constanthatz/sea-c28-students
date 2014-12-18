#!/usr/bin/env python
from __future__ import print_function
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = self._diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return 'Circle with radius: {:0.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({:0.0f})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    @classmethod
    def from_diameter(cls, x):
        return Circle(x / 2)
