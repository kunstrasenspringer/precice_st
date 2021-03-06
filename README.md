# precice_st
Design und Implementation of system tests for the distributed multi-physics simulation package preCICE

# preCICE
- Dockerfile.precice docker image with ubuntu 16.04 and preCICE
[preCICE - github](https://github.com/precice)

# System tests
- Dockerfile.su2-ccx coupled simulation with SU2 and CalculiX
[FSI tutorial](https://github.com/precice/precice/wiki/FSI-tutorial)
- Dockerfile.of-of coupled simulation with OpenFOAM
[Tutorial for CHT: Flow over a heated plate](https://github.com/precice/openfoam-adapter/wiki/Tutorial-for-CHT:-Flow-over-a-heated-plate)
- Dockerfile.of-ccx conjugate heat transfer simulation with OpenFOAM and CalculiX
[Tutorial for CHT with OpenFOAM and CalculiX](https://github.com/precice/precice/wiki/Tutorial-for-CHT-with-OpenFOAM-and-CalculiX)

# travis.yml
Continuous Integration config.
Two [build stages](https://docs.travis-ci.com/user/build-stages/):
- stage 1 (build stage): precice docker image build and pushed to [Docker Hub](https://hub.docker.com/r/kunstrasenspringer/precice/)
- stage 2 (testing stage): build su2-ccx, of-of, of-ccx and push outputfiles to repo

# compare_*.py
Python script to compare reference data with output data.

# ref_*
Reference files.

# Others
- Makefile_*: needed to build calculix-adapter in Dockerfile.su2-ccx and Dockerfile.of-ccx
- push_*: script to push outputfiles back to rep [HowTo](https://gist.github.com/willprice/e07efd73fb7f13f917ea#file-push-sh)
- How to push to [hub.docker.com](https://hub.docker.com/) [link1](https://docs.travis-ci.com/user/docker/#Pushing-a-Docker-Image-to-a-Registry) [link2](https://docs.travis-ci.com/user/build-stages/share-docker-image/)
- log_*: script to log infomation about the build

# Status
[![Build Status](https://travis-ci.org/kunstrasenspringer/precice_st.svg?branch=develop)](https://travis-ci.org/kunstrasenspringer/precice_st)
