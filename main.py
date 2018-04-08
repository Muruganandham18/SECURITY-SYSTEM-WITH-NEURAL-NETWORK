import speechtotext as st
import googlespeak as gs
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer 

import time,os


def lis():
    r=sr.Recognizer()
    with sr.Microphone(device_index = 1, chunk_size=100) as source:
        text='  '
##        r.adjust_for_ambient_noise(source, duration=3)
        mixer.init()
        mixer.music.load('/home/pi/new-project/fbmngrpulldownrfsh.mp3')
        mixer.music.play()
        print("Listerning....")
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=3)
        print("Processing....")
        mixer.init()
        mixer.music.load('/home/pi/Desktop/msn_msg.mp3')
        mixer.music.play()
    try:
        text=r.recognize_google(audio)
        lang= 'en'
    except Exception as e:
        print(e)
    return text
gs.speak('hello sir , how are u')
s=lis()
print(s)
