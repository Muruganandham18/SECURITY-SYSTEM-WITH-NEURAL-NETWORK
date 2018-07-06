# SECURITY-SYSTEM-WITH-NEURAL-NETWORK
FACE RECOGNIZE AND VOICE COMMAND SECURITY SYSTEM WITH NEURAL NETWORK
Abstraction:
               To recognize face using trained neural network and in addition to increase security, we use voice id (password) as credentials to open the door automatically.
Technology Stack:
•	Python 3.x
•	Broadcom Arm x64 bit based processor
•	PiGpio library
•	Google speech recognition
•	OpenCv library
•	1.3 Mega pixel cam for capturing live frames

WORKING:
               The aim of this project is to use Neural network for face Recognition. Here, we have used 1000's of images for training Neural Network which is not enough to recognize face correctly and we require large amount of GPU to process. Here we use an Arm x64 based microprocessor which is not sufficient for image processing with neural networks. This is to try which cannot identify the person correctly. So, we have implemented voice ID for reliability of the system.
                Let's get into the project. Here, the image dataset is trained and the result is creating. yml file that we are going to use to predict the image, In Neural Network prediction is possible. The data set contains two image sets one is Image of the person, another is Image of the unknown person. Here we have less amount of image due to this microprocessor can’t process large data type.
                As, the face is detected now it’s time for voice Id. Here we use google pre trained Neural Network for voice recognition.
								Here googles speech to text conversation API will convert our voice into string and compare with the credentials, here we have given 3 change for correct password.
               If the credentials are matched, here comes servo to open the door automatically. There is servo motor attached to door it will create a 80° rotation of the servo shaft and the door is relocked after 5 seconds to the initial value.


STOPPER:
•	poor Internet connection
•	Low accuracy
•	Dark environment
•	Only Language English as voice Command
•	Less memory

