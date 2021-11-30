
class FizzBuzz:
    def game(self, num):
        if isinstance(num, int) or isinstance(num, float):
            if num % 15 == 0:
                return "FizzBuzz"
            elif num % 5 == 0:
                return "Buzz"
            elif num % 3 == 0:
                return "Fizz"
            else:
                return num
        else:
            raise Exception("Error in FizzBuzz")