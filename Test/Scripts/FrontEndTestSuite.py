from Directories import Directories
import os
import subprocess as sub
import sys
#sys.path.insert(0, Directories.frontendSourceDir)
#import FrontEnd

class FrontEndTestSuite:
    def __init__(self):
        self.directories = Directories()
        self.modulesToTest = self.getModulesToTest()

    '''def getCommandsFromFile(self, testFile):
        commands = open(testFile).readlines()
        commands = [line.strip() for line in commands]
        return commands'''

    def runTest(self, testFile):
        scriptOutput = sub.check_output([self.directories.runScript, testFile])
        return scriptOutput

    def getModulesToTest(self):
        modules = os.listdir(self.directories.frontendModulesDir)
        modules = [self.directories.frontendModulesDir + self.directories.slash + module for module in modules if '.' not in module]
        return modules

    def getTestInputFiles(self, modulePath):
        inputDir = self.directories.getTestInputDir(modulePath)
        testFiles = os.listdir(inputDir)
        testFiles = [inputDir + self.directories.slash + testFile for testFile in testFiles if '.' in testFile]
        return testFiles


frontEndTestSuite = FrontEndTestSuite()

print frontEndTestSuite.directories.frontEndProgram
modules = frontEndTestSuite.getModulesToTest()
testFiles = frontEndTestSuite.getTestInputFiles(modules[0])
print testFiles[0]
print frontEndTestSuite.runTest(testFiles[0])


