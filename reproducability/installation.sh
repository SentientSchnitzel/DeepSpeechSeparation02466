#!/bin/bash

# Install "special" version of asteroid, modified to accept CUDA in WER eval.
# cd ./asteroid
python -m pip install -e .
# cd ..

# Install regular versions of packages.
python -m pip install -r requirements.txt