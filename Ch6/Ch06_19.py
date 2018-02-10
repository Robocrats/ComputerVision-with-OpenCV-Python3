import numpy as np
import cv2
cap = cv2.VideoCapture('basket1.mp4')
canvas = np.ones([480,640,3],'uint8')*255
for im in range(0,640,20):
    cv2.line(canvas,(im,0),(im,640),(50,255,0),1)
    cv2.line(canvas,(0,im),(640,im),(50,255,0),1)
while(cap.isOpened()):
    ret, frame = cap.read()
    img=cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.5,100,param1=50,param2=30,
                              minRadius=5,maxRadius=20)
    for i in circle[0,:]:
        cv2.circle(img,(i[0],i[1]),20,(0,0,255),2)
        cv2.circle(canvas,(i[0],i[1]),3,(0,0,255),-1)
        cv2.circle(canvas,(i[0],i[1]),15,(255,0,0),1)
    cv2.imshow('track',np.hstack([img,canvas]))
    c= cv2.waitKey(0) 
    if c == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()

