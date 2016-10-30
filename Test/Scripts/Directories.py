import os.path
import datetime


class Directories:

    scriptsDir = os.path.dirname(os.path.realpath(__file__))
    testDir = os.path.dirname(scriptsDir)
    rootDir = os.path.dirname(testDir)
    sourceDir = rootDir + "\Source"
    frontendSourceDir = sourceDir + "\FrontEnd"
    frontendTestDir = testDir + "\FrontEnd"
    frontendModulesDir = frontendTestDir + "\Modules"
    frontendOutputDir = frontendTestDir + "\Outputs"

    def __init__(self):
        self.numTestRuns = 0

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
        return self.testPath + "\Inputs"

    def getTestExpectedDir(self, testPath):
        return self.testPath + "\ExpectedOutputs"