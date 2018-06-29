import unittest

from main import House


class BoolTest(unittest.TestCase):
    def test_truthy_falsy(self):
        good_house = House(2, 4)
        self.assertTrue(good_house)

        bad_house = House(0, 0)
        self.assertFalse(bad_house)

        ugly_house = House(-1, -2)
        self.assertFalse(bool(ugly_house))


if __name__ == '__main__':
    unittest.main()
