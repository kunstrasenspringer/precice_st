"""Script for testing on the local machine.

This script allows to build preCICE with a branch choosen by the user, execute
all or choosen system tests and allows to push the results to the output repository
of preCICE system test.

    Example:
        Example to use preCICE branch "master" and only system tests "of-of" and "su2-ccx":

            $ python local_test.py --branch=master --systemtest of-of su2-ccx
"""

import subprocess
import argparse
import os

# Parsing flags
parser = argparse.ArgumentParser(description='Build local.')
parser.add_argument('-b', '--branch', help="choose branch you want to use for preCICE (default: develop branch)")
parser.add_argument('-s', '--systemtest', nargs='+', help="choose system tests you want to use (default: all tests)")
args = parser.parse_args()

if __name__ == "__main__":
    tests=['of-of', 'of-ccx', 'su2-ccx']
    if args.systemtest:
        tests=args.systemtest

    # Checking for older docker images
    devnull = open(os.devnull, 'w')
    lst1 = list(( x for x in tests if subprocess.call("docker image ls | grep " + x, shell=True, stdout=devnull) == 0))
    if subprocess.call("docker image ls | grep precice", shell=True, stdout=devnull) == 0:
        lst1.append('precice')
    if lst1:
        print "Deleting following docker images:\n"
        for x in lst1:
            subprocess.call("docker image ls | grep " + x, shell=True)
        answer = raw_input("\nOk? (yes/no)\n")
        if answer=="yes" or answer=="y":
            for x in lst1:
                subprocess.call("docker rmi -f " + x, shell=True)
        else:
            print "BE CAREFUL!: Not deleting previous images can later lead to problems.\n\n"
    # Checking for older docker containers
    lst2 = list(( x for x in tests if subprocess.call("docker ps -a | grep " + x + "_container", shell=True, stdout=devnull) == 0))
    if lst2:
        print "Deleting following docker containers\n"
        for x in lst2:
            subprocess.call("docker ps -a | grep " + x + "_container", shell=True)
        answer = raw_input("\nOk? (yes/no)\n")
        if answer=="yes" or answer=="y":
            for x in lst2:
                subprocess.call("docker rm -f " + x + "_container", shell=True)
        else:
            print "BE CAREFUL!: Not deleting previous containers can later lead to problems."

    # Building preCICE
    print "\n\nBuilding preCICE docker image with choosen branch\n\n"
    branch = "develop"
    if args.branch:
        branch=args.branch
    try:
        subprocess.call("docker build -f Dockerfile.precice -t precice --build-arg branch="+branch+" .", shell=True)
    except:
        raise Exception('Building preCICE with choosen branch docker image failed!')

    # Starting system tests
    failed = []
    success = []
    for x in tests:
        print "\n\nStarting system test %s\n\n" % x
        if subprocess.call("python system_testing.py --local -s " + x, shell=True) == 0:
            success.append(x)
        else:
            failed.append(x)

    # Results
    print "\n\n\n\n\nLocal build finished.\n"
    if success:
        print "Following system tests succeeded: "
        print ", ".join(success)
        print '\n'
    if failed:
        print "Following system tests failed: "
        print ", ".join(failed)
        print '\n'

    # Push
    answer = raw_input("Do you want to push the results (logfiles and possibly output files) to the output repo? (yes/no)\n")
    if answer=='yes' or answer=='y':
        for x in success:
            subprocess.call("python push.py -s -t " + x + " -b " + args.branch, shell=True)
        for y in failed:
            subprocess.call("python push.py -t " + y + " -b " + args.branch, shell=True)
