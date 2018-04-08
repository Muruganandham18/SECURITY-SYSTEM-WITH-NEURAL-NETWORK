import speech_recognition as sr
import googlespeak as gs
import pyaudio
import speech_recognition as sr
import os
os.system("sudo pigpiod")
import pigpio
import time
pi = pigpio.pi()

pi.set_mode(18, pigpio.OUTPUT)
pi.get_mode(18)


def rotate(a,x,t=0):
	os.system("sudo pigpiod")
	if x<500:
		x=500
	if x>2000:
		x=2000
	pi.set_mode(a, pigpio.OUTPUT)
	pi.get_mode(a)
	pi.set_servo_pulsewidth(a,x)
	pi.get_servo_pulsewidth(a)
	time.sleep(t)
	pi.stop()
	return
r=sr.Recognizer()
def lis():
	with sr.Microphone(device_index = 1, chunk_size=512) as source:
                r.adjust_for_ambient_noise(source, duration=5)
                text=" "
                print("Listerning....")
                audio = r.listen(source)
                print("Processing....")
                try:
                        text=r.recognize_google(audio)
                        lang= 'en'
                except Exception as e:
                        print(e)
                        return text
retry=4
gs.speak("Hellooo sir,Face ID has been verified")
gs.speak("Voice ID ,veriiification is loading.....")
while not retry==0:
        
        password=lis()
        if password=="12345678":
                gs.speak("doooar ,opened")
                pi.set_servo_pulsewidth(18,800)
                time.sleep(5)
                pi.set_servo_pulsewidth(18,2000)
                time.sleep(1)
                pi.stop()
                s=0
                c=0
                gs.speak("doooar ,locked")
                retry=0

        else:
                if retry==1:
                        gs.speak("sorry,your are not allowed,due to incorrect Credential")
                        break
                gs.speak("sorry,incorrect password,please try again")
                
                retry=retry-1

