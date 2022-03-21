# how to draw lines and shapes in python
import cv2 as cv
import numpy as np

# draw a canvas 0 is for black 
img = np.zeros((600,600))# black
img1 = np.ones((600,600))# white
# print size
print("The size of our canvas is :",img.shape)
# adding colors to the canvas
colored_img = np.zeros((600,600,3),np.uint8)# color channel addition
colored_img[:]= 255,0,255 # color complete image
colored_img[150:230,100:287]= 255,0,0 # part of image to be colored
# adding line
cv.line(colored_img,(0,0),(300,300),(255,0,0),3)#part line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)# croosed line
# adding rectangles
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),3)# draw
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),cv.FILLED)#fill
# adding circle
cv.circle(colored_img,(400,300),50,(255,100,0),5)
cv.circle(colored_img,(400,300),50,(255,100,0),cv.FILLED)
# Adding text
cv.putText(colored_img,"Ch Amin Youtube channel",(200,500),cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),1)



cv.imshow('black',img)
cv.imshow('white',img1)
cv.imshow('color',colored_img)
cv.waitKey(0)
cv.destroyAllWindows()