from batchbill import BatchBill
from bill import Bill
import unittest

class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.bill5 = Bill(5)
        self.bill10 = Bill(10)
        self.batch = BatchBill([self.bill5, self.bill10])

    def test_batchbill_init(self):
        self.assertIn(self.bill5, self.batch)
        self.assertIn(self.bill10, self.batch)

    def test_len(self):
        self.assertEqual(2, len(self.batch))

if __name__ == '__main__':
    unittest.main()
