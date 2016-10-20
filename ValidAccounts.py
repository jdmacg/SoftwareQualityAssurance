import fileinput
import pdb
class ValidAccounts:

    def __init__(self, fileName):
        self.validAccounts = []
        self.amountWithdrawn = dict()
        self.createdAccounts = dict()
        self.invalidAccounts = dict()
        f = open(fileName,"r")
        endsWithZeros = False
        for line in f.read().split():
            if line == "00000000" :
                endsWithZeros = True
                break
            if len(str(line)) != 8:
                print("this should not happen, throw an error because wrong input")
            elif str(line)[0] == "0":
                print("Numbers cannot start with 0");
            else:
                self.validAccounts.append(line)
                self.amountWithdrawn[line] = 0
        f.close()
        if endsWithZeros == False:
            print("Throw an error, the valid accounts file is not proper")
        else:
            print("Valid accounts file has been sucessfully loaded.")

    def checkValidAccount(self, accountChecking):
        for key in self.invalidAccounts:
            if accountChecking == key:
                return False
        for existingAccounts in self.validAccounts :
            if existingAccounts == accountChecking:
                return True
        return False

    def checkValidAmount(self, isAdmin, amount):
        if isAdmin == True:
            if amount < 99999999 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
                return True
            else:
                return False
        if isAdmin == False:
            if amount < 100000 and amount > 0 and len(str(amount)) >= 3 and len(str(amount)) <= 8:
                return True
            else:
                return False


    def checkWithdrawAmount(self, withdrawAmount, accountNumber , isAdmin):
        if not self.checkValidAmount(isAdmin, withdrawAmount):
            return False
        if isAdmin == False:
            if withdrawAmount > 100000:
                return False
            temp = withdrawAmount + self.amountWithdrawn[accountNumber];
            if temp < 100000:
                print "Amount" + str(withdrawAmount) + " sucessfully withdrawn"
            else:
                print "You have exceeded the amount allowed to withdrawn in the session"
                return False
        return True


    def withdrawAmount(self,accountNumber,amount):
        self.amountWithdrawn[accountNumber] += amount;

    def deleteAccount(self, accountNumber, accountName):
        for i in self.validAccounts:
            if i == accountNumber:
                del self.validAccounts[i]
                print "Account deleted"
                self.invalidAccounts[accountNumber] = accountName
                return True

        print "Account does not exist"
        return False