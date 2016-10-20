class Session:

	def __init__(self, userInput):
		self.admin = None
		self.isReady = False
		if userInput.strip() == "login":
			while userInput.strip() != "agent" and userInput.strip() != "atm":
				userInput = raw_input("Enter a command : ")
				if userInput.strip() != "agent" and userInput.strip() != "atm":
					print "Please enter 'atm' or 'agent'"
			if userInput.strip() == "agent":
				self.admin = False
				self.isReady = True
			elif userInput.strip() == "atm" :
				self.admint = True
				self.isReady = True
		else:
			print "You must log in using 'login' command"
		
	def runCommand(self,userInput):
		if userInput == "create" and self.admin == 1:
			userInput = raw_input("Enter account number")
		elif userInput == "delete" and self.admin == 1:
			print("hi")
		elif userInput == "deposit":
			print("hi")
		elif userInput == "withdraw":
			print("hi")
		elif userInput == "transfer":
			print("hi")

	def checkValidAmount(self,amount):
		if self.admin == 1 and amount < 99999999 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
			return 1
		else:
			return 0
		if self.admin == 0 and amount < 1000 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
			return 1
		else:
			return 0
