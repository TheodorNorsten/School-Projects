#!/usr/bin/env python3
"""
Contains the handler/manager class for the accounts.
"""
from datetime import date, datetime
import json
from accounts import Account, SavingsAccount
from person import Person


class AccountManager():
    """ Initiation of class AccountManager, stores accounts from,
     classes Account and SavingsAccount"""

    _CLASSES = {
        "Account": Account,
        "SavingsAccount": SavingsAccount
    }

    def __init__(self):
        """init method, creates the attribute accounts, an empty list ,
        and loads in all accounts in json-file to the list.
        """
        self._accounts = []
        self._persons = []
        self.load_data()




    def load_data(self):
        "Instance method, load alla accounts from json-file"

        data_json = json.load(open("static/data/accounts.json"), encoding="utf-8")
        for i in data_json["Accounts"]:
            self.accounts.append(self._CLASSES[i["type"]].create_accounts(i))

        for i in data_json["Persons"]:
            self.persons.append(Person.create_person(i))


    def save_data(self):
        "Instance method, saves data from accounts to json-file"

        data_json = {}

        data_json["Accounts"] = [i.to_json() for i in self.accounts]
        data_json['Persons'] = [i.to_json() for i in self._persons]

        with open("static/data/accounts.json", 'w') as file:
            json.dump(data_json, file, indent=4)



    def add_acoounts(self, account):
        "Instance method that creates account and addds it to account list"
        self.accounts.append(self._CLASSES[account["type"]].create_accounts(account))


    def add_persons(self, person):
        "Instance method that creates a person object and addds it to person list"
        for pers_obj in self._persons:
            if person["id"] == pers_obj.id_:
                return False

        return self._persons.append(Person.create_person(person))




    @property
    def accounts(self):
        "get-instance method, returns the list of all accounts."
        return self._accounts

    @property
    def persons(self):
        "get instance method, returns all persons in the _person attribute"
        return self._persons



    def get_account_by_id(self, id_nr):
        """ instance method, takes an id(int) as argument and,
        returns the corresponding account in the account list """
        for account in self.accounts:
            if account.id_ == id_nr:
                return account
        return "konto med detta id finns inte"


    def get_person_by_id(self, id_nr):
        """instance method, takes a person Id as input and
         returns the corresponding person object."""
        for person in self._persons:
            if person.id_ == id_nr:
                return person
        return "Detta id har ingen ägare"



    def connect_person_account(self, connect_data):
        """instance method, connects person to account based on input from
        form request. adds the person name and id as string to account obj.
        if personId already exist returns False. """

        person_obj = self.get_person_by_id(connect_data["person"])
        account_obj = self.get_account_by_id(int(connect_data["account"]))
        temp_lista = []

        for holder in account_obj.holders:
            if holder[-1] == person_obj.id_:
                return False

        temp_lista.append(person_obj.name)
        temp_lista.append(person_obj.id_)
        account_obj.add_holder(temp_lista)
        return True

    def transfer(self, data):
        """ instance method, takes one argument data(immutableMultidict) and
        transfer given amount between two accounts. """

        from_account = self.get_account_by_id(int(data["from_account"]))
        to_account = self.get_account_by_id(int(data["to_account"]))
        amount = float(data["amount"])

        from_account.balance -= amount
        trans_fee = from_account.calculate_transaction_fee(amount)
        to_account.balance += (amount - trans_fee)



    @staticmethod
    def calculate_interest_rate(account, date_future):
        """staticmethod, takes an account and string(date) as argument,
        calculates the interest between todays date and input date."""

        date_future = datetime.strptime(date_future, '%Y-%m-%d').date()
        todays_date = date.today()

        daily_interest = account.calculate_daily_interest_rate()
        numb_days = date_future - todays_date
        interest = daily_interest * (numb_days.days)
        return interest





if __name__ == "__main__":
    pass
