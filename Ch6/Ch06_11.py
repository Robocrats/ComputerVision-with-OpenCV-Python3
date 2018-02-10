import numpy as np
import cv2
n=0
img = cv2.imread('pipes.jpg',1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(thresh, contours, -1, (255,20,250), 2)
circle = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1.5,100,
                            param1=50,param2=30,minRadius=15,maxRadius=80)
no_circles = np.uint16(np.around(circle))
v=len(no_circles)
for i in no_circles[0,:]:
    n=n+1
    cv2.circle(img,(i[0],i[1]),40,(0,200,0),2)
    cv2.putText(img,str(n),(i[0],i[1]), 1, 2,(0,0,255))
cv2.rectangle(img,(500,420),(640,480),(0,255,0),-1)
cv2.putText(img,str("Total pipes"),(500,445),5,1,(0,0,0))   
cv2.putText(img,str(n),(580,470),5,1,(0,0,0))    
cv2.imshow("Pipe Counting",img)
c= cv2.waitKey(0)
if c==ord('q'):
    cv2.destroyAllWindows()
