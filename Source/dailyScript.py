import os 
import sys
sys.path.append(sys.path[0]+'/FrontEnd/')
import subprocess

frontEndPath = sys.path[0] + '/FrontEnd/FrontEnd.py'
backEndPath = sys.path[0] + '/BackEnd/BackEnd.py'
runScriptPath = sys.path[0] + '/RunScript.sh'
textPath = sys.path[0] + '/textInput/'
transactionSummPath = sys.path[0] + '/dailyTransactionFiles/'

def startNewDay():
	newDay = dailyScript()
	newDay.clearOldTransactionFiles()
	newDay.runFrontEnd()
	newDay.mergeTransactionFiles()
	newDay.callBackEnd()

class dailyScript:

	def __init__(self):
		self.hasRan = 0;
		self.testOuput = None
	def runTestFront(self, testFile):
		#testOutput = os.system('python ' + frontEndPath + ' < ' + testFile)
		testOutput = subprocess.check_output([runScriptPath,frontEndPath, testFile])
		return testOutput
	
	def getTextFiles(self, path):
		textFiles = os.listdir(path)
		textFiles = [path + textFile for textFile in textFiles	if '.' in textFile]
		return textFiles
	
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
	def clearOldTransactionFiles(self):
		oldTransactions = os.listdir(transactionSummPath)
		oldTransactions = [transactionSummPath + oldTransaction for oldTransaction in oldTransactions if '.' in oldTransaction]
		for oldTransaction in oldTransactions:
			os.system('rm ' + oldTransaction)
	
	def mergeTransactionFiles(self):
		transFiles = os.listdir(transactionSummPath)
		transFiles = [transactionSummPath + transFile for transFile in transFiles if '.' in transFile]
		mergedFileLocation = sys.path[0] + '/BackEnd/MergedTransactionSummaryFile.txt';
		merging = open(mergedFileLocation, 'w+')
		for transFile in transFiles:
			f = open(transFile, 'r')
			for line in f:
				merging.write(line)

	def callBackEnd(self):
		os.chdir(sys.path[0] + '/BackEnd/')
		os.system('python ' + backEndPath)	

startNewDay()
