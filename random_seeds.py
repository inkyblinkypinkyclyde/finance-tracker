import pdb
from models.account import Account
from models.transaction import Transaction
import random

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




# pdb.set_trace()