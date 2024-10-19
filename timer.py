import time
import tkinter as tk
from pydub import AudioSegment
from pydub.playback import play

#time.sleep(1)

running = True


    










def timeBomb(hours, minutes, seconds):
    #countdown is -1 because the while loop will only count down to 1 if countdown is zero because it will end the loop when seconds == 0
    #therefore we use -1 in order to count down to zero and only skip the loop when seconds == -1
    countdown = -1
#    seconds2 = 0
#    print(f"{minutes}:{seconds}")
    song = AudioSegment.from_mp3("okletsgo.mp3")
    play(song)
    while seconds != countdown and minutes != countdown and hours != countdown:
#        timer = f"{hours}:{minutes}:{seconds}"
#        timer = f"{hours}:{minutes}:{seconds}"
#        print(f"{minutes}:{seconds}")
        
        if seconds != -1:

                print(f"{minutes}:{seconds}")
    #            print(seconds)
        seconds = seconds - 1
        time.sleep(1)
        def beep():
            if minutes<1 and seconds <10:
                
                song = AudioSegment.from_mp3("beep.mp3")
                                    
                play(song)
                
            if seconds == -1:
                song = AudioSegment.from_mp3("explosion.mp3")
                play(song)
                
    
        
        beep()

        
        time.sleep(0.155)
        ''' or minutes>0 and seconds2 == -1'''
        #the if statement below was partially fixed by removing the seconds2 == 60 condition which was useless because if minutes>1 then seconds is turned into 59 anyways we dont need a variable to see when a minute has passed
        
        
        if minutes>0 and seconds == 0 :

            minutes = minutes -1
            seconds = 59
#            print(timer)
            '''if seconds == 0 and minutes == 0 and hours ==0:
                song = AudioSegment.from_mp3("explosion.mp3")
                
                play(song)
            else:
                continue'''
            
        else:
            continue


running = True
while running: 
    seconds1 = int(input("seconds: "))
    minutes1 = int(input("minutes: "))
    hours1 = int(input("hours: "))
    

    if seconds1<=59 and minutes1<=59 and hours1<=23:
        

        if minutes1>0 and seconds1 == 0:
            minutes1 = minutes1-1
            seconds1 = 59
            
            timeBomb(hours1, minutes1, seconds1)
#            print(seconds1)

        else:
            timeBomb(hours1, minutes1, seconds1)
        
        running = False
        
    else:
        print("you cant have more than 59 seconds or 60 minutes or 23 hours, same deal for minutes")
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

