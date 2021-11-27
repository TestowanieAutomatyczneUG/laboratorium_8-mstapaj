import unittest
from src.sample.Is_Pangram import Is_Pangram
from parameterized import parameterized, parameterized_class


class Is_Pangram_Parameterized_in_class(unittest.TestCase):

    def setUp(self):
        self.temp = Is_Pangram()

    @parameterized.expand([
        ('N', 'abcsdfs', False),
        ('N', 'abcdefghijklmnopqrstuvwxyz', True),
        ('N', 'jklwxyamnopqrbcdevfstughiz', True),
        ('N', 'abcdefghi  jklmnopqrst  uvwxy z', True),
        ('N', 'abcefghi  jklmnopqrst  uvxy z', False),
        ('N', 'abcde//*fghijk+-lmno.pqrstu+++vwx,,yz', True),
        ('N', 'acde//*fghijk+-lmno.pqrtu+++vwx,,yz', False),
        ('N', 'abc445defghi25jklmno4654pqrst14uvwxy77z4', True),
        ('N', 'ac445defghi25jklmno4654pqst14uvwxy77z4', False),
        ('N', '3212', False),
        ('E', 25, Exception),
        ('E', -15, Exception),
        ('E', 2.54, Exception),
        ('E', -15, Exception),
        ('E', -4.1253, Exception),
        ('E', [], Exception),
        ('E', {}, Exception),
        ('E', None, Exception),
        ('E', True, Exception),
        ('E', False, Exception)
    ])
    def test_Is_Pangram_Parameterized(self, type, input, output):
        if type == 'N':
            if output:
                self.assertTrue(self.temp.check(input))
            else:
                self.assertFalse(self.temp.check(input))
        elif type == 'E':
            self.assertRaises(output, self.temp.check, input)


@parameterized_class(('type', 'input', 'output'), [
    ('N', 'abcsdfs', False),
    ('N', 'abcdefghijklmnopqrstuvwxyz', True),
    ('N', 'jklwxyamnopqrbcdevfstughiz', True),
    ('N', 'abcdefghi  jklmnopqrst  uvwxy z', True),
    ('N', 'abcefghi  jklmnopqrst  uvxy z', False),
    ('N', 'abcde//*fghijk+-lmno.pqrstu+++vwx,,yz', True),
    ('N', 'acde//*fghijk+-lmno.pqrtu+++vwx,,yz', False),
    ('N', 'abc445defghi25jklmno4654pqrst14uvwxy77z4', True),
    ('N', 'ac445defghi25jklmno4654pqst14uvwxy77z4', False),
    ('N', '3212', False),
    ('E', 25, Exception),
    ('E', -15, Exception),
    ('E', 2.54, Exception),
    ('E', -15, Exception),
    ('E', -4.1253, Exception),
    ('E', [], Exception),
    ('E', {}, Exception),
    ('E', None, Exception),
    ('E', True, Exception),
    ('E', False, Exception)
])
class Is_Pangram_Parameterized_out_of_class(unittest.TestCase):

    def setUp(self):
        self.temp = Is_Pangram()

    def test_Is_Pangram_Parameterized(self):
        if self.type == 'N':
            if self.output:
                self.assertTrue(self.temp.check(self.input))
            else:
                self.assertFalse(self.temp.check(self.input))
        elif self.type == 'E':
            self.assertRaises(self.output, self.temp.check, self.input)


if __name__ == '__main__':
    unittest.main()
