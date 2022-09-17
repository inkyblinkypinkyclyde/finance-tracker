import pdb
from models.account import Account
from models.transaction import Transaction

import repositories.account_repository as account_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
account_repository.delete_all()

account_1 = Account('test account 1', 10000, 0, True)
account_repository.save(account_1)
account_2 = Account('test account 2', 10000, 0, True)
account_repository.save(account_2)
merchant_1 = Account('test merchant 1', 0, 0, False)
account_repository.save(merchant_1)
merchant_2 = Account('test merchant 2', 0, 0, False)
account_repository.save(merchant_2)


# transaction_1 = Transaction(50000, "2022-06-01", "Mortgage", 4, 1, True)
# transaction_repository.save(transaction_1)
# # transaction_2 = Transaction(50000, "2022-06-01", "Mortgage2", 4, 1, True)
# # transaction_repository.save(transaction_2)
# transaction_2 = Transaction(5000, "2022-06-01", "Phone bill", 5, 1, True)
# transaction_repository.save(transaction_2)
# transaction_3 = Transaction(8000, "2022-06-01", "Gas and Electric", 5, 1, True)
# transaction_repository.save(transaction_3)
# transaction_4 = Transaction(1699, "2022-06-10", "Groceries", 5, 1, True)
# transaction_repository.save(transaction_4)
# transaction_5 = Transaction(1250, "2022-06-13", "Pizza", 6, 1, True)
# transaction_repository.save(transaction_5)

pdb.set_trace()