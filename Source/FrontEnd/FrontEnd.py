'''The front end of simbank
The intention of this program is to ensure that users input proper values into the simbank application
If a user attempts to input incorrect values, or access commands they do not have the privillage to,
the program will stop them. The program requires an input of a valid accounts list, which is read on a sucessful logon
and then lines of text can be inputted into the program. The program outputs a daily transaction file which holds
all of the transactions that were executed within a session.
The program is intended to be ran with a text file "ValidAccounts.txt", and is intended to user terminal input, but if
pipelined a textfile through the terminal as long as the commands are correct the program will also run as intended.
'''
from Session import Session
import os

import sys
accountsIndex = 1
transactionIndex = 2
testFileIndex = 3

#accountsFile = open(sys.argv[accountsIndex])
#transactionFile = open(sys.argv[transactionIndex])
transactionFile = "TransactionSummary.txt"
accountsFile = "ValidAccounts.txt"
testFile = ""

runFromTextFile = False
if len(sys.argv) > 1:
	runFromTextFile = True

if runFromTextFile:
	#until a logon is sucessful the following loop will continue to run
	while True:
		userInput = raw_input("Enter a command : ")
		session = Session(userInput, accountsFile, transactionFile)
		if session.isReady is True:
			break
	print("Welcome!")

	#until the user gives the logout command the following loop for inputs will be run
	while session.isLoggedIn is True:
		userInput = session.getInput()
		session.runCommand(userInput)

else:
	testFile = open(sys.argv[1])
	testData = testFile.readlines()
	print testData
	lineIdx = 0
	while True:
		print "Enter a command : "
		userInput = testData[lineIdx]
		lineIdx += 1
		session = Session(userInput, accountsFile, transactionFile)
		if session.isReady is True:
			break
	print("Welcome!")

	while session.isLoggedIn is True:
		userInput = session.getInput(testData[lineIdx])
		lineIdx += 1
		session.runCommand(userInput)




