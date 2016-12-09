import os
import sys
import subprocess
import dailyScript

#Creating path names based off of the system
textPath = sys.path[0] + '/textInput/'
weeklyText = sys.path[0] + '/weeklyTextInput/'
validAccountBackend = sys.path[0] + '/BackEnd/ValidAccounts.txt'
masterAccountBackend = sys.path[0] + '/BackEnd/MasterAccountList.txt'
frontEndDir = sys.path[0] + '/FrontEnd/'
masterAccount = sys.path[0] + '/weeklyMasterAccount/'

#Contains all of the necessary classes to run the weekly script
class weeklyScript:
	
	#Initialization method for the python class, doesn't really do anything
	def __init__(self):
		self.hasRan = 0

	#input: Directory to remove files from
	#output: none
	#description:Clears all files in a given directory
	#this is called to remove all textFiles between daily runs
	def cleanTextPath(self, directory):
		textFiles = os.listdir(directory)
		textFiles = [directory + textFile for textFile in textFiles if '.' in textFile]
		for textFile in textFiles:
			os.system('rm ' + textFile)
	
	#input: directory to copy files from
	#output: none
	#description: Copies all files from the given directory to the textInput directory for the dailyScript run 
	def copyFiles(self, directory):
		copyFiles = os.listdir(directory)
		copyFiles = [directory + copyFile for copyFile in copyFiles if '.' in copyFile]
		for copyFile in copyFiles:
			os.system('cp ' + copyFile + ' ' + textPath)	

	#Input: none
	#Output: none
	#Description: Gets all directories inside the weeklyTextInputs/ folder
	#and then one directory at a time the files are copied into the textInput, the dailyScript is run
	#the master account file is saved, and the validAccounts file is transferred to the front end
	def runWeekly(self):
		weeklyDirectories = os.listdir(weeklyText)
		for directory in weeklyDirectories:
			newFileDir = weeklyText + directory + '/'
			self.cleanTextPath(textPath)
			self.copyFiles(newFileDir)
			os.chdir(sys.path[0] + '/BackEnd/')
			dailyScript.startNewDay()
			os.chdir(sys.path[0])
			os.system('cp ' + validAccountBackend + ' ' + frontEndDir)
			os.system('cp ' + masterAccountBackend + ' ' + masterAccount)
			masterAccountName = masterAccount + 'MasterAccountList.txt'
			newMasterAccountName  = masterAccount + 'MasterAccountList' + str(directory) + '.txt'
			os.system('mv ' + masterAccountName + ' ' + newMasterAccountName)



newWeek = weeklyScript()
newWeek.cleanTextPath(masterAccount)
newWeek.runWeekly()
