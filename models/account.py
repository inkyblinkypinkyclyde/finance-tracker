class Account:
    def __init__(self, name, balance, credit_limit, is_account, id=None):
        self.name = name
        self.balance = balance
        self.credit_limit = credit_limit
        self.is_account = is_account
        self.id = id
    
    def available_funds(self):
        return self.credit_limit + self.balance
    
    def to_string_funds(self):
        if self.available_funds() < 100 and self.available_funds() > -100:
            return f"{self.available_funds()}p"
        else:
            return f"£{self.available_funds()/100:.2f}"
    
    def to_string_balance(self):
        if self.balance < 100 and self.balance > -100:
            return f"{self.balance}p"
        else:
            return f"£{self.balance/100:.2f}"
    
    def to_pence(amount):
        return amount * 100

    def to_pounds(amount):
        return amount/100

    def get_total_of_transactions(self, transactions):
        balance = 0
        for transaction in transactions:
            balance = balance + transaction['amount'] #### comment this out to run the tests
            # balance = balance + transaction.amount #### comment this out to run the app
        return balance

    def update_balance(self, transactions):
        self.balance = self.balance - self.get_total_of_transactions(transactions)

    # def update_all_balances(self, transaction)
