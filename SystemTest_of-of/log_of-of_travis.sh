#!/bin/sh
# saving version numbers of used software in variables. Variables will be used
# later in git comment. Version numbers are in file: log_of-of
if [ -e "log_of-of" ]; then
  PRECICE_VERSION=$(sed '1!d' log_of-of)
  OF_VERSION=$(sed '2!d' log_of-of)
  OF_ADAPTER_VERSION=$(sed '3!d' log_of-of)
fi
