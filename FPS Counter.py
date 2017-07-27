import cv2
from time import clock
camera1 = cv2.VideoCapture(0)

FPS_VAL = 0
i = 0
sec = clock()

while True:

    ret,frame = camera1.read()

    if clock()-sec >=1:

        cv2.putText(frame,str(i),(0,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2,cv2.LINE_AA)
        sec = clock()
        FPS_VAL = i
        i=0

    else:

        i+=1
        cv2.putText(frame,str(FPS_VAL),(0,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow('view',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

camera1.release()
cv2.destroyAllWindows()
