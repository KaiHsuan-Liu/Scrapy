import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

class testTitle(unittest.TestCase):
    def setUpClass():
        print('setUp~~')
        global bsObj
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        bsObj = BeautifulSoup(urlopen(url))

    # def tearDown(self):
        # print('tearDown~~~')

    def test_add(self):
        total = 2+2
        self.assertEqual(total, 4)

    def test_title(self):
        pageTitle = bsObj.find('h1').get_text()
        self.assertEqual('Monty Python', pageTitle)

if __name__ == "__main__":
    unittest.main()