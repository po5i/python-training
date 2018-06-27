import unittest

from main import V6Engine, V8Engine, Car


class InheritanceTest(unittest.TestCase):
    def test_v6_engine_car(self):
        car = Car(V6Engine())
        car.turn_on()
        self.assertEqual(car._engine.active_pistons, 6)

    def test_v8_engine_car(self):
        car = Car(V8Engine())
        car.turn_on()
        self.assertEqual(car._engine.active_pistons, 8)


if __name__ == '__main__':
    unittest.main()
