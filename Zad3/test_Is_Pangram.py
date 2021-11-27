import unittest
from Is_Pangram import Is_Pangram


class Is_Pangram_Test(unittest.TestCase):

    def setUp(self):
        self.temp = Is_Pangram()

    def test_Is_Pangram_not_alphabet(self):
        self.assertFalse(self.temp.check('abcsdfs'))

    def test_Is_Pangram_alphabet(self):
        self.assertTrue(self.temp.check('abcdefghijklmnopqrstuvwxyz'))

    def test_Is_Pangram_alphabet_random(self):
        self.assertTrue(self.temp.check('jklwxyamnopqrbcdevfstughiz'))

    def test_Is_Pangram_alphabet_spaces(self):
        self.assertTrue(self.temp.check('abcdefghi  jklmnopqrst  uvwxy z'))

    def test_Is_Pangram_not_alphabet_spaces(self):
        self.assertFalse(self.temp.check('abcefghi  jklmnopqrst  uvxy z'))

    def test_Is_Pangram_alphabet_symbols(self):
        self.assertTrue(self.temp.check('abcde//*fghijk+-lmno.pqrstu+++vwx,,yz'))

    def test_Is_Pangram_not_alphabet_symbols(self):
        self.assertFalse(self.temp.check('acde//*fghijk+-lmno.pqrtu+++vwx,,yz'))

    def test_Is_Pangram_alphabet_numbers(self):
        self.assertTrue(self.temp.check('abc445defghi25jklmno4654pqrst14uvwxy77z4'))

    def test_Is_Pangram_not_alphabet_numbers(self):
        self.assertFalse(self.temp.check('ac445defghi25jklmno4654pqst14uvwxy77z4'))

    def test_Is_Pangram_string_number(self):
        self.assertFalse(self.temp.check('3212'))

    def test_Is_Pangram_int(self):
        self.assertRaises(Exception, self.temp.check, 25)

    def test_Is_Pangram_int_negative(self):
        self.assertRaises(Exception, self.temp.check, -15)

    def test_Is_Pangram_float(self):
        self.assertRaises(Exception, self.temp.check, 2.35)

    def test_Is_Pangram_float_negative(self):
        self.assertRaises(Exception, self.temp.check, -4.315)

    def test_Is_Pangram_array(self):
        self.assertRaises(Exception, self.temp.check, [])

    def test_Is_Pangram_object(self):
        self.assertRaises(Exception, self.temp.check, {})

    def test_Is_Pangram_none(self):
        self.assertRaises(Exception, self.temp.check, None)

    def tearDown(self):
        self.temp = None
