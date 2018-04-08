from gtts import gTTS
from pygame import mixer 

import time,os

def speak(text):
    file=gTTS(text=text,lang='en')
    filename='/home/pi/temp.mp3'
    file.save(filename)
    mixer.init()
    mixer.music.load('/home/pi/temp.mp3')
    mixer.music.play()
    time.sleep(4)
    mixer.music.stop()      

