import cv2
import numpy as np
upper_red = np.array([255,255,255])
upper_blue=np.array([255,255,242])
upper_green=np.array([160,48,112])
upper_yellow=np.array([103,255,255])
img = cv2.imread('balls.jpg',1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
circle = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1.5,100,param1=50,param2=30,minRadius=15,maxRadius=80)
no_circles = np.uint16(np.around(circle))
img2 = img.copy()
for i in no_circles[0,:]:
    centre=img2[i[0],i[1]]
    if all(centre==upper_red):
        cv2.putText(img2,'Red',(i[0],i[1]+70), 2, 0.8,(0,0,0))
    elif all(centre==upper_blue):
        cv2.putText(img2,'Blue',(i[0],i[1]+70), 2, 0.8,(0,0,0))
    elif all(centre==upper_green):
        cv2.putText(img2,'Green',(i[0],i[1]+70), 2, 0.8,(0,0,0))
    elif all(centre==upper_yellow):
        cv2.putText(img2,'Yellow',(i[0],i[1]+70), 2, 0.8,(0,0,0))
    else:
        cv2.putText(img2,'Not recognized',(i[0],i[1]+70), 2, 0.8,(0,0,0))
cv2.imshow('Color Recognition',img2)
c= cv2.waitKey(0)
if c==ord('q'):
    cv2.destroyAllWindows()
