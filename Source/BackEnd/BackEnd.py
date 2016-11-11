from Account import Account
import os.path

class BackEnd:

	#Input: None
	#Output: The Backend Object
	#Description: Reads in the Master Account List and Merged Transaction Summary File
	#Into a dictionary containing account objects
	def __init__(self):
		self.accountIdx = 0
		self.amountIdx = 1
		self.nameIdx = 2
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
			masterLineToWrite = str(account.account) + " " + str(account.amount) + " " + str(account.name)
			masterAccountListFile.write(masterLineToWrite)
			validLineToWrite = str(account.account)
			validAccountsListFile.write(validLineToWrite)
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
		transactionCode = lineData[0]
		accountTo = lineData[1]
		accountFrom = lineData[2]
		amount = lineData[3]
		name = lineData[4]
		if self.accountDict.has_key(accountTo):
			if transactionCode == "DL":
				if self.accountDict[accountTo].canDeleteAccount(name):
					del self.accountDict[accountTo]
				else:
					print "Incorrect name or account does not exist"
			elif transactionCode == "TR":
				if self.accountDict.has_key(accountFrom):
					if not self.accountDict[accountFrom].transfer(amount, self.accountDict[accountTo]):
						print "Error Transferring"
				else:
					print "Error Transferring"
			elif transactionCode == "WD":
				if not self.accountDict[accountTo].withdrawMoney(amount):
					print "Withdraw error"
			elif transactionCode == "DE":
				if not self.accountDict[accountTo].depositMoney(amount)
					print "Deposit error"
		else:
			if transactionCode == "CR":
				wasCreated = Account(accountTo, amount, name, self.accountDict).isCreated


backEnd = BackEnd()
backEnd.readMergedFile()

