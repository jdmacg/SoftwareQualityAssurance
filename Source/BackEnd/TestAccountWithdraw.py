import unittest
import mock
import copy
from Account import Account

class TestAccountCreate(unittest.TestCase):

    def test_withdrawAmount_lessThanZero(self):
        initialAmount = 10000
        accountNum = "00000000"
        accountAmount = initialAmount
        accountName = "ABC"
        allAccounts = dict()
        account = Account(accountNum, accountAmount, accountName, allAccounts)

        self.assertEqual(initialAmount, account.amount)
        amountToWithdraw = -100
        didWithdraw = account.withdrawMoney(amountToWithdraw)
        self.assertEqual(initialAmount, account.amount)
        self.assertFalse(didWithdraw)


if __name__ == '__main__':
    unittest.main()

