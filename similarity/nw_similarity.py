'''

'''


class NWAlgorithm(object):
    '''
    https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
    '''

    def __init__(self, string_a, string_b):
        '''
        Constructor
        '''
        self.string_a = string_a
        self.string_b = string_b

        self.__compute()

    def __compute(self):
        '''
        '''
        rows = len(self.string_a) + 1
        cols = len(self.string_b) + 1
        self.matrix = [[0 for i in range(cols)] for i in range(rows)]
        for i in range(cols):
            self.matrix[0][i] = i
        for i in range(rows):
            self.matrix[i][0] = i

        for i in range(1, rows):
            for j in range(1, cols):
                c = NWAlgorithm.cost(self.string_a[i - 1], self.string_b[j - 1])
                v1 = self.matrix[i - 1][j - 1] + c
                v2 = self.matrix[i - 1][j] + 1
                v3 = self.matrix[i][j - 1] + 1
                self.matrix[i][j] = min(v1, v2, v3)

    def alignments(self):
        '''
        '''
        align_a = ''
        align_b = ''

        a = len(self.string_a)
        b = len(self.string_b)

        while a > 0 or b > 0:
            if a > 0 and b > 0 and self.matrix[a][b] == self.matrix[a - 1][b - 1] + NWAlgorithm.cost(
                    self.string_a[a - 1], self.string_b[b - 1]):
                align_a = self.string_a[a - 1] + align_a
                align_b = self.string_b[b - 1] + align_b
                a = a - 1
                b = b - 1
            elif a > 0 and self.matrix[a][b] == self.matrix[a - 1][b] + 1:
                align_a = self.string_a[a - 1] + align_a
                align_b = "-" + align_b
                a = a - 1
            else:
                align_a = "-" + align_a
                align_b = self.string_b[b - 1] + align_b
                b = b - 1

        return (align_a, align_b)

    def print_matrix(self):
        rows = len(self.string_a) + 1
        cols = len(self.string_b) + 1

        print "    ",
        print '_  ',
        for i in range(1, cols):
            print self.string_b[i - 1],
            print " ",
        print

        print '_',
        for i in range(0, rows):
            if i > 0:
                print self.string_a[i - 1], "  ",
            else:
                print "  ",
            for j in range(0, cols):
                print NWAlgorithm.__as_string(self.matrix[i][j], 3),
            print

    @staticmethod
    def __as_string(n, length):
        '''
        '''
        s = str(n)
        if n >= 0:
            s = ' ' + s
        if len(s) > length:
            s = s[0: length]
        else:
            while len(s) < length:
                s = s + ' '

        return s

    @staticmethod
    def cost(a, b):
        '''
        '''
        if a == b:
            return 0
        else:
            return 1