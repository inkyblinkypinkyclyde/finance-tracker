from flask import Flask, redirect, render_template, request, Blueprint
from datetime import date

from models.transaction import Transaction
from models.account import Account

import repositories.transaction_repository as transaction_repository
import repositories.account_repository as account_repository


accounts_blueprint = Blueprint("accounts", __name__)

#show all accounts
@accounts_blueprint.route('/accounts/all', methods=['GET'])
def accounts_all():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    today = date.today()
    return render_template(
        '/accounts/index_accounts.html',
        merchants=merchants,
        accounts=accounts,
        today=today
        )

#show all merchants
@accounts_blueprint.route('/merchants/all', methods=['GET'])
def merchants_all():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    today = date.today()
    return render_template(
        '/accounts/index_merchants.html',
        merchants=merchants,
        accounts=accounts,
        today=today
        )
    
#add new account
@accounts_blueprint.route('/accounts/new', methods=['GET'])
def new_account():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    today = date.today()
    return render_template(
        '/accounts/new_account.html',
        merchants=merchants,
        accounts=accounts,
        today=today
        )

@accounts_blueprint.route('/accounts/new', methods=['POST'])
def add_new_account():
    name = request.form['name']
    balance = Account.to_pence(int(request.form['balance']))
    credit_limit = Account.to_pence(int(request.form['credit_limit']))
    account = Account(name, balance, credit_limit, True)
    account_repository.save(account)
    return redirect('/accounts/all')

#add new merchant
@accounts_blueprint.route('/merchants/new', methods=['GET'])
def new_merchant():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    today = date.today()
    return render_template(
        '/accounts/new_merchant.html',
        merchants=merchants,
        accounts=accounts,
        today=today
        )

@accounts_blueprint.route('/merchants/new', methods=['POST'])
def add_new_merchant():
    name = request.form['name']
    merchant = Account(name, 0, 0, False)
    account_repository.save(merchant)
    return redirect('/merchants/new')

@accounts_blueprint.route('/future', methods=['GET'])
def view_future_balances():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    today = date.today()
    return render_template(
        '/future.html',
        merchants=merchants,
        accounts=accounts,
        today=today
    )

@accounts_blueprint.route('/future', methods=['POST'])
def add_balance_transfer():
    amount = Transaction.to_pence(int(request.form['amount']))
    date = request.form['date']
    description = "Balance transfer"
    into_account = account_repository.select(int(request.form['account_id_out']))
    out_of_account = account_repository.select(int(request.form['account_id_in']))
    transaction = Transaction(amount, date, description, into_account.id, out_of_account.id, True)
    transaction_repository.save(transaction)
    return redirect('/future')




#edit

#delete