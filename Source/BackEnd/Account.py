class Account:

	#Input: account number, amount initally in account, account name, dictionary of all accounts
	#Output: account object
	#Description: creates an account object which has an account number, amount in it, account name,
	#and adds it to the account dict
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

	#Input: amount to withdraw
	#Output: nothing
	#Description: reduces the ammount of money in this account
	def withdrawMoney(self, amount) :
		if self.amount - int(amount) < 0:
			return False
		self.amount -= int(amount)
		return True

	#Input: amount to deposit
	#Output: nothing
	#Description: increases the amount of money in this account
	def depositMoney(self, amount):
		self.amount += int(amount)
		return True

	#Input: amount to transfer, the other account to put the money in
	#Output: nothing
	#Description: withdraws specified amount from this account,
	#deposits money of specified ammount in other account
	def transfer(self, amount, toAccount):
		if self.withdrawMoney(amount) :
			toAccount.depositMoney(amount)
			return True
		return False

	#Input: Name of account
	#Output: Boolean representing whether this account can be deleted
	#Description: only returns true if this account has no money and its name matches
	def canDeleteAccount(self, name) :
		if self.amount != 0:
			return False
		if self.name != name:
			return False
		return True
