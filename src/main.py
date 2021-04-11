from vocals import vocalDistanceBetweenTwoMusic
from tempo import diff
from chorus import compareChorus

music1 = 'music/Darude_Sandstorm.wav'
music2 = 'music/Darude_Sandstorm.wav'
name1 = music1.replace("music/", "")
name2 = music2.replace("music/", "")

# Tempo Diff
tempoDiff = diff(music1, music2)
print("Tempo difference between", name1, "and", name2, "is", tempoDiff)

# Vocal Diff
vocalDiff = vocalDistanceBetweenTwoMusic(music1, music2)
print("Vocal difference between", name1, "and", name2, "is", vocalDiff)

# Chorus Diff
chorusDiff = compareChorus(music1, music2)
print("Chorus difference between", name1, "and", name2, "is", chorusDiff)








