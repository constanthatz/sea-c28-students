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
        expected = '<p>\n</p>'

        p = hr.P()
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

if __name__ == '__main__':
    unittest.main()
