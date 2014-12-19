import unittest
import cStringIO
import html_render as hr


class MyTests(unittest.TestCase):
    def test_Html(self):
        expected = '<!DOCTYPE html>\n<html>\n</html>'

        html = hr.Html()
        f = cStringIO.StringIO()
        html.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

    def test_Body(self):
        expected = '<body>\n</body>'

        body = hr.Body()
        f = cStringIO.StringIO()
        body.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

    def test_P(self):
        expected = '<p style="text-align: center">\n    This is a paragraph.\n</p>'

        p = hr.P(u"This is a paragraph.", style=u"text-align: center")
        f = cStringIO.StringIO()
        p.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

    def test_Head(self):
        expected = '<head>\n</head>'

        head = hr.Head()
        f = cStringIO.StringIO()
        head.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

    def test_Title_OneLineTag(self):
        expected = '<title>This is a title.</title>'

        title = hr.Title(u"This is a title.")
        f = cStringIO.StringIO()
        title.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

    def test_Hr_SelfClosingTag(self):
        expected = '<hr />'

        Hr = hr.Hr()
        f = cStringIO.StringIO()
        Hr.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

    def test_Ul(self):
        expected = '<ul style="line-height:200%" id="This is a list">\n</ul>'

        ul = hr.Ul(id=u"This is a list", style=u"line-height:200%")
        f = cStringIO.StringIO()
        ul.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)
if __name__ == '__main__':
    unittest.main()
