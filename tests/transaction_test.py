import unittest
from datetime import date

from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction0 = Transaction(0, "2022-08-03", "date", 1, 2, True)
        self.transaction10 = Transaction(0, "2022-08-04", "date", 1, 2, True)
        self.transaction1 = Transaction(10000, "2022-06-01", "Chairs", 1, 2, True)
        self.transaction2 = Transaction(20, "2022-06-02", "Chairs", 1, 2, True)
        self.transaction3 = Transaction(30, "2022-06-03", "Chairs", 1, 2, True)
        self.transaction11 = Transaction(110, "2022-06-11", "Chairs", 1, 2, True)
        self.transaction12 = Transaction(120, "2022-06-12", "Chairs", 1, 2, True)
        self.transaction13 = Transaction(130, "2022-06-13", "Chairs", 1, 2, True)
        self.transaction21 = Transaction(210, "2022-06-21", "Chairs", 1, 2, True)
        self.transaction22 = Transaction(220, "2022-06-22", "Chairs", 1, 2, True)
        self.transaction23 = Transaction(230, "2022-06-23", "Chairs", 1, 2, True)
        self.transaction24 = Transaction(240, "2022-06-24", "Chairs", 1, 2, True)

    def test_transaction_has_amount(self):
        self.assertEqual(10000, self.transaction1.amount)
    
    def test_transaction_can_return_amount_formatted_100(self):
        self.assertEqual("£100.00", self.transaction1.formatted_amount())
        
    def test_transaction_can_return_amount_formatted_20(self):
        self.assertEqual("20p", self.transaction2.formatted_amount())

    def test_transaction_can_return_amount_formatted_30(self):
        self.assertEqual("30p", self.transaction3.formatted_amount())

    def test_transaction_can_return_amount_formatted_110(self):
        self.assertEqual("£1.10", self.transaction11.formatted_amount())

    def test_transaction_can_return_amount_formatted_240(self):
        self.assertEqual("£2.40", self.transaction24.formatted_amount())

    def test_returns_date_formatted_1(self):
        self.assertEqual("1st June 2022", self.transaction1.formatted_date())

    def test_returns_date_formatted_2(self):
        self.assertEqual("2nd June 2022", self.transaction2.formatted_date())

    def test_returns_date_formatted_3(self):
        self.assertEqual("3rd June 2022", self.transaction3.formatted_date())

    def test_returns_date_formatted_11(self):
        self.assertEqual("11th June 2022", self.transaction11.formatted_date())

    def test_returns_date_formatted_12(self):
        self.assertEqual("12th June 2022", self.transaction12.formatted_date())

    def test_returns_date_formatted_13(self):
        self.assertEqual("13th June 2022", self.transaction13.formatted_date())

    def test_returns_date_formatted_21(self):
        self.assertEqual("21st June 2022", self.transaction21.formatted_date())

    def test_returns_date_formatted_22(self):
        self.assertEqual("22nd June 2022", self.transaction22.formatted_date())

    def test_returns_date_formatted_23(self):
        self.assertEqual("23rd June 2022", self.transaction23.formatted_date())

    def test_returns_date_formatted_24(self):
        self.assertEqual("24th June 2022", self.transaction24.formatted_date())

    def test_can_compare_dates_when_in_present(self):
        self.assertEqual(True, self.transaction0.is_in_past())

    def test_can_compare_dates_when_in_future(self):
        self.assertEqual(False, self.transaction10.is_in_past())

    def test_can_compare_dates_when_in_past(self):
        self.assertEqual(True, self.transaction1.is_in_past())


