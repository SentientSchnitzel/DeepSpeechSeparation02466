#!/bin/sh 
#BSUB -q hpc
#BSUB -J python_script
#BSUB -n 4 
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -M 4GB
### wall-time 1 hr
#BSUB -W 1:00 
#BSUB -u simondanielschneider@gmail.com
#BSUB -N

### Doesnt overwrite, just makes new. 
#BSUB -o Output_%J.out 
#BSUB -e Error_%J.err

module load pandas

### Write which script to run below
python3 test_create_csv.py