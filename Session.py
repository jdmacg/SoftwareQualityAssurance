import pdb
from ValidAccounts import ValidAccounts
from Transactions import Transactions
class Session:

	def __init__(self, userInput, accountFile, transactionFile):
		self.validAccount = ValidAccounts(accountFile)
		self.transactionRecords = Transactions(transactionFile)
		self.admin = None
		self.isReady = False

		if userInput == "login":
			while userInput != "agent" and userInput != "atm":
				userInput = self.getInput()
				if userInput != "agent" and userInput != "atm":
					print "Please enter 'atm' or 'agent'"
			if userInput == "agent":
				self.admin = True
				self.isReady = True
			elif userInput == "atm" :
				self.admin = False
				self.isReady = True
		else:
			print "You must log in using 'login' command"
		
	def runCommand(self,userInput):
		if userInput == "create":
			self.create()
		elif userInput == "delete":
			self.delete()
		elif userInput == "deposit":
			print "call deposit function"
		elif userInput == "withdraw":
			self.withdraw()
		elif userInput == "transfer":
			print "call trasnfer function"
		else:
			print "Not a valid command"

	def getInput(self, printStatement=""):
		if len(printStatement) == 0:
			printStatement = "Enter a command : "
		userInput = raw_input(printStatement)
		if len(userInput) > 0:
			return userInput
		else:
			print "Command cannot be length 0"
		return ""

	def delete(self):
		if self.admin is False:
			print "Not running as atm mode!"
		else:
			accountNumber = self.getInput("Please enter account number: ")
			accountName = self.getInput("Please enter account name: ")
			self.validAccount.deleteAccount(accountNumber, accountName)


	def create(self):
		accountNumber = self.getInput("Please enter account number: ")
		accountName = self.getInput("Please enter account name: ")

		if self.validAccount.isValidAccountNumberToCreate(accountNumber) and \
			self.validAccount.isValidAccountNameToCreate(accountName):
				self.validAccount.createAccount(accountName, accountNumber )

	def withdraw(self):
		accountNumber = self.getInput("Enter account number to withdraw from")
		if not self.validAccount.checkValidAccount(accountNumber):
			print accountNumber, " is an invalid account number"
			accountNumber = self.getInput("Enter account number to withdraw from")
		requestedAmount = self.getInput("Enter amount to withdraw")
		if not self.validAccount.checkWithdrawAmount(int(requestedAmount) ,accountNumber,self.admin):
			print "invalid amount requested"
		else:
			self.validAccount.withdrawAmount(accountNumber, int(requestedAmount))

