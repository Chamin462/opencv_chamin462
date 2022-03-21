# conveting video to gray or black and white
import cv2 as cv
cap = cv.VideoCapture('resources/c.mp4')

while(True):
    (ret, frame) = cap.read()
    # convert gray
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # convert black and white
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    # to show in player
    if ret == True:
        cv.imshow("video",binary)
        # to quit with q key
        if cv.waitKey(5000) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
cv.destroyAllWindows()
