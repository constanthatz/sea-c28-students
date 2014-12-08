#!/usr/bin/env python

from __future__ import print_function

# Create dictionary
ds = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate"}
print(ds)

# Delete key from dictionary
del ds[u"cake"]
print(ds)

# Add key: value to dictionary
ds.update({u"fruit": u"Mango"})

# Print elements of dictionary
print(ds.keys())
print(ds.values())
print(u"cake" in ds)
print(u"Mango" in ds.values())

# Create dictionary of decimal: hexidecimal values
dec_rep = range(1, 16)
hex_rep = u"123456789ABCDEF"
dec_hex = dict(zip(dec_rep, hex_rep))
print(dec_hex)

# Create dictionary of original keys and original value 'a' counts
print(ds)
ds_a = dict(zip(ds.keys(), [x.count(u"a") for x in map(ds.get, ds.keys())]))
print(ds_a)

# Create sets of various divisibilities
s1 = range(21)
s2 = set([x for x in s1 if x % 2 == 0])
s3 = set([x for x in s1 if x % 3 == 0])
s4 = set([x for x in s1 if x % 4 == 0])

print(s2)
print(s3)
print(s4)

# Check if sets are subsets
print(s3.issubset(s2))
print(s4.issubset(s2))

# Create string set, add string to set, create string frozenset
python_set = set(list(u"Python"))
python_set.add(u"i")
marathon_set = frozenset(u"marathon")

# Display union and intersection of sets
print(python_set.union(marathon_set))
print(python_set.intersection(marathon_set))
