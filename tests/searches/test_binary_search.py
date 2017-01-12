import unittest

from collections import OrderedDict
from fractions import Fraction
from searches.binary_search import find_lower

class MyTestCase(unittest.TestCase):
    def test_binary_search(self):
        lisst = [1, 7, 9, 14, 23, 80]
        lisst[find_lower(lisst, 80)]
        for i in range(1, 81):
            x = find_lower(lisst, i)
            if x != -1:
                print '{0} answer={1}'.format(i, lisst[x])


        self.assertEqual(True, True)

    def test_binary_search_1(self):
        d = {}
        d[10] = 100
        d[5] = 20
        d[7] = 70
        d[2] = 50
        od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
        print od
        print type(od.keys())
        for k in od.keys():
            print k

        x = [Fraction(2, 3), Fraction(1, 2)]
        sorted(x)


if __name__ == '__main__':
    unittest.main()
