import pdb
from FrontEndValidator import FrontEndValidator
from ValidAccounts import ValidAccounts
from Transactions import Transactions
import os
#The session class represents a logged in session for simbank, on creation of the class
#there exists a transaction record, the valid accounts class, if the current class of session is an admin
#if the current session is ready (i.e logged in, not logged off), and if the current session is logged in
#this class contains all of the necessary calls to complete the availablec ommands exisiting in simbank

transactionCodes = {
	'delete': 'DL',
	'withdraw' : 'WD',
	'transfer' : 'TR',
	'create' : 'CR',
	'delete' : 'DL',
	'deposit' : 'DE'
}
class Session:
	#Inputs: User input (the command, ideally "login"), name of the valid account file, name of the transaction file
	#outputs: None
	#description: initilazes half of the class variables, and then checks that user logs in properly before finishing
	#the class setup, as well before accepting any other commands
	def __init__(self, userInput, accountFile, transactionFile, isRunningFromFile=False):
		self.transactionRecords = Transactions(transactionFile)
		self.frontEndValidator = FrontEndValidator()
		self.admin = None
		self.isReady = False
		self.isLoggedIn = True
                
		if userInput == "login":
			while userInput != "agent" and userInput != "atm":
                                if not isRunningFromFile:
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

	#inputs: User input (command the user entered
	#outputs: None
	#description: A large if statement with all of the command cases, given one of the valid commands calls the necessary
	#method to execute the command
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
		elif userInput == "logout":
			self.isLoggedIn = False
			self.transactionRecords.writeTransactonFile()
		else:
			print "Not a valid command"
	#Inputs: none (print statement is always "")
	#outputs: a string of a command, or an empty string if the user does not enter a command
	#description: Receieves raw input from the user so that the user can use simbank
	def getInput(self, printStatement=""):
		if len(printStatement) == 0:
			printStatement = "Enter a command : "
		userInput = raw_input(printStatement)
		if len(userInput) > 0:
			return userInput
		else:
			print "Command cannot be length 0"
		return ""

	#inputs: none
	#outputs: none
	#description: Called when the "delete" command is inputted, the method checks if the session is in admin mode,
	#and rejects the command if it is in atm mode, the program then recieves user input for the account number and name
	#and then calls another function to process the information
	def delete(self):
		if self.admin is False:
			print "Not running as atm mode!"
		else:
			accountNumber = self.getInput("Please enter account number: ")
			accountName = self.getInput("Please enter account name: ")
			self.validAccount.deleteAccount(accountNumber, accountName)
			self.transactionRecords.appendToTransactionFile(transactionCodes['delete'], firstAccount=accountNumber, accountName=accountName)

	#inputs: none
	#outputs: none
	#description: gets user account number and name to be added, then calls other methods to check the data, if the data
	#fits the requirements then the account is created with another method that is called
	def create(self):
		accountNumber = self.getInput("Please enter account number: ")
		accountName = self.getInput("Please enter account name: ")
		if self.frontEndValidator.isValidAccountNumberToCreate(accountNumber) and \
			self.frontEndValidator.isValidAccountNameToCreate(accountName) and \
				self.admin is True:
				self.validAccount.createAccount(accountName, accountNumber )
				self.transactionRecords.appendToTransactionFile(transactionCodes['create'], firstAccount=accountNumber,
														accountName=accountName)
	#inputs : none
	#outputs : none
	#description: gets account to be withdrawn from, and the ammount to be withdrawn. Throughout the method
	#various other methods are called to check that the data entered is valid

	def withdraw(self):
		accountNumber = self.getInput("Enter account number to withdraw from: ")
		if not self.frontEndValidator.checkValidAccount(self.validAccount.validAccounts, self.validAccount.invalidAccounts, accountNumber):
			print accountNumber, " is an invalid account number"
			return
		requestedAmount = self.getInput("Enter amount to withdraw: ")
		if not self.frontEndValidator.checkWithdrawAmount(int(requestedAmount) ,accountNumber, self.validAccount.amountWithdrawn, self.admin):
			print "invalid amount requested"
		else:
			self.validAccount.withdrawAmount(accountNumber, int(requestedAmount))
			self.transactionRecords.appendToTransactionFile(transactionCodes['withdraw'], firstAccount=accountNumber,
															amount=requestedAmount)

	#inputs: none
	#outputs; none
	#description: Asks for the account number to deposist to and the amount to deposist. throughout the method various other
	#methods are called to check that the data is valid
	def deposit(self):
		accountNumber = self.getInput("Enter account number to deposit to: ")
		if not self.frontEndValidator.checkValidAccount(self.validAccount.validAccounts, self.validAccount.invalidAccounts, accountNumber):
			print accountNumber, " is an invalid account number"
			return
		requestedAmount = self.getInput("Enter amount to deposit: ")
		if not self.frontEndValidator.checkValidAmount(self.admin, (int(requestedAmount))):
			print "invalid amount requested"
		else:
			self.validAccount.depositAmount(accountNumber, int(requestedAmount))
			self.transactionRecords.appendToTransactionFile(transactionCodes['deposit'], firstAccount=accountNumber, amount=requestedAmount)
			print "Amount $" + str(requestedAmount)[:-2] + "." + str(requestedAmount)[-2:] + " has been deposited"

	# inputs: none
	# outputs; none
	# description: Asks for the account number to transfer from then the account number to trabsfer ti and the amount to transfer. throughout the method various other
	# methods are called to check that the data is valid
	def transfer(self):
		accountNumberFrom = self.getInput("Enter account number to transfer from: ")
		if not self.frontEndValidator.checkValidAccount(self.validAccount.validAccounts, self.validAccount.invalidAccounts, accountNumberFrom):
			print accountNumberFrom, " is an invalid account number"
			return
		accountNumberTo = self.getInput("Enter account number to transfer to: ")
		if not self.frontEndValidator.checkValidAccount(self.validAccount.validAccounts, self.validAccount.invalidAccounts, accountNumberTo):
			print accountNumberTo, " is an invalid account number"
			return
		if accountNumberTo == accountNumberFrom:
			print "The account number entered is the same"
			return
		requestedAmount = self.getInput("Enter amount to Transfer: ")
		if not self.frontEndValidator.checkWithdrawAmount(int(requestedAmount), accountNumberFrom, self.validAccount.amountWithdrawn, self.admin):
			print "invalid amount requested"
		else:
			self.validAccount.withdrawAmount(accountNumberFrom, int(requestedAmount))
			self.transactionRecords.appendToTransactionFile(transactionCodes['transfer'], firstAccount=accountNumberFrom, secondAccount=accountNumberTo, amount=requestedAmount)
			print "Amount $" + str(requestedAmount)[:-2] + "." + str(requestedAmount)[-2:] + " has been transferred to " + accountNumberTo
