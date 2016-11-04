from Directories import Directories
import os
import subprocess as sub
import sys
import subprocess as sub
import pdb

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
            outputFiles = self.directories.getTestFiles(moduleOutputDir)
            expectedFiles = self.directories.getTestFiles(moduleExpectedDir)
            for outputFile in outputFiles:
                if "ConsoleOutput" in outputFile:
                    continue
                elif "TransactionOutput" in outputFile:
                    testName = self.directories.getModuleNameFromOutputPath(outputFile)
                    expectedFile = [expectedFile for expectedFile in expectedFiles if testName.upper() in expectedFile.upper()]
                    
                    expectedFile = expectedFile[0]
                    commonDiffPath = moduleOutputDir + "CommonDiff.txt"
                    comparison = self.compareFiles(expectedFile, outputFile, testName, moduleOutputDir, commonDiffPath)

    def compareFiles(self, expectedFile, outputFile, testName, moduleOutputDir, commonDiffPath):
        diffFileDestination = moduleOutputDir + testName + "_diffFile.txt" 
        process = sub.Popen(["diff", expectedFile, outputFile,]
        ,stdout=sub.PIPE,
        stderr=sub.STDOUT)
        diffFile = open(diffFileDestination, 'w+')
        for line in process.stdout.read():
            diffFile.write(line)
        diffFile.close()
        process = sub.Popen(["diff", expectedFile, outputFile,],
        stdout=sub.PIPE,
        stderr=sub.STDOUT)      
        commonDiff = open(commonDiffPath, "a")
	commonDiff.write("----" + testName + "----")
	commonDiff.write("\n")
        for line in process.stdout.read():
            commonDiff.write(line)
        commonDiff.close()
        #pdb.set_trace()

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

