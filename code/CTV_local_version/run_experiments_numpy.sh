#!/bin/sh
bsub -n 1 < submit_numpy.sh
bsub -n 2 < submit_numpy.sh
bsub -n 4 < submit_numpy.sh
bsub -n 8 < submit_numpy.sh
bsub -n 16 < submit_numpy.sh
