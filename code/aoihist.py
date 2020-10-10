import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

plt.rc('font', family='serif')
plt.rcParams['figure.constrained_layout.use'] = True

mMarkerSize = 10
mTickSize = 20
mLabelSize = 20
mLegendSize = 20

folder = "../results/AoIHist/CoherenceTime_3/N3_WC"

with open (f"{folder}/config.json") as f:
    config = json.load(f)

with open (f"{folder}/avg_Loss.json") as f:
    p = json.load(f)[0]

pTrans = config["Transition Probability"]
pLossGOOD = config["LossGood"]
pLossBAD = config["LossBad"]
H = config["Horizon"]
R = config["Simulation Steps"]

with open (f"{folder}/A100_AoI_hist.json") as f:
    a100 = json.load(f)
    a100 = np.array(a100)
with open (f"{folder}/A125_AoI_hist.json") as f:
    a125 = json.load(f)
    a125 = np.array(a125)
# with open (f"{folder}/A135_AoI_hist.json") as f:
#     a135 = json.load(f)
#     a135 = np.array(a135)
with open (f"{folder}/A150_AoI_hist.json") as f:
    a150 = json.load(f)
    a150 = np.array(a150)
# maxAoI = max([a100.max(), a125.max(), a150.max()])
maxAoI = 11

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

loopName = [r"$A_1=1.0$", r"$A_2=1.25$", r"$A_3=1.5$"]
ax.hist([a100, a125, a150], bins=np.arange(1, maxAoI+1)-0.5, label=loopName)
# ax.hist([a100], bins=np.arange(1, maxAoI)-0.5, rwidth=0.8, label=loopName[0]) # density option to normalize

x = np.arange(1, maxAoI)

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(mTickSize)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(mTickSize)
ax.set_xticks(x)
ax.set_xlabel(r'Age of Information', fontsize=mLabelSize)
ax.set_ylabel('Counts', fontsize=mLabelSize)
ax.set(xlabel="Age of Information (AoI)", ylabel="Counts", xticks=x)
# ax.set_title(f"Transition probability: {pTrans} \n Loss probability: {pLossGOOD}(GOOD) {pLossBAD}(BAD) \n Average Loss probability: {p:.3f}")
# aoi_dist = (1 - p) * p ** (x - 1)
# ax.plot(x, R*aoi_dist, label="Paper AoI distribution")
plt.legend(fontsize=mLegendSize)
plt.grid()
plt.savefig("AoI_Histogram_N3_WC.pdf")
plt.show()
