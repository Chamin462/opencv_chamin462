# image saving an image / writing images 
from importlib import resources
import cv2 as cv
from cv2 import imwrite
# read image
img = cv.imread('resources/ch.jpg')
# conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
binary = cv.resize(binary, (800,600))
imwrite('resources/gray.png',gray)
imwrite('resources/binary.png', binary)
#cv.waitKey(0)
#cv.destroyAllWindows()