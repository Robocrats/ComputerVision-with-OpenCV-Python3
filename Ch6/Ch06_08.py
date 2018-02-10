import numpy as np
import cv2
cap = cv2.VideoCapture(1)
def nothing(x):
	pass
bg =cv2.createBackgroundSubtractorMOG2()
panel=np.zeros([100,500],np.uint8)
cv2.namedWindow("panel")
cv2.createTrackbar("LH","panel",0,180,nothing)
cv2.createTrackbar("UH","panel",180,180,nothing)
cv2.createTrackbar("LS","panel",0,255,nothing)
cv2.createTrackbar("US","panel",255,255,nothing)
cv2.createTrackbar("LV","panel",0,255,nothing)
cv2.createTrackbar("UV","panel",255,255,nothing)
while(True):
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("LH","panel")
    ls=cv2.getTrackbarPos("LS","panel")
    lv=cv2.getTrackbarPos("LV","panel")
    uh=cv2.getTrackbarPos("UH","panel")
    us=cv2.getTrackbarPos("US","panel")
    uv=cv2.getTrackbarPos("UV","panel")	
    lower_green = np.array([lh,ls,lv])
    upper_green=np.array([uh,us,uv])
    bgmask=cv2.inRange(gray, lower_green,upper_green)
    bgmask_inv=cv2.bitwise_not(bgmask)
    bg= cv2.bitwise_and(frame,frame,mask=bgmask)
    fg=cv2.bitwise_and(frame,frame,mask=bgmask_inv)
    cv2.imshow('display',np.hstack([bg,fg])) 
    cv2.imshow('panel',panel)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

