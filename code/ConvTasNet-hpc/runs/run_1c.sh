#!/bin/sh
#BSUB -q gpuv100
#BSUB -J 1c
exp_dir_out=exp/1c
conf_path=conf_1c.yml
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=24GB]"
#BSUB -R "select[gpu32gb]"
#BSUB -M 32GB
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 24:00 
#BSUB -u simondanielschneider@gmail.com
#BSUB -N

#BSUB -o output_errors/Output_%J.out
#BSUB -e output_errors/Error_%J.err

source act-venv.sh
module load python3/3.8.9
module load cuda/11.3

python train.py --exp_dir $exp_dir_out --conf_path $conf_path
