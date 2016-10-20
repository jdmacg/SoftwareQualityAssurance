import pdb
from ValidAccounts import ValidAccounts
from Transactions import Transactions
class Session:

	def __init__(self, userInput, accountFile, transactionFile):
		self.transactionRecords = Transactions(transactionFile)
		self.admin = None
		self.isReady = False

		if userInput == "login":
			while userInput != "agent" and userInput != "atm":
				userInput = self.getInput()
				if userInput != "agent" and userInput != "atm":
					print "Please enter 'atm' or 'agent'"
			self.validAccount = ValidAccounts(accountFile)
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
			self.deposit()
		elif userInput == "withdraw":
			self.withdraw()
		elif userInput == "transfer":
			self.transfer()
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
			return
		requestedAmount = self.getInput("Enter amount to withdraw")
		if not self.validAccount.checkWithdrawAmount(int(requestedAmount) ,accountNumber,self.admin):
			print "invalid amount requested"
		else:
			self.validAccount.withdrawAmount(accountNumber, int(requestedAmount))

	def deposit(self):
		accountNumber = self.getInput("Enter account number to deposit to")
		if not self.validAccount.checkValidAccount(accountNumber):
			print accountNumber, " is an invalid account number"
			return
		requestedAmount = self.getInput("Enter amount to deposit")
		if not self.validAccount.checkValidAmount(self.admin, (int(requestedAmount))):
			print "invalid amount requested"
		else:
			print "Amount $" + requestedAmount + " has been deposited"

	def transfer(self):
		accountNumberFrom = self.getInput("Enter account number to transfer from")
		if not self.validAccount.checkValidAccount(accountNumberFrom):
			print accountNumberFrom, " is an invalid account number"
			return
		accountNumberTo= self.getInput("Enter account number to transfer to")
		if not self.validAccount.checkValidAccount(accountNumberTo):
			print accountNumberTo, " is an invalid account number"
			return
		if accountNumberTo == accountNumberFrom:
			print "The account number entered is the same"
			return
		requestedAmount = self.getInput("Enter amount to Transfer")
		if not self.validAccount.checkWithdrawAmount(int(requestedAmount), accountNumberFrom, self.admin):
			print "invalid amount requested"
		else:
			self.validAccount.withdrawAmount(accountNumberFrom, int(requestedAmount))
			print "Amount $" + requestedAmount + " has been transferred to " + accountNumberTo