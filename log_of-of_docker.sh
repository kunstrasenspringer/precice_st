#!/bin/sh
# Saving used sofware version in a log file

# log file
touch log_su2-ccx

# version of preCICE
cd /home/alice/precice/
PRECICE_VERSION=$(git describe --tags)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> /home/alice/log_of-of

# version of OpenFOAM
OF_version=$(sed '1!d' /opt/openfoam*/.build)
OF_version="OpenFOAM version: "$OF_version
echo $OF_version >> /home/alice/log_of-of

# version of OpenFOAM-adapter
cd /home/alice/openfoam-adapter
OF_Adapter_ver=$(git describe --tags)
OF_Adapter_ver="OpenFOAM-adapter version: "$OF_Adapter_ver
echo $OF_Adapter_ver >> /home/alice/log_of-of
