#!/bin/sh
# Saving used sofware version in a log file

# log file
touch log_su2-ccx

# version of preCICE
cd /precice/
PRECICE_VERSION=$(git describe --tags)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> /log_su2-ccx

# version of SU2
cd /su2-source
SU2_VERSION=$(git describe --tags)
SU2_VERSION="su2_version: "$SU2_VERSION
echo $SU2_VERSION >> /log_su2-ccx

# version of SU2-adapter
cd /su2-adapter/
SU2_ADAPTER_VERSION=$(git rev-parse HEAD)
SU2_ADAPTER_VERSION="su2-adapter_commit_version: "$SU2_ADAPTER_VERSION
echo $SU2_ADAPTER_VERSION >> /log_su2-ccx

# version of CalculiX
CALCULIX_VERSION="calculix_version: 2.13"
echo $CALCULIX_VERSION >> /log_su2-ccx

# version of CalculiX-adapter
cd /calculix-adapter/
CCX_ADAPTER_VERSION=$(git rev-parse HEAD)
CCX_ADAPTER_VERSION="calculix-adapter_commit_version: "$CCX_ADAPTER_VERSION
echo $CCX_ADAPTER_VERSION >> /log_su2-ccx

# version of tutorials
cd /tutorials/
TUTORIALS_VERSION=$(git rev-parse HEAD)
TUTORIALS_VERSION="calculix-adapter_commit_version: "$TUTORIALS_VERSION
echo $TUTORIALS_VERSION >> /log_su2-ccx
