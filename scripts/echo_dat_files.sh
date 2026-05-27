#!/bin/bash
# Script to concatenate all unfiltered dat files from a given directory. Add in Record Node to grab files from, e.g.:
# >> bash cat_dat_files.sh 104
# This will grab all files from Record Node 104

# This works well but isn't flexible in case the record node changes
find ./ -type f -wholename '**/Record Node '$1'/**/*continuous.dat' | sort -t'/'  -k2,2
