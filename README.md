
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
