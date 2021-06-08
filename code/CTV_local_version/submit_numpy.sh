#!/bin/sh
#BSUB -J numpy
#BSUB -o numpy_%J.out
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=1G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 10
#BSUB -u simondanielschneider@gmail.com
#BSUB -B
#BSUB -N	
# end of BSUB options

# load a scipy module
# replace VERSION and uncomment
# module load scipy/

# set the number of threads used by OpenBLAS (called from numpy)
export OPENBLAS_NUM_THREADS=$LSB_DJOB_NUMPROC

python3 matmul_numpy.py
