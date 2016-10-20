import fileinput
class ValidAccounts:
    def __init__(self):
        self.validAccounts = []
        f = open("ValidAccounts.txt","r")
        endsWithZeros = 0
        for line in f.read().split():
            if line == "00000000" :
                endsWithZeros = 1
                break
            if len(str(line)) != 8:
                print("this should not happen, throw an error because wrong input")
            elif str(line)[0] == "0":
                print("Numbers cannot start with 0");
            else:
                self.validAccounts.append(line)
        f.close()
        if endsWithZeros == 0:
            print("Throw an error, the valid accounts file is not proper")
        else:
            print("Valid accounts file has been sucessfully loaded.")
    def checkValidAccount(self, accountChecking):
        for existingAccounts in self.validAccounts :
            if existingAccounts == accountChecking:
                return 1
        return 0