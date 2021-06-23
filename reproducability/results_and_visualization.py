import pandas as pd
pd.set_option("display.precision", 2)

import os
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import random
from statsmodels.api import qqplot
import statsmodels as sm

import seaborn as sns
sns.set_theme()

MODELS = ['1c', '1g', '2c', '2g', '3c', '3g']
metrics = ["SDR", "SI_SDR", "SIR", "WER"]





def confint(data):
    CI = st.t.interval(alpha=0.95,
                  df=len(data)-1,
                  loc=np.mean(data),
                  scale=st.sem(data))
    return CI


def HypothesisTest(data1, data2):
    # t-test for paired data.
    return st.ttest_rel(data1, data2)[1]


def PowerTest(data1: pd.DataFrame, data2: pd.DataFrame, power=True):
    # Power-test - and in extension Cohen's d
    n1, n2 = data1.__len__(), data2.__len__()
    mean1, mean2 = data1.mean(), data2.mean()
    diff_std = (data1-data2).std()
    cohens_d = abs((mean1-mean2) / diff_std)
    analysis = sm.stats.power.TTestPower()
    POWER = analysis.solve_power(effect_size=cohens_d, alpha=0.05, nobs=n1, alternative="two-sided")
    return POWER if power==True else cohens_d


def TheBarPlot(data: pd.DataFrame, metric: str, ax):
    # plots bargraphs of the metrics for each model config
    mean_values = data.mean()
    conf_values = 1.96*data.std()/np.sqrt(data.__len__())
    colors=["pink", "dark pink", "sky blue", "blue", "green", "forest green"]
    colors = ["xkcd:"+color for color in colors]
    ax.bar(range(len(data.columns)), mean_values,
            yerr=conf_values, align='center', alpha=1, color=colors,
            )
    ax.set(xlabel="Model", ylabel=metric)
    ax.set(xticks=range(len(data.columns)))
    ax.set_xticklabels(data.columns)

def CliffsDelta(data1: pd.DataFrame, data2: pd.DataFrame):
    return (sum(data1 > data2) - sum(data1 < data2)) / (data1.__len__() * data2.__len__())

def histo(data: pd.DataFrame, metric: str, model: str, ax):
    ax.hist(data, bins=30, density=True, histtype="stepfilled")
    ax.set(xlabel=model, ylabel=metric)

def QQPlot_regressionline(data: pd.DataFrame, metric: str, model: str, ax):
    qqplot(data, line="r", ax=ax)
    ax.set(xlabel=model, ylabel=metric)


def dataload(exp_dir: str):
    '''
    :param exp_dir: the path where all results from experiments reside.
    load data into lists and convert to DataFrames.
    Uses relative path from where the script is called.

    :return: Returns list of dataframes. Each dataframe is for one metric. Rows are samples, columns are
    model configurations, so each cell corresponds to the value of the dataframe's metric found when using
    the column's model (e.g. dataframe for sdr and column for model 1c)
    '''
    all_sdr = []
    all_si_sdr = []
    all_sir = []
    all_wer = []

    for row, item in enumerate(MODELS):
        csv_path = os.path.join(exp_dir, item, "OUTPUT_EVAL/all_metrics.csv")
        with open(csv_path, "r") as file:
            chosen_metrics = pd.read_csv(file)[["sdr", "si_sdr", "sir", "wer"]]
            all_sdr.append(chosen_metrics["sdr"])
            all_si_sdr.append(chosen_metrics["si_sdr"])
            all_sir.append(chosen_metrics["sir"])
            all_wer.append(chosen_metrics["wer"])

    df_sdr = pd.DataFrame(all_sdr, index=MODELS).T
    df_si_sdr = pd.DataFrame(all_si_sdr, index=MODELS).T
    df_sir = pd.DataFrame(all_sir, index=MODELS).T
    df_wer = pd.DataFrame(all_wer, index=MODELS).T

    dfs = [df_sdr, df_si_sdr, df_sir, df_wer]

    print(f'Completed dataload, list of 3-head() of dataframes below')
    [print(df.head(3)) for df in dfs]
    return dfs


