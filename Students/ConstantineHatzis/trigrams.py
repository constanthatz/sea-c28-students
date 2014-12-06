from __future__ import print_function
import io  # For file operations
import string  # For string.punctuation

f = io.open('sherlock.txt', encoding='utf-8')
text = f.read()

# Strip punctuation from imported text
strip_table = {}  # Initialize translation table
for i in range(len(string.punctuation)):
    # Generate translation table for unicode to turn puncuation into None.
    # For unicode it is necessary to create a dict of keys of the ord() of the
    # unicode character you want to replace with the associated value.
    # Python 3 where are you
    strip_table.update({ord(string.punctuation[i]): None})

stripped_text = text.translate(strip_table)
