#!/bin/sh
# pushes generated output files back to github, if output files != ref files
output=$1

# Saving used sofware version in a log file
# log file
if [ -f log_of-ccx ]
then
	rm log_of-ccx
else
	touch log_of-ccx
fi

Date=$(date)
date >> log_of-ccx

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

# version of preCICE
PRECICE_VERSION=$(git ls-remote --tags https://github.com/precice/precice.git | tail -1)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> log_of-ccx

# version of CalculiX
CALCULIX_VERSION="calculix_version: 2.12"
echo $CALCULIX_VERSION >> log_of-ccx

# version of CalculiX-adapter
CCX_ADAPTER_VERSION=$(git ls-remote https://github.com/precice/calculix-adapter.git | tail -1)
CCX_ADAPTER_VERSION="calculix-adapter version: "$CCX_ADAPTER_VERSION
echo $CCX_ADAPTER_VERSION >> log_of-ccx

# version of tutorials
TUTORIALS_VERSION=$(git ls-remote https://github.com/precice/tutorials.git | tail -1)
TUTORIALS_VERSION="tutorials version: "$TUTORIALS_VERSION
echo $TUTORIALS_VERSION >> log_of-ccx


setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git pull
  git checkout master
  if [ -d "$output" ]
  then
      git add $output log_of-ccx
      git commit -m "Output!=Ref $TRAVIS_BUILD_NUMBER" -m "$Ubuntu_Version,
      $PRECICE_VERSION,
      $OF_VERSION,
      $OF_ADAPTER_VERSION,
      $CALCULIX_VERSION,
      $CCX_ADAPTER_VERSION,
      $TUTORIALS_VERSION,
			$Date"
  else
      git add log_of-ccx
      git commit -m "Output==Ref $TRAVIS_BUILD_NUMBER" -m "$Ubuntu_Version,
      $PRECICE_VERSION,
      $OF_VERSION,
      $OF_ADAPTER_VERSION,
      $CALCULIX_VERSION,
      $CCX_ADAPTER_VERSION,
      $TUTORIALS_VERSION,
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
