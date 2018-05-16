import sys
import os
import subprocess
import time

def git(success, systest):
    # Clone repository
    subprocess.call(["git clone https://github.com/kunstrasenspringer/precice_st_output"], shell=True)
    os.chdir(os.getcwd() + "/precice_st_output")
    # Setting up git user
    subprocess.call(["git config --local user.email \"travis@travis-ci.org\""], shell=True)
    subprocess.call(["git config --local user.name \"Travis CI\""], shell=True)
    if success == 0:
        # Move ouput to repository
        subprocess.call(["mv ${TRAVIS_BUILD_DIR}/SystemTest_"+systest+"/Output_"+systest+" ${TRAVIS_BUILD_DIR}/precice_st_output"], shell=True)
        subprocess.call(["mv ${TRAVIS_BUILD_DIR}/log_"+systest+" ${TRAVIS_BUILD_DIR}/precice_st_output"], shell=True)
        subprocess.call(["git add ."], shell=True)
        subprocess.call(["git commit -m \"${TRAVIS_BUILD_NUMBER} Output != Reference\""], shell=True)
    else:
        subprocess.call(["mv ${TRAVIS_BUILD_DIR}/log_"+systest+" ${TRAVIS_BUILD_DIR}/precice_st_output"], shell=True)
        subprocess.call(["git add ."], shell=True)
        subprocess.call(["git commit -m \"${TRAVIS_BUILD_NUMBER} Output == Reference\""], shell=True)
        #subprocess.call(["mv ${PWD}/log_"+systest+" ${PWD}/precice_st_output"], shell=True)
    subprocess.call(["git remote set-url origin https://${GH_TOKEN}@github.com/kunstrasenspringer/precice_st_output.git > /dev/null 2>&1"], shell=True)
    subprocess.call(["git push"], shell=True)

if __name__ == "__main__":
    # creating new logfile. if it exists, truncate content
    systest = sys.argv[2]
    log = open("log_" + systest, "w")

    if systest == "of-ccx":
        log.write("OpenFOAM version: 4.1\n")
        subprocess.call(["echo OpenFOAM-adapter Version: $(git ls-remote https://github.com/precice/calculix-adapter.git  | tail -1)"],shell=True, stdout=log)
        log.write("CalculiX version: 2.12\n")
        subprocess.call(["echo CalculiX-adapter Version: $(git ls-remote https://github.com/precice/calculix-adapter.git | tail -1)"],shell=True, stdout=log)
        subprocess.call(["echo tutorials Version: $(git ls-remote https://github.com/precice/tutorials.git | tail -1)"],shell=True, stdout=log)
    elif systest == "of-of":
        log.write("OpenFOAM version: 4.1\n")
        subprocess.call(["echo OpenFOAM-adapter Version: $(git ls-remote https://github.com/precice/calculix-adapter.git  | tail -1)"],shell=True, stdout=log)
    elif systest == "su2-ccx":
        log.write("CalculiX version: 2.13\n")
        log.write("SU2 version: 6.0.0\n")
        subprocess.call(["echo CalculiX-adapter Version: $(git ls-remote https://github.com/precice/calculix-adapter.git | head -n 1)"],shell=True, stdout=log)
        subprocess.call(["echo SU2-adapter Version: $(git ls-remote https://github.com/precice/su2-adapter.git | tail -1)"],shell=True, stdout=log)
        subprocess.call(["echo tutorials Version: $(git ls-remote https://github.com/precice/tutorials.git | tail -1)"],shell=True, stdout=log)


    # save used Ubuntu and preCICE version in logfile
    subprocess.call(["echo preCICE Version: $(git ls-remote --tags https://github.com/precice/precice.git | tail -1)"],shell=True, stdout=log)
    log.write("Ubuntu version: 16.04\n")
    # save current date in logfile
    localtime = str(time.asctime(time.localtime(time.time())))
    log.write("System testing at " + localtime + "\n")

    # Push to repository
    success = sys.argv[1]
    git(success, systest)
