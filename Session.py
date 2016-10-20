class Session:
	def __init__(self,isAdmin):
		self.admin = isAdmin
	
	def command(self,userInput):
		if userInput == "create" and self.admin == 1:
			userInput = input("Enter account number")
		elif userInput == "delete" and self.admin == 1:
			print("hi")
		elif userInput == "deposit":
			print("hi")
		elif userInput == "withdraw":
			print("hi")
		elif userInput == "transfer":
			print("hi")
	
	
	def logInPage(userInput):
		while userInput != "agent" and userInput != "atm":
			while userInput != "login":
				userInput = input("Enter a command : ")
			userInput = input("Which mode : ")	
			if userInput == "agent":
				return Session(1)
			else:
				return Session(0)
	
	def checkValidAmount(self,amount):
		if self.admin == 1 and amount < 99999999 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
			return 1
		else:
			return 0
		if self.admin == 0 and amount < 1000 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
			return 1
		else:
			return 0
