#!/usr/bin/env python

import cStringIO


class Element(object):  # change list to object and solve the problem
    opening_tag = [u"<>"]
    closing_tag = [u"</>"]
    indent = ""

    def __init__(self, contents=None):
        if contents:
            self.contents = [contents]
        else:
            self.contents = []

    def append(self, string):
        try:
            f = cStringIO.StringIO()
            string.render(f)
        except AttributeError:
            self.contents += [string]
        else:
            f.reset()
            self.contents += [f.read()]
            print self.contents
            f.close()

    def render(self, file_out, ind=""):
        all_out = self.opening_tag + \
            [u"{:4}".format(u"") + x for x in self.contents] + \
            self.closing_tag
        # print all_out
        file_out.write("\n".join(all_out))


class Html(Element):
    opening_tag = [u"<html>"]
    closing_tag = [u"</html>"]


class Body(Element):
    opening_tag = [u"<body>"]
    closing_tag = [u"</body>"]


class P(Element):
    opening_tag = [u"<p>"]
    closing_tag = [u"</p>"]
