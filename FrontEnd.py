#the main file of the front end
from Session import Session

import sys
accountsIndex = 1
transactionIndex = 2

#accountsFile = open(sys.argv[accountsIndex])
#transactionFile = open(sys.argv[transactionIndex])
transactionFile = "TransactionSummary.txt"
accountsFile = "ValidAccounts.txt"

while True:
	userInput = raw_input("Enter a command : ")
	session = Session(userInput, accountsFile, transactionFile)
	if session.isReady is True:
		break
print("Welcome!")


while session.isLoggedIn is True:
	userInput = session.getInput()
	session.runCommand(userInput)

