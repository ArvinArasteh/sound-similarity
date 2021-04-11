#peepee.py

import functools
import pychorus
import librosa
import librosa.display
from pydub import AudioSegment
import scipy
import numpy as np
import math
from matplotlib import pyplot as plt

BUGS = True

music1="src/Money-Trees-bBNpSXAYteM.mp4"
music2="src/aweEevee.wav"



notes = {
    11:'B',
    10:'Bb',
    9:'A',
    8:'Aa',
    7:'G',
    6:'Gg',
    5:'F',
    4:'E',
    3:"Ee",
    2:"D",
    1:"Dd",
    0:"C"
}



def compareChorus():
    y1, sr1 = librosa.load(music1)
    y2, sr2 = librosa.load(music2)

    a = getChorus(y1,sr1)
    b = getChorus(y2,sr2)

    print(lcs("".join(a),"".join(b)))



def getChorus(y, sr):
    """ 
    Compute the spectrogram magnitude and phase
    stft -> Short-time Fourier transform (STFT). 
    stft: Used to determine the sin wave frequency and phase content of local sections of a signal as it changes over time.
    This contains both Vocal and Instruments
    """
    
    
    duration = librosa.get_duration(y,sr)
    
    mono = librosa.to_mono(y)

    if(BUGS):
        print(y)
        print(duration)
        print(mono)

    S_full, phase = librosa.magphase(librosa.stft(mono))

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
    


    #Get Chroma values which results in the 12 note system
    chroma = librosa.feature.chroma_cqt(mono, sr)
    noteSheet = []
    if(BUGS):
        print(len(chroma[0]))
        print(int(len(chroma[0])/duration))

    #Runs through the length of the song
    for i in range(len(chroma[0])):
        largestChar = ['a',0]
        
        #Runs through 12 notes
        for j in range(len(chroma)):
            if largestChar[1]<chroma[j][i]:
                largestChar = [notes[j], chroma[j][i]]

        if(len(noteSheet)==0):
            noteSheet.append(largestChar[0])
        elif(noteSheet[-1] != largestChar[0]):
            noteSheet.append(largestChar[0])
    if(BUGS):
        print(noteSheet[:10])
        print(len(noteSheet))

    #I know runtime is bad, its n^2 ffs
    
    longestCommonSubArray = []


    #gets longest common subarray inside the array and determines it as the chorus
    for i in range(len(noteSheet)):
        tempArray = []
        sVal = 0
        for j in range(i+1, len(noteSheet)):

            if(noteSheet[j-sVal]==noteSheet[j] and sVal!=0):
                tempArray.append(noteSheet[j])
            elif(noteSheet[i] == noteSheet[j] and sVal==0):
                sVal = j
                tempArray.append(noteSheet[j])
            else:
                if len(longestCommonSubArray)<len(tempArray):
                    longestCommonSubArray = tempArray
                    tempArray.clear()
                    sVal=0
    if(BUGS):
        print(longestCommonSubArray)
        print(len(longestCommonSubArray))  

    return(longestCommonSubArray)  

    """ plt.figure(figsize=(18,5))
    librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
    plt.title('Chromagram')
    plt.colorbar()
    #librosa.display.specshow(chroma, sr=sr, x_axis='s', y_axis='chroma')
    plt.show() """

             
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

#Compute Tempo
def computeTempo(y, sr):
    #Tempo
    return librosa.beat.tempo(y,sr)
    #librosa.beat.tempo(z,pr)

#Returns the accuracy of the 2 tempos
def compareTempo(a,b):
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



#Returns the Longest Common substring
def lcs(X, Y):
    m = len(X)
    n = len(Y)

    @functools.lru_cache(None)
    def lcsHelper(X, Y, m, n): 
        if m == 0 or n == 0:
            return 0
        elif X[m-1] == Y[n-1]:
            return 1 + lcsHelper(X, Y, m-1, n-1)
        else:
            return max(lcsHelper(X, Y, m, n-1), lcsHelper(X, Y, m-1, n))
    return(lcsHelper(X,Y,m,n))



if __name__ == "__main__":
    compareChorus()
