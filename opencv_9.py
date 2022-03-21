# how to capture a webcam inside python
# step_1 import libraries
import cv2 as cv
import numpy as np
# step_2 read the frame from Camera
cap = cv.VideoCapture(0)# webcam no. 1
# check video is write correct or error 
if (cap.isOpened() ==False):
    print("There is error")
# read and untill the end
# step_3 display the cam frame by frame
while(cap.isOpened()):
    # capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # to display frame
        cv.imshow('Frame',frame)
        # to quit with q key
        if cv.waitKey(1)& 0xFF == ord('q'):
            break
    else:
        break
# step_4  release and close windows easily
cap.release()
cv.destroyAllWindows() 