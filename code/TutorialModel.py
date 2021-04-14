from torch.optim import Adam
from torch.utils.data import DataLoader
import pytorch_lightning as pl

from asteroid.data import LibriMix
from asteroid.engine.system import System
from asteroid.losses import PITLossWrapper, pairwise_neg_sisdr
from asteroid import ConvTasNet

train_set, val_set = LibriMix.mini_from_download(task='sep_clean')
train_loader = DataLoader(train_set, batch_size=4, drop_last=True)
val_loader = DataLoader(val_set, batch_size=4, drop_last=True)

# Define model and optimizer (one repeat to be faster)
model = ConvTasNet(n_src=2, n_repeats=3)
optimizer = Adam(model.parameters(), lr=1e-3)
# Define Loss function.
loss_func = PITLossWrapper(pairwise_neg_sisdr, pit_from='pw_mtx')
# Define System
system = System(model=model, loss_func=loss_func, optimizer=optimizer,
                train_loader=train_loader, val_loader=val_loader)
# Define lightning trainer, and train
trainer = pl.Trainer(fast_dev_run=True)
trainer.fit(system)



# Nico og Kristine er seje rejer !!!