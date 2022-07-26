from calendar import month_abbr
from datetime import date
from datetime import datetime

class Transaction:
    def __init__(self, amount, date, description, into_account_id, out_of_account_id, is_visible, id=None):
        self.amount = amount
        self.date = date
        self.description = description
        self.into_account_id = into_account_id
        self.out_of_account_id = out_of_account_id
        self.is_visible = is_visible
        self.id = id

    def formatted_amount(self):
        if self.amount < 100:
            return f"{self.amount}p"
        else:
            return f"£{self.amount/100:.2f}"
    
    def to_pence(amount):
        return amount * 100

    def to_pounds(amount):
        return amount/100 
    
    def return_merchant(self, merchants):
        for merchant in merchants:
            if merchant.id == self.into_account_id:
                return merchant.name
            else:
                return 'error'

    def today():
        return date.today()
    
    def yesterday():
        return date.today() - 1
        

    def formatted_date(self):
        months_list = [
            'January',
            'Febuary',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        month_count = 0
        for month in months_list:
            month_count+=1
            if month_count == int(self.date[5:7]):
                month_string = month
        if self.date[8:10] == '11':
            date_string_suffix = 'th'
        elif self.date[8:10] == '12':
            date_string_suffix = 'th'
        elif self.date[8:10] =='13':
            date_string_suffix = 'th'
        elif self.date[9:10] == '1':
            date_string_suffix = 'st'
        elif self.date[9:10] == '2':
            date_string_suffix = 'nd'
        elif self.date[9:10] == '3':
            date_string_suffix = 'rd'
        else:
            date_string_suffix = 'th'
        entire_date_formatted = f'{int(self.date[8:10])}{date_string_suffix} {month_string} {self.date[0:4]}'
        return entire_date_formatted
    
    def is_in_past(self):
        htmlDate = self.date
        dateTokens = htmlDate.split('-')
        pythonDate = date(int(dateTokens[0]), int(dateTokens[1]), int(dateTokens[2]))
        if  (pythonDate <= date.today()):
            return True
        else:
            return False


