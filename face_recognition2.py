
# Import OpenCV2 for image processing
import cv2
import pigpio

# Import numpy for matrices calculations
import numpy as np
                                ## Import GPIO Library.
import time

pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)
xx=500
x1=500
# Create Local Binary Patterns Histograms for face recognization
recognizer= cv2.face.createLBPHFaceRecognizer()

# Load the trained mode
recognizer.load('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = ("haarcascade_frontalface_default.xml")

Id=0
Ids=0
# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);
# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)
i=1100
j=1180
trackx=1
trackxm=1
tracky=1
trackym=1
pi.get_mode(17)
pi.set_servo_pulsewidth(17,i)
pi.get_servo_pulsewidth(17)
pi.get_mode(18)
pi.set_servo_pulsewidth(18,j)
pi.get_servo_pulsewidth(18)
# Loop

while True:
    # Read the video frame
    ret,im =cam.read()
    
    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
 

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w,y+h), (255,255,255), 1)
        
        # Recognize the face belongs to  ID
        Id=recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        if(Id ==1):
            Id = ("Santosh ")
            
        #If not exist, then it is Unknown
        elif(Id==2):
            Id=("sir ")
        elif(Id==3):
            Id=("sanjay ")
        else:
            Id==("unknown")
	    # Put text describe who is in the picture
        #cv2.rectangle(im, (x-22,y-90), (x+w+10, y-10), (255,0,0), -1)
        Ids=Id
        xaxis= str(x)
        yaxis=str(y)
        height=str(h)
        width=str(w)
        w1=w/2
        h1=h/2
        trackx=x+int(w1)
        tracky=y+int(h1)
        cv2.putText(im,str("*"+str(tracky)),(x+int(w1),y+int(h1)), font, 1, (255,255,255), 1)
        cv2.putText(im, str(Id), (x-10,y-30), font, 1, (255,255,255), 1)
##        print(x+int(w1),":",y+int(h1))
    cv2.imshow("img",im)
    if Id==1 or Ids== ("Santosh "):
        
        if trackym<220 and j<1500:
            pi.get_mode(18)
            pi.set_servo_pulsewidth(18,j)
            pi.get_servo_pulsewidth(18)
            j=j+10
##            print("                              i:",j)
        if trackym>220 and trackym<250 :
            pi.get_mode(18)
            pi.set_servo_pulsewidth(18,0)
            pi.get_servo_pulsewidth(18)
##            print("                                           i:",j)
        if trackym>250 and j>1000:
            
            pi.get_mode(18)
            pi.set_servo_pulsewidth(18,j)
            pi.get_servo_pulsewidth(18)
            j=j-10
##            print("                                                         i:",i)

        trackym=tracky
        if j<500:
            j=500
        if j>2400:
            j=2400
 
        if trackxm<240 and i<1500:
            pi.get_mode(17)
            pi.set_servo_pulsewidth(17,i)
            pi.get_servo_pulsewidth(17)
            i=i+10
            
##            print("                              i:",i)
        if trackxm>240 and trackxm<300 :
            pi.get_mode(17)
            pi.set_servo_pulsewidth(17,0)
            pi.get_servo_pulsewidth(17)
##            print("                                           i:",i)
        if trackxm>300 and i>1000:
            pi.get_mode(17)
            pi.set_servo_pulsewidth(17,i)
            pi.get_servo_pulsewidth(17)
            i=i-10

cam.release()

# Close all windows
cv2.destroyAllWindows()
