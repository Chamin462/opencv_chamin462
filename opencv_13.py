# Basic functions or manipulation in open cv

import cv2 as cv
import numpy as np
from cv2 import dilate

img = cv.imread('resources/ch1.jpg')

# resize
resize_img = cv.resize(img,(450,250))
# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blurred image
blurr_img = cv.GaussianBlur(img,(7,7),0)
# edge detection
edge_img = cv.Canny(img, 48,48)
# thickness of lines
mat_kernel = np.ones((7,7),np.uint8)
dilate_img = cv.dilate(edge_img,(mat_kernel),iterations=1)
# make thinner outline
ero_img = cv.erode(dilate_img,mat_kernel,iterations=1)
# cropping we will use numpy library not open cv
print('The size of our image is:',img.shape)
cropped_img = resize_img[0:400,150:300]

cv.imshow('original',img)
cv.imshow('Resized',resize_img)
cv.imshow('Gray',gray_img)
cv.imshow('Blurred', blurr_img)
cv.imshow('edge',edge_img)
cv.imshow('dilated',dilate_img)
cv.imshow('Erosion',ero_img)
cv.imshow('Cropped',cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
