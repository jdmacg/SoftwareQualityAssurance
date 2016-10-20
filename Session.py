from ValidAccounts import ValidAccounts
class Session:

	def __init__(self, userInput, accountFile, transactionFile):
	    self.validAccount = ValidAccounts(accountFile)
	    self.transactionRecords = Transactions(transactionFile)
		self.admin = None
		self.isReady = False
		
		if userInput == "login":
		#self.amount = 0

			while userInput != "agent" and userInput != "atm":
				userInput = self.getInput()
				if userInput != "agent" and userInput != "atm":
					print "Please enter 'atm' or 'agent'"
			if userInput == "agent":
				self.admin = False
				self.isReady = True
			elif userInput == "atm" :
				self.admint = True
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
			print "call withdraw function"
		elif userInput == "transfer":
			print "call trasnfer function"
		else:
			print "Not a valid command"

	def getInput(self):
		userInput = raw_input("Enter a command : ")
		if len(userInput) > 0:
			return userInput
		else:
			print "Command cannot be length 0"
		return ""

	def delete(self, userInput):
		if self.admin is False:
			print "Not running as atm mode!"


	def checkValidAmount(self,amount):
		if self.admin == 1 and amount < 99999999 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
			return 1
		else:
			return 0
		if self.admin == 0 and amount < 1000 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
			return 1
		else:
			return 0
			
    def withdraw(self):
        accountNumber = self.getInput("Enter account number to withdraw from")
        while not self.validAccount.checkAccount(accountNumber): 
            print accountNumber, " is an invalid account number
            accountNumber = self.getInput("Enter account number to withdraw from")
        requestedAmount = self.getInput("Enter amount to withdraw")
        if not self.validAccount.checkWithdrawAmount(requestedAmount,accountNumber,self.admin):
            print "invalid amount requested"
        else:
            self.validAccount.withdrawAmount(requestedAmount,accountNumber)
            
            
            
        
        
            
        
            
        
        
