import unittest

from main import sum_all_numbers, surround


class DecoratorTest(unittest.TestCase):
    def test_double_decorator(self):
        result = sum_all_numbers(4)
        self.assertEqual(result, 12)

    def test_uppercase_decorator(self):
        result = surround('hElLo')
        self.assertEqual(result, '--- HELLO ---')


if __name__ == '__main__':
    unittest.main()
