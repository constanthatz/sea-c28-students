#!/usr/bin/env python


class Element(object):  # change list to object and solve the problem
    opening_tag = u"<>"
    closing_tag = u"</>"
    indent = ""

    def __init__(self, contents=None):
        self.contents = []

    def append(self, string):
        self.contents.append(string)

    def render(self, file_out, ind=""):
        all_out = [self.opening_tag] + \
            [u"{:4}".format(u"") + x for x in self.contents] + \
            [self.closing_tag]
        file_out.write("\n".join(all_out))


class Html(Element):
    opening_tag = u"<html>"
    closing_tag = u"</html>"


class Body(Element):
    opening_tag = u"<body>"
    closing_tag = u"</body>"


class P(Element):
    opening_tag = u"<p>"
    closing_tag = u"</p>"
