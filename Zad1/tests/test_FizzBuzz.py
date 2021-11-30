import unittest
from hamcrest import *
from src.sample.FizzBuzz import FizzBuzz


class FizzBuzzPyHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = FizzBuzz()

    def testEquals_5(self):
        assert_that(self.temp.game(5), equal_to("Buzz"))

    def testEquals_3(self):
        assert_that(self.temp.game(3), equal_to("Fizz"))

    def testEquals_15(self):
        assert_that(self.temp.game(15), equal_to("FizzBuzz"))

    def testEquals_negative_95(self):
        assert_that(self.temp.game(-95), equal_to("Buzz"))

    def testEquals_negative_33(self):
        assert_that(self.temp.game(-33), equal_to("Fizz"))

    def testEquals_negative_150(self):
        assert_that(self.temp.game(-150), equal_to("FizzBuzz"))

    def testEquals_28(self):
        assert_that(self.temp.game(28), equal_to(28))

    def testEquals_41(self):
        assert_that(self.temp.game(41), equal_to(41))

    def testEquals_negative_82(self):
        assert_that(self.temp.game(-82), equal_to(-82))

    def testEquals_negative_113(self):
        assert_that(self.temp.game(-113), equal_to(-113))

    def testEquals_1531(self):
        assert_that(self.temp.game(1531), equal_to(1531))

    def testEquals_negative_decimal(self):
        assert_that(self.temp.game(-1.13), equal_to(-1.13))

    def testEquals_negative_decimal_2(self):
        assert_that(self.temp.game(-23.13), equal_to(-23.13))

    def testStartWith(self):
        assert_that(self.temp.game(12), starts_with("Fi"))

    def testEndsWith(self):
        assert_that(self.temp.game(20), ends_with("zz"))

    def testContains(self):
        assert_that(self.temp.game(33), contains_string('iz'))

    def testContainsInOrder(self):
        assert_that(self.temp.game(45), string_contains_in_order('iz', 'uz'))

    def testAnyOf(self):
        assert_that(self.temp.game(5), all_of(equal_to("Buzz"), contains_string("Buzz")))

    def testHasString(self):
        assert_that(self.temp.game(100000), has_string('Buzz'))

    def testHasLength(self):
        assert_that(self.temp.game(396392826), has_length(4))

    def testGreaterThan(self):
        assert_that(self.temp.game(21.11234), greater_than(10))

    def testLessThan(self):
        assert_that(self.temp.game(22.31331), less_than(25))

    def testCloseTo(self):
        assert_that(self.temp.game(33.12315234), close_to(33.13, 0.05))

    def testCloseTo2(self):
        assert_that(self.temp.game(12.5), close_to(12, 0.5))

    def testHasLengthGreaterThan(self):
        assert_that(self.temp.game(3693345), has_length(greater_than(6)))

    def testHasLengthLessThan(self):
        assert_that(self.temp.game(35), has_length(less_than(6)))

    def testInstance(self):
        assert_that(self.temp, is_(FizzBuzz))

    def testInstance2(self):
        assert_that(self.temp, instance_of(FizzBuzz))

    def testException_string(self):
        self.assertRaises(Exception, self.temp.game, "slowo")

    def testException_array(self):
        self.assertRaises(Exception, self.temp.game, [])

    def testException_object(self):
        self.assertRaises(Exception, self.temp.game, {})

    def testException_none(self):
        self.assertRaises(Exception, self.temp.game, None)

    def testException_string_number(self):
        self.assertRaises(Exception, self.temp.game, "31")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
