import unittest
from fizzbuzz import Fizzbuzz

class testFizzbuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = Fizzbuzz()

    def test_returns_one_if_given_one(self):
        expected = 1
        actual = Fizzbuzz.fizzbuzzer(self.fizzbuzz, 1)
        self.assertEqual(expected, actual)

    def test_returns_two_if_given_two(self):
        self.assertEqual(2, Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 2))

    def test_returns_buzz_if_given_three(self):
        self.assertEqual("Buzz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 3))

    def test_returns_buzz_if_given_six(self):
        self.assertEqual("Buzz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 6))

    def test_returns_fizz_if_given_five(self):
        self.assertEqual("Fizz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 5))

    def test_returns_fizz_if_given_ten(self):
        self.assertEqual("Fizz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 10))

    def test_returns_fizzbuzz_if_given_fifteen(self):
        self.assertEqual("FizzBuzz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 15))

    def test_returns_fizzbuzz_if_given_thirty(self):
        self.assertEqual("FizzBuzz", Fizzbuzz.fizzbuzzer(
            self.fizzbuzz, 30))
