#!/usr/bin/env python3
import json
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

plt.rc('font', family='serif')
plt.rcParams['figure.constrained_layout.use'] = True

H = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 3
mMarkerSize = 10
mTickSize = 20
mLabelSize = 20
mLineWidth = 3
mLegendSize = 20

Linux = '../results/OSPerformance/Linux/'
Mac = '../results/OSPerformance/Mac/'
Windows = '../results/OSPerformance/Windows/'

os = [Linux, Mac, Windows]

def mean_confidence_interval(data, confidence=0.95):
    arr = 1.0 * np.array(data)
    num = len(arr)
    me, se = np.mean(arr), scipy.stats.sem(arr)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., num-1)
    return me, h


def plot_aoi_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    for folderName in os: 
        AoI_against_H = []

        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + 'avg_AoI.json') as json_file:
                fh_aoi = json.load(json_file)
                json_file.close()

            AoI_against_H.append(mean_confidence_interval(fh_aoi))

            mean = [i[0] for i in AoI_against_H]
            err = [i[1] for i in AoI_against_H]
        # e6858c
        ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
                    label=folderName.split('/')[-2], marker='o', markerfacecolor='None', markersize=mMarkerSize)

        mean.clear()
        err.clear()

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Age of Information', fontsize=mLabelSize)

    plt.legend(fontsize=mLegendSize)
    plt.grid()
    plt.savefig('OS_AoI_against_H.pdf')


def plot_nie_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    for folderName in os:

        NIE_against_H = []

        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + 'avg_NIE.json') as json_file:
                fh_nie = json.load(json_file)
                json_file.close()

            NIE_against_H.append(mean_confidence_interval(fh_nie))

            mean = [i[0] for i in NIE_against_H]
            err = [i[1] for i in NIE_against_H]

        ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
                    label=folderName.split('/')[-2], marker='o', markerfacecolor='None', markersize=mMarkerSize)
        err.clear()
        mean.clear()

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Mean Squared Error', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    plt.legend(fontsize=mLegendSize)
    plt.grid()
    plt.savefig('OS_MSE_against_H.pdf')

def plot_J_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    for folderName in os:

        J_against_H = []

        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + 'avg_J.json') as json_file:
                fh_J = json.load(json_file)
                json_file.close()

            J_against_H.append(mean_confidence_interval(fh_J))

            mean = [i[0] for i in J_against_H]
            err = [i[1] for i in J_against_H]

        ax.errorbar(H[:], mean, yerr=err, linestyle='solid', linewidth=mLineWidth,
                    label=folderName.split('/')[-2], marker='^', markerfacecolor='None', markersize=mMarkerSize)
        mean.clear()
        err.clear()

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Control Cost', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    plt.legend(fontsize=mLegendSize)
    plt.grid()
    plt.savefig('OS_J_against_H.pdf')

def plot_complexity_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))


    for folderName in os:
        nodeCount_against_H = []

        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + 'avg_NodeCount.json') as json_file:
                fh_nodeCount = json.load(json_file)
                json_file.close()

            nodeCount_against_H.append(mean_confidence_interval(fh_nodeCount))

            mean = [i[0] for i in nodeCount_against_H]
            err = [i[1] for i in nodeCount_against_H]

        ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
                    label=folderName.split('/')[-2], marker='D', markerfacecolor='None', markersize=mMarkerSize)
        mean.clear()
        err.clear()

    worstcase_against_H = [((N + 1) ** (h + 1) - 1) / N for h in H]
    # ax.plot(H[:], worstcase_against_H, linestyle='solid', linewidth=mLineWidth, c='lightblue',
#                label='worst-case', marker='*', markerfacecolor='None', markersize=mMarkerSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Complexity', fontsize=mLabelSize)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.yaxis.offsetText.set_fontsize(mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    plt.legend(fontsize=mLabelSize)
    plt.grid()
    plt.savefig('OS_AvgNodeCount_against_H.pdf')

def plot_costMap():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    colorList = ['C2', 'C1', 'C0']
    aoi = np.arange(100)
    aoi = np.stack((aoi,aoi,aoi))

    for folderName in os: 
        costMap = np.genfromtxt(folderName + 'costMap.csv', delimiter=",")
        ax.plot(aoi.T, costMap.T, colorList.pop(), alpha=0.7, label=folderName.split('/')[-2])
            
    ax.set_yscale("log")
    ax.set_xlabel('Age of Information', fontsize=mLabelSize)
    ax.set_ylabel('Cost', fontsize=mLabelSize)
    ax.yaxis.offsetText.set_fontsize(mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    
    handles, labels = plt.gca().get_legend_handles_labels()
    newLabels, newHandles = [], []
    for handle, label in zip(handles, labels):
        if label not in newLabels:
            newLabels.append(label)
            newHandles.append(handle)
    plt.legend(newHandles, newLabels, fontsize=mLabelSize)
    # plt.legend(fontsize=mLabelSize)
    plt.grid()
    plt.savefig('costMaps.pdf')

plot_aoi_against_H(H)

plot_nie_against_H(H)

plot_J_against_H(H)

plot_complexity_against_H(H)

plot_costMap()

plt.show()
