import librosa
import scipy
import numpy as np


def getResults(file):
    y, sr = librosa.load(file)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    prior_lognorm = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)

    dtempo_lognorm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None,prior=prior_lognorm)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None)
    
    return dtempo_lognorm

def diff(music1, music2):
    res1 = getResults(music1)
    res2 = getResults(music2)

    sum1 = 0
    sum2 = 0

    for elem in res1:
        sum1 += elem

    for elem in res2:
        sum2 += elem

    return sum2 - sum1