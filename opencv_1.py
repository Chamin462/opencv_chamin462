# install open cv
# pip install opencv-python
# Reading image and display


import cv2 as cv

img = cv.imread('resources/ch.jpg')

cv.imshow('original',img)
cv.waitKey(5000)
cv.destroyAllWindows()

