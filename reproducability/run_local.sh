#!/bin/bash
set -e
set -o pipefail

model=1c

exp_dir=exp/$model
conf_path="conf_$model.yml"

python train.py --exp_dir $exp_dir --conf_path $conf_path

python eval.py --exp_dir $exp_dir