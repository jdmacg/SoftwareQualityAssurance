import unittest
import mock
import copy
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
	self.assertFalse(didWithdraw)

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
        self.assertEqual(initialAmount, account.amount)
        self.assertFalse(didWithdraw)
		
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
        self.assertEqual(initialAmount, account.amount)
        self.assertFalse(didWithdraw)

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

if __name__ == '__main__':
    unittest.main()

