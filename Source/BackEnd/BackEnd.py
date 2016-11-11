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
		masterAccountListFile = open(self.masterAccountListName, 'r')
		for line in masterAccountListFile.read():
			lineData = line.split()
			account = lineData[self.accountIdx]
			amount = int(lineData[self.amountIdx])
			name = lineData[self.nameIdx]
			wasCreated = Account(account, amount, name, accountDict).isCreated
		masterAccountListFile.close()
		return accountDict

	def writeMasterAccountList(self):
		masterAccountList = []
		for key in self.accountDict:
			masterAccountList.append(self.accountDict[key])

		masterAccountList = sorted(masterAccountList, key=lambda x: x.account)
		masterAccountListFile = open(self.masterAccountListName, 'w')
		for account in masterAccountList:
			lineToWrite = str(account.account) + " " + str(account.amount) + " " + str(account.name)
			masterAccountListFile.write(lineToWrite)
		masterAccountListFile.close()

	def readMergedFile(self):
		transactionSummaryFile = open(self.mergedTransactionSummaryFileName)
		for line in transactionSummaryFile.read():
			lineData = line.split()
			self.transactionCodeChooser(lineData)
		if lineData[0] == "ES":
			self.writeMasterAccountList()
		else:
			print "The merged transaction summary file is invalid"

	def transactionCodeChooser(self,lineData):
		transactionCode = lineData[0]
		if transactionCode == "CR":
			account = lineData[1]
			name = lineData[2]
			amount = 0
			wasCreated = Account(account, amount, name, self.accountDict).isCreated
		elif transactionCode == "DL":
			account = lineData[1]
			name = lineData[2]
			if self.accountDict[account].canDeleteAccount(name):
				del self.accountDict[account]
			else:
				print "Incorrect name or account does not exist"
		elif transactionCode == "TR":
			accountTo = lineData[1]
			accountFrom = lineData[2]
			amount = lineData[3]
			if not self.accountDict[accountFrom].transfer(amount,accountTo):
				print "Error transfering"
		elif transactionCode == "WD":
			account = lineData[1]
			amount = lineData[2]
			if not self.accountDict[account].withdrawMoney(amount):
				print "Withdraw error"
		elif transactionCode == "DE":
			account = lineData[1]
			amount = lineData[2]
			self.accountDict[account].depositMoney(amount)




backEnd = BackEnd()
backEnd.readMergedFile()

