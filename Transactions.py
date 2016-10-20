
from FrontEndValidator import FrontEndValidator

maxLineLengthWithoutNewline = 59


class Transactions:
    def __init__(self, transactionFile):
        self.transactionFile = transactionFile
        self.transactionList = []
        self.frontEndValidator = FrontEndValidator()

    def checkValidTransactionSummary(self, transactionCode, firstAccount="00000000", secondAccount="00000000", amount="000", accountName="***"):
        if len(" ".join([transactionCode, firstAccount, secondAccount, amount, accountName])) > maxLineLengthWithoutNewline:
            return False
        if len(str(firstAccount)) != 8:
            return False
        if len(str(secondAccount)) != 8:
            return False
        if len(str(amount)) < 3 or len(str(amount)) > 8:
            return False



    #def appendToTransactionFile(self, transactionCode, firstAccount, secondAccount, amount, accountName="***"):

    def writeTransactonFile(self):
        f = open(self.transactionFile, 'w')
        for transaction in self.transactionList:
            f.write("".join(transaction) + "\n")
        f.write("ES")
        f.close()


