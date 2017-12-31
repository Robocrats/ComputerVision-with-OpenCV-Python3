import cv2
import numpy as np
lower = np.array([0, 50, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
cap = cv2.VideoCapture(1)
while (True):
    ret,frame=cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    skinMask = cv2.inRange(hsv, lower, upper)
    skinMask = cv2.GaussianBlur(skinMask,(3,3),1)
    skin = cv2.bitwise_and(frame, frame, mask = skinMask)
    cv2.imshow("images", np.hstack([frame, skin]))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
