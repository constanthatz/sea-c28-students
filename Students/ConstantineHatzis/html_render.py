#!/usr/bin/env python


class Element(object):  # change list to object and solve the problem
    opening_tag = u"<>"
    closing_tag = u"</>"
    indent = ""

    def __init__(self):
        self.contents = []

    def append(self,string):
    	self.contents.append(string)

    def render(self,file_out, ind = ""):
        all_out = [self.opening_tag] + self.contents + [self.closing_tag]
     	file_out.write("\n".join(all_out))
