import unittest
import mock
import copy
from Account import Account

class TestAccount(unittest.TestCase):

    def test_createAccount_alreadyExistingAccountNumber(self):
        accountNum = "00000000"
        accountAmount = 0
        accountName = "A"
        accountDict = dict()

        existingAccount = Account(accountNum, accountAmount, accountName, accountDict)
        self.assertEqual(1, len(accountDict))
        numAccounts = 1

        copyAccount = Account(accountNum, accountAmount, accountName, accountDict)
        self.assertEqual(numAccounts, len(accountDict))


    

