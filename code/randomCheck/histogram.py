import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

os = ['Mac', 'Linux', 'Windows']

fig1 = plt.figure()
fig2 = plt.figure()
sns.set_style('darkgrid')

ax1 = fig1.add_subplot()
ax2 = fig2.add_subplot()

ax1.set_title(r"Normal distribution $\mathcal{N}(0.5, 0.2)$")
ax2.set_title(r"Uniform distribution $\mathcal{U}(0, 1)$")

for folder in os:

    with open (f"{folder}/normal_distribution.json") as f: 
        norm = np.array(json.load(f))

    with open (f"{folder}/uniform_distribution.json") as f:
        uni = np.array(json.load(f))

    sns.distplot(norm, label=folder, ax=ax1)
    plt.savefig('normal.pdf')
    sns.distplot(uni, label=folder, ax=ax2)
    plt.savefig('uniform.pdf')

plt.legend()
plt.show()
