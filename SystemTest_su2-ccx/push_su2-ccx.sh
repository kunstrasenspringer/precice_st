#!/bin/sh
# pushes generated output files back to github, if output files != ref files
output=$1

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git fetch
  git checkout master
  git add $output
  git commit -m "Output!=Ref $TRAVIS_BUILD_NUMBER" -m "$PRECICE_VERSION,
  $SU2_VERSION,
  $SU2_ADAPTER_VERSION,
  $CALCULIX_VERSION,
  $CCX_ADAPTER_VERSION,
  $TUTORIALS_VERSION"
}

upload_files() {
  git remote set-url origin https://${GH_TOKEN}@github.com/kunstrasenspringer/travis_test.git > /dev/null 2>&1
  git push --quiet --set-upstream origin master
}

if [ -d "$output" ]; then
  setup_git
  commit_files
  upload_files
fi
