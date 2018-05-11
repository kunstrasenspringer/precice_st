#!/usr/bin/env python
import os
import filecmp

pathToRef = os.getcwd() + '/referenceOutput_su2-ccx/'
pathToOutput = os.getcwd() + '/Output_su2-ccx/'

fileListRef = os.listdir(pathToRef)
fileListOutput = os.listdir(pathToOutput)

fileListRef.sort()
fileListOutput.sort()

def comparison():
    for x, y in zip(fileListRef, fileListOutput):
        if not filecmp.cmp(pathToRef + x, pathToOutput + y):
            print(x)
            raise Exception('Output differs from reference')

if __name__ == "__main__":
    comparison()
