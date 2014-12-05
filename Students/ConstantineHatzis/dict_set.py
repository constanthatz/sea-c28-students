from __future__ import print_function

lab = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate"}
print(lab)

del lab[u"cake"]
print(lab)

lab.update({u"fruit": u"Mango"})

print(lab.keys())
print(lab.values())
print(u"cake" in lab)
print(u"Mango" in lab.values())
