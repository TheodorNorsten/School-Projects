"""
Account classes."""


class Account():
    "Initiation of class Account"
    account_number = 1
    transaction_fee = 0.01

    def __init__(self, balance, holders=None):
        "init method for attribute Initiation"
        self._balance = balance
        self._type = self.__class__.__name__
        self.holders = holders if holders else []
        self._id = Account.account_number
        Account.account_number += 1


    @property
    def id_(self):
        "get instance method, id attribute"
        return self._id


    def get_holder(self):
        "get instance method, holder(list) attribute"
        if self.holders:
            if len(self.holders) > 1:
                string = ''
                for index, i in enumerate(self.holders):
                    if index != (len(self.holders) - 1):
                        string += i[-1] + ', '
                    else:
                        string += i[-1]

                return string


            return self.holders[-1][-1]


        return ''


    def add_holder(self, name):
        "setter instance method, "
        self.holders.append(name)


    @property
    def balance(self):
        "get-instance method, balance attribute"
        return self._balance


    @balance.setter
    def balance(self, balance):
        "setter instance method, balance attribute"
        self._balance = balance



    @classmethod
    def calculate_transaction_fee(cls, amount):
        "class method, calculate transaction fee based on input argument amount"
        fee = cls.transaction_fee * amount
        return fee



    @property
    def type_(self):
        "get-instance method, for object type "
        return self._type
        #return self.__class__.__name__


    def to_json(self):
        "converts object to dictionary format"
        return {
            "type": self.__class__.__name__,
            "balance": self._balance,
            "id": self._id,
            "holders": self.holders
        }

    @classmethod
    def create_accounts(cls, data_json):
        "classmethod creates new object from json-format"
        return cls(float(data_json["balance"]), data_json.get('holders', []))



    def __str__(self):
        return "balance: {b} type: {t} id: {i} holders: {h}".format(
            b=self.balance, t=self.type_, i=self.id_, h=self.holders)



class SavingsAccount(Account):
    "Initiation of class SavingsAccount- inherits from Account class"
    interest_rate = 0.0015
    transaction_fee = 0.013

    #def __init__(self, balance):
    "init method"
    #super().__init__(balance)


    def calculate_daily_interest_rate(self):
        "instance method, calculates the daily interest based on attribute balance"
        return self._balance * (self.interest_rate / 365)



if __name__ == "__main__":
    pass
