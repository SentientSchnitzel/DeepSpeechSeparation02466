import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
import numpy as np

def multiplot():
    N = 5
    samples = np.empty(shape=(N,2), dtype=object)
    directory = "./MiniLibriMix/train/mix_clean/"

    fig = plt.figure(figsize=(15,7))
    gs = fig.add_gridspec(N, hspace=0)
    # fig, axs = plt.subplots(N, sharex=True, figsize=(15,7))
    axs = gs.subplots(sharex=True, sharey=True)
    for root, dirs, files in os.walk(directory):
        for i, filename in enumerate(files[0:N]):
            data, sample_rate = librosa.load(directory + filename, sr=22050, mono=True, offset=0.0, duration=15,
                                             res_type="kaiser_best")
            axs[i].plot(data)
            axs[i].label_outer()
            # samples[i] = [data, sample_rate]
            # librosa.display.waveplot(data, sr=sample_rate, max_points=5000.0, x_axis="time", offset=0.0, max_sr=1000, alpha=0.3)
            print(f"Here is sample {filename}")
    plt.show()

def splitplot(ID = "17-362-0014_2999-156967-0015.wav"):
    # ID = "17-362-0014_2999-156967-0015.wav"
    speak2 = "./MiniLibriMix/train/mix_clean/"
    s1 = "./MiniLibriMix/train/s1/"
    s2 = "./MiniLibriMix/train/s2/"
    dirs = [s1,s2]
    sr = 0
    samples = np.empty(2, dtype=object)
    for i, dir in enumerate(dirs):
        samples[i], sr = librosa.load(dir+ID, duration=30)

    fig = plt.figure(figsize=(15,7))
    gs = fig.add_gridspec(3, hspace=0)
    axs = gs.subplots(sharex=True, sharey=True)
    axs[0].plot(samples[0], color="blue", alpha=0.3)
    axs[0].plot(samples[1], color="red", alpha=0.3)
    axs[1].plot(samples[0], color="blue", alpha=0.7)
    axs[2].plot(samples[1], color="red", alpha=0.7)

    n = len(samples[0])
    plt.yticks([-0.2,0,0.2])
    ticcs = np.arange(0,n+sr+1, sr)
    seconds = [int(num) for num in np.arange(n/sr+1)]
    plt.xticks(ticcs, seconds) # define tickposition and label in seconds.
    # seconds = np.arange(n/sr+1) #float
    for ax in axs:
        ax.label_outer()
    fig.text(0.5, 0.04, "Time (seconds)", ha="center")
    fig.text(0.08, 0.5, "Amplitude (dB)", va="center", rotation="vertical")
    plt.show()

N=10
directory = "./MiniLibriMix/train/mix_clean/"
wavs = np.zeros(10, dtype=object)
for root, dirs, files in os.walk(directory):
    for i, filename in enumerate(files[0:N]):
        wavs[i] = filename
splitplot(wavs[0])
