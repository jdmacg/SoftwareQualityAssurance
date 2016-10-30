import os.path
import datetime
import sys



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
            testOutputPath = self.frontendOutputDir + "\\" + testOutputName + "_" + day + month + year + "_" + hour + minute

        if not os.path.exists(testOutputPath):
            os.makedirs(testOutputPath)
        self.numTestRuns += 1
        return testOutputPath

    def getTestInputDir(self, testPath):
        return self.testPath + self.slash + "Inputs"

    def getTestExpectedDir(self, testPath):
        return self.testPath + self.slash + "ExpectedOutputs"


