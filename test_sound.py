import time
from pydub import AudioSegment
from pydub.playback import play
bool = True
seconds = int(input("Seconds: "))
for i in range(seconds):
    if bool and seconds>=10:
        time.sleep(0.4)
        song = AudioSegment.from_mp3("beep.mp3")
                        
        play(song)
        seconds = seconds -1
        if seconds == 0:
            song = AudioSegment.from_mp3("explosion.mp3")
            play(song)
        else:
            print("")
    elif bool and seconds<10 and seconds>=5:
        time.sleep(0.05)
        song = AudioSegment.from_mp3("beep.mp3")
                        
        play(song)
        seconds = seconds -1
        if seconds == 0:
            song = AudioSegment.from_mp3("explosion.mp3")
            play(song)
        else:
            print("")
    elif bool and seconds<5:
        time.sleep(0)
        song = AudioSegment.from_mp3("beep2.mp3")
                        
        play(song)
        seconds = seconds -1
        if seconds == 0:
            song = AudioSegment.from_mp3("explosion.mp3")
            play(song)
        else:
            print("")

    else:
        print(1)
