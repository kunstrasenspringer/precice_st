#!/usr/bin/env python
import subprocess
import os

pathToTest1 = os.getcwd() + '/reference_SU2-CCX/'
pathToTest2 = os.getcwd() + '/Output_su2-ccx/'

fileListTest1 = os.listdir(pathToTest1)
fileListTest2 = os.listdir(pathToTest2)

fileListTest1.sort()
fileListTest2.sort()

def comparison():
    for x, y in zip(fileListTest1, fileListTest2):
        if subprocess.call(['diff', '-y', pathToTest1 + x, pathToTest2 + y]) != 0:
            print ('diff ' + pathToTest1 + x + ' ' + pathToTest2 + y)
            return -1


if __name__ == "__main__":
    comparison
