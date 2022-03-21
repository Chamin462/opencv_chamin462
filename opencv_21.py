import cv2 as cv
import numpy as np

img = cv.imread("resources/ch.jpg")
# convert in hsv (hue, saturation, value)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# Sliders
def slider():
    pass

path = "resources/ch1.jpg"
cv.namedWindow("Bars")
cv.resizeWindow('Bars',900,300)
cv.createTrackbar("Hue Min","Bars",0,179,slider)
cv.createTrackbar("Hue Max","Bars",179,179,slider)
cv.createTrackbar("Sat Min","Bars",0,255,slider)
cv.createTrackbar("Sat Max","Bars",255,255,slider)
cv.createTrackbar("Value Min","Bars",0,255,slider)
cv.createTrackbar("Value Max","Bars",255,255,slider)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min","Bars")
    hue_max = cv.getTrackbarPos("Hue Max","Bars")
    sat_min = cv.getTrackbarPos("Sat Min","Bars")
    sat_max = cv.getTrackbarPos("Sat Max","Bars")
    val_min = cv.getTrackbarPos("Value Min","Bars")
    val_max = cv.getTrackbarPos("Value Max","Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

# to see these changes inside an image
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])
    mask_img = cv.inRange(hsv_img,lower,upper)
    out_img = cv.bitwise_and(img, img,mask=mask_img)

    cv.imshow("original", img)
    cv.imshow("HSV",hsv_img)
    cv.imshow("Mask",mask_img)
    cv.imshow("Final output",out_img)
    if cv.waitKey(1) & 0xFF  == ord('q'):
            break
cv.waitKey(0)
cv.destroyAllWindows()
