#the main file of the front end
from Session import Session
userInput = "doesntMatter"

newSession = Session.logInPage(input("Enter a command : "))
print("Welcome")

while userInput != "logout":
	userInput = input("Enter a command : ")
	newSession.command(userInput)


