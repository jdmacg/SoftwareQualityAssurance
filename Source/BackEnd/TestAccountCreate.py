import unittest
import mock
import copy
from Account import Account

class TestAccountCreate(unittest.TestCase):

    def test_createAccount_newValidAccount(self):
        accountNum = "00000000"
        accountAmount = 100
        accountName = "ABC"
        allAccounts = dict()

        expectedNumAccountsBeforeCreate = 0
        self.assertEqual(expectedNumAccountsBeforeCreate, len(allAccounts))
        newAccount = Account(accountNum, accountAmount, accountName, allAccounts)
        expectedNumAccountsAfterCreate = 1
        self.assertEqual(expectedNumAccountsAfterCreate, len(allAccounts))


    def test_createAccount_alreadyExistingAccountNumber(self):
        accountNum = "00000000"
        accountAmount = 0
        accountName = "ABC"
        allAccounts = dict()

        existingAccount = Account(accountNum, accountAmount, accountName, allAccounts)
        expectedNumAccounts = 1
        self.assertEqual(expectedNumAccounts, len(allAccounts))
        copyAccount = Account(accountNum, accountAmount, accountName, allAccounts)
        self.assertEqual(expectedNumAccounts, len(allAccounts))


    def test_createAccount_amountLessThanZero(self):
        accountNum = "00000000"
        accountAmount = -1
        accountName = "ABC"
        allAccounts = dict()

        expectedNumAccounts = 0
        self.assertEqual(expectedNumAccounts, len(allAccounts))
        newAccount = Account(accountNum, accountAmount, accountName, allAccounts)
        self.assertEqual(expectedNumAccounts, len(allAccounts))



if __name__ == '__main__':
    unittest.main()