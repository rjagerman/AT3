#!/bin/bash
# Copyright (c) Rolf Jagerman, Laurens Versluis and Martijn de Vos, 2014.
# This script first checks if certain folders and files exist. It first builds kivy and then the whole app (after kivy is set) because of some error with binaries.
# The main and build functions should be reviewed first.

# Load configuration
source configuration
rm -r "${APPNAME}/main.pyo"
rm -r "${APPNAME}/service/main.pyo"
source functions.sh

main