def statistics(dfs):
    '''

    :param dfs:
    :return:
    '''

    # Descriptive statistics - mean and standard deviation
    matrix_mean = np.zeros((6,4))
    matrix_std = np.zeros((6,4))
    for col, data in enumerate(dfs):
        for row, model in enumerate(MODELS):
            matrix_mean[row, col] = data[model].mean()
            matrix_std[row, col] = data[model].std()

    pd.DataFrame(matrix_mean, columns=metrics, index=MODELS).round(4).to_csv("matrix_mean.csv")
    pd.DataFrame(matrix_std, columns=metrics, index=MODELS).round(4).to_csv("matrix_std.csv")


    # Statistical metrics in matrices - for SI-SDR and WER
    df_si_sdr, df_wer = dfs[1], dfs[3]

    p_power_matrix_si_sdr = np.zeros((6,6))
    p_power_matrix_wer = np.zeros((6,6))
    cohen_power_matrix_si_sdr = np.zeros((6,6))
    cohen_power_matrix_wer = np.zeros((6,6))
    for row, model1 in enumerate(MODELS):
        for col, model2 in enumerate(MODELS):
            if col == row:
                # division by zero when data1=data2 - inserts placeholder, will be removed anyway.
                p_power_matrix_si_sdr[row, col] = None
                p_power_matrix_wer[row, col] = None
                cohen_power_matrix_si_sdr[row, col] = None
                cohen_power_matrix_wer[row, col] = None
            elif col > row:
                p_power_matrix_si_sdr[row, col] = PowerTest(df_si_sdr[model1], df_si_sdr[model2])
                p_power_matrix_wer[row, col] = PowerTest(df_wer[model1], df_wer[model2])
                cohen_power_matrix_si_sdr[row, col] = PowerTest(df_si_sdr[model1], df_si_sdr[model2], power=True)
                cohen_power_matrix_wer[row, col] = PowerTest(df_wer[model1], df_wer[model2], power=True)
            else:
                p_power_matrix_si_sdr[row, col] = HypothesisTest(df_si_sdr[model1], df_si_sdr[model2])
                p_power_matrix_wer[row, col] = HypothesisTest(df_wer[model1], df_wer[model2])
                cohen_power_matrix_si_sdr[row, col] = PowerTest(df_si_sdr[model1], df_si_sdr[model2], power=False)
                cohen_power_matrix_wer[row, col] = PowerTest(df_wer[model1], df_wer[model2], power=False)
    # round to 4 decimals, then export to csv
    names = ['p_power_matrix_si_sdr', 'p_power_matrix_wer', 'cohen_power_matrix_si_sdr', 'cohen_power_matrix_wer']
    matrices = [p_power_matrix_si_sdr, p_power_matrix_wer, cohen_power_matrix_si_sdr, cohen_power_matrix_wer]
    for matrix, name in zip(matrices, names):
        pd.DataFrame(matrix, columns=MODELS, index=MODELS).round(4).to_csv(name+".csv")

    # Confidence intervals
    long_CI_list = np.zeros(24, object)
    i = 0
    for data in dfs:
        for metric in data:
            long_CI_list[i] = np.round(confint(data[metric]),2)
            i += 1
    reshaped_CIs = long_CI_list.reshape(4,6).T # reshaping and transposing to match
    CIs = pd.DataFrame(reshaped_CIs, columns=metrics, index=MODELS)
    CIs.to_csv("metrics_CIs.csv")

    print(f'Statistics completed')



