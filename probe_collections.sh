#!/bin/bash

# Run main.py for various collections
#collections=("landsat_ot_c2_l1" "landsat_ot_c2_l2" "reanalysis-era5-single-levels" "reanalysis-era5-pressure-levels" "reanalysis-era5-land")
#
#for collection in "${collections[@]}"; do
#    python main.py -c "$collection"
#    echo $?
#done

python main.py -c landsat_ot_c2_l1 -o 84
python main.py -c landsat_ot_c2_l2 -o 84
python main.py -c reanalysis-era5-single-levels -o 24
python main.py -c reanalysis-era5-pressure-levels -o 24
python main.py -c reanalysis-era5-land -o 24
