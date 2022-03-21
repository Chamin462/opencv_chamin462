# Reading image and display and resize


import cv2 as cv

img = cv.imread('resources/ch.jpg')
img1 = cv.resize(img, (800,600))

cv.imshow('first',img)

cv.imshow('second',img1)
cv.waitKey(5000)
cv.destroyAllWindows()
