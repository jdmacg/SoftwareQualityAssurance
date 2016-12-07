import os
import sys
import subprocess
import dailyScript

textPath = sys.path[0] + '/textInput/'
weeklyText = sys.path[0] + '/weeklyTextInput/'
validAccountBackend = sys.path[0] + '/BackEnd/ValidAccounts.txt'
frontEndDir = sys.path[0] + '/FrontEnd/'


class weeklyScript:
	
	def __init__(self):
		self.hasRan = 0

	def cleanTextPath(self):
		textFiles = os.listdir(textPath)
		textFiles = [textPath + textFile for textFile in textFiles if '.' in textFile]
		for textFile in textFiles:
			os.system('rm ' + textFile)

	def copyFiles(self, directory):
		copyFiles = os.listdir(directory)
		copyFiles = [directory + copyFile for copyFile in copyFiles if '.' in copyFile]
		for copyFile in copyFiles:
			os.system('cp ' + copyFile + ' ' + textPath)	

	def runWeekly(self):
		weeklyDirectories = os.listdir(weeklyText)
		for directory in weeklyDirectories:
			newFileDir = weeklyText + directory + '/'
			self.cleanTextPath()
			self.copyFiles(newFileDir)
			os.chdir(sys.path[0] + '/BackEnd/')
			dailyScript.startNewDay()
			os.chdir(sys.path[0])
			os.system('cp ' + validAccountBackend + ' ' + frontEndDir)



newWeek = weeklyScript()
newWeek.runWeekly()
