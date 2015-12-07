from BankAccount import BankAccount
import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Vladko", 2000, "RON")
        self.account1 = BankAccount("Phillip", 4114, "RON")

    def test_init(self):
        self.assertEqual(self.account.get_name(), "Vladko")
        self.assertEqual(self.account1.get_name(), "Phillip")
        self.assertEqual(self.account.get_currency(), "RON")
        self.assertTrue(self.account.get_currency() == self.account1.get_currency())

    def test_str(self):
        self.assertEqual(str(self.account), "Bank account for Vladko with balance of 2000 RON")
        self.assertEqual(str(self.account1), "Bank account for Phillip with balance of 4114 RON")

    def test_get_name(self):
        self.assertEqual(self.account.get_name(), "Vladko")

    def test_get_currency(self):
        self.assertEqual(self.account1.get_currency(), "RON")

    def test_int(self):
        self.assertEqual(int(self.account), 2000)
        self.assertEqual(int(self.account1), 4114)

    def test_history(self):
        self.assertEqual(self.account.history(), ['Account was created.'])

    def test_deposit(self):
        self.account.deposit(213)
        self.assertEqual(int(self.account), 2213)
        self.account1.deposit(400)
        self.assertEqual(int(self.account1), 4514)

    def test_balance(self):
        self.assertEqual(self.account.balance(), 2000)

    def test_withdraw(self):
        self.account.withdraw(1200)
        self.assertEqual(self.account.balance(), 800)
        self.account1.withdraw(10000)
        self.assertEqual(self.account1.balance(), 4114)

    def test_transfer(self):
        self.account1.transfer_to(self.account, 114)
        self.assertEqual(int(self.account), 2114)
        self.assertEqual(int(self.account1), 4000)

    def test_history(self):
        self.assertEqual(self.account.history(), ['Account was created.'])


if __name__ == '__main__':
    unittest.main()
