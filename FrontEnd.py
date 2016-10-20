#the main file of the front end
from Session import Session


while True:
	userInput = raw_input("Enter a command : ")
	session = Session(userInput)
	if session.isReady is True:
		break



while userInput != "logout":
	userInput = raw_input("Enter a command : ")
	session.runCommand(userInput)


