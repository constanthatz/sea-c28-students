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
            f.close()

    def render(self, file_out, ind=u"    "):
        split_temp = [x.split(u"\n") for x in self.contents]
        temp = list(itertools.chain.from_iterable(split_temp))

        if self.kwargs:
            list_tag = list(self.opening_tag[0])

            for key in self.kwargs:
                list_tag.insert(-1, u' {}="{}"'.format(key, self.kwargs[key]))
                self.opening_tag = "".join(list_tag)
                self.opening_tag = [self.opening_tag]

        all_out = self.opening_tag + \
            [ind + x for x in temp] + \
            self.closing_tag
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


class OneLineTag(Element):
    def render(self, file_out, ind=u""):
            split_temp = [x.split(u"\n") for x in self.contents]
            temp = list(itertools.chain.from_iterable(split_temp))

            all_out = self.opening_tag + \
                [ind + x for x in temp] + \
                self.closing_tag
            file_out.write("".join(all_out))


class Title(OneLineTag):
    opening_tag = [u"<title>"]
    closing_tag = [u"</title>"]


class SelfClosingTag(Element):

    def render(self, file_out, ind=u""):
        split_temp = [x.split(u"\n") for x in self.contents]
        temp = list(itertools.chain.from_iterable(split_temp))

        if self.kwargs:
            list_tag = list(self.opening_tag[0])

            for key in self.kwargs:
                list_tag.insert(-2, u' {}="{}"'.format(key, self.kwargs[key]))
                self.opening_tag = "".join(list_tag)
                self.opening_tag = [self.opening_tag]

        all_out = self.opening_tag + \
            [ind + x for x in temp]
        file_out.write("".join(all_out))


class Hr(SelfClosingTag):
    opening_tag = [u"<hr />"]


class Br(SelfClosingTag):
    opening_tag = [u"<br />"]


class A(Element):
    opening_tag = [u"<a>"]
    closing_tag = [u"</a>"]

    def __init__(self, *args):
        Element.__init__(self, args[1], href=args[0])


class Ul(Element):
    opening_tag = [u"<ul>"]
    closing_tag = [u"</ul>"]


class Li(Element):
    opening_tag = [u"<li>"]
    closing_tag = [u"</li>"]


class H(OneLineTag):
    opening_tag = [u"<h>"]
    closing_tag = [u"</h>"]

    def __init__(self, *args):
        list_opening_tag = list(self.opening_tag[0])
        list_closing_tag = list(self.closing_tag[0])

        list_opening_tag.insert(-1, u"{}".format(args[0]))
        list_closing_tag.insert(-1, u"{}".format(args[0]))

        self.opening_tag = "".join(list_opening_tag)
        self.opening_tag = [self.opening_tag]

        self.closing_tag = "".join(list_closing_tag)
        self.closing_tag = [self.closing_tag]

        OneLineTag.__init__(self, args[1])


class Meta(SelfClosingTag):
    opening_tag = [u"<meta />"]
