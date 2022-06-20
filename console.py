import pdb
from models.account import Account
from models.transaction import Transaction

import repositories.account_repository as account_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
account_repository.delete_all()

