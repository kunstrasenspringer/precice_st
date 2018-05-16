"""Script for pushing output and logfile to a repository.

This script pushes output files of a system test, if they exists, and a logfile
to the repository: https://github.com/kunstrasenspringer/precice_st_output.

    Args:
        sys.argv[1] (int): Indicator for succesful test.
        sys.argv[2] (str): Name of the system test.

    Example:
        Example use to push output files and logfile of system test of-of:

            $ python push.py 0 of-of

        Example use to only push logfile of system test of-of:

            $ python push.py 1 of-of
"""

import sys
import os
import subprocess
import time

if __name__ == "__main__":
    success = sys.argv[1] # success = 0 -> Output!=Reference, else -> Output==Reference
    systest = sys.argv[2]

    # Creating new logfile. if it exists, truncate content.
    log = open("log_" + systest, "w")
    # Saving versions of used software in system test systest.
    if systest == "of-ccx":
        log.write("OpenFOAM version: 4.1\n")
        subprocess.call(["echo OpenFOAM-adapter Version: $(git ls-remote https://github.com/precice/openfoam-adapter.git  | tail -1)"],shell=True, stdout=log)
        log.write("CalculiX version: 2.12\n")
        subprocess.call(["echo CalculiX-adapter Version: $(git ls-remote https://github.com/precice/calculix-adapter.git | tail -1)"],shell=True, stdout=log)
        subprocess.call(["echo tutorials Version: $(git ls-remote https://github.com/precice/tutorials.git | tail -1)"],shell=True, stdout=log)
    elif systest == "of-of":
        log.write("OpenFOAM version: 4.1\n")
        subprocess.call(["echo OpenFOAM-adapter Version: $(git ls-remote https://github.com/precice/openfoam-adapter.git  | tail -1)"],shell=True, stdout=log)
    elif systest == "su2-ccx":
        log.write("CalculiX version: 2.13\n")
        log.write("SU2 version: 6.0.0\n")
        subprocess.call(["echo CalculiX-adapter Version: $(git ls-remote https://github.com/precice/calculix-adapter.git | head -n 1)"],shell=True, stdout=log)
        subprocess.call(["echo SU2-adapter Version: $(git ls-remote https://github.com/precice/su2-adapter.git | tail -1)"],shell=True, stdout=log)
        subprocess.call(["echo tutorials Version: $(git ls-remote https://github.com/precice/tutorials.git | tail -1)"],shell=True, stdout=log)
    # Saving general information of all system tests.
    # Saving used Ubuntu and preCICE version in logfile.
    subprocess.call(["echo preCICE Version: $(git ls-remote --tags https://github.com/precice/precice.git | tail -1)"],shell=True, stdout=log)
    log.write("Ubuntu version: 16.04\n")
    # Saving current date in logfile.
    localtime = str(time.asctime(time.localtime(time.time())))
    log.write("System testing at " + localtime + "\n")


    # Pushing outputfiles and logfile to repo.
    # Clone repository.
    subprocess.call(["git clone https://github.com/kunstrasenspringer/precice_st_output"], shell=True)
    os.chdir(os.getcwd() + "/precice_st_output")
    # Setting up git user.
    subprocess.call(["git config --local user.email \"travis@travis-ci.org\""], shell=True)
    subprocess.call(["git config --local user.name \"Travis CI\""], shell=True)
    if success == 0:
        # Move ouput to local repository.
        subprocess.call(["mv ${TRAVIS_BUILD_DIR}/SystemTest_"+systest+"/Output_"+systest+" ${TRAVIS_BUILD_DIR}/precice_st_output"], shell=True)
        subprocess.call(["mv ${TRAVIS_BUILD_DIR}/log_"+systest+" ${TRAVIS_BUILD_DIR}/precice_st_output"], shell=True)
        subprocess.call(["git add ."], shell=True)
        subprocess.call(["git commit -m \"${TRAVIS_BUILD_NUMBER} Output != Reference\""], shell=True)
    else:
        subprocess.call(["mv ${TRAVIS_BUILD_DIR}/log_"+systest+" ${TRAVIS_BUILD_DIR}/precice_st_output"], shell=True)
        subprocess.call(["git add ."], shell=True)
        subprocess.call(["git commit -m \"${TRAVIS_BUILD_NUMBER} Output == Reference\""], shell=True)
    subprocess.call(["git remote set-url origin https://${GH_TOKEN}@github.com/kunstrasenspringer/precice_st_output.git > /dev/null 2>&1"], shell=True)
    subprocess.call(["git push"], shell=True)
