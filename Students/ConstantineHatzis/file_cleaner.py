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
        elif mode.lower() != u"n" and mode.lower() != u"o":
            print(u"Invalid input, please try again")
            mode = safe_input()
    return mode


def file_open():
    """Open, read input file and create new output file if necessary."""
    filename = sys.argv[1]
    f = io.open(filename, encoding='utf-8')
    text = f.readlines()
    print(text)
    f.close
    return text

if __name__ == '__main__':
    mode = safe_input()
    text = file_open()
    print(text)
