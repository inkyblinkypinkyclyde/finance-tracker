from flask import Flask, redirect, render_template, request, Blueprint
from datetime import date
from datetime import datetime


from models.transaction import Transaction
from models.account import Account

import repositories.transaction_repository as transaction_repository
import repositories.account_repository as account_repository

transactions_blueprint = Blueprint("transactions", __name__)

#show all
@transactions_blueprint.route('/transactions/all', methods=['GET'])
def transactions_all():
    transactions = transaction_repository.select_all()
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    all_accounts = account_repository.select_all()
    today = date.today()
    return render_template(
        '/transactions/index.html',
        transactions=transactions,
        accounts=accounts,
        merchants=merchants,
        all_accounts=all_accounts,
        today=today
        )

#add new
@transactions_blueprint.route('/transactions/new', methods=['GET'])
def transactions_new():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    payees = account_repository.select_all_payees()
    today = Transaction.today()
    today = date.today()
    return render_template(
        'transactions/new.html',
        payees=payees,
        accounts=accounts,
        merchants=merchants,
        today=today
        )

@transactions_blueprint.route('/transactions/new_payment_out', methods=['POST'])
def transactions_new_post_out():
    amount = Transaction.to_pence(int(request.form['amount']))
    date_of_transaction = request.form['date']
    description = request.form['description']
    account = account_repository.select(int(request.form['account_id']))
    merchant = account_repository.select(int(request.form['merchant_id']))
    transaction = Transaction(amount, date_of_transaction, description, merchant.id, account.id, True)
    if (transaction.is_in_past()):
        new_balance_account = account.balance - amount
        new_balance_merchant = merchant.balance + amount
        new_account_data_account = Account(account.name, new_balance_account, account.credit_limit, account.is_account, account.id)
        new_account_data_merchant = Account(merchant.name, new_balance_merchant, merchant.credit_limit, merchant.is_account, merchant.id)
        account_repository.update(new_account_data_account)
        account_repository.update(new_account_data_merchant)
        transaction_repository.save(transaction)
    return redirect('/transactions/new')

@transactions_blueprint.route('/transactions/new_payment_in', methods=['POST'])
def transactions_new_post_in():
    amount = Transaction.to_pence(int(request.form['amount']))
    date_of_transaction = request.form['date']
    description = request.form['description']
    account = account_repository.select(int(request.form['account_id']))
    payee = account_repository.select(int(request.form['merchant_id']))
    transaction = Transaction(amount, date_of_transaction, description, payee.id, account.id, True)
    if (transaction.is_in_past()):
        new_balance_account = account.balance - amount
        new_balance_payee = payee.balance + amount
        new_account_data_account = Account(account.name, new_balance_account, account.credit_limit, account.is_account, account.id)
        new_account_data_payee = Account(payee.name, new_balance_payee, payee.credit_limit, payee.is_account, merchant.id)
        account_repository.update(new_account_data_account)
        account_repository.update(new_account_data_payee)
        transaction_repository.save(transaction)
    return redirect('/transactions/new')


#edit

#delete


