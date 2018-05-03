#!/usr/bin/env python
import subprocess
import os

pathToTest1 = os.getcwd() + '/referenceOutput_of-ccx/'
pathToTest2 = os.getcwd() + '/Output_of-ccx/'

os.chdir(pathToTest1)
subprocess.call(['sed', '-i', '-e', '1,110d', 'Fluid.log'])
subprocess.call(['sed', '-i', '-e', '1,75d', 'Solid.log'])

os.chdir(pathToTest2)
subprocess.call(['sed', '-i', '-e', '1,110d', 'Fluid.log'])
subprocess.call(['sed', '-i', '-e', '1,75d', 'Solid.log'])


fileListTest1 = os.listdir(pathToTest1)
fileListTest2 = os.listdir(pathToTest2)

fileListTest1.sort()
fileListTest2.sort()

def comparison():
    for x, y in zip(fileListTest1, fileListTest2):
        #print ('diff ' + pathToTest1 + x + ' ' + pathToTest2 + y)
        if subprocess.call(['diff', '-y', pathToTest1 + x, pathToTest2 + y]) != 0:
            print('fail')
            return -1


if __name__ == "__main__":
    comparison()
