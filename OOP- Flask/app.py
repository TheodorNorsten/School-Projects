#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""

from datetime import date, timedelta
from flask import Flask, render_template, request
from account_manager import AccountManager

app = Flask(__name__)
bank = AccountManager()

@app.route("/")
def main():
    """
    Home route
    Shows a table of all accounts and their information.
    """
    return render_template("index.html", accounts=bank.accounts)



@app.route("/transfer", methods=["POST", "GET"])
def transfer():
    """
    Transaction route
    Displays a form where you can transfer balance.
    """
    message = None
    if request.method == "POST":
        bank.transfer(request.form)
        bank.save_data()
        message = "Moved ${amount} from account #{from_} to #{to}".format(
            amount=request.form["amount"],
            from_=request.form["from_account"],
            to=request.form["to_account"],
        )

    return render_template(
        "transfer.html",
        accounts=bank.accounts,
        message=message
    )

@app.route('/account/<int:account_id>', methods=["POST", "GET"])
def account(account_id):
    """
    Account route
    Takes an account id and displays its "own" page.
    """
    interests = None
    current_account = bank.get_account_by_id(account_id)
    date_ = date.today() + timedelta(days=1)

    if request.method == "POST":
        date_ = request.form["calculation_date"]
        interests = bank.calculate_interest_rate(current_account, date_)

    return render_template(
        "account.html",
        account=current_account,
        time=date_,
        interests=interests
    )



@app.route("/add/<string:what>", methods=["POST", "GET"])
def add(what):
    """
    Route to add accounts or persons
    - /add/person  returns a create form for the class Person
    - /add/account returns a create form for the Account classes
    """
    message = None
    if request.method == "POST":

        if what == 'person':
            check_person_id = bank.add_persons(request.form)
            if check_person_id is False:
                message = "Error: id {i} already exist".format(i=request.form["id"])
            else:
                message = "{name} has been added".format(name=request.form["name"])
            print(request.form)

        else:
            bank.add_acoounts(request.form)
            message = "a new {acc} has been added".format(acc=request.form["type"])
            print(request.form)

        bank.save_data()

    return render_template(
        "add.html",
        what=what,
        account_types=[{"id_": "Account"}, {"id_": "SavingsAccount"}],
        message=message
    )




@app.route("/connect", methods=["POST", "GET"])
def connect():
    """
    Route to connect a person to an account
    """
    message = None
    if request.method == "POST":
        print(request.form)
        boolean = bank.connect_person_account(request.form)
        if not boolean:
            message = "Error {id} already owns the account #{acc}".format(
                id=request.form["person"], acc=request.form["account"])
        else:
            message = "{id} has been added to account #{acc}".format(
                id=request.form["person"], acc=request.form["account"])

        bank.save_data()

    return render_template(
        "connect.html",
        message=message,
        persons=bank.persons,
        accounts=bank.accounts
        )



@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument,import-outside-toplevel
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)
