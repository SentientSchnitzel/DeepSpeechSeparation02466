#!/bin/sh
#BSUB -q gpuv100
#BSUB -J 1c_eval
exp_dir_out=exp/1c
#BSUB -n 2
#BSUB -R "span[hosts=-1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -M 16GB
#BSUB -gpu "num=2:mode=exclusive_process"
#BSUB -W 24:00
#BSUB -u simondanielschneider@gmail.com
#BSUB -N

#BSUB -o outputs/o_1c_eval_%J.out
#BSUB -e errors/e_1c_eval_%J.err

source act-venv.sh
module load python3/3.7.7
module load cuda/11.3

python eval.py --exp_dir $exp_dir_out
