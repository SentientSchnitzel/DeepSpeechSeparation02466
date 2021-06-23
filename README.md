## Prerequisites
This project was built on python 3.7.7 \
Assert that the python version for use is not 3.8 or later - optimally same version. \
[python 3.7.7](https://www.python.org/downloads/release/python-377/)

Make sure that Microsoft C++ Build Tools 14.0+ is installed. \
[Most recent build tools installer](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Make sure you can run shell scripts (.sh) \

Otherwise, download Windows git bash \
[git bash](https://git-scm.com/download/win)


## Installation
Clone the repo and run the bash script [installation.sh](./reproduce_project/installation.sh). \
This contains the installation of the modified Asteroid and the default ESPnet.
```bash
# Clone repo
git clone https://github.com/SentientSchnitzel/...

# Then run installation.sh in command prompt or editor
installation.sh
```




### Downloading the dataset
The project relies on Libri2Mix with sample rate 8k, max-mode and train-100.\
To only get this dataset (~60GB) and not the full LibriMix (~500GB), the [data generation script](./reproduce_project/asteroid/ConvTasNet/LibriMix/generate_librimix.sh) has been modified to only create the necessary training and test sets.

Instructions on wget for downloading from webpages \
https://builtvisible.com/download-your-website-with-wget/


[dataset](https://nordictankers-my.sharepoint.com/:f:/g/personal/ksc_molnt_com/EplfAMci9nRAgLZIz8pHUL4BoDk6edAWpkhlQFXSptFswA?e=5%3aLP5BRj&at=9)

Password: SpeechProject2021

### Common problems
Assert that packages fulfill the hard requirement:
```
torch==1.8.1
torchaudio==0.8.1
```
