import unittest
class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit money must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds")
        self.balance -= amount

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Other account must be a BankAccount instance")
        self.withdraw(amount)
        other_account.deposit(amount)

    def get_balance(self):
        return self.balance

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Створення тестових рахунків для перевірок
        self.account = BankAccount(100)
        self.other_account = BankAccount(50)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)
        with self.assertRaises(ValueError):
            self.account.deposit(0)

        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50)

        with self.assertRaises(InsufficientFunds):
            self.account.withdraw(200)

        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    def test_transfer(self):
        self.account.transfer(self.other_account, 50)
        self.assertEqual(self.account.get_balance(), 50)
        self.assertEqual(self.other_account.get_balance(), 100)

        with self.assertRaises(InsufficientFunds):
            self.account.transfer(self.other_account, 200)
        with self.assertRaises(TypeError):
            self.account.transfer("not_a_bank_account", 50)

    def test_get_balance(self):
        # Перевірка початкового балансу
        self.assertEqual(self.account.get_balance(), 100)
        self.account.deposit(50)
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 120)

if __name__ == '__main__':
    unittest.main()
