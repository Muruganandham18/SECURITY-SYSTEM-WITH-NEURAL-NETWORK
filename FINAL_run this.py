
import cv2


import numpy as np
import googlespeak as gs
import pyaudio
import speech_recognition as sr

import time ,os
from gtts import gTTS
from pygame import mixer
os.system("sudo pigpiod")
import pigpio
import time
pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.get_mode(18)
pi.set_servo_pulsewidth(18,2000)
s=0

c=0

r=sr.Recognizer()
def lis():
    with sr.Microphone(device_index = 1, chunk_size=512) as source:
        r.adjust_for_ambient_noise(source, duration=5)
        text=" "
        gs.speak("please tell your ID,After the beep sound")
        mixer.init()
        mixer.music.load('/home/pi/new-project/msn_msg.mp3')
        mixer.music.play()
        time.sleep(1)
        mixer.music.stop()
        print("Listerning....")
        audio = r.listen(source)
        print("Processing....")
    try:
        text=r.recognize_google(audio)
        lang= 'en'
    except Exception as e:
        print(e)
    return text

gs.speak("Initiilizing the face recognition system please wait.")

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.createLBPHFaceRecognizer()

# Load the trained mode
recognizer.load('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)
mixer.init()
mixer.music.load('/home/pi/new-project/fbmngrpulldownrfsh.mp3')
mixer.music.play()
time.sleep(4)
mixer.music.stop()
gs.speak("Loading complete")
# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        if(Id == 1):
            Id = ("san")
            s=s+1
            print(s)
            
            
        #If not exist, then it is Unknown
        
        else:
            
            Id = ("Unknow")
            c=c+1
            s=0
            print(c)

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im)
    if s>= c and s>=10:
            retry=4
            gs.speak("Hellooo sir,  Face ID has been verified")
            gs.speak("Voice ID ,veriiification , please wait")
            while not retry==0:
                password=lis()
                print(password)
                if password=="12345678":
                
                
                
                    gs.speak("welcome sir,dooor is opening")
                    pi.set_servo_pulsewidth(18,800)
                    time.sleep(5)
                    pi.set_servo_pulsewidth(18,2000)
                    time.sleep(1)
                    s=0
                    c=0
                    gs.speak("door ,locked")
                    retry=0

                else: 
                    if retry==1:
                            gs.speak("sorry,your are not allowed,due to incorrect Credential")
                            break
                    gs.speak("sorry,incorrect password,please try again")
                    retry=retry-1
                    s=0
                    c=5
	    
    if c>=s and c>=5:
	    
	    gs.speak("un authorized person")
	    c=0
	    s=0
	    	
    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
