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
			userInput = raw_input("Enter account number")
		elif userInput == "delete":
			print "call delete function"
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

	def delete(self, userInput):
		if self.admin is False:
			print "Not running as atm mode!"

	"""def createAccount(self, accountNumber, accountName):
        if len(str(accountNumber)) != 8:
            print "Must be exactly 8 digits"
            return False
        elif str(accountNumber)[0] == "0":
            print "Numbers cannot start with 0"
            return False
        elif len(accountName) > 30 or len(accountName) < 3:
            print "Account name must be between 3-30 digits"
            return False
        elif accountName[0] == " " or accountName[len(accountName)] == " ":
            print "Account name cannot start or end with a space"
            return False
        if self.checkValidAccount(accountNumber) == True:
            print "Account number already exists"
            return False
        else:
            self.createdAccounts[accountNumber] = accountName
            return True"""



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

