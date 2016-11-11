class Account:
	def __init__(self, account, amount, name, accountDict):
		self.isCreated = True
		if accountDict.has_key(account):
			self.isCreated = False
		elif amount < 0:
			self.isCreated = False
		else:
			self.account = account
			self.amount = amount
			self.name = name
			accountDict[account] = self

	def withdrawMoney(self, amount) :
		if self.amount - amount < 0:
			return False
		self.amount -= amount
		return True

	def depositMoney(self, amount) :
		self.amount += amount
		return True

	def transfer(self, amount, toAccount):
		if self.withdrawMoney(amount) :
			self.depositMoney(toAccount,amount)
			return True
		return False

	def canDeleteAccount(self, name) :
		if self.amount != 0:
			return False
		if self.name != name:
			return False
		return True