def visualization(dfs, savefigs=True):
    '''
    Plots plots

    :param dfs: list containing multiple dataframes, one for each metric. Each dataframe has columns for type
    of model and each row is a sample, which has a computed value for the dataframe's metric in every cell.
    :param savefigs: bool, tells the function if the figures should be saved if savefigs=Ture, otherwise shows
    figures in IDE
    :return: some plots :)
    '''

    # barplots
    fig_bar, axs = plt.subplots(1,3, figsize=(11,4)) # plot with 3 horizontally placed subplots
    [TheBarPlot(data, metric, ax) for data, metric, ax in zip(dfs, metrics, axs)]

    fig_bar_wer, a = plt.subplots(1,1,figsize=(5,4))
    TheBarPlot(dfs[3], "WER", a) # index 3 is WER

    # Normality Check by QQplot and histograms
    fig_hist, axs_hist = plt.subplots(4,6, figsize=(15,12))
    fig_qqplot, axs_qq = plt.subplots(4,6, figsize=(15,12))
    for row, df in enumerate(dfs):
        for col, model in enumerate(MODELS):
            histo(df[model], metrics[row], model, axs_hist[row, col])
            QQPlot_regressionline(df[model], metrics[row], model, axs_qq[row, col])
    # only showing outer labels and getting rid of ticks
    for ax1, ax2 in zip(axs_hist.flat, axs_qq.flat):
        ax1.label_outer()
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax2.label_outer()
        ax2.set_xticks([])
        ax2.set_yticks([])


    if savefigs:
        fig_bar.savefig("plot_1x3_metrics.png", bbox_inches='tight')
        fig_bar_wer.savefig("plot_1x1_WER.png", bbox_inches='tight')
        fig_hist.savefig("plot_4x6_histograms.png", bbox_inches='tight')
        fig_qqplot.savefig("plot_4x6_qqplots.png", bbox_inches='tight')
    else:
        plt.show()

    print(f'Visualizations compeleted:\nBarplot, qqplots and histograms')

def plot_Truth_Mixture_Estimates(exp_dir: str, modelconf: str='1g', exp_nr: str='ex_151', savefig: bool=True):
    import librosa
    exp_dir = os.path.join(exp_dir, modelconf, 'OUTPUT_EVAL', 'examples', exp_nr)
    # show ground truths, mixture signal and then the estimated separated signals
    samples = np.empty(5, dtype=object)
    i=0
    for _, elem in enumerate(os.listdir(exp_dir)):
        if elem.endswith('.wav'):
            samples[i], sr = librosa.load(os.path.join(exp_dir, elem), duration=30)
            i += 1
        else:
            pass

    fig, axs = plt.subplots(5, 1, figsize=(15, 10))
    #
    axs[0].plot(samples[1], color="blue", alpha=0.7)
    axs[1].plot(samples[3], color="red", alpha=0.7)
    axs[2].plot(samples[1], color="blue", alpha=0.5)
    axs[2].plot(samples[3], color="red", alpha=0.5)
    axs[3].plot(samples[2], color="blue", alpha=0.7)
    axs[4].plot(samples[4], color="red", alpha=0.7)


    if savefig:
        name = "plot_5way_audio_" + modelconf + "_" + exp_nr + ".png"
        fig.savefig(name, bbox_inches='tight')
    else:
        plt.show()

    print(f'Ground truth signals vs estimated separated signals for {modelconf}, {exp_nr}')

if __name__ == "__main__":

    # choose what place the results are
    exp_dir = "exp_finished_results"

    dfs = dataload(exp_dir=exp_dir)
    visualization(dfs, savefigs=True)
    statistics(dfs)

    plot_Truth_Mixture_Estimates(exp_dir=exp_dir, modelconf='3c', exp_nr='ex_2643', savefig=True)
    plot_Truth_Mixture_Estimates(exp_dir=exp_dir, modelconf='1g', exp_nr='ex_151', savefig=True)

# df_sdr.stack().reset_index().rename(columns={'level_0': 'sample_nr', 'level_1': 'model', 0: 'metric_val'})
# for getting a vertical stack for data...