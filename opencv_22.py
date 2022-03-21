# Face detection in an image
import cv2 as cv

fase_cascade = cv.CascadeClassifier("resources/haarcasecade_frontalface_default.xml")

img = cv.imread("resources/faces.jpg")
#img = cv.resize(img,(600,550))
#print(img.shape)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = fase_cascade.detectMultiScale(gray_img, 1.1, 4)

# draw a rectangle
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)

cv.imshow("Image",img)
cv.imwrite("resources/f.png",img)
cv.waitKey(0)
cv.destroyAllWindows()