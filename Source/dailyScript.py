import os 
import sys
sys.path.append(sys.path[0]+'/FrontEnd/')
import subprocess

frontEndPath = sys.path[0] + '/FrontEnd/FrontEnd.py'
backEndPath = sys.path[0] + '/BackEnd/BackEnd.py'
runScriptPath = sys.path[0] + '/RunScript.sh'
textPath = sys.path[0] + '/textInput/'

class dailyScript:

	def __init__(self):
		self.hasRan = 0;
		self.testOuput = None
	def runTestFront(self, testFile):
		testOutput = subprocess.check_output([runScriptPath,frontEndPath, testFile])
		return testOutput
	
	def getTextFiles(self, path):
		textFiles = os.listdir(path)
		textFiles = [path + textFile for textFile in textFiles	if '.' in textFile]
		return textFiles
	
	def runFrontEnd(self):
		textFiles = self.getTextFiles(textPath)
		for textFile in textFiles:
			textOutput = self.runTestFront(textFile)
			print textOutput


newDay = dailyScript()
newDay.runFrontEnd()
