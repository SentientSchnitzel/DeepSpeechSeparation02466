#!/bin/bash
#BSUB -q hpc
#BSUB -J python_script
#BSUB -n 4 
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=16GB]"
#BSUB -M 20GB
### wall-time 24 hr
#BSUB -W 24:00 
#BSUB -u simondanielschneider@gmail.com
#BSUB -N

### Doesnt overwrite, just makes new. 
#BSUB -o Output_%J.out 
#BSUB -e Error_%J.err

module load python3/3.8.9
module load cuda/11.3
# module load pandas/1.2.4-python-3.8.9

ckpt=

### Write which script to run below
python3 train.py --resume_path $ckpt