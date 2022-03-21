# conveting video to gray or black and  saving
import cv2 as cv
cap = cv.VideoCapture('resources/c.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# writing format, codec ,video write object and file output
out = cv.VideoWriter('resources/output_video.avi', cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width, frame_height),isColor =False)

while(True):
    (ret, frame) = cap.read()
    # convert gray
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   
    # to show in player
    if ret == True:
        out.write(frame)
        cv.imshow("video",grayframe)
        # to quit with q key
        if cv.waitKey(5000) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
out.release()
cv.destroyAllWindows()
