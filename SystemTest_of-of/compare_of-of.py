#!/usr/bin/env python
import os
import filecmp

def comparison(pathToRef, pathToOutput):
    fileListRef = os.listdir(pathToRef)
    fileListOutput = os.listdir(pathToOutput)

    fileListRef.sort()
    fileListOutput.sort()

    for x, y in zip(fileListRef, fileListOutput):
        if os.path.isdir(pathToRef+x):
            comparison(pathToRef+x+'/',pathToOutput+y+'/')
        else:
            if not filecmp.cmp(pathToRef + x, pathToOutput + y):
                raise Exception('Output differs from reference')

if __name__ == "__main__":
    comparison(os.getcwd() + '/referenceOutput_of-of/', os.getcwd() + '/Output_of-of/')
