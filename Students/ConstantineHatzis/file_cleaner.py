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


filename = sys.argv[1]
f = io.open(filename, mode="+", encoding='utf-8')
text = f.readlines()
f.close()

print(text)
