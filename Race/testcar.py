from car import Car
import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Opel", "Astra", 100)

    def test_car_init(self):
        self.assertEqual(self.car._car, "Opel")
        self.assertEqual(self.car._model, "Astra")
        self.assertEqual(self.car._max_speed, 100)

    def test_car_str(self):
        self.assertEqual(str(self.car), "Opel Astra with maximum speed 100 kmph.")

    def test_repr(self):
        self.assertEqual(repr(self.car), str(self.car))


if __name__ == '__main__':
    unittest.main()
