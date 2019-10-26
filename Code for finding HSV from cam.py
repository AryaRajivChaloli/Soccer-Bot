import cv2
import numpy as np
cap=cv2.VideoCapture(0)
lh=[0,100,100]
uh=[0,0,0]
while(1):
	_,img=cap.read()
	cv2.circle(img,(325,215),90,(0,255,0),3)
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img)