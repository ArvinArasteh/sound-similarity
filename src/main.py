from vocals import vocalDistanceBetweenTwoMusic
from tempo import diff
from chorus import compareChorus

# MUSIC DATA SETS
BASE_DIR = "../music/"
music = ['Darude_Sandstorm.wav', 'America_A_Horse_With_No_Name.wav', 'Lift_Yourself_Kanye.wav', "The_Beatles_Don't_Let_Me_Down.wav"]
# USE THE ONE BELOW FOR QUICK TESTING
#music = ['Darude_Sandstorm.wav', 'America_A_Horse_With_No_Name.wav']


for music1 in music:
    for music2 in music:
        file1 = BASE_DIR + music1
        file2 = BASE_DIR + music2
        print("Comparing", music1, "VS", music2)
        tempoDiff = diff(file1, file2)

        # Vocal Diff
        vocalDiff = vocalDistanceBetweenTwoMusic(file1, file2)

        # Chorus Diff
        #chorusDiff = compareChorus(file1, file2)

        print("Scores:")
        print("\tTempo:", tempoDiff)
        print("\tVocal:", vocalDiff)
        #print("\tChorus:", chorusDiff)
        print("===========================================\n")




