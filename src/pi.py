import pychorus
import librosa
from pydub import AudioSegment

# Command to GET song info ./youtube-dl.exe -f 251 "https://www.youtube.com/watch?v=bBNpSXAYteM"
song = AudioSegment.from_mp3("Money-Trees-bBNpSXAYteM.mp3")

print(song)