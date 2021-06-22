
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

download git bash
https://git-scm.com/download/win

[dataset](https://nordictankers-my.sharepoint.com/personal/ksc_molnt_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fksc%5Fmolnt%5Fcom%2FDocuments%2FSHARED%2FSIMONS&originalPath=aHR0cHM6Ly9ub3JkaWN0YW5rZXJzLW15LnNoYXJlcG9pbnQuY29tLzpmOi9nL3BlcnNvbmFsL2tzY19tb2xudF9jb20vRXBsZkFNY2k5blJBZ0xaSXo4cEhVTDRCb0RrNmVkQVdwa2hsUUZYU3B0RnN3QT9ydGltZT11bEhrVXNnMTJVZw)
