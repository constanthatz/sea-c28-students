#!/usr/bin/env python

import cStringIO
import itertools


class Element(object):
    tag = u""
    indent = u" "

    def __init__(self, inside=None, **kwargs):
        # Initialize list for contents of html elements
        # print(self.tag)
        if inside:
            self.insides = [inside]
        else:
            self.insides = []

        self.kwargs = kwargs

    def append(self, stuff):
        self.insides += [stuff]

    def render(self, file_out, ind=0):

        ind += 4
        insides = self.insides[:]
        for i, x in enumerate(insides):
            if isinstance(x, Element):
                f = cStringIO.StringIO()
                x.render(f, ind)
                f.reset()
                insides[i] = f.read()
                # print([insides[i]])
                # print()
                f.close()
        # print(insides)
        ind -= 4

        # insides = ([self.indent * ind + u"<{}>".format(self.tag)] +
        #            [self.indent * (ind + 4) + x for x in insides] +
        #            [self.indent * ind + u"</{}>".format(self.tag)])

        if self.kwargs:
            insides = ([self.indent * ind + u"<{} >".format(self.tag)] +
                       [self.indent * (ind + 4) + x for x in insides] +
                       [self.indent * ind + u"</{}>".format(self.tag)])
        else:
            insides = ([self.indent * ind + u"<{}>".format(self.tag)] +
                       [self.indent * (ind + 4) + x for x in insides] +
                       [self.indent * ind + u"</{}>".format(self.tag)])
        file_out.write("\n".join(insides))


class Html(Element):
    # tag = (u"<!DOCTYPE html>\n<html>", u"</html>")
    tag = u"html"


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"


class Head(Element):
    tag = u"head"


class OneLineTag(Element):

    def render(self, file_out, ind=0):
        insides = self.insides[:]
        insides = ([self.indent * ind + u"<{}>".format(self.tag)] +
                   insides +
                   [u"</{}>".format(self.tag)])
        file_out.write("".join(insides))


class Title(OneLineTag):
    tag = u"title"


class SelfClosingTag(Element):

    def render(self, file_out, ind=0):
        temp_tags = list(self.tags)
        if self.kwargs:
            list_tag = temp_tags

            for key in self.kwargs:
                list_tag.insert(-2, u'{}="{}"'.format(key, self.kwargs[key]))
            temp_tags = "".join(list_tag)

        # Combine the single tag into a list.
        all_out = temp_tags
        file_out.write("".join(all_out))


class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = u"a"

    def __init__(self, *args):
        OneLineTag.__init__(self, args[1], href=args[0])


class Ul(Element):
    tag = u"ul"


class Li(Element):
    tag = u"li"


class H(OneLineTag):
    tag = u"h"

    def __init__(self, *args):
        # Modify name of tag with arg[0]
        list_tags = [list(x) for x in self.tags]
        [x.insert(-1, u"{}".format(args[0])) for x in list_tags]
        self.tags = ["".join(x) for x in list_tags]
        OneLineTag.__init__(self, args[1])


class Meta(SelfClosingTag):
    tag = u"meta"
