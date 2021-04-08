from src.fizzbuzz import fizzbuzz
import unittest

class TestFizzbuzz(unittest.TestCase):

    # check if we have received an integer:
        # return error message if not 😀
    # check if number is divisible by 3:
        # return fizz 😀
    # check if it is divisible by 5:
        # return buzz 😀
    # check if it is divisible by both:
        # return fizzbuzz
    # else return input as string 😀
    
    def test_fizzbuzz_non_integer_input_fails(self):
        self.assertEqual("Please enter an integer", fizzbuzz("1"))

    def test_fizzbuzz_returns_integer_as_string(self):
        self.assertEqual("1", fizzbuzz(1))

    def test_fizzbuzz_3_returns_fizz(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_fizzbuzz_6_returns_fizz(self):
        self.assertEqual("fizz", fizzbuzz(6))

    def test_fizzbuzz_5_returns_buzz(self):
        self.assertEqual("buzz", fizzbuzz(5))

    def test_fizzbuzz_10_returns_buzz(self):
        self.assertEqual("buzz", fizzbuzz(10))

    def test_fizzbuzz_15_returns_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))

    def test_fizzbuzz_30_returns_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizzbuzz(30))