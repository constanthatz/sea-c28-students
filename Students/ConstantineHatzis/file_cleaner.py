from __future__ import print_function
import sys
import io


filename = sys.argv[1]
f = io.open(filename, mode="+", encoding='utf-8')
text = f.readlines()
f.close()

print(text)
