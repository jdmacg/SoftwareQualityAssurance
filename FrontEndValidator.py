
class FrontEndValidator:

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

    def checkValidAccount(self, validAccounts, invalidAccounts, accountChecking):
        for key in invalidAccounts:
            if accountChecking == key:
                return False
        for existingAccounts in validAccounts :
            if existingAccounts == accountChecking:
                return True
        return False

    def checkWithdrawAmount(self, withdrawAmount, accountNumber, amountWithdrawn, isAdmin):
        if not self.checkValidAmount(isAdmin, withdrawAmount):
            return False
        if isAdmin == False:
            if withdrawAmount > 100000:
                return False
            temp = withdrawAmount + amountWithdrawn[accountNumber]
            if temp < 100000:
                print "Amount $" + str(withdrawAmount)[:-2] + "." + str(withdrawAmount)[-2:] + " sucessfully withdrawn"
            else:
                print "You have exceeded the amount allowed to withdrawn in the session"
                return False
        return True

    def isValidAccountNumberToCreate(self, accountNumber):
        if len(str(accountNumber)) != 8:
            print "Must be exactly 8 digits"
            return False
        elif str(accountNumber)[0] == "0":
            print "Numbers cannot start with 0"
            return False
        if self.checkValidAccount(accountNumber) == True:
            print "Account number already exists"
            return False
        else:
            return True

    def isValidAccountNameToCreate(self, accountName):
        if accountName[0] == " " or accountName[-1] == " ":
            print "Account name cannot start or end with a space"
            return False
        elif len(accountName) > 30 or len(accountName) < 3:
            print "Account name must be between 3-30 digits"
            return False
        else:
            return True