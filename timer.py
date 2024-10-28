import time
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play


#root = Tk()


running = True

def timeBomb(hours, minutes, seconds):
    #countdown is -1 because the while loop will only count down to 1 if countdown is zero because it will end the loop when seconds == 0
    #therefore we use -1 in order to count down to zero and only skip the loop when seconds == -1
    countdown = -1

    while seconds != countdown and minutes != countdown and hours != countdown:
#        timer = f"{hours}:{minutes}:{seconds}"

        if seconds != -1:
# not using the commented out variable above -->timer because seconds does not display correctly for some reason when saying print(timer)
#print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
                print(f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

        seconds = seconds - 1
        time.sleep(1)
        def beep():
            if minutes<1 and seconds <10 and seconds >-1:###
                
                song = AudioSegment.from_mp3("beep.mp3")
                                    
                play(song)
            if minutes<1 and seconds == 0:###
                print(f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
                song1 = AudioSegment.from_mp3("mozart40nokia.mp3")
                song = AudioSegment.from_mp3("explosion.mp3")
                play(song1)
                play(song)
        beep()

        time.sleep(0.155)
        
        if minutes>0 and seconds == -1 :###

            minutes = minutes -1
            seconds = 59

        else:
            continue


running = True

while running: 
    seconds1 = int(input("seconds: "))
    minutes1 = int(input("minutes: "))
    hours1 = int(input("hours: "))
    

    if seconds1<=59 and minutes1<=59 and hours1<=23:
        
        if minutes1>0 and seconds1 == 0:
            song = AudioSegment.from_mp3("click.mp3")
            play(song)
            print(f"{str(minutes1).zfill(2)}:{str(seconds1).zfill(2)}")
            minutes1 = minutes1-1
            seconds1 = 59
            
            timeBomb(hours1, minutes1, seconds1)
#            print(seconds1)

        else:
            song = AudioSegment.from_mp3("click.mp3")
            play(song)
            timeBomb(hours1, minutes1, seconds1)
        
        running = False
        
    else:
        song = AudioSegment.from_mp3("error2.mp3")
        play(song)
        print("!!you cant have more than 59 seconds, 59 minutes or 23 hours!!".upper())

        running = True


    
   


# PROBLEMS TO FIX NEXT TIME:
#   1.start working on getting hours to work 
#   2.use tkinter or smth else to put the timer on something graphical


# LEARNED SKILLS:
#   1. finally learned how to loop a program until a 
#      certain condition is met e.g.
'''
running = True
while running: 
    seconds1 = int(input("seconds: "))
    minutes1 = int(input("minutes: "))
    hours1 = int(input("hours: "))   
    if seconds1<=59 and minutes1<=59:
        timeBomb(hours1, minutes1, seconds1)
        running = False
        
    else:
        print("you cant have more than 60 seconds or 60 seconds, same deal for minutes")
        running = True
'''

