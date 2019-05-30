import numpy as np
import cv2

print(cv2.__version__)
cap = cv2.VideoCapture(1)
print(cap.isOpened())
print(cap.open(0))
while(True):
    ret, frame = cap.read()
    print(frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


