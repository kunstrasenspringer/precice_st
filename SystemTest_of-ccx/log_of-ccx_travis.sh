#!/bin/sh
# saving version numbers of used software in variables. Variables will be used
# later in git comment. Version numbers are in file: log_of-ccx
if [ -e "log_of-ccx" ]; then
  PRECICE_VERSION=$(sed '1!d' log_of-ccx)
  OF_VERSION=$(sed '2!d' log_of-ccx)
  OF_ADAPTER_VERSION=$(sed '3!d' log_of-ccx)
  CALCULIX_VERSION=$(sed '4!d' log_of-ccx)
  CCX_ADAPTER_VERSION=$(sed '5!d' log_of-ccx)
  TUTORIALS_VERSION=$(sed '6!d' log_of-ccx)
fi
