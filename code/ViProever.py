
# Asteroid is based on PyTorch and PyTorch-Lightning.
from torch import optim
from pytorch_lightning import Trainer

# We train the same model architecture that we used for inference above.
from asteroid.models import ConvTasNet

# In this example we use Permutation Invariant Training (PIT) and the SI-SDR loss.
from asteroid.losses import pairwise_neg_sisdr, PITLossWrapper

# MiniLibriMix is a tiny version of LibriMix (https://github.com/JorisCos/LibriMix),
# which is a free speech separation dataset.
from asteroid.data import LibriMix

# Asteroid's System is a convenience wrapper for PyTorch-Lightning.
from asteroid.engine import System


def loader():
    # This will automatically download MiniLibriMix from Zenodo on the first run.
    train_loader, val_loader = LibriMix.loaders_from_mini(task="sep_clean", batch_size=4)
    return train_loader, val_loader

def model_train(train_loader, val_loader):
    model = ConvTasNet(n_src=2) # use ConvTasNet

    loss = PITLossWrapper(pairwise_neg_sisdr, pit_from="pw_mtx")
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    system = System(model, optimizer, loss, train_loader, val_loader)

    trainer = Trainer(max_epochs=1, gpus=1)
    trainer.fit(system)

    return model

if __name__ == "__main__":
    train = True
    if train == True:
        train, val = loader()
        model = model_train(train, val)

    wav = "twoSpeakers.wav"
    model.separate(wav, force_overwrite=True)
