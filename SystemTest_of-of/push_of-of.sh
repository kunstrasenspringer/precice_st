#!/bin/sh
# pushes generated output files back to github, if output files != ref files
output=$1

# Saving used sofware version in a log file
# log file
if [ -f log_su2-ccx ]
then
	rm log_su2-ccx
else
	touch log_su2-ccx
fi

Date=$(date)
date >> log_of-of

# version of preCICE
PRECICE_VERSION=$(git ls-remote --tags https://github.com/precice/precice.git | cut -d/ -f3 | sort -Vu | tail -1)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> log_of-of

# version of OpenFOAM
OF_VERSION="OpenFOAM version: 4.1"
echo $OF_VERSION >> log_of-of

# version of Ubunutu
Ubuntu_Version="Ubuntu version: 16.04"
echo $Ubuntu_Version >> log_of-of

# version of OpenFOAM-adapter
OF_ADAPTER_VERSION=$(git ls-remote https://github.com/precice/calculix-adapter.git  | cut -d/ -f3 | sort -Vu | tail -1)
OF_ADAPTER_VERSION="OpenFOAM-adapter version: "$OF_ADAPTER_VERSION
echo $OF_ADAPTER_VERSION >> log_of-of

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git pull
  git checkout master
  if [ -d "$output" ]
  then
      git add log_of-of $output
			git commit -m "Output!=Ref $TRAVIS_BUILD_NUMBER" -m "$Ubuntu_Version,
			$PRECICE_VERSION,
			$OF_VERSION,
			$OF_ADAPTER_VERSION,
			$Date"
  else
      git add log_of-of
			git commit -m "Output==Ref $TRAVIS_BUILD_NUMBER" -m "$Ubuntu_Version,
			$PRECICE_VERSION,
			$OF_VERSION,
			$OF_ADAPTER_VERSION,
			$Date"
  fi
}

upload_files() {
  git remote set-url origin https://${GH_TOKEN}@github.com/kunstrasenspringer/travis_test.git > /dev/null 2>&1
	git pull
	git push --quiet --set-upstream origin master
}

setup_git
commit_files
upload_files
