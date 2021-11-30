import unittest
from src.sample.FizzBuzz import FizzBuzz


class FizzBuzzParameterizedFile(unittest.TestCase):

    def test_from_file(self):
        fileTest = open("data/data_test_FizzBuzz")
        tmpFizzBuzz = FizzBuzz()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            elif line.startswith('*'):
                data = line.split(" ")
                inp, result = float(data[1]), float(data[2])
                self.assertEqual(tmpFizzBuzz.game(inp), result)
            elif line.startswith('!'):
                data = line.split(" ")
                inp = data[1]
                self.assertRaises(Exception,tmpFizzBuzz.game,inp)
            else:
                data = line.split(" ")
                inp, result = float(data[0]), data[1].strip("\n")
                self.assertEqual(tmpFizzBuzz.game(inp), result)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
