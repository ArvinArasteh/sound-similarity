import librosa
import scipy
import numpy as np

y, sr = librosa.load("Money-Trees-bBNpSXAYteM.mp4")
onset_env = librosa.onset.onset_strength(y, sr=sr)
prior_lognorm = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)

dtempo_lognorm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None,prior=prior_lognorm)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None)
res = dict()
for elem in dtempo_lognorm:
    if elem not in res:
        res[elem] = 1
    else:
        res[elem] = res[elem] + 1

for elem in res:
    print(elem, res[elem])