import unittest

from main import my_list_of


class InheritanceTest(unittest.TestCase):
    def test_list_length(self):
        my_list = list(my_list_of(6))
        self.assertEqual(len(my_list), 6)

    def test_element_values(self):
        my_list = list(my_list_of(3))
        self.assertEqual(my_list, [0, 1, 2])

    def test_second_generated_value(self):
        my_gen = my_list_of(5)
        next_value = next(my_gen)
        next_value = next(my_gen)
        self.assertEqual(1, next_value)


if __name__ == '__main__':
    unittest.main()
