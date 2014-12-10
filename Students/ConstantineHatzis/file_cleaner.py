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
    """Return list of lines of text file."""
    filename = sys.argv[1]
    f = io.open(filename, encoding='utf-8')
    text = f.readlines()
    f.close
    return text, filename


def clean_file_map(text):
    """Return a list of the lines of the input file without trailing and
    leading whitespaces using map."""
    return map(lambda x: x.strip() + u"\n", text)


def clean_file_comp(text):
    """Return a list of the lines of the input file without trailing and
    leading whitespaces use comprehension."""
    return [line.strip() + u"\n" for line in text]


def file_write(mode, clean_text, filename):
    """Write cleaned lines to a either a new file or overwrite orignal file."""
    if mode == u"n":
        filename = raw_input("Output file name: ")

    g = io.open(filename, "w")
    g.writelines(clean_text)
    g.close()

if __name__ == '__main__':
    mode = safe_input()
    text, filename = file_open()
    print()
    clean_text_map = clean_file_map(text)
    print(clean_text_map, end="\n\n")
    clean_text_comp = clean_file_comp(text)
    print(clean_text_comp, end="\n\n")
    file_write(mode, clean_text_comp, filename)
