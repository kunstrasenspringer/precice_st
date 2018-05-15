"""Script for system testing preCICE with docker and comparing output.

This script builds a docker image for an system test of preCICE.
It starts a container of the builded image and copys the output generated by the
simulation within the test to the host.
The output is compared to a reference.
It passes if files are equal, else it raises an exception.

Example:
    Example use:

        $ python system_testing.py of-of
"""

import sys
import os
import subprocess
import filecmp

def build(systest):
    """Building docker image.

    This function builds a docker image with the respectively system test,
    runs a container in background to copy the output generated by the
    simulation to the host:

    Args:
        systest (str): Name of the system test.
    """
    dirname = "/SystemTest_" + systest
    print(os.getcwd() + dirname)
    os.chdir(os.getcwd() + dirname)
    print(os.getcwd())
    subprocess.call("docker build -t "+ systest +" -f Dockerfile."+ systest +" .", shell=True)
    subprocess.call("docker run -it -d --name "+ systest +"_container "+ systest, shell=True)
    subprocess.call("docker cp "+ systest +"_container:Output_"+ systest +" .", shell=True)

def comparison(pathToRef, pathToOutput):
        """Building docker image.

        This function builds a docker image with the respectively system test,
        runs a container in background to copy the output generated by the
        simulation to the host:

        Args:
            pathToRef (str): Path to the reference files.
            pathToOutput (str): Path to the output files.

        Raises:
            Exception: Raises exception then output differs from reference.
        """
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
    # Build
    build(sys.argv[1])
    # Preparing string for path
    pathToRef = os.getcwd() + "/referenceOutput_" + sys.argv[1] + "/"
    pathToOutput = os.getcwd() + "/Output_" + sys.argv[1] + "/"
    # Comparing
    comparison(pathToRef, pathToOutput)
