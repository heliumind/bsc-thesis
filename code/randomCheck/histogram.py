import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rc('font', family='serif')
sns.set_style('whitegrid', {'font.family':'serif'})

mTickSize = 18
mLabelSize = 20
mLegendSize = 20

os = ['Linux', 'Mac', 'Windows']

def plot_uniform():
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot()
    # ax.set_title(r"Uniform distribution $\mathcal{U}(0, 1)$")

    for folder in os:
        with open (f"{folder}/uniform_distribution.json") as f:
            uni = np.array(json.load(f))

        sns.distplot(uni, kde=False, label=folder, ax=ax)

    ax.set_xlabel(r'$X$', fontsize=mLabelSize)
    ax.set_ylabel('Counts', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    plt.legend(fontsize=mLegendSize, bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
    plt.savefig('uniform.pdf')

def plot_normal():
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot()
    # ax.set_title(r"Normal distribution $\mathcal{N}(0.5, 0.2)$")

    for folder in os:
        with open (f"{folder}/normal_distribution.json") as f: 
            norm = np.array(json.load(f))

        sns.distplot(norm, kde=False, label=folder, ax=ax)
        
    ax.set_xlabel(r'$X$', fontsize=mLabelSize)
    ax.set_ylabel('Counts', fontsize=mLabelSize)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(mTickSize)

    plt.legend(fontsize=mLegendSize)
    plt.savefig('normal.pdf')

plot_uniform()
plot_normal()
plt.show()
