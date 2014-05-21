#!/bin/bash
# Copyright (c) Rolf Jagerman, Laurens Versluis and Martijn de Vos, 2014.
# This script first checks if certain folders and files exist. It first builds kivy and then the whole app (after kivy is set) because of some error with binaries.
# The main and build functions should be reviewed first.

# Load variables
source buildconfig.conf
source functions.sh

# Call the main method from the functions script.
main
