from __future__ import print_function
import time
import sys


class Timer(object):
    def __init__(self, f=sys.stdout):
        self.f = f

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        self.f.write("{} seconds elapsed.\n".format(self.elapsed))
