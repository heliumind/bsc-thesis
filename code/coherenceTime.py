import json
import itertools
import pandas as pd
import numpy as np

def avgCoherenceTime(folder):
    with open(f"../results/avgCoherenceTime/{folder}/config.json") as f:
        config = json.load(f)
    with open (f"../avgCoherenceTime/{folder}/A100_chState.json") as f:
        chStates = json.load(f)
    pTrans = config["Transition Probability"]
    buf = [(x, len(list(y))) for x, y in itertools.groupby(chStates)]

    avgTimeGOOD = []
    avgTimeBAD = []
    for n in buf:
        if n[0] == 0:
            avgTimeGOOD.append(n[1])
        else:
            avgTimeBAD.append(n[1])

    return pTrans, np.mean(avgTimeGOOD), np.std(avgTimeGOOD), np.mean(avgTimeBAD), np.std(avgTimeBAD)
    out = {'Transition Probability': pTrans, 'avgTimeGOOD': np.mean(avgTimeGOOD), 'avgTimeBAD': np.mean(avgTimeBAD)} 

timeList = ["3", "10", "30", "100"]
pTrans = []
avgTimeGOOD = []
stdGood = []
avgTimeBAD = []
stdBad = []

for time in timeList:
    p, good, stdg, bad, stdb  = avgCoherenceTime(time)
    pTrans.append(p)
    avgTimeGOOD.append(good)
    stdGood.append(stdg)
    avgTimeBAD.append(bad)
    stdBad.append(stdb)
    
df = pd.DataFrame({'Transition Probability': pTrans, 'avgTimeGOOD': avgTimeGOOD, 'stdGOOD': stdGood, 'avgTimeBAD': avgTimeBAD, 'stdBAD': stdBad})
df.to_html("AvgCoherenceTime.html", index=False)
