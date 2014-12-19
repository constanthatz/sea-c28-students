import unittest
import cStringIO
import html_render as hr

class MyTests(unittest.TestCase):
    def test_Html(self):
        expected = '<!DOCTYPE html>\n<html>\n</html>'

        page = hr.Html()
        f = cStringIO.StringIO()
        page.render(f)
        f.reset()
        actual = f.read()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
