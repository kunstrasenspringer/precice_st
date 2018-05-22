"""Script for pushing output and logfile to a repository.

This script pushes output files of a system test, if they exists, and a logfile
to the repository: https://github.com/kunstrasenspringer/precice_st_output.

    Example:
        Example use to push output files and logfile of system test of-of:

            $ python push.py -s -t of-of
"""

import sys
import os
import subprocess
import time
import argparse

# Parsing flags
parser = argparse.ArgumentParser(description='Build local.')
parser.add_argument('-b', '--branch', help="log choosen preCICE branch")
parser.add_argument('-t', '--test', help="choose system tests you want to use")
parser.add_argument('-s', '--success', action='store_true' ,help="only upload log file")
args = parser.parse_args()

if __name__ == "__main__":
    systest = args.test

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
    # git ls-remote https://github.com/precice/precice.git | grep master
    if args.branch:
        subprocess.call(["echo preCICE Version: $(git ls-remote https://github.com/precice/precice.git | grep "+ args.branch +")"],shell=True, stdout=log)
    else:
        subprocess.call(["echo preCICE Version: $(git ls-remote --tags https://github.com/precice/precice.git | tail -1)"],shell=True, stdout=log)
    log.write("Ubuntu version: 16.04\n")
    # Saving current date in logfile.
    localtime = str(time.asctime(time.localtime(time.time())))
    log.write("System testing at " + localtime + "\n")
    log.close()

    # Pushing outputfiles and logfile to repo.
    # Clone repository.
    subprocess.call(["git clone https://github.com/kunstrasenspringer/precice_st_output"], shell=True)
    os.chdir(os.getcwd() + "/precice_st_output")
    # Setting up git user.
    if not args.branch:
        subprocess.call(["git config --local user.email \"travis@travis-ci.org\""], shell=True)
        subprocess.call(["git config --local user.name \"Travis CI\""], shell=True)

    if not args.success:
        # Move ouput to local repository.
        subprocess.call(["mv "+ os.path.abspath(os.path.join(os.getcwd(), os.pardir)) +"/SystemTest_"+systest+"/Output_"+systest+" "+ os.getcwd()], shell=True)
        subprocess.call(["mv "+ os.path.abspath(os.path.join(os.getcwd(), os.pardir)) +"/log_"+systest+" "+ os.getcwd()], shell=True)
        subprocess.call(["git add ."], shell=True)
        if args.branch:
            subprocess.call(["git commit -m \"Output != Reference, local build with preCICE branch: "+ args.branch +"\""], shell=True)
        else:
            subprocess.call(["git commit -m \"Output != Reference, build number: ${TRAVIS_BUILD_NUMBER}\""], shell=True)
    else:
        subprocess.call("rm -rf Output_" + systest, shell=True)
        subprocess.call(["mv "+ os.path.abspath(os.path.join(os.getcwd(), os.pardir)) +"/log_"+systest+" "+ os.getcwd()], shell=True)
        subprocess.call(["git add ."], shell=True)
        if args.branch:
            subprocess.call(["git commit -m \"Output == Reference, local build with preCICE branch: "+ args.branch +"\""], shell=True)
        else:
            subprocess.call(["git commit -m \"Output == Reference, build number: ${TRAVIS_BUILD_NUMBER} \""], shell=True)
    subprocess.call(["git remote set-url origin https://${GH_TOKEN}@github.com/kunstrasenspringer/precice_st_output.git > /dev/null 2>&1"], shell=True)
    subprocess.call(["git push"], shell=True)
