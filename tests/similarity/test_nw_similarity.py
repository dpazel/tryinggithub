import unittest

from similarity.nw_similarity import NWAlgorithm


class TestNewSimilarity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nw_algorithm(self):
        t = NWAlgorithm('abcdefghij', 'dgj')
        t.print_matrix()

        (a, b) = t.alignments()
        print '---------------'
        print a
        print b


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSimple']
    print 'Starting new similarity tests'
    unittest.main()