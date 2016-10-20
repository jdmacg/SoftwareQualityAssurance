import fileinput
class ValidAccounts:

    def __init__(self, fileName):
        self.validAccounts = []
        self.ammountWithdrawn = dict()
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

    def withdrawAmount(self,accountNumber,amount):
        if self.admin == False:
            temp = amount + self.amountWithdrawn[accountNumber];
            if temp < 100000:
                print "Amount" + amount + " sucessfully withdrawn"
            else:
                print "You have exceeded the amount allowed to withdrawn in the session"
                return False
        self.ammountWithdrawn[accountNumber] += amount;
        return True

    def createAccount(self, accountNumber, accountName):
        if len(str(accountNumber)) != 8:
            print "Must be exactly 8 digits"
            return False
        elif str(accountNumber)[0] == "0":
            print "Numbers cannot start with 0"
            return False
        elif len(accountName) > 30 or len(accountName) < 3:
            print "Account name must be between 3-30 digits"
            return False
        elif accountName[0] == " " or accountName[len(accountName)] == " ":
            print "Account name cannot start or end with a space"
            return False
        if self.checkValidAccount(accountNumber) == True:
            print "Account number already exists"
            return False
        else:
            self.createdAccounts[accountNumber] = accountName
            return True

    def deleteAccount(self, accountNumber, accountName):
        for i in self.validAccounts:
            if i == accountNumber:
                del self.validAccounts[i]
                print "Account deleted"
                self.invalidAccounts[accountNumber] = accountName
                return True

        print "Account does not exist"
        return False