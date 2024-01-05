from fizzbuzz import fizzbuzz
import unittest

class TestFizzBuzzGame(unittest.TestCase):
    def test_fizzbuzz_default_range(self):
        """
        Test FizzBuzz for the default range (1 to 15).
        """
        expected_output = [
            '1', '2', '3 fizz', '4', '5 buzz', '6 fizz', '7', '8', '9 fizz', '10 buzz',
            '11', '12 fizz', '13', '14', '15 fizz buzz'
        ]
        self.assertEqual(fizzbuzz(1, 15), expected_output)

    def test_fizzbuzz_custom_range(self):
        """
        Test FizzBuzz for a custom range (10 to 20).
        """
        expected_output = [
            '10 buzz', '11', '12 fizz', '13', '14', '15 fizz buzz', '16', '17', '18 fizz', '19', '20 buzz'
        ]
        self.assertEqual(fizzbuzz(10, 20), expected_output)

    def test_fizzbuzz_out_of_range(self):
        """
        Test FizzBuzz for out-of-range values.
        """
        with self.assertRaises(ValueError):
            fizzbuzz(0, 101)

    def test_fizzbuzz_same_numbers(self):
        """
        Test FizzBuzz for the same start and end numbers.
        """
        expected_output = ['5 buzz']
        self.assertEqual(fizzbuzz(5, 5), expected_output)
        
    def test_fizzbuzz_invalid_range(self):
        """
        Test FizzBuzz for an invalid range where start is greater than end.
        """
        with self.assertRaises(ValueError):
            fizzbuzz(20, 10)


if __name__ == '__main__':
    unittest.main()