#!/usr/bin/env python3
import json
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib.pyplot import cm
import itertools
import csv
import scipy.stats

plt.rc('font', family='serif')

H = [1, 2, 3, 4]
N = 3
mMarkerSize = 10
mTickSize = 20
mLabelSize = 20
mLineWidth = 3
mLegendSize = 20

prefix = 'GES3_'
folderName = '../results/GEPerformance/GES/IEEE/'


def mean_confidence_interval(data, confidence=0.95):
    arr = 1.0 * np.array(data)
    num = len(arr)
    me, se = np.mean(arr), scipy.stats.sem(arr)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., num-1)
    return me, h


def plot_aoi_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))


    AoI_against_H = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_AoI.json') as json_file:
            fh_aoi = json.load(json_file)
            json_file.close()

        AoI_against_H.append(mean_confidence_interval(fh_aoi))

        mean = [i[0] for i in AoI_against_H]
        err = [i[1] for i in AoI_against_H]
    # e6858c
    ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth, c='coral',
                label='AoI', marker='o', markerfacecolor='None', markersize=mMarkerSize)

    mean.clear()
    err.clear()

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Age of Information', fontsize=mLabelSize)

    #plt.legend()
    plt.grid()
    plt.savefig(prefix + 'AoI_against_H.pdf', format='pdf')


def plot_nie_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    NIE_against_H = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_NIE.json') as json_file:
            fh_nie = json.load(json_file)
            json_file.close()

        NIE_against_H.append(mean_confidence_interval(fh_nie))

        mean = [i[0] for i in NIE_against_H]
        err = [i[1] for i in NIE_against_H]

    ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth, c='crimson',
                label='MSE', marker='o', markerfacecolor='None', markersize=mMarkerSize)



    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Mean Squared Error', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    # plt.legend()
    plt.grid()
    #plt.show()
    plt.savefig(prefix + 'MSE_against_H.pdf', format='pdf')


def plot_aoi_against_H_separate(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    AoI_against_H = []

    loopList = ['A100', 'A125', 'A150']

    for loopName in loopList:
        if loopName == 'A100':
            mMarker = '<'
            loopLabel = r'$\Delta_1$'
        elif loopName == 'A125':
            mMarker = 'd'
            loopLabel = r'$\Delta_2$'
        elif loopName == 'A135':
            mMarker = 'p'
            loopLabel = r'$\Delta_4$'
        elif loopName == 'A150':
            mMarker = 's'
            loopLabel = r'$\Delta_3$'

        AoI_against_H.clear()
        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + loopName + '_AoI.json') as json_file:
                fh_aoi = json.load(json_file)
                json_file.close()

            AoI_against_H.append(mean_confidence_interval(fh_aoi))

            mean = [i[0] for i in AoI_against_H]
            err = [i[1] for i in AoI_against_H]

        ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
                    label=loopLabel, marker=mMarker, markerfacecolor='None', markersize=mMarkerSize)

    AoI_against_H = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_AoI.json') as json_file:
            fh_aoi = json.load(json_file)
            json_file.close()

        AoI_against_H.append(mean_confidence_interval(fh_aoi))

        mean = [i[0] for i in AoI_against_H]
        err = [i[1] for i in AoI_against_H]
        print(f"AoI mean FH{h}: {mean_confidence_interval(fh_aoi)[0]}")
    # e6858c
    ax.errorbar(H[:], mean, yerr=err, linestyle='solid', linewidth=mLineWidth, c='black',
                label=r'$\overline{\Delta}$', marker='o', markerfacecolor='None', markersize=mMarkerSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Age of Information', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    plt.legend(fontsize=mLegendSize, ncol=2, bbox_to_anchor=(0.58, 0.55))
    plt.grid()
    #plt.show()
    plt.savefig(prefix + 'AoI_against_H_separate.pdf', format='pdf', bbox_inches='tight')


def plot_nie_against_H_separate(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    NIE_against_H = []

    loopList = ['A100', 'A125', 'A150']

    for loopName in loopList:
        if loopName == 'A100':
            mMarker = '<'
            loopLabel = r'$MSE_1$'
        elif loopName == 'A125':
            mMarker = 'd'
            loopLabel = r'$MSE_2$'
        elif loopName == 'A135':
            mMarker = 'p'
            loopLabel = r'$MSE_4$'
        elif loopName == 'A150':
            mMarker = 's'
            loopLabel = r'$MSE_3$'
        NIE_against_H.clear()
        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + loopName + '_NIE.json') as json_file:
                fh_nie = json.load(json_file)
                json_file.close()

                #print("A: {} H: {} e: {}".format(loopName, h, np.mean(fh_nie)))

            NIE_against_H.append(mean_confidence_interval(fh_nie))

            mean = [i[0] for i in NIE_against_H]
            err = [i[1] for i in NIE_against_H]

        ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
                    label=loopLabel, marker=mMarker, markerfacecolor='None', markersize=mMarkerSize)

    NIE_against_H = []
    NIE_against_H_boxplot = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_NIE.json') as json_file:
            fh_nie = json.load(json_file)
            json_file.close()

        print(f"NIE mean FH{h}: {mean_confidence_interval(fh_nie)[0]}")
        NIE_against_H.append(mean_confidence_interval(fh_nie))

        mean = [i[0] for i in NIE_against_H]
        #print(mean)
        err = [i[1] for i in NIE_against_H]

    plt.xticks(H)
    ax.errorbar(H[:], mean, yerr=err, linestyle='solid', linewidth=mLineWidth, c='black',
                label=r'$\overline{MSE}$', marker='o', markerfacecolor='None', markersize=mMarkerSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Mean Squared Error', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    plt.legend(fontsize=mLegendSize, ncol=2)
    plt.grid()
    #ax.set_yscale("log")
    #ax.set_ylim((0, 30.0))
    #plt.show()
    plt.savefig(prefix + 'MSE_against_H_separate.pdf', format='pdf', bbox_inches='tight')



def plot_nie_against_H_separate_boxplot(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    NIE_against_H = []

    loopList = ['A100', 'A125', 'A150']

    for loopName in loopList:
        if loopName == 'A100':
            mMarker = '<'
            loopLabel = r'$MSE_1$'
        elif loopName == 'A125':
            mMarker = 'd'
            loopLabel = r'$MSE_2$'
        elif loopName == 'A150':
            mMarker = 's'
            loopLabel = r'$MSE_3$'
        NIE_against_H.clear()
        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + loopName + '_NIE.json') as json_file:
                fh_nie = json.load(json_file)
                json_file.close()

                #print("A: {} H: {} e: {}".format(loopName, h, np.mean(fh_nie)))

            NIE_against_H.append(mean_confidence_interval(fh_nie))

            mean = [i[0] for i in NIE_against_H]
            err = [i[1] for i in NIE_against_H]

        #ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
        #            label=loopLabel, marker=mMarker, markerfacecolor='None', markersize=mMarkerSize)

    NIE_against_H = []
    NIE_against_H_boxplot = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_NIE.json') as json_file:
            fh_nie = json.load(json_file)
            json_file.close()


        #print(np.mean(fh_nie))
        NIE_against_H.append(mean_confidence_interval(fh_nie))
        NIE_against_H_boxplot.append(fh_nie)

        mean = [i[0] for i in NIE_against_H]
        #print(mean)
        err = [i[1] for i in NIE_against_H]

    ax.boxplot(NIE_against_H_boxplot, showmeans=True, showfliers=False)
    plt.xticks(H)
    #ax.errorbar(H[:], mean, yerr=err, linestyle='solid', linewidth=mLineWidth, c='black',
    #            label=r'$\overline{MSE}$', marker='o', markerfacecolor='None', markersize=mMarkerSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Mean Squared Error', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    plt.legend(fontsize=mLegendSize, ncol=2)
    plt.grid()
    #ax.set_yscale("log")
    #ax.set_ylim((0, 30.0))
    #plt.show()
    plt.savefig(prefix + 'MSE_against_H_boxplot.pdf', format='pdf', bbox_inches='tight')


def plot_J_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    J_against_H = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_J.json') as json_file:
            fh_J = json.load(json_file)
            json_file.close()

        J_against_H.append(mean_confidence_interval(fh_J))

        mean = [i[0] for i in J_against_H]
        err = [i[1] for i in J_against_H]

    ax.errorbar(H[:], mean, yerr=err, linestyle='solid', linewidth=mLineWidth, c='salmon',
                label='MSE', marker='^', markerfacecolor='None', markersize=mMarkerSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Control Cost', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    # plt.legend()
    plt.grid()
    #plt.show()
    plt.savefig(prefix + 'J_against_H.pdf', format='pdf')

def plot_networkshare_against_H_separate(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    NS_against_H = []
    UR_against_H = []

    loopList = ['A100', 'A125', 'A150']

    for h in H:
        if h == 4:
            UR = np.zeros(160)
        else:
            UR = np.zeros(200)
        for loopName in loopList:
            with open(folderName + 'FH' + str(h) + '/' + loopName + '_sumScheduledCnt.json') as json_file:
                UR = UR + json.load(json_file)
        UR_against_H.append(UR)

    for loopName in loopList:
        if loopName == 'A100':
            mMarker = '<'
            loopLabel = r'$A_1$'
        elif loopName == 'A125':
            mMarker = 'd'
            loopLabel = r'$A_2$'
        elif loopName == 'A135':
            mMarker = 'p'
            loopLabel = r'$A_4$'
        elif loopName == 'A150':
            mMarker = 's'
            loopLabel = r'$A_3$'
        NS_against_H.clear()
        for h in H:
            with open(folderName + 'FH' + str(h) + '/' + loopName + '_sumScheduledCnt.json') as json_file:
                fh_ns = json.load(json_file)
                json_file.close()

            fh_ns = fh_ns / UR_against_H[h-1]
            NS_against_H.append(mean_confidence_interval(fh_ns*100))

            mean = [i[0] for i in NS_against_H]
            err = [i[1] for i in NS_against_H]

        ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth,
                    label=loopLabel, marker=mMarker, markerfacecolor='None', markersize=mMarkerSize)

    ax.set_xlabel('Horizon', fontsize=mLabelSize)
    ax.set_ylabel('Network Share [%]', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    plt.legend(fontsize=mLegendSize, bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
    plt.grid()
    plt.savefig(prefix + 'NS_against_H_separate.pdf', format='pdf', bbox_inches='tight')    

def plot_complexity_against_H(H):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    nodeCount_against_H = []
    worstcase_against_H = []

    for h in H:
        with open(folderName + 'FH' + str(h) + '/' + 'avg_NodeCount.json') as json_file:
            fh_nodeCount = json.load(json_file)
            json_file.close()

        nodeCount_against_H.append(mean_confidence_interval(fh_nodeCount))

        mean = [i[0] for i in nodeCount_against_H]
        err = [i[1] for i in nodeCount_against_H]
        worstcase_against_H.append(((N + 1) ** (h + 1) - 1) / N)

    ax.errorbar(H[:], mean, yerr=err, linestyle='dotted', linewidth=mLineWidth, c='teal',
                label='simulation', marker='D', markerfacecolor='None', markersize=mMarkerSize)

    print("FH: {}".format(mean))

    ax.errorbar(H[:], worstcase_against_H, yerr=err, linestyle='solid', linewidth=mLineWidth, c='lightblue',
                label='worst-case', marker='*', markerfacecolor='None', markersize=mMarkerSize)
    print("WC: {}".format(worstcase_against_H))
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
    #plt.show()
    plt.savefig(prefix + 'AvgNodeCount_against_H.pdf', format='pdf')

# plot_aoi_against_H(H)

# plot_nie_against_H(H)

plot_J_against_H(H)

plot_complexity_against_H(H)

plot_aoi_against_H_separate(H)

plot_nie_against_H_separate(H)

# plot_nie_against_H_separate_boxplot(H)

# plot_networkshare_against_H_separate(H)

plt.show()
