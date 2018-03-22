#!/bin/sh
touch log_su2-ccx

PRECICE_VERSION=$(command grep -m1 '##[^"]*' /home/alice/precice/CHANGELOG.md)
PRECICE_VERSION="precice_version: "$PRECICE_VERSION
echo $PRECICE_VERSION >> log_su2-ccx

cd /home/alice/su2-source
SU2_VERSION=$(git describe --tags)
SU2_VERSION="su2_version: "$SU2_VERSION
echo $SU2_VERSION >> /home/alice/log_su2-ccx

cd /home/alice/su2-adapter/
SU2_ADAPTER_VERSION=$(git rev-parse HEAD)
SU2_ADAPTER_VERSION="su2-adapter_commit_version: "$SU2_ADAPTER_VERSION
echo $SU2_ADAPTER_VERSION >> /home/alice/log_su2-ccx

CALCULIX_VERSION="calculix_version: 2.13"
echo $CALCULIX_VERSION >> /home/alice/log_su2-ccx

cd /home/alice/calculix-adapter/
CCX_ADAPTER_VERSION=$(git rev-parse HEAD)
CCX_ADAPTER_VERSION="calculix-adapter_commit_version: "$CCX_ADAPTER_VERSION
echo $CCX_ADAPTER_VERSION >> /home/alice/log_su2-ccx











#source log.sh
#PRECICE_VERSION=$(command grep -m1 '##[^"]*' /home/kunst/tmp/test/doc)
#PRECICE_VERSION="precice_version: "$PRECICE_VERSION
