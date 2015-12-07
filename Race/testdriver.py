from driver import Driver
from car import Car
import unittest

class TestDriver(unittest.TestCase):
    def setUp(self):
        self.car = Car("Opel", "Astra", 100)
        self.driver = Driver("Vladimir", self.car)

    def test_init(self):
        self.assertEqual(self.driver._name, "Vladimir")
        self.assertEqual(self.driver._car, self.car)

if __name__ == '__main__':
    unittest.main()
