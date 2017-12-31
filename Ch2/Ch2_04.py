import cv2
img = cv2.imread("panda.jpg",0)
#cv2.imshow("image",img)
ret,thresh = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("CV Threshold",thresh)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("newpanda.png",img)
    cv2.destroyAllWindows() 	
elif k == 27:        
    cv2.destroyAllWindows()
