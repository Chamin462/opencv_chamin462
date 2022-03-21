# how to change the perspective of an image
import imp
from turtle import width


import cv2 as cv
import numpy as np

img = cv.imread('resources/image name')
#print(img.shape) check height width
# defining points
point1 = np.float32([[124,125],[124.251],[456,251],[412,12]])
width = 800
height = 900
width,height = 800,900
point2 = np.float32([[0,0],[800,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(point1,point2) 
out_img = cv.warpPerspective(img, matrix,(width,height))

cv.imshow('original',img)
cv.imshow('transformed',out_img)
cv.imwrite('resources/name',out_img)
cv.waitKey(0)
cv.destroyAllWindows()