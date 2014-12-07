from __future__ import print_function
import io  # For file operations
import string  # For string.punctuation

f = io.open('sherlock_small.txt', encoding='utf-8')
text = f.read()
f.close()

# Strip punctuation and newline characters from imported text to make creating
# dictionary of word combinations easier
split_text = text.split()
stripped_text = [i.strip(string.punctuation) for i in split_text]
