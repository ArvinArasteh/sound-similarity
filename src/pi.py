import pychorus
import librosa
from pydub import AudioSegment
import scipy
import numpy as np

# Command to GET song info ./youtube-dl.exe -f 251 "https://www.youtube.com/watch?v=bBNpSXAYteM"
'''song = AudioSegment.from_file("src/Money-Trees-bBNpSXAYteM.mp4")

loudness = song.dBFS
song.

print(loudness)'''

y, sr = librosa.load("src/Money-Trees-bBNpSXAYteM.mp3")
onset_env = librosa.onset.onset_strength(y, sr=sr)
prior_lognorm = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)

dtempo_lognorm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None,prior=prior_lognorm)

res = []
for elem in dtempo_lognorm:
    if elem not in res:
        res.append(elem)

print(res)
        