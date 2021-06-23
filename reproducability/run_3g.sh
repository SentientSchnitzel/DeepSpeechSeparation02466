#!/bin/sh
#BSUB -q gpuv100
#BSUB -J 3g_train
exp_dir_out=exp/3g
conf_path=conf_3g.yml
#BSUB -n 2
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4G]"
#BSUB -R "select[gpu32gb]"
#BSUB -M 10GB
#BSUB -gpu "num=2:mode=exclusive_process"
#BSUB -W 24:00
#BSUB -u simondanielschneider@gmail.com
#BSUB -N

#BSUB -o outputs/o_3g_train_%J.out 
#BSUB -e errors/e_3g_train_%J.err

source act-venv.sh
module load python3/3.7.7
module load cuda/11.3

python train.py --exp_dir $exp_dir_out --conf_path $conf_path