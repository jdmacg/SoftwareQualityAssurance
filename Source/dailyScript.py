import os 
import sys
import subprocess

#Setting up constant paths based off of system directory
frontEndPath = sys.path[0] + '/FrontEnd/FrontEnd.py'
backEndPath = sys.path[0] + '/BackEnd/BackEnd.py'
runScriptPath = sys.path[0] + '/RunScript.sh'
textPath = sys.path[0] + '/textInput/'
transactionSummPath = sys.path[0] + '/dailyTransactionFiles/'
#Inputs:none
#Outputs:none
#Description: Instantiates a new dailyScript object, clears all old transaction files
#Runs the front end with all text inputs in the folder "/textInput/", merges all transaction files
#And then lastly calls the backend
def startNewDay():
	newDay = dailyScript()
	newDay.clearOldTransactionFiles()
	newDay.runFrontEnd()
	newDay.mergeTransactionFiles()
	newDay.callBackEnd()


#Contains all of the necessary classes to run the daily script
class dailyScript:

	#Initializes a dailyScript class, has to be here because it's a python class
	#but the actual method does nothing
	def __init__(self):
		self.hasRan = 0;
		self.testOuput = None

	#Input:The name of a text file to run combined with it's path
	#output:The console output of the python run
	#Description: Runs a bash script that pipelines the testFile into the python program
	#The bash is simply: python frontEndPath < testFile
	def runTestFront(self, testFile):
		#testOutput = os.system('python ' + frontEndPath + ' < ' + testFile)
		testOutput = subprocess.check_output([runScriptPath,frontEndPath, testFile])
		return testOutput
	
	#input: Path of where to get test files
	#output an array consisting of all test files
	#Description: Finds all files that have a "." in that name in the directory given
	def getTextFiles(self, path):
		textFiles = os.listdir(path)
		textFiles = [path + textFile for textFile in textFiles	if '.' in textFile]
		return textFiles
	

	#input: none
	#output: none
	#Description: Runs all of the test files with the methods described above
	#Then it copies the transaction file to a different location and concatanates the string
	#name with a number to tell the difference between between the transaction files
	#this is all done using python system commands, and hence will not work if this is not ran on a linux machine
	def runFrontEnd(self):
		textFiles = self.getTextFiles(textPath)
		i = 1
		for textFile in textFiles:
			textOutput = self.runTestFront(textFile)
			transactionFile = sys.path[0] + '/FrontEnd/TransactionSummary.txt';
			os.system('cp ' + transactionFile + ' ' + transactionSummPath)
			oldFileName = transactionSummPath + 'TransactionSummary.txt'
			newFileName = transactionSummPath + 'TransactionSummary' + str(i) + '.txt'
			os.system('mv ' + oldFileName + " " + newFileName) 
			i = i + 1

	#input: none
	#output: none
	#Description: clears all transaction files from the location where transactionfiles are saved for the daily script
	#This is called before the actual textInputs are tested
	def clearOldTransactionFiles(self):
		oldTransactions = os.listdir(transactionSummPath)
		oldTransactions = [transactionSummPath + oldTransaction for oldTransaction in oldTransactions if '.' in oldTransaction]
		for oldTransaction in oldTransactions:
			os.system('rm ' + oldTransaction)
	
	#Input: none
	#Output: none
	#Description: Takes all transaction files created in runFrontEnd() and writes them to the backEnd merged transaction summary file
	def mergeTransactionFiles(self):
		transFiles = os.listdir(transactionSummPath)
		transFiles = [transactionSummPath + transFile for transFile in transFiles if '.' in transFile]
		mergedFileLocation = sys.path[0] + '/BackEnd/MergedTransactionSummaryFile.txt';
		merging = open(mergedFileLocation, 'w+')
		for transFile in transFiles:
			f = open(transFile, 'r')
			for line in f:
				merging.write(line)
	#Input: none
	#output: none
	#Description: Calls the backend using python system, but changes the directory beforehand
	def callBackEnd(self):
		os.chdir(sys.path[0] + '/BackEnd/')
		os.system('python ' + backEndPath)	

startNewDay()
