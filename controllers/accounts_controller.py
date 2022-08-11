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

#show all payees
@accounts_blueprint.route('/payees/all', methods=['GET'])
def payees_all():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    payees = account_repository.select_all_payees()
    today = date.today()
    return render_template(
        '/accounts/index_payees.html',
        merchants=merchants,
        accounts=accounts,
        payees=payees,
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

#add new payee
@accounts_blueprint.route('/payees/new', methods=['GET'])
def new_payee():
    accounts = account_repository.select_all_accounts()
    merchants = account_repository.select_all_merchants()
    today = date.today()
    return render_template(
        '/accounts/new_payee.html',
        merchants=merchants,
        accounts=accounts,
        today=today
        )

@accounts_blueprint.route('/payees/new', methods=['POST'])
def add_new_payee():
    name = request.form['name']
    payee = Account(name, 0, 1, False)
    # breakpoint()
    account_repository.save(payee)
    return redirect('/payees/new')

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
    sender = account_repository.select(int(request.form['account_id_out']))
    reciever  = account_repository.select(int(request.form['account_id_in']))
    description = f'out of {sender.name} into {reciever.name}'
    transaction = Transaction(amount, date, description, sender.id, reciever.id, True)
    if (transaction.is_in_past()):
        new_balance_sender = sender.balance - amount
        new_balance_reciever = reciever.balance + amount
        new_account_data_sender = Account(sender.name, new_balance_sender, sender.credit_limit, sender.is_account, sender.id)
        new_account_data_reciever = Account(reciever.name, new_balance_reciever, reciever.credit_limit, reciever.is_account, reciever.id)
        account_repository.update(new_account_data_sender)
        account_repository.update(new_account_data_reciever)
        transaction_repository.save(transaction)
    return redirect('/future')




#edit

#delete