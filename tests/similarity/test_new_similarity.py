import unittest

from similarity.nw_algorithm import NWAlgorithm


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nw_algorithm(self):
        t = NWAlgorithm('abcdefghij', 'dgj')
        t.print_matrix()

        (a, b) = t.alignments()
        print a
        print b


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSimple']
    unittest.main()