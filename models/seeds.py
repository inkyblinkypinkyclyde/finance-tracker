from re import I


from models.transaction import Transaction
from models.account import Account

class Seeds:
    def __init__(self, name):
        self.name = name


    def get_list_of_length(number):
        new_list = []
        for x in range(number):
            i = 0
            new_list.append(i)
            i = i + 1
        return new_list
    
    def get_uniform_accounts_of_balance(balance, number_of_accounts):
        new_list = self.get_list_of_length(number_of_accounts)

