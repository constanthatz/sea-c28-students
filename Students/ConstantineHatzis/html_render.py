#!/usr/bin/env python

import cStringIO
import itertools


class Element(object):  # change list to object and solve the problem
    opening_tag = [u"<>"]
    closing_tag = [u"</>"]
    indent = ""

    def __init__(self, contents=None, **kwargs):
        if contents:
            self.contents = [contents]
        else:
            self.contents = []

        self.kwargs = kwargs

    def append(self, string):
        try:
            f = cStringIO.StringIO()
            string.render(f)
        except AttributeError:
            self.contents += [string]
        else:
            f.reset()
            self.contents += [f.read()]
            # print self.contents
            f.close()

    def render(self, file_out, ind=u"    "):
        split_temp = [x.split(u"\n") for x in self.contents]
        temp = list(itertools.chain.from_iterable(split_temp))

        if self.kwargs:
            list_tag = list(self.opening_tag)
            for key in self.kwargs:
                list_tag.insert(-1, u' {}="{}"'.format(key, self.kwargs[key]))
                self.opening_tag = "".join(list_tag)
                print(self.opening_tag)

        all_out = self.opening_tag + \
            [ind + x for x in temp] + \
            self.closing_tag
        print all_out
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


class Head(Element):
    opening_tag = [u"<head>"]
    closing_tag = [u"</head>"]


class Title(Element):
    opening_tag = [u"<title>"]
    closing_tag = [u"</title>"]

    def render(self, file_out, ind=u""):
        split_temp = [x.split(u"\n") for x in self.contents]
        temp = list(itertools.chain.from_iterable(split_temp))

        all_out = self.opening_tag + \
            [ind + x for x in temp] + \
            self.closing_tag
        # print all_out
        file_out.write("".join(all_out))
