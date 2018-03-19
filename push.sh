#!/bin/sh
output=$1

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git fetch
  git checkout master
  git add $output
  git commit --message "$ref updated: $TRAVIS_BUILD_NUMBER"
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
