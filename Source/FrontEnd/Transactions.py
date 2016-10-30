
from FrontEndValidator import FrontEndValidator

class Transactions:
    def __init__(self, transactionFile):
        self.transactionFile = transactionFile
        self.transactionList = []
        self.frontEndValidator = FrontEndValidator()


    #this appends transactions to the list representing hte transaction file, if it is of the valid form
    def appendToTransactionFile(self, transactionCode, firstAccount="00000000", secondAccount="00000000", amount="000", accountName="***"):
        if self.frontEndValidator.checkValidTransactionSummary(transactionCode, firstAccount, secondAccount, amount, accountName):
            transactionSummary = " ".join([transactionCode, firstAccount, secondAccount, amount, accountName])
            self.transactionList.append(transactionSummary)

    #This opens and writes to the actual transaction file
    def writeTransactonFile(self):
        f = open(self.transactionFile, 'w')
        for transaction in self.transactionList:
            f.write("".join(transaction) + "\n")
        f.write("ES")
        f.close()


