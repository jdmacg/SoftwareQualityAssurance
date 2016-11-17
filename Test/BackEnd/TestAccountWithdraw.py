import unittest
import mock
import copy
import os
import sys
testdir = os.path.dirname(os.path.abspath(os.pardir))
srcdir = [dir for dir in os.listdir(testdir) if "Source" in dir][0]
srcdir = os.path.abspath(os.path.join(testdir, srcdir))
backend = [dir for dir in os.listdir(srcdir) if "BackEnd" in dir][0]
backend = os.path.abspath(os.path.join(srcdir, backend))

sys.path.append(backend)
from Account import Account

class TestAccountCreate(unittest.TestCase):

    def test_withdrawAmount_lessThanZero(self):
        initialAmount = 10000
        accountNum = "00000001"
        accountAmount = initialAmount
        accountName = "ABC"
        allAccounts = dict()
        account = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(initialAmount, account.amount)
        amountToWithdraw = -100
        didWithdraw = account.withdrawMoney(amountToWithdraw)
        self.assertEqual(initialAmount, account.amount)
        self.assertFalse(didWithdraw)
    def test_withdrawAmount_equalToZero(self):
	initialAmount = 1000
	accountNum = "00000001"
	accountAmount = initialAmount
	accountName = "ABC"
	allAccounts = dict()
	account = Account(accountNum, accountAmount, accountName, allAccounts)
	
	self.assertEqual(initialAmount,account.amount)
	amountToWithdraw = 0
	didWithdraw = account.withdrawMoney(amountToWithdraw)
	self.assertEqual(initialAmount, account.amount)
	self.assertTrue(didWithdraw)

    def test_withdrawAmount_LessThan1000(self):
        initialAmount = 1000
        accountNum = "00000001"
        accountAmount = initialAmount
        accountName = "ABC"
        allAccounts = dict()
        account = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(initialAmount,account.amount)
        amountToWithdraw = 100
        didWithdraw = account.withdrawMoney(amountToWithdraw)
        self.assertEqual(initialAmount-amountToWithdraw, account.amount)
        self.assertTrue(didWithdraw)
		
    def test_withdrawAmount_LessThan99999999(self):
        initialAmount = 50000000
        accountNum = "00000001"
        accountAmount = initialAmount
        accountName = "ABC"
        allAccounts = dict()
        account = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(initialAmount,account.amount)
        amountToWithdraw = 1000000
        didWithdraw = account.withdrawMoney(amountToWithdraw)
        self.assertEqual(initialAmount-amountToWithdraw, account.amount)
        self.assertTrue(didWithdraw)

    def test_withdrawAmount_moreThan99999999(self):
        initialAmount = 1000
        accountNum = "00000001"
        accountAmount = initialAmount
        accountName = "ABC"
        allAccounts = dict()
        account = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(initialAmount,account.amount)
        amountToWithdraw = 100000000
        didWithdraw = account.withdrawMoney(amountToWithdraw)
        self.assertEqual(initialAmount, account.amount)
        self.assertFalse(didWithdraw)

    def test_withdrawAmount_moreThanBalance(self):
        initialAmount = 100
        accountNum = "00000001"
        accountAmount = initialAmount
        accountName = "ABC"
        allAccounts = dict()
        account = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(initialAmount,account.amount)
        amountToWithdraw = 1000
        didWithdraw = account.withdrawMoney(amountToWithdraw)
        self.assertEqual(initialAmount, account.amount)
        self.assertFalse(didWithdraw)

if __name__ == '__main__':
    unittest.main()

