import unittest

from models.account import Account
from models.transaction import Transaction

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.transaction1 = Transaction(10000, "2022-06-01", "Chairs", 1, 2, True)
        self.transaction2 = Transaction(20, "2022-06-02", "Chairs", 1, 2, True)
        self.transaction3 = Transaction(30, "2022-06-03", "Chairs", 1, 2, True)
        self.account1 = Account("Current Account", 10000, 100000, True)
        self.account2 = Account("Credit Card", -50000, 100000, True)
        self.account3 = Account("Savings", 10, 0, True)

    def test_account_has_name(self):
        self.assertEqual("Current Account", self.account1.name)
    
    def test_account_has_balace(self):
        self.assertEqual(10000, self.account1.balance)
    
    def test_account_has_credit_limit(self):
        self.assertEqual(100000, self.account1.credit_limit)
    
    def test_returns_available_funds_CC(self):
        available_funds_CC = self.account2.available_funds()
        self.assertEqual(50000, available_funds_CC)
        
    def test_returns_available_funds_CA(self):
        available_funds_CA = self.account1.available_funds()
        self.assertEqual(110000, available_funds_CA)
    
    def test_return_available_funds_string_CA(self):
        funds_string_CA = self.account1.to_string_funds()
        self.assertEqual('£1100.00', funds_string_CA)

    def test_return_available_funds_string_CC(self):
        funds_string_CC = self.account2.to_string_funds()
        self.assertEqual('£500.00', funds_string_CC)

    def test_return_available_funds_string_Sa(self):
        funds_string_Sa = self.account3.to_string_funds()
        self.assertEqual('10p', funds_string_Sa)
    
    def test_return_balance_string_CA(self):
        balance_string_CA = self.account1.to_string_balance()
        self.assertEqual('£100.00', balance_string_CA)

    def test_return_balance_string_CC(self):
        balance_string_CC = self.account2.to_string_balance()
        self.assertEqual('£-500.00', balance_string_CC)

    def test_return_balance_string_Sa(self):
        balance_string_Sa = self.account3.to_string_balance()
        self.assertEqual('10p', balance_string_Sa)

    def test_can_add_up_transactions(self):
        transactions = [
            self.transaction1,
            self.transaction2,
            self.transaction3
            ]
        self.assertEqual(10050, self.account1.get_total_of_transactions(transactions))

    def test_can_update_balance_with_transactions(self):
        transactions = [
            self.transaction1,
            self.transaction2,
            self.transaction3
            ]
        self.account1.update_balance(transactions)
        self.assertEqual(20050, self.account1.balance)
    
    def test_can_return_amount_as_pence(self):
        amount = 1
        self.assertEqual(100, self.account1.to_pence(amount))
    
    def test_can_return_amount_as_pounds(self):
        amount = 100
        self.assertEqual(1, self.account1.to_pounds(amount))