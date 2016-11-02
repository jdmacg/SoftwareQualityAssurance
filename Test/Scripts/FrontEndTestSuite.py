from Directories import Directories
import os
import subprocess as sub
import sys
import subprocess as sub
#sys.path.insert(0, Directories.frontendSourceDir)
#import FrontEnd



class FrontEndTestSuite:
    def __init__(self):
        self.directories = Directories()
        self.modulesToTest = self.directories.getModulesToTest()
        self.modulesWithPaths = dict()
        for moduleInputDir in self.modulesToTest:
            moduleName = self.directories.getModuleNameFromPath(moduleInputDir)
            self.modulesWithPaths[moduleName] = [moduleInputDir]
        self.inputIdx = 0
        self.outputIdx = 1

    def runTests(self):
        testOutputDir = self.directories.createTestDirectory()
        modules = self.modulesToTest
        for modulePath in modules:
            moduleName = self.directories.getModuleNameFromPath(modulePath)
            self.modulesWithPaths[moduleName].append(self.directories.getModuleOutputDirGivenName(moduleName, testOutputDir))
            testFiles = self.directories.getTestInputFiles(modulePath)
            for testFile in testFiles:
                testOutput = self.runTest(testFile)
                self.writeTestResultsToDir(testOutput, testOutputDir, testFile)
        
    def writeTestResultsToDir(self, testOutput, testOutputDir, testFile):
        testName = self.directories.getTestNameFromFile(testFile)
        moduleName = self.directories.getModuleNameFromPath(testFile)
        outputTestFilePath = self.modulesWithPaths[moduleName][self.outputIdx] + testName + "_Ouput.txt"
        f = open(outputTestFilePath, 'w')
        f.write(testOutput)
        f.close()

    def runTest(self, testFile):
        #calls the bash script, returns the script output
        testOutput = sub.check_output([self.directories.runScript, self.directories.frontEndProgram, testFile])
        return testOutput


frontEndTestSuite = FrontEndTestSuite()
frontEndTestSuite.runTests()
'''
frontEndTestSuite = FrontEndTestSuite()
#print frontEndTestSuite.directories.frontEndProgram
modules = frontEndTestSuite.getModulesToTest()
testFiles = frontEndTestSuite.getTestInputFiles(modules[0])
#print testFiles[0]
#print frontEndTestSuite.runTest(testFiles[0])
print "this is in python"
print frontEndTestSuite.runTest(testFiles[0])
print "now not in python"
'''
