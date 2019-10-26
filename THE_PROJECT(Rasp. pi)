import wiringpi as wp
from collections import deque
import imutils
import cv2
import numpy as np
import cv2.cv as cv
import time
import sys


wp.wiringPiSetupGpio()


#function definitions:

def Motor(x,y,pwm):
        wp.pinMode(x,1)
        wp.pinMode(y,1)
        wp.pinMode(pwm,1)
        wp.softPwmCreate(pwm,0,200)
        return x,y,pwm
def forward(wheel,speed):
        (x,y,pwm)=wheel
        if wheel==right_wheel:
                wp.digitalWrite(x,0)
                wp.digitalWrite(y,1)
        else:
                wp.digitalWrite(x,1)
                wp.digitalWrite(y,0)
        wp.softPwmWrite(pwm,speed)
def backward(wheel,speed):
        (x,y,pwm)=wheel
        if wheel==left_wheel:
                wp.digitalWrite(x,0)
                wp.digitalWrite(y,1)
        else:
                wp.digitalWrite(x,1)
                wp.digitalWrite(y,0)
        wp.softPwmWrite(pwm,speed)
def stop(motor):
        (x,y,pwm)=motor
        wp.digitalWrite(x,0)
        wp.digitalWrite(y,0)
def move_dist(dist):
        time_move=1200*dist/circum_wheel
        forward(left_wheel,37)
        forward(right_wheel,52)
        wp.delay(int(round(time_move)))
        stop(left_wheel)
        stop(right_wheel)



def rotate(speed,dir='counter_clock'):
        if dir=='counter_clock':
                forward(right_wheel,speed)
                backward(left_wheel,speed)
        else:
                backward(right_wheel,speed)
                forward(left_wheel,speed)

def left_turn(speed):
        rotate(speed,'counter_clock')
def right_turn(speed):
        rotate(speed,'clock')
def straight():
        forward(left_wheel,37)
        forward(right_wheel,52)
def stop_bot():
        stop(left_wheel)
        stop(right_wheel)

def Go_to_Location(place):
        camera = cv2.VideoCapture(0)
        try:
                Lower=place[0]
                Upper=place[1]
                check_loc=True
                caught=False
                while check_loc:
                        if not caught:
                                rotate(set_speed)
                        (grabbed, frame) = camera.read()
                        frame = imutils.resize(frame, width=200,height=200)
                        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        mask = cv2.inRange(hsv,Lower,Upper)
                        mask = cv2.erode(mask, None, iterations=2)
                        mask= cv2.dilate(mask, None, iterations=2)
                        cnts =cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                        center = None
                        if len(cnts)>0:
                                c = max(cnts, key=cv2.contourArea)
                                ((x,y),radius) = cv2.minEnclosingCircle(c)
                                M = cv2.moments(c)
                                center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
                                if center[0]<90:
                                        print 'turn right'
                                        caught=True
                                        right_turn(set_speed)
                                elif center[0]>110:
                                        print 'turn left'
                                        caught=True
                                        left_turn(set_speed)
                                else :
                                        caught=True
                                        print 'straight \t', radius
                                        straight()
                                        if 47<radius:
                                                check_loc=False

                stop_bot()
                move_dist(8)
                print 'Moved Front successfuly'
        except KeyboardInterrupt:
                print 'stopped'
                stop_bot()
                sys.exit()

def Servo(pin):
        wp.softPwmCreate(pin,0,100)
        return pin

def Sweep(servo,dir,delay,angle):
        pin=servo
        if dir=='down' or dir=='close':
                for i in range(0,int(angle+1),1):
                        wp.softPwmWrite(pin,i)
                        wp.delay(delay)
        else:
                for i in range(int(angle),-1,-1):
                        wp.softPwmWrite(pin,i)
                        wp.delay(delay)

def Collect_ball():
        try:
                Sweep(main_arm,'down',200,14)
                wp.delay(200)
                Sweep(collector_arm,'close',200,13)
                wp.delay(200)
                Sweep(main_arm,'up',200,14)
        except :
                wp.softPwmWrite(main_arm,0)
                wp.softPwmWrite(collector_arm,0)

def Shoot_ball():
        try:
                Sweep(main_arm,'down',200,8)
                wp.delay(200)
                Sweep(collector_arm,'open',200,12)
                wp.delay(2000)
                Sweep(main_arm,'up',200,8)
                wp.delay(200)


                Sweep(collector_arm,'close',200,12)

        except :
                wp.softPwmWrite(main_arm,0)
                wp.softPwmWrite(collector_arm,0)


right_wheel=Motor(23,24,25)
left_wheel=Motor(17,27,22)
main_arm=Servo(12)
collector_arm=Servo(26)

circum_wheel=17
dist_between_wheels=17.9
set_speed=25

orange_Lower = (0,114,215)
orange_Upper = (34,255,255)
pink_Lower = (0,114,215)
pink_Upper = (34,255,255)

ball=(orange_Lower,orange_Upper)
goal=(pink_Lower,pink_Upper)

Go_to_Location(ball)
Collect_ball()
Go_to_Location(goal)
Shoot_ball()

