from ViPrøver import *
train = True
if train == True:
    train, val = loader()
    model = model_train(train, val)

wav = "./twoSpeakers.wav"
model.separate(wav, force_overwrite=True)

