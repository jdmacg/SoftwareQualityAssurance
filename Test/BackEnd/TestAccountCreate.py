import unittest
import copy
import sys
import os

testdir = os.path.dirname(os.path.abspath(os.pardir))
srcdir = [dir for dir in os.listdir(testdir) if "Source" in dir][0]
srcdir = os.path.abspath(os.path.join(testdir, srcdir))
backend = [dir for dir in os.listdir(srcdir) if "BackEnd" in dir][0]
backend = os.path.abspath(os.path.join(srcdir, backend))

sys.path.append(backend)
from Account import Account


class TestAccountCreate(unittest.TestCase):

    def test_createAccount_newValidAccount(self):
        accountNum = "00000001"
        accountAmount = 0
        accountName = "Valid"
        allAccounts = dict()

        expectedNumAccountsBeforeCreate = 0
        self.assertEqual(expectedNumAccountsBeforeCreate, len(allAccounts))
        newAccount = Account(accountNum, accountAmount, accountName, allAccounts)
        expectedNumAccountsAfterCreate = 1

        self.assertEqual(expectedNumAccountsAfterCreate, len(allAccounts))
        self.assertTrue(newAccount.isCreated)


    def test_createAccount_alreadyExistingAccountNumber(self):
        accountNum = "00000001"
        accountAmount = 0
        validAccountName = "Valid"
        invalidAccountName = "Invalid"
        allAccounts = dict()

        existingAccount = Account(accountNum, accountAmount, validAccountName, allAccounts)
        expectedNumAccounts = 1
        self.assertEqual(expectedNumAccounts, len(allAccounts))
        copyAccount = Account(accountNum, accountAmount, invalidAccountName, allAccounts)

        self.assertEqual(expectedNumAccounts, len(allAccounts))
        self.assertTrue(existingAccount.isCreated)
        self.assertFalse(copyAccount.isCreated)
        self.assertEqual(validAccountName, allAccounts.pop(accountNum).name)


    def test_createAccount_amountLessThanZero(self):
        accountNum = "00000001"
        accountAmount = -100
        accountName = "Invalid"
        allAccounts = dict()

        expectedNumAccounts = 0
        self.assertEqual(expectedNumAccounts, len(allAccounts))
        newAccount = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(expectedNumAccounts, len(allAccounts))
        self.assertFalse(newAccount.isCreated)



if __name__ == '__main__':
    unittest.main()
