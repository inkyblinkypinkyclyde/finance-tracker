from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.account_repository as account_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, date, description, into_account_id, out_of_account_id, is_visible) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.amount, transaction.date, transaction.description, transaction.into_account_id, transaction.out_of_account_id, transaction.is_visible]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        transaction = Transaction(row['amount'], row['date'], row['description'], row['into_account_id'], row['out_of_account_id'], row['is_visible'], row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    account = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        into_account = account_repository.select(result['into_account_id'])
        out_of_account = account_repository.select(result['out_of_account_id'])
        account =Transaction(result['amount'], result['date'], result['description'], into_account, out_of_account, result['id'])
    return account

def delete_all():
    sql = 'DELETE FROM transactions'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM transactions WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = 'UPDATE transactions SET (amount, date, description, account_id, merchant_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [transaction.amount, transaction.date, transaction.description, transaction.into_account_id, transaction.out_of_account_id, transaction.is_visible, transaction.id]
    run_sql(sql, values)

def get_transaction_up_to_date_and_including(date):
    sql = "SELECT * FROM transactions WHERE date <= %s"
    values = [date]
    return run_sql(sql, values)


