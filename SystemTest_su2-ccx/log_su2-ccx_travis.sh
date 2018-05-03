#!/bin/sh
# saving version numbers of used software in variables. Variables will be used
# later in git comment. Version numbers are in file: log_su2-ccx
if [ -e "log_su2-ccx" ]; then
  PRECICE_VERSION=$(sed '1!d' log_su2-ccx)
  SU2_VERSION=$(sed '2!d' log_su2-ccx)
  SU2_ADAPTER_VERSION=$(sed '3!d' log_su2-ccx)
  CALCULIX_VERSION=$(sed '4!d' log_su2-ccx)
  CCX_ADAPTER_VERSION=$(sed '5!d' log_su2-ccx)
  TUTORIALS_VERSION=$(sed '6!d' log_su2-ccx)
fi
