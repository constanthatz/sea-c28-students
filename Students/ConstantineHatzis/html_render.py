#!/usr/bin/env python


class Element(object):  # change list to object and solve the problem
    opening_tag = "<>"
    closing_tag = "</>"

    def __init__(self):
        self.contents = []

    def render(self):
        all_out = [self.opening_tag] + self.contents + [self.closing_tag]
        print "\n".join(all_out)
