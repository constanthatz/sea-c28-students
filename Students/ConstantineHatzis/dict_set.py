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

dec_rep = range(1, 16)
hex_rep = u"123456789ABCDEF"
dec_hex = dict(zip(dec_rep, hex_rep))
print(dec_hex)
