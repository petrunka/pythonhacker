import unittest
from bill import Bill

class TestBill(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(5)
        
    def test_bill_init(self):
        self.assertEqual(self.bill._amount, 5)

    def test_bill_str(self):
        self.assertEqual(str(self.bill), 'A 5$ bill')

    def test_bill_int(self):
        self.assertEqual(int(self.bill), 5)

    def test_bill_eq(self):
        bill2 = Bill(10)
        bill3 = Bill(5)
        self.assertTrue(self.bill == bill3)
        self.assertFalse(self.bill == bill2)

if __name__ == '__main__':
    unittest.main()

# Тестовете не трябва да зависят един от друг по между си
