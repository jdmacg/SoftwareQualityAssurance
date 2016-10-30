from Directories import Directories
import os
import sys
import subprocess as sub
#sys.path.insert(0, Directories.frontendSourceDir)
#import FrontEnd

class FrontEndTestSuite:
    def __init__(self):
        self.directories = Directories()
        self.modulesToTest = self.getModulesToTest()

    #def runTests(self):


    def getModulesToTest(self):
        modules = os.listdir(self.directories.frontendModulesDir)
        modules = [self.directories.frontendModulesDir + "\\" + module for module in modules if '.' not in module]
        return modules


frontEndTestSuite = FrontEndTestSuite()
ex = frontEndTestSuite.directories.frontendSourceDir + frontEndTestSuite.directories.slash + "FrontEnd.py"
#print ex
#os.system(ex)
#p = os.popen("python " + ex, "r")
#p = sub.Popen(["python " + ex], stdout=sub.PIPE, stderr=sub.PIPE)
#output, errors = p.communicate()
#print output
sub.call(['ls', '-l'], shell=True)
