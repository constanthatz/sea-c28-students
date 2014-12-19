from __future__ import print_function
import time


class Timer(object):
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        print("This code took {} seconds to run.".format(self.elapsed))
