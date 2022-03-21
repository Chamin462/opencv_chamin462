# reading video
import cv2 as cv
cap = cv.VideoCapture('resources/c.mp4')
# indicator most help different things
if (cap.isOpened()==False):
    print('error is reading video')
# reading and playing video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
cv.destroyAllWindows()
