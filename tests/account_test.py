import unittest

from models.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = Account("Current Account", 10000, 100000, True)
        self.account2 = Account("Credit Card", -50000, 100000, True)
        self.account3 = Account("Savings", 10, 0, True)

    def test_account_has_name(self):
        self.assertEqual("Current Account", self.account1.name)
    
    def test_account_has_balace(self):
        self.assertEqual(10000, self.account1.balance)
    
    def test_account_has_credit_limit(self):
        self.assertEqual(100000, self.account1.credit_limit)
    
    def test_returns_available_funds(self):
        available_funds_CA = self.account1.available_funds()
        available_funds_CC = self.account2.available_funds()
        self.assertEqual(50000, available_funds_CC)
        self.assertEqual(110000, available_funds_CA)
    
    def test_return_available_funds_string(self):
        funds_string_CA = self.account1.to_string_funds()
        funds_string_CC = self.account2.to_string_funds()
        funds_string_Sa = self.account3.to_string_funds()
        self.assertEqual('£1100.00', funds_string_CA)
        self.assertEqual('£500.00', funds_string_CC)
        self.assertEqual('10p', funds_string_Sa)
    
    def test_return_balance_string(self):
        balance_string_CA = self.account1.to_string_balance()
        balance_string_CC = self.account2.to_string_balance()
        balance_string_Sa = self.account3.to_string_balance()
        self.assertEqual('£100.00', balance_string_CA)
        self.assertEqual('£-500.00', balance_string_CC)
        self.assertEqual('10p', balance_string_Sa)



