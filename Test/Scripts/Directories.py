import os.path
import datetime
import sys
import pdb


class Directories:

    def __init__(self):
        self.numTestRuns = 0
        self.slash = "/"
        if sys.platform == "win32":
            self.slash = "\\"
        self.scriptsDir = os.path.dirname(os.path.realpath(__file__))
        self.testDir = os.path.dirname(self.scriptsDir)
        self.rootDir = os.path.dirname(self.testDir)
        self.sourceDir = self.rootDir + self.slash + "Source"
        self.frontendSourceDir = self.sourceDir + self.slash + "FrontEnd"
        self.frontendTestDir = self.testDir + self.slash + "FrontEnd"
        self.frontendModulesDir = self.frontendTestDir + self.slash + "Modules"
        self.frontendOutputDir = self.frontendTestDir + self.slash + "Outputs"
        self.frontEndProgram = self.frontendSourceDir + self.slash + "FrontEnd.py"
        self.runScript = self.scriptsDir + self.slash + "RunScript.sh"

    def createTestDirectory(self, isFrontEnd=True):
        testOutputName = "TestOutput_"
        testOutputName += "v" + str(self.numTestRuns) + "_"
        currDate = datetime.datetime.today()
        day = '{:02d}'.format(currDate.day)
        month = '{:02d}'.format(currDate.month)
        year = '{:04d}'.format(currDate.year)
        hour =  '{:02d}'.format(currDate.hour)
        minute = '{:02d}'.format(currDate.minute)

        if isFrontEnd:
            testOutputPath = self.frontendOutputDir + self.slash + testOutputName + "_" + day + month + year + "_" + hour + minute

        if not os.path.exists(testOutputPath):
            os.makedirs(testOutputPath)

        modules = self.getModulesToTest()
        for module in modules:
            moduleOutputPath = testOutputPath + self.slash
            moduleOutputPath += self.getModuleNameFromPath(module) + self.slash
            if not os.path.exists(moduleOutputPath):
                os.makedirs(moduleOutputPath)

        self.numTestRuns += 1
        return testOutputPath

    def getTransactionSummaryFile(self):
        return self.frontendSourceDir + self.slash + "TransactionSummary.txt"

    def getTestInputFiles(self, modulePath):
        inputDir = self.getTestInputDir(modulePath)
        testFiles = os.listdir(inputDir)
        testFiles = [inputDir + self.slash + testFile for testFile in testFiles if '.' in testFile]
        return testFiles

    def getTestFiles(self, modulePath):
        print modulePath
        testFiles = os.listdir(modulePath)
        #removed slash here
        testFiles = [modulePath + testFile for testFile in testFiles if '.' in testFile]
        return testFiles

    def getModulesToTest(self):
        modules = os.listdir(self.frontendModulesDir)
        modules = [self.frontendModulesDir + self.slash + module for module in modules if '.' not in module]
        return modules

    def getTestInputDir(self, testPath):
        return testPath + self.slash + "Inputs"

    def getTestExpectedDir(self, testInputPath):
        #removed going up a directory here
        return testInputPath + self.slash + "Expected" + self.slash

    def upDirectory(self, path):
        slashIdx = path.rindex(self.slash)
        if path[-1] == self.slash:
            slashIdx = path.rindex(self.slash, end=len(path) - 1)
        return path[:slashIdx]

    def getModuleNameFromOutputPath (self, path):
        testOutputIdx = path.index("Testoutput")
        leftSlashIdx = path.index(self.slash, testOutputIdx)
        leftSlashIdx += 29
        rightSlashIdx = len(path)
        if self.slash in path[leftSlashIdx + 1:]:
            rightSlashIdx = path.index(self.slash, leftSlashIdx + 1)
        return path[leftSlashIdx + 1: rightSlashIdx]        
        

    def getModuleNameFromPath(self, path):
        moduleIdx = path.index("Modules")
        leftSlashIdx = path.index(self.slash, moduleIdx)
        rightSlashIdx = len(path)
        if self.slash in path[leftSlashIdx + 1:]:
            rightSlashIdx = path.index(self.slash, leftSlashIdx + 1)
        return path[leftSlashIdx + 1: rightSlashIdx]

    def getModuleInputDirGivenName(self, moduleName):
        return self.frontendModulesDir + self.slash + moduleName + self.slash

    def getModuleOutputDirGivenName(self, moduleName, testOutputDir):
        return testOutputDir + self.slash + moduleName + self.slash

    def getTestNameFromFile(self, testFile):
        slashIdx = testFile.rfind(self.slash)
        underscoreIdx = testFile.rfind("_")
        return testFile[slashIdx + 1: underscoreIdx]

