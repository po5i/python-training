import unittest

from main import D


class InheritanceTest(unittest.TestCase):
    def test_invocations(self):
        x = D()
        invocations = x.method_return()

        self.assertEqual(len(invocations), 4)
        self.assertEqual(invocations[0], 'method of D called')
        self.assertEqual(invocations[1], 'method of B called')
        self.assertEqual(invocations[2], 'method of C called')
        self.assertEqual(invocations[3], 'method of A called')

    def test_mro(self):
        self.assertEqual(len(D.mro()), 5)
        self.assertIn('main.D', str(D.mro()[0]))
        self.assertIn('main.B', str(D.mro()[1]))
        self.assertIn('main.C', str(D.mro()[2]))
        self.assertIn('main.A', str(D.mro()[3]))


if __name__ == '__main__':
    unittest.main()
