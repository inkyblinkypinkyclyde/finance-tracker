class Account:
    def __init__(self, name, balance, credit_limit, is_account, id=None):
        self.name = name
        self.balance = balance
        self.credit_limit = credit_limit
        self.is_account = is_account
        self.id = id
    
    def available_funds(self):
        return (0 - self.credit_limit) + self.balance
    
    def to_string_funds(self): #
        if self.available_funds() < 100:
            return f"{self.available_funds()}p"
        else:
            return f"£{self.available_funds()/100:.2f}"
    
    def to_string_balance(self):
        if self.balance < 100 and self.balance > -100:
            return f"{self.balance}p"
        else:
            return f"£{self.balance/100:.2f}"
        