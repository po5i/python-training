import unittest

from main import sum_all_numbers, to_uppercase, sandwich


class DecoratorTest(unittest.TestCase):
    def test_double_decorator(self):
        result = sum_all_numbers(4)
        self.assertEqual(result, 12)

    def test_bold_decorator(self):
        result = to_uppercase('hElLo')
        self.assertEqual(result, '<strong>HELLO</strong>')

    def test_sandwich_decorator(self):
        result = sandwich()
        self.assertIn('-- ham --', result)
        self.assertIn('#tomatoes#', result)
        self.assertIn('<\_______/>', result)


if __name__ == '__main__':
    unittest.main()
