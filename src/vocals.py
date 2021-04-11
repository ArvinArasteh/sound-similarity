from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.spatial import distance

import librosa.display


def main():
    def soundWaves(file):

        """ 

        Load the audio file

        """ 
        
        y, sr = librosa.load(str(file))

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


        """ 

        Use a margin to reduce bleed between the vocals and instrumentation masks.
        
        """

        margin_i, margin_v = 2, 10
        power = 2
        mask_v = librosa.util.softmask(S_full - S_filter,
                                       margin_v * S_filter,
                                       power=power)
        """ 

        Multiply with the input spectrum to separate the vocals
        
        """                     
        S_foreground = mask_v * S_full


        """ 

        Avg vocal component at each array
        
        """      

        avgVocalRes = []
        for i in S_foreground:
            avgVocalRes.append(np.average(i))

        return avgVocalRes

    def vocalDistanceBetweenTwoMusic(music1, music2):

        """ 

        Calculate euclidean distance (because the input variables are similar) between two sound files' vocal phases
        
        """      
        list1 = np.array(soundWaves(str(music1)))
        list2 = np.array(soundWaves(str(music2)))
        list1 = list1.reshape(-1,1)
        list2 = list2.reshape(-1,1)
        dst = distance.euclidean(list1, list2) 
        return dst

    # Test
    print(vocalDistanceBetweenTwoMusic('aweEevee.wav','aweEevee.wav'))


if __name__ == "__main__":
    main()