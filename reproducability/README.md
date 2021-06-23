## Prerequisites
This project was built on python 3.7.7 \
Assert that the python version in use is not 3.8 or later - optimally same version (python 3.7.7). \
Get it from here [python 3.7.7](https://www.python.org/downloads/release/python-377/)
In addition, we recommend creating a virtual environment for this project.
```
# install virtualenv
pip install virtualenv
```

Make sure that Microsoft C++ Build Tools 14.0+ is installed. \
[Most recent build tools installer](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Make sure you can run shell scripts (.sh) \

Otherwise, download Windows git bash \
[git bash](https://git-scm.com/download/win)


## Installation
Clone the repo, create virtualenv and activate it, 
then run the bash script [installation.sh](./reproduce_project/installation.sh) for installing all required packages\
This contains the installation of the modified Asteroid and the default ESPnet.
```bash
# Clone repo
git clone https://github.com/SentientSchnitzel/DeepSpeechSeparation02466

# create virtual environment
python -m virtualenv venv

# activate
cd venv/Scripts/ # or similar on unix: venv/bin
activate

# Enter root dir (DeepSpeechSeparation02466)
# Then run installation.sh in command prompt or editor
installation.sh
```


### Downloading the dataset
The project relies on Libri2Mix with sample rate 8k, max-mode and train-100.\
To only get this dataset (~60GB) and not the full LibriMix (~500GB), the [data generation script](./reproduce_project/asteroid/ConvTasNet/LibriMix/generate_librimix.sh) has been modified to only create the necessary training and test sets.

Instructions on wget for downloading from webpages \
https://builtvisible.com/download-your-website-with-wget/

The following link contains the directory "Data" (~25GB) under the directory "SIMONS". Password is SpeechProject2021   
[SIMONS](https://nordictankers-my.sharepoint.com/:f:/g/personal/ksc_molnt_com/EplfAMci9nRAgLZIz8pHUL4BoDk6edAWpkhlQFXSptFswA?e=5%3aLP5BRj&at=9)

Extract from the zip-container directory "Libri2Mix" and set it as the child-directory of "DeepSpeechSeparation02466" \
The folder structure should look like:

```
├── data/
│   ├── wav8k/
│       ├── max/
│           ├── dev/
│           .
│           .
│   └── test_annotations.csv
├── exp/
├── libri2Mix/
│   └── wav8k/
│       └── max/
│           ├── dev/
│               ├── mix_both
│               ├── mix_clean
│               .
│               .
├── local/
README.md
.
.
.
```

## Running the scripts
To run the scripts ``train.py`` and ``eval.py``, provide them each with the following:
experiment directory (exp/...) and conf_path (conf_....yml)

### Example
```
# training
python train.py --exp_dir exp/1c --conf_path conf_1c.yml

# evaluation
python eval.py --exp_dir exp/1c

# evaluation with GPU
python eval.py --exp_dir exp/1c --use_gpu 1
```

Run ``run_local.sh`` to run a full experiment of training and evaluation for one model. (can be changed in the shell script)

Finally run ``results_and_visualization.py`` for creation of all tables (in .csv) and plots (in .png)

### Our setup
Our project used a remote UNIX based system for submitting jobs for remote computing. \
Bash scripts containing what was run, and what was the configurations can be found in the bash scripts \
``run_1c...3g.sh`` and ``run_eval_1c...3g.sh`` 

The directory "our_project_results" contains the visuals and table-data for the report. \
It also contains the models that were trained and of course all metrics aswell.

### Common problems
Assert that packages fulfill the hard requirement: (torch can complain about Iterator objects...)
```
torch==1.8.1
torchaudio==0.8.1
```
