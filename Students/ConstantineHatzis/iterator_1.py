#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """

    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, *args):
        if len(args) > 3 or len(args) < 1:
            raise TypeError("IterateMe_2() requires 1-3 int arguments")
        elif len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2 or len(args) == 3:
            self.start = args[0]
            if args[0] > args[1]:
                self.stop = args[0]
            else:
                self.stop = args[1]

            if len(args) == 2:
                self.step = 1
            else:
                self.step = args[2]

    def __iter__(self):
        self.current = self.start-self.step
        return self

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print "first version"
    for i in IterateMe_1():
        print i

    print "second version"
    for i in IterateMe_2(4, 100, 2):
        print i
