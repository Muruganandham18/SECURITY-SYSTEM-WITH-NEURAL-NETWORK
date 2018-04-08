import os
os.system("sudo pigpiod")
import pigpio
import time
pi = pigpio.pi()

pi.set_mode(18, pigpio.OUTPUT)
pi.get_mode(18)
while True:
        pi.get_servo_pulsewidth(18)
        time.sleep(1)
        pi.set_servo_pulsewidth(18,2000)
        time.sleep(1)
        pi.set_servo_pulsewidth(18,1000)
        time.sleep(1)
        pi.set_servo_pulsewidth(18,2000)
        time.sleep(1)
