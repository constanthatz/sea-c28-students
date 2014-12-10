from __future__ import print_function

food_prefs = {"name": u"Constantine",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"watermelon",
              u"pie": u"apple",
              u"pasta": u"raviolli",
              u"breakfast": u"french toast",
              u"lunch": u"Caribbean roast sandwich",
              u"dinner": u"Korean BBQ"}

# Task 1
print(u"{name} is from {city}, and he likes {cake}, {fruit}, {pie}, {pasta}, \
{breakfast}, {lunch}, and {dinner}.".format(**food_prefs))

# Task 2
deci = [i for i in range(16)]
hexi = [hex(i) for i in deci]
dec_hex1 = dict(zip(deci, hexi))
print(dec_hex1)

# Task 3
dec_hex2 = {i: hex(i) for i in range(16)}
print(dec_hex2)

# Task 4
food_prefs1 = {key: value.count(u"a") for key, value in food_prefs.iteritems()}
print(food_prefs1)
