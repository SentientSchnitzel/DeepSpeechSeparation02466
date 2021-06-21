#!/bin/bash

# Exit on error
set -e
set -o pipefail

# Storage must be same in this script as in the 'run' script.
# this is where data will be loaded to
storage_dir=../dataset

#echo $storage_dir
#sleep 5

sample_rate=8000
mode=max
n_src=2
task=sep_clean

. utils/parse_options.sh

sr_string=$(($sample_rate/1000))
suffix=wav${sr_string}k/$mode

if [ -z "$eval_mode" ]; then
  eval_mode=$mode
fi

train_dir=data/$suffix/train-100 # changed from default train-360
valid_dir=data/$suffix/dev
test_dir=data/wav${sr_string}k/$eval_mode/test


echo "Stage 0: Generating Librimix dataset"
. local/generate_librimix.sh --storage_dir $storage_dir --n_src $n_src
