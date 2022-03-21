# setting of camera or video
from tkinter import Frame
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

cap.set(10, 50)# 10 is the key to set brightness
cap.set(3,640) # 3 is the key to set of width
cap.set(4,480) # 4 is the key to set of height

while(True):
    ret, Frame = cap.read()
    if ret == True:
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF  == ord('q'):
            break
cap.release()
cv.destroyAllWindows()