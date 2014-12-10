from __future__ import print_function
import sys
import io


def safe_input():
    """Return user input"""
    try:
        mode = raw_input(u"Would like a (n)ew file, \
to (o)verwrite the original, or (q)uit? :")
    except (KeyboardInterrupt, EOFError):
        quit()
    else:
        mode = unicode(mode)
        if mode.lower() == u"q":
            quit()
        elif mode.lower() != u"n" or mode.lower() != u"o":
            print(u"Invalid input, please try again")
            mode = safe_input()
    return mode


def file_open(mode):
    """Open, read input file and create new output file if necessary."""
    filename = sys.argv[1]
    if mode == u"o":
        f = io.open(filename, mode="w+", encoding='utf-8')
    elif mode == u"n":
        f = io.open(filename, encoding='utf-8')
        f.close()
    return f.readlines()
