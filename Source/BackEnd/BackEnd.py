from Account import Account

class BackEnd:

    def __init__(self):
        self.accountIdx = 0
        self.amountIdx = 1
        self.nameIdx = 2
        self.masterAccountListName = "MasterAccountList.txt"
        self.accountDict = self.readAccountListFromFile()

    def readAccountDictFromFile(self):
        accountDict = dict()
        masterAccountListFile = open(self.masterAccountListName)
        for line in masterAccountListFile.read():
            lineData = line.split()
            account = lineData[self.accountIdx]
            amount = int(lineData[self.amountIdx])
            name = lineData[self.nameIdx]
            wasCreated = Account(account, amount, name, accountDict).isCreated
        masterAccountListFile.close()
        return accountDict




backEnd = BackEnd()
backEnd.readMergedFile()

