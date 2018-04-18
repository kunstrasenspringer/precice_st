#!/bin/sh
# Saving used sofware version in a log file

# log file
touch log_of-ccx

# version of preCICE
cd /home/alice/precice/
PRECICE_VERSION=$(git describe --tags)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> /home/alice/log_of-ccx

# version of OpenFOAM
OF_version=$(sed '1!d' /opt/openfoam*/.build)
OF_version="OpenFOAM version: "$OF_version
echo $OF_version >> /home/alice/log_of-ccx

# version of OpenFOAM-adapter
cd /home/alice/openfoam-adapter
OF_Adapter_ver=$(git describe --tags)
OF_Adapter_ver="OpenFOAM-adapter version: "$OF_Adapter_ver
echo $OF_Adapter_ver >> /home/alice/log_of-ccx

# version of CalculiX
CALCULIX_VERSION="calculix_version: 2.12"
echo $CALCULIX_VERSION >> /home/alice/log_of-ccx

# version of CalculiX-adapter
cd /home/alice/calculix-adapter/
CCX_ADAPTER_VERSION=$(git rev-parse HEAD)
CCX_ADAPTER_VERSION="calculix-adapter_commit_version: "$CCX_ADAPTER_VERSION
echo $CCX_ADAPTER_VERSION >> /home/alice/log_of-ccx

# version of tutorials
cd /home/alice/tutorials/
TUTORIALS_VERSION=$(git rev-parse HEAD)
TUTORIALS_VERSION="calculix-adapter_commit_version: "$TUTORIALS_VERSION
echo $TUTORIALS_VERSION >> /home/alice/log_of-ccx
