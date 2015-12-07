from race import Race
from driver import Driver
from car import Car
import unittest
class TestRace(unittest.TestCase):
    def setUp(self):
        self.car1 = Car("Opel", "Astra", 100)
        self.car2 = Car("Renault", "CX5", 300)
        self.driver1 = Driver("Vladimir", self.car1)
        self.driver2 = Driver("Peter", self.car2)
        self.driver3 = Driver("Victor", self.car1)
        self.race = Race([self.driver1, self.driver2, self.driver3], 0.12)

    def test_init(self):
        self.assertEqual(self.race._crash_chance, 0.12)
        self.assertEqual(self.race._drivers[1], self.driver2)

if __name__=='__main__':
    unittest.main()
