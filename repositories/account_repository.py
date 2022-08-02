from db.run_sql import run_sql

from models.account import Account
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

def save(account):
    sql = 'INSERT INTO accounts (name, balance, credit_limit, is_account) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [account.name, account.balance, account.credit_limit, account.is_account]
    results = run_sql(sql, values)
    id = results[0]['id']
    account.id = id
    return account

def select_all():
    accounts = []
    sql = "SELECT * FROM accounts"
    results = run_sql(sql)
    for row in results:
        account = Account(row['name'], row['balance'], row['credit_limit'], row['is_account'], row['id'])
        accounts.append(account)
    return accounts

def select_all_accounts():
    accounts = []
    sql = "SELECT * FROM accounts WHERE is_account = TRUE"
    results = run_sql(sql)
    for row in results:
        account = Account(row['name'], row['balance'], row['credit_limit'], row['is_account'], row['id'])
        accounts.append(account)
    return accounts

def select_all_merchants():
    accounts = []
    sql = "SELECT * FROM accounts WHERE is_account = FALSE"
    results = run_sql(sql)
    for row in results:
        account = Account(row['name'], row['balance'], row['credit_limit'], row['is_account'], row['id'])
        accounts.append(account)
    return accounts

def select(id):
    account = None
    sql = "SELECT * FROM accounts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        account = Account(result['name'], result['balance'], result['credit_limit'], result['is_account'], result['id'])
    return account

def delete_all():
    sql = 'DELETE FROM accounts'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM accounts WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(account):
    sql = 'UPDATE accounts SET (name, description, balance) = (%s, %s, %s, %s) WHERE id = %s'
    values = [account.name, account.balance, account.credit_limit, account.is_account, account.id]
    run_sql(sql, values)

def get_account_balance(account_id):
    sql = 'SELECT balance FROM accounts WHERE id = %s'
    values = [account_id]
    balance = run_sql(sql, values)
    return balance[0][0]

def get_balance_by_date(date, account_id):
    transactions = transaction_repository.get_transaction_up_to_date_and_including(date)
    balance = get_account_balance(account_id)
    for transaction in transactions:
        if transaction['out_of_account_id'] == account_id:
            balance = balance + transaction['amount']
    return balance

def return_all_balances_by_date(date):
    accounts = select_all_accounts()
    all_transactions = transaction_repository.get_transaction_up_to_date_and_including(date)
    for account in accounts:
        transactions_for_each_account = []
        for transaction in all_transactions:
            # print(transaction)
            if transaction['out_of_account_id'] == account.id:
                transactions_for_each_account.append(transaction)
        account.update_balance(transactions_for_each_account)
    return accounts


