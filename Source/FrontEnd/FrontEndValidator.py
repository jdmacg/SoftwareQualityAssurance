import pdb
maxLineLengthWithoutNewline = 59

#this class contains all the checks for various transactions as described in the handout

class FrontEndValidator:
    #inputs: isAdmin (is the current session admin), amount to check if valid
    #outputs: True/false, true if the amount is valid
    #description: Checks if the amount is valid for withdraw/transfer based off if the user is in ATM or agent mode
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
    #inputs: Account number to be checked
    #outputs: True/False (true if the account is valid)
    #Description: Iterates through all of the account numbers and checks if the account number exists
    #in the case that the account number has been deleted it checks the "invalidAccounts" and returns false if the deleted
    #account exists
    def checkValidAccount(self, validAccounts, invalidAccounts, accountOfInterest):

        for key in invalidAccounts:
            if accountOfInterest == key:
                return False
        for existingAccounts in validAccounts :
            if existingAccounts == accountOfInterest:
                return True
        return False
        # inputs: amount to be withdrawn, account to be withdrawn from, amount that has been withdrawn in the current session, if the current session is admin
        # outputs: True/false (true if the withdrawl was sucessfuly
        # description: Attempts to withdraw the given amount from the given account, if in ATM mode it checks if the account
        # has not withdrawn >$1000 before allowing the amount to be withdrawn (this is skipped for agent mode).
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

    #inputs: Account number of account to create
    #outputs: True/false, true if the account is created
    #description: Checks if the account number given is 8 digits, does not start with 0, and does not already exist
    def isValidAccountNumberToCreate(self,validAccounts,invalidAccounts,accountNumber, isTransactionCheck=False):
        if len(str(accountNumber)) != 8:
            print "Must be exactly 8 digits"
            return False
        elif str(accountNumber)[0] == "0":
            print "Numbers cannot start with 0"
            return False
        if isTransactionCheck is False:
            if self.checkValidAccount(validAccounts,invalidAccounts, accountNumber) == True:
                print "Account number already exists"
                return False
        return True
    #inputs: Account name
    #outputs: true/false, true if the account name is valid
    #description: Checks if the account name is between 3-30 characters, and that it does not start or end with " "
    def isValidAccountNameToCreate(self, accountName):
        if accountName[0] == " " or accountName[-1] == " ":
            print "Account name cannot start or end with a space"
            return False
        elif len(accountName) > 30 or len(accountName) < 3:
            print "Account name must be between 3-30 digits"
            return False
        else:
            return True

    def checkValidTransactionSummary(self, transactionCode, firstAccount, secondAccount, amount, accountName):
        if len(" ".join([transactionCode, firstAccount, secondAccount, amount, accountName])) > maxLineLengthWithoutNewline:
            return False
        if not self.isValidAccountNameToCreate(accountName):
            return False
        #if not self.isValidAccountNumberToCreate(firstAccount, isTransactionCheck=True):
        #    return False
        #if not self.isValidAccountNumberToCreate(secondAccount, isTransactionCheck=True):
        #    return False
        return True
