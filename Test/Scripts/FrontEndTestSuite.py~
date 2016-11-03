from Directories import Directories
import os
import subprocess as sub
import sys
import subprocess as sub

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
                self.copyTransactionSummaryToOutput(testOutputDir, testFile)
                self.writeTestResultsToDir(testOutput, testOutputDir, testFile)

    def compareTransactionTestResults(self):
        for moduleName in self.modulesWithPaths:
            moduleInputDir = self.modulesWithPaths[moduleName][self.inputIdx]
            moduleOutputDir = self.modulesWithPaths[moduleName][self.outputIdx]
            moduleExpectedDir = self.directories.getTestExpectedDir(moduleInputDir)
            outputFiles = moduleOutputDir[:-1]
            expectedFiles = moduleExpectedDir[:-1]
            for outputFile in outputFiles:
                if "ConsoleOutput" in outputFile:
                    continue
                elif "TranscationOutput" in outputFile:
                    testName = self.directories.getModuleNameFromPath(outputFile)
                    expectedFile = [file for file in expectedFiles if testName in file]
                    outputFileData = open(outputFile).readlines()
                    expectedfileData = open(expectedFile).readlines()
                    comparison = self.compareFiles(expectedFiles, outputFiles)

    def compareFiles(self, expectedData, outputData):
	    testName = self.directories.getNameFromFile(expectedData)
	    moduleName = self.directories.getModuleNameFromPath(expectedData)
	    diffFileDestination = self.modulesWithPaths[moduleName][self.outputIdx] + testName + "_diffFile.txt"
        print diffFileDestination
	    bashcommand = ("diff " + expectedData + " " + outputData + " > " + diffFileDestination)
	    process = sub.Popen(bashCommand)         
	    #for expectedLine in expectedData:
                #for outputLine in outputData:
                    #do some comparison

    def copyTransactionSummaryToOutput(self, testOutputDir, testFile):
        testName = self.directories.getTestNameFromFile(testFile)
        moduleName = self.directories.getModuleNameFromPath(testFile)
        transactionSummaryDestination = self.modulesWithPaths[moduleName][self.outputIdx] + testName + "_TransactionOutput.txt"
        transactionSummarySource = self.directories.getTransactionSummaryFile()
        with open(transactionSummarySource) as src:
            with open(transactionSummaryDestination, 'w+') as dst:
                for line in src:
                    dst.write(line)

    def writeTestResultsToDir(self, testOutput, testOutputDir, testFile):
        testName = self.directories.getTestNameFromFile(testFile)
        moduleName = self.directories.getModuleNameFromPath(testFile)
        outputTestFilePath = self.modulesWithPaths[moduleName][self.outputIdx] + testName + "_ConsoleOuput.txt"
        f = open(outputTestFilePath, 'w')
        for line in testOutput: 
            f.write(line)
        f.close()

    def runTest(self, testFile):
        #calls the bash script, returns the script output
        testOutput = sub.check_output([self.directories.runScript, self.directories.frontEndProgram, testFile])
        return testOutput


frontEndTestSuite = FrontEndTestSuite()
frontEndTestSuite.runTests()
frontEndTestSuite.compareTransactionTestResults()

