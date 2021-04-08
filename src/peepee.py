#peepee.py

import pychorus
import librosa
import librosa.display
from pydub import AudioSegment
import scipy
import numpy as np
import math
from matplotlib import pyplot as plt

music1="src/Money-Trees-bBNpSXAYteM.mp4"
music2="src/aweEevee.wav"

y, sr = librosa.load(music1)
z, pr = librosa.load(music2)


def getChorus(y, sr):
    """ 
    Compute the spectrogram magnitude and phase
    stft -> Short-time Fourier transform (STFT). 
    stft: Used to determine the sin wave frequency and phase content of local sections of a signal as it changes over time.
    This contains both Vocal and Instruments

    """

    S_full, phase = librosa.magphase(librosa.stft(y))

    """ 
    Compare frames using cosine similarity and aggregate similar frames
            by taking their (per-frequency) median value.
    To avoid being biased by local continuity, constrain similar frames to be
            separated by at least 2 seconds.

    """

    S_filter = librosa.decompose.nn_filter(S_full,
                                    aggregate=np.median,
                                    metric='cosine',
                                    width=int(librosa.time_to_frames(2, sr=sr)))
    S_filter = np.minimum(S_full, S_filter)

    
             
#harmonics





""" chroma1, _, _, _ = pychorus.create_chroma(music1)
chroma2, _, _, _ = pychorus.create_chroma(music2)
time_time_similarity = pychorus.TimeTimeSimilarityMatrix(chroma1, sr)
time_lag_similarity = pychorus.TimeLagSimilarityMatrix(chroma1, sr)

# Visualize the results
time_time_similarity.display()
time_lag_similarity.display() 

print("\nTrying Harmonics \n")

chroma = librosa.feature.chroma_cqt(y, sr)
plt.figure(figsize=(18,5))
librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
plt.title('Chromagram')
plt.colorbar()
plt.figure(figsize=(20,8))
plt.title('')
librosa.display.specshow(chroma, sr=sr, x_axis='s', y_axis='chroma')

plt.show()
#print()

"""


## Code used from https://gist.github.com/vivjay30/6ab1c1d1831d3c6b6ad4c8c28ba075be#file-time_time_similarity-py
## Author of Pychorus


def computetempo(y, sr):
    #Tempo
    return librosa.beat.tempo(y,sr)
    #librosa.beat.tempo(z,pr)

def compareTemp(a,b):
    accuracy = (1 - abs(a - b)/(a))*100
    print('Tempo Accuracy: ', accuracy)

def compute_similarity_matrix_slow(self, chroma):
    """Slow but straightforward way to compute time time similarity matrix"""
    num_samples = chroma.shape[1]
    time_time_similarity = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        for j in range(num_samples):
            # For every pair of samples, check similarity
            time_time_similarity[i, j] = 1 - (
                np.linalg.norm(chroma[:, i] - chroma[:, j]) / math.sqrt(12))

    return time_time_similarity