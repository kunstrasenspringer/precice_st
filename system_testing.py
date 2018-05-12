import sys
import os
import subprocess
import filecmp

def build(systest):
    dirname = "/SystemTest_" + systest
    print(os.getcwd() + dirname)
    os.chdir(os.getcwd() + dirname)
    print(os.getcwd())
    subprocess.call("docker build -t "+ systest +" -f Dockerfile."+ systest +" .", shell=True)
    subprocess.call("docker run -it -d --name "+ systest +"_container "+ systest, shell=True)
    subprocess.call("docker cp "+ systest +"_container:Output_"+ systest +" .", shell=True)

def comparison(pathToRef, pathToOutput):
    fileListRef = os.listdir(pathToRef)
    fileListOutput = os.listdir(pathToOutput)

    fileListRef.sort()
    fileListOutput.sort()

    for x, y in zip(fileListRef, fileListOutput):
        if os.path.isdir(pathToRef+x):
            comparison(pathToRef+x+'/', pathToOutput+y+'/')
        else:
            if not filecmp.cmp(pathToRef + x, pathToOutput + y):
                raise Exception('Output differs from reference')

if __name__ == "__main__":
    build(sys.argv[1])
    pathToRef = os.getcwd() + "/referenceOutput_" + sys.argv[1] + "/"
    pathToOutput = os.getcwd() + "/Output_" + sys.argv[1] + "/"
    comparison(pathToRef, pathToOutput)
