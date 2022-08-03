from flask import Flask, render_template, request
# from flask_mail import Mail, Message
import repositories.account_repository as account_repository
import repositories.transaction_repository as transaction_repository
from datetime import date
from controllers.accounts_controller import accounts_blueprint
from controllers.transactions_controller import transactions_blueprint

app = Flask(__name__)


app.register_blueprint(accounts_blueprint)
app.register_blueprint(transactions_blueprint)



@app.route('/')
def home():
    accounts = account_repository.return_all_balances_by_date(date.today())
    return render_template('home.html', accounts = accounts)


if __name__ == '__main__':
    app.run(debug=True)