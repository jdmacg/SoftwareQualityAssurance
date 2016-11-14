from Account import Account
import os.path
import pdb

#Nicholas Petrielli 10107308
#Andrew Storus 		10103737
#Jordan McGregor 	10052770
#The intention of this program is to implement a backend of a banking system.
#The backend reads in the input files given which are a merged transaction summary file and a master account list.
#After setting up all of the accounts in the master account list file all of the transactions from the merged transaction summary file are applied
#Upon completion the program outputs a new updated master account list file, as well as a valid account list file.
#The program is intended to be ran with the master account list file as well as the merged transaction summary file to be in the same
#directory as the python file. The accounts should be named MasterAccountList.txt and MergedTransactionSummaryFile.txt to
#represent the master account list and the merged transaction summary file respectively.

class BackEnd:

    #Input: None
    #Output: The Backend Object
    #Description: Reads in the Master Account List and Merged Transaction Summary File
    #Into a dictionary containing account objects
    def __init__(self):
        self.accountIdx = 0
        self.amountIdx = 1
        self.nameIdx = 2
        self.transactionIdx = 0
        self.accountToIdx = 1
        self.accountFromIdx = 2
        self.amountDataIdx = 3
        self.nameDataIdx = 4
        self.masterAccountListName = "MasterAccountList.txt"
        self.mergedTransactionSummaryFileName = "MergedTransactionSummaryFile.txt"
        self.validAccountsFile = "ValidAccountsFile.txt"
        self.accountDict = self.readAccountDictFromFile()

    #Input: Old Master Account List File
    #Output: Dictionary of account objects indexed by account number
    #Description: Parses the master account list file into a dictionary
    def readAccountDictFromFile(self):
        accountDict = dict()
        if os.path.exists(self.masterAccountListName):
            masterAccountListFile = open(self.masterAccountListName, 'r')
            for line in masterAccountListFile.readlines():
                lineData = line.split()
                account = lineData[self.accountIdx]
                amount = int(lineData[self.amountIdx])
                name = lineData[self.nameIdx]
                wasCreated = Account(account, amount, name, accountDict).isCreated
            masterAccountListFile.close()
        return accountDict

    #Input: Dictionary of all accounts
    #Output: New Master Account List File
    #Description: Formats all the accounts at the end of a backend session into a text file
    def writeAccountsFiles(self):
        masterAccountList = []
        for key in self.accountDict:
            masterAccountList.append(self.accountDict[key])

        masterAccountList = sorted(masterAccountList, key=lambda x: x.account)
        masterAccountListFile = open(self.masterAccountListName, 'w+')
        validAccountsListFile = open(self.validAccountsFile, 'w+')
        for account in masterAccountList:
            masterLineToWrite = str(account.account) + " " + str(account.amount) + " " + str(account.name) + "\n"
            masterAccountListFile.writelines(masterLineToWrite)
            validLineToWrite = str(account.account) + "\n"
            validAccountsListFile.writelines(validLineToWrite)
        masterAccountListFile.close()
        validAccountsListFile.close()

    #Input: Merged Transaction Summary File
    #Output: None
    #Description: Reads Merged Transaction Summary File, updates the accounts dictionary
    #based on the contents of the transaction summary file
    def readMergedFile(self):
        transactionSummaryFile = open(self.mergedTransactionSummaryFileName)
        transactionSummaryFileData = transactionSummaryFile.readlines()
        idx = 0
        while idx < len(transactionSummaryFileData):
            lineData = transactionSummaryFileData[idx].split()
            if len(lineData) == 5:
                self.transactionCodeChooser(lineData)
            idx += 1

        if transactionSummaryFileData[-1].split()[0] == "ES":
            self.writeAccountsFiles()
        else:
            print "The merged transaction summary file is invalid"

    #Input: Parsed line from merged transaction summary file
    #Output: Updated accounts Dictionary
    #Description: Based on the contents of the merged transaction summary file line,
    #update the accounts dict to reflect the command
    def transactionCodeChooser(self, lineData):
        transactionCode = lineData[self.transactionIdx]
        accountTo = lineData[self.accountToIdx]
        accountFrom = lineData[self.accountFromIdx]
        amount = lineData[self.amountDataIdx]
        name = lineData[self.nameDataIdx]
        if self.accountDict.has_key(accountTo):
            if transactionCode == "DL":
                if self.accountDict[accountTo].canDeleteAccount(name):
                    del self.accountDict[accountTo]
                else:
                    print "Incorrect name or account does not exist"
            elif transactionCode == "TR":
                if self.accountDict.has_key(accountFrom):
                    if not self.accountDict[accountTo].transfer(amount, self.accountDict[accountFrom]):
                        print "Error Transferring"
                else:
                    print "Error Transferring"
            elif transactionCode == "WD":
                if not self.accountDict[accountTo].withdrawMoney(amount):
                    print "Withdraw error"
            elif transactionCode == "DE":
                if not self.accountDict[accountTo].depositMoney(amount):
                    print "Deposit error"
        else:
            if transactionCode == "CR":
                wasCreated = Account(accountTo, amount, name, self.accountDict).isCreated


backEnd = BackEnd()
backEnd.readMergedFile()

