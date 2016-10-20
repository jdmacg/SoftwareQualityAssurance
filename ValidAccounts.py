import fileinput
import pdb
from FrontEndValidator import FrontEndValidator

class ValidAccounts:

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


    def createAccount(self, accountName, accountNumber):
        self.createdAccounts[accountNumber] = accountName

    def withdrawAmount(self,accountNumber,amount):
        self.amountWithdrawn[accountNumber] += amount;

    def depositAmount(self, accountNumber, amount):
        self.amountDeposited[accountNumber] += amount

    def deleteAccount(self, accountNumber, accountName):
        for i in range(len(self.validAccounts)):
            if self.validAccounts[i] == accountNumber:
                del self.validAccounts[i]
                print "Account deleted"
                self.invalidAccounts[accountNumber] = accountName
                return True

        print "Account does not exist"
        return False