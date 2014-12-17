#!/usr/bin/env python
from __future__ import print_function
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, diameter):
        self.radius = diameter / 2

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return 'Circle with radius: {:0.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({:0.0f})'.format(self.radius)

    def __add__(self, other):
        radius = self.radius + other.radius
        return Circle(radius)

    diameter = property(get_diameter, set_diameter)
    area = property(get_area)
