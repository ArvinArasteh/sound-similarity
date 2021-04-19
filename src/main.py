from vocals import vocalDistanceBetweenTwoMusic
from tempo import diff
from chorus import compareChorus
 
# Compare All Files
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
        chorusDiff = compareChorus(file1, file2)

        print("Scores:")
        print("\tTempo:", tempoDiff)
        print("\tVocal:", vocalDiff)
        print("\tChorus:", chorusDiff)

        score = 0

        if abs(tempoDiff) < 2:
            score+=1
        if abs(vocalDiff) < 3:
            score+=1
        if chorusDiff <= 20:
            score+=1

        print("\tScore:", score / 3)

        if (score >= 0.5):
            print("\tSimilarity:","Similar")
        else:
            print("\tSimilarity:","Not Similar")

        print("===========================================\n")

