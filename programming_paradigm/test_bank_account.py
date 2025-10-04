import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_deposit_and_display(self):
        acc = BankAccount(0)
        acc.deposit(50)
        self.assertEqual(acc.account_balance, 50)

    def test_withdraw_success(self):
        acc = BankAccount(100)
        result = acc.withdraw(40)
        self.assertTrue(result)
        self.assertEqual(acc.account_balance, 60)

    def test_withdraw_insufficient(self):
        acc = BankAccount(30)
        result = acc.withdraw(50)
        self.assertFalse(result)
        self.assertEqual(acc.account_balance, 30)

    def test_deposit_invalid(self):
        acc = BankAccount(10)
        with self.assertRaises(ValueError):
            acc.deposit(-5)


if __name__ == '__main__':
    unittest.main()
