#!/usr/bin/env python
import subprocess
import os

pathToTest1 = os.getcwd() + '/ref_of-of/'
pathToTest2 = os.getcwd() + '/Output_of-of/'

os.chdir(pathToTest2)
subprocess.call(['sed', '-i', '-e', '1,110d', 'Fluid.log'])
subprocess.call(['sed', '-i', '-e', '1,75d', 'Solid.log'])
command = ["sed", "-i", "/ExecutionTime/d", "Solid.log"]
subprocess.call(command)
command = ["sed", "-i", "/ExecutionTime/d", "Fluid.log"]
subprocess.call(command)

fileListTest1 = os.listdir(pathToTest1)
fileListTest2 = os.listdir(pathToTest2)

fileListTest1.sort()
fileListTest2.sort()

def comparison():
    for x, y in zip(fileListTest1, fileListTest2):
        #print ('diff ' + pathToTest1 + x + ' ' + pathToTest2 + y)
        if subprocess.call(['diff', '-y', pathToTest1 + x, pathToTest2 + y]) != 0:
            subprocess.call(['exit', '-1'])


if __name__ == "__main__":
    comparison()
