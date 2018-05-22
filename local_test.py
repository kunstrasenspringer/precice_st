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

# Parsing flags
parser = argparse.ArgumentParser(description='Build local.')
parser.add_argument('-b', '--branch', help="choose branch you want to use for preCICE (default: develop branch)")
parser.add_argument('-s', '--systemtest', nargs='+', help="choose system tests you want to use (default: all tests)")
args = parser.parse_args()

if __name__ == "__main__":
    print "\n\nBuilding preCICE docker image with choosen branch\n\n"
    branch = "develop"
    if args.branch:
        branch=args.branch
    try:
        subprocess.call("docker build -f Dockerfile.precice -t precice --build-arg branch="+branch+" .", shell=True)
    except:
        raise Exception('Building preCICE with choosen branch docker image failed!')

    tests=['of-of', 'of-ccx', 'su2-ccx']
    if args.systemtest:
        tests=args.systemtest
    failed = []
    success = []
    for x in tests:
        print "\n\nStarting system test %s\n\n" % x
        try:
            subprocess.call("python system_testing.py --local -s " + x, shell=True)
            success.append(x)
        except:
            failed.append(x)

    print "\n\n\n\n\nLocal build finished.\n"
    if success:
        print "Following system tests succeeded: "
        print ", ".join(success)
        print '\n'
    if failed:
        print "Following system tests failed: "
        print ", ".join(failed)
        print '\n'

    answer = raw_input("Do you want to push the results (logfiles and possibly output files) to the output repo? (yes/no)\n")
    if answer=='yes' or answer=='y':
        for x in success:
            subprocess.call("python push.py -s -t " + x + " -b " + args.branch, shell=True)
        for y in failed:
            subprocess.call("python push.py -t " + y + " -b " + args.branch, shell=True)
