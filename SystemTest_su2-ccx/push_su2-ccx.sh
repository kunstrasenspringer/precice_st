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
date >> log_su2-ccx

# version of Ubunutu
Ubuntu_Version="Ubuntu version: 16.04"
echo $Ubuntu_Version >> log_of-of

# version of preCICE
PRECICE_VERSION=$(git ls-remote --tags https://github.com/precice/precice.git | tail -1)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> log_su2-ccx

# version of SU2
SU2_VERSION=v6.0.0
SU2_VERSION="su2_version: "$SU2_VERSION
echo $SU2_VERSION >> log_su2-ccx

# version of SU2-adapter
SU2_ADAPTER_VERSION=$(git ls-remote https://github.com/precice/su2-adapter.git | tail -1)
SU2_ADAPTER_VERSION="su2-adapter version: "$SU2_ADAPTER_VERSION
echo $SU2_ADAPTER_VERSION >> log_su2-ccx

# version of CalculiX
CALCULIX_VERSION="calculix_version: 2.13"
echo $CALCULIX_VERSION >> log_su2-ccx

# version of CalculiX-adapter
CCX_ADAPTER_VERSION=$(git ls-remote https://github.com/precice/calculix-adapter.git | tail -1)
CCX_ADAPTER_VERSION="calculix-adapter version: "$CCX_ADAPTER_VERSION
echo $CCX_ADAPTER_VERSION >> log_su2-ccx

# version of tutorials
TUTORIALS_VERSION=$(git ls-remote https://github.com/precice/tutorials.git | tail -1)
TUTORIALS_VERSION="tutorials version: "$TUTORIALS_VERSION
echo $TUTORIALS_VERSION >> log_su2-ccx


setup_git() {
  git config --local user.email "travis@travis-ci.org"
  git config --local user.name "Travis CI"
}

commit_files() {
  git pull --allow-unrelated-histories
  git checkout master
  if [ -d "$output" ]
  then
      git add $output log_su2-ccx
      git commit -m "Output!=Ref $TRAVIS_BUILD_NUMBER" -m "$Ubuntu_Version,
			$PRECICE_VERSION,
      $SU2_VERSION,
      $SU2_ADAPTER_VERSION,
      $CALCULIX_VERSION,
      $CCX_ADAPTER_VERSION,
      $TUTORIALS_VERSION,
			$Date"
  else
      git add log_su2-ccx
      git commit -m "Output==Ref $TRAVIS_BUILD_NUMBER" -m "$Ubuntu_Version,
			$PRECICE_VERSION,
      $SU2_VERSION,
      $SU2_ADAPTER_VERSION,
      $CALCULIX_VERSION,
      $CCX_ADAPTER_VERSION,
      $TUTORIALS_VERSION,
			$Date"
  fi
}

upload_files() {
  git remote set-url origin https://${GH_TOKEN}@github.com/kunstrasenspringer/travis_test.git > /dev/null 2>&1
	git pull --allow-unrelated-histories
	git push --quiet --set-upstream origin master
}

setup_git
commit_files
upload_files
