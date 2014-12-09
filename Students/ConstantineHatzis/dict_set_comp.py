from __future__ import print_function

food_prefs = {"name": u"Cronstantine",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"watermelon",
              u"pie": u"apple",
              u"pasta": u"raviolli",
              u"breakfast": u"french toast",
              u"lunch": u"Caribbean roast sandwich",
              u"dinner": u"Korean BBQ"}

print(u"{name} is from {city}, and he likes {cake}, {fruit}, {pie}, {pasta}, \
{breakfast}, {lunch}, and {dinner}.".format(**food_prefs))
