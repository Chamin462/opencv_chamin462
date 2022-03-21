# grayscale conversion
import cv2 as cv
from cv2 import cvtColor
from matplotlib.pyplot import gray

img = cv.imread('resources/ch.jpg')
img = cv.resize(img, (800,600))

# conversion
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)
# display
cv.imshow('first',img)
cv.imshow('Gray',gray_img)

 # delay code 
cv.waitKey(5000)
cv.destroyAllWindows()