# joining two images
from importlib import resources
import cv2 as cv
import numpy as np

img =cv.imread('resources/ch.jpg')

# Stacking same image

# 1- Horizontal stack
hor_img = np.hstack((img,img))
# 2- Vertical stack
ver_img = np.vstack((img,img))


cv.imshow("horizontal",hor_img)
cv.imshow('Vertical',ver_img)
cv.waitKey(0)
cv.destroyAllWindows()
# you can only stack images same shape (width, height,color channel)
# you have to define a function to stack multiple images of different  size and tunes
# we can not resize the stack image (function)
# same number of channel np function