#pylint: disable=protected-access
"test file"

import unittest
from account_manager import AccountManager
from accounts import Account


#saving = SavingsAccount(5000)

class TestBank(unittest.TestCase):
    "Initiation of Test class"

    def setUp(self):
        """ creates object for all tests"""
        Account.account_number = 1
        self.bank = AccountManager()


    def tearDown(self):
        "Removes dependicies after every test"
        self.bank = None

    def test_init_accounts(self):
        " test init init methods from both account types"
        account_obj = self.bank.accounts[0]
        saving_obj = self.bank.accounts[3]
        self.assertEqual(account_obj.balance, 9499.0)
        self.assertEqual(account_obj.type_, 'Account')
        self.assertEqual(account_obj.id_, 1)
        self.assertEqual(account_obj.holders, [])

        self.assertEqual(saving_obj.balance, 10990.0)
        self.assertEqual(saving_obj.type_, 'SavingsAccount')
        self.assertEqual(saving_obj.id_, 4)
        self.assertEqual(saving_obj.holders, [])



    def test_get_account_id_notfound(self):
        "Test that bank returns correct string when accountID not exist"
        self.assertEqual(
            self.bank.get_account_by_id(10), "konto med detta id finns inte")



    def test_get_account_id_found(self):
        "Test bank returns correct account object when accountID exist"
        self.assertEqual(self.bank.get_account_by_id(1), self.bank.accounts[0])



    def test_transaction_account(self):
        "Test transaction Account"
        input_dic = {'from_account':'1', 'to_account':'2', 'amount':'1000'}
        self.assertEqual(self.bank.accounts[0].balance, 9499.0)
        self.assertEqual(self.bank.accounts[1].balance, 6698.0)

        self.bank.transfer(input_dic)
        self.assertEqual(self.bank.accounts[0].balance, 8499.0)
        self.assertEqual(self.bank.accounts[1].balance, 7688.0)


    def test_transaction_savingccount(self):
        "test transaction SavingsAccount"
        input_dic = {'from_account':'4', 'to_account':'5', 'amount':'1000'}
        self.assertEqual(self.bank.accounts[3].balance, 10990.0)
        self.assertEqual(self.bank.accounts[4].balance, 11800.0)

        self.bank.transfer(input_dic)
        self.assertEqual(self.bank.accounts[3].balance, 9990.0)
        self.assertEqual(self.bank.accounts[4].balance, 12787.0)


    def test_interest_cal(self):
        "test interest calculation between two days."
        string = '2021-02-17'
        acc = self.bank.get_account_by_id(4)

        self.assertEqual(self.bank.calculate_interest_rate(acc, string), 0.09032876712328768)


    def test_init_persons(self):
        "test init method of person class"
        person_obj = self.bank.persons[0]
        self.assertEqual(person_obj.name, 'theodor')
        self.assertEqual(person_obj.id_, 'ted')

    def test_get_person_id_notfound(self):
        "Test bank returns correct string when personId not found"
        self.assertEqual(
            self.bank.get_person_by_id('lena'), "Detta id har ingen ägare")



    def test_get__id_found(self):
        "Test bank returns correct person object when personId found."
        self.assertEqual(self.bank.get_person_by_id('tedy'), self.bank.persons[1])



    def test_person_id_false(self):
        "Test bank returns False when personId already exist"
        input_dic = {'name':'oskar', 'id':'ted'}
        self.assertFalse(self.bank.add_persons(input_dic))



    def test_person_id_true(self):
        "Test bank returns correct personId after adding the object."
        input_dic = {'name':'oskar', 'id':'osk'}
        self.bank.add_persons(input_dic)
        self.assertEqual(self.bank.get_person_by_id('osk'), self.bank.persons[-1])



    def test_connect_false(self):
        "Test bank returns False when connection to id already exist to account"
        input_dic = {'person':'bols', 'account':'3'}
        self.assertFalse(self.bank.connect_person_account(input_dic))



    def test_connect(self):
        "Test bank returns correct id after connection with account."
        input_dic = {'person':'hum', 'account':'1'}
        self.bank.connect_person_account(input_dic)
        self.assertTrue(self.bank.get_person_by_id('hum'))


if __name__ == "__main__":
    unittest.main(verbosity=3)
