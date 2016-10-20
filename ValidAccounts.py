import fileinput
import pdb
from FrontEndValidator import FrontEndValidator

#This class contains all of the valid, as well as invalid, accounts for a given session
#The class is iniated with a file name which is the name of valid accounts text file
#this class holds all data related to bank accounts
class ValidAccounts:
    #the initiation method, called when the class is created.
    #inputs: File name
    #outputs: None
    #Description: Initializes various array's for use later in the program, and then reads the valid account text file
    #inputting all of the accounts in an array, it also checks for the account number constraints, as well as that the
    #last account number in the file is "00000000", if incorrect values are given it will print an "error" statement
    #but for debugging purposes this is just a textstatement currently
    def __init__(self, fileName):
        self.validAccounts = []
        self.amountWithdrawn = dict()
        self.amountDeposited = dict()
        self.createdAccounts = dict()
        self.invalidAccounts = dict()
        self.frontEndValidator = FrontEndValidator()
        f = open(fileName,"r")
        endsWithZeros = False
        for line in f.read().split():
            if line == "00000000" :
                endsWithZeros = True
                break
            if len(str(line)) != 8:
                print("this should not happen, throw an error because wrong input")
            elif str(line)[0] == "0":
                pdb.set_trace()
                print("Numbers cannot start with 0");
            else:
                self.validAccounts.append(line)
                self.amountWithdrawn[line] = 0
                self.amountDeposited[line] = 0
        f.close()
        if endsWithZeros == False:
            print("Throw an error, the valid accounts file is not proper")
        else:
            print("Valid accounts file has been sucessfully loaded.")

    #inputs: Account number and Account name of the account to be added
    #outputs: None
    #description: Adds the account name and number to a dictonary of created accounts during the session
    def createAccount(self, accountName, accountNumber):
        self.createdAccounts[accountNumber] = accountName

    #inputs: account number of the account withdrawing, amount the account is withdrawing
    #outputs: none
    #description: This adds the amount an account has withdrawn in a given session
    def withdrawAmount(self,accountNumber,amount):
        self.amountWithdrawn[accountNumber] += amount;

    #same as withdraw, but applied to amountDeposited dictonary
    def depositAmount(self, accountNumber, amount):
        self.amountDeposited[accountNumber] += amount

    # inputs: Account number to be deleted, account name for reference in the transaction file
    # outputs: True/false, true means that the account was deleted
    # description: If the account is a valid account and the login is in agent mode the account is deleted and added
    # to an invalid accounts list (for use of checking valid accounts as well as writing to the transaction summary file)
    def deleteAccount(self, accountNumber, accountName):
        for i in range(len(self.validAccounts)):
            if self.validAccounts[i] == accountNumber:
                del self.validAccounts[i]
                print "Account deleted"
                self.invalidAccounts[accountNumber] = accountName
                return True

        print "Account does not exist"
        return False