import unittest
import mock
import copy
from Account import Account

class TestAccount(unittest.TestCase):

    def test_createAccount_alreadyExistingAccountNumber(self):
        accountNum = "00000000"
        accountAmount = 0
        accountName = "ABC"
        accountDict = dict()

        existingAccount = Account(accountNum, accountAmount, accountName, accountDict)
        self.assertEqual(1, len(accountDict))
        expectedNumAccounts = 1

        copyAccount = Account(accountNum, accountAmount, accountName, accountDict)
        self.assertEqual(expectedNumAccounts, len(accountDict))


    def test_createAccount_amountLessThanZero(self):
        accountNum = "00000000"
        accountAmount = -1
        accountName = "ABC"
        accountDict = dict()

        expectedNumAccounts = 0

        newAccount = Account(accountNum, accountAmount, accountName, accountDict)
        self.assertEqual(expectedNumAccounts, len(accountDict))


if __name__ == '__main__':
    unittest.main()