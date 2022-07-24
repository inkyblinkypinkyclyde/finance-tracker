from flask import Flask, redirect, render_template, request, Blueprint

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
    return render_template('/transactions/index.html', transactions=transactions, accounts=accounts, merchants=merchants)

#add new
@transactions_blueprint.route('/transactions/new', methods=['GET'])
def transactions_new():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    return render_template('transactions/new.html', accounts=accounts, merchants=merchants)

@transactions_blueprint.route('/transactions/new', methods=['POST'])
def transactions_new_post():
    amount = Transaction.to_pence(int(request.form['amount']))
    date = request.form['date']
    description = request.form['description']
    account = account_repository.select(int(request.form['account_id']))
    merchant = account_repository.select(int(request.form['merchant_id']))
    transaction = Transaction(amount, date, description, merchant.id, account.id, True)
    transaction_repository.save(transaction)
    return redirect('/transactions/new')

#edit

#delete


