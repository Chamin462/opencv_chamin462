# image converion white into black
import cv2 as cv
# read image
img = cv.imread('resources/ch.jpg')
# conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# display
cv.imshow('original',img)
cv.imshow('Gray',gray)
cv.imshow('Black and White',binary)
# delay code 
cv.waitKey(0)
cv.destroyAllWindows()