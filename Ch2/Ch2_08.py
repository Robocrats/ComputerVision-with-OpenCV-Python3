import numpy as np
import cv2
image = cv2.imread("monkey.jpg")
blur = cv2.GaussianBlur(image, (5,55),0)
kernel = np.ones((5,5),'uint8')
dilate = cv2.dilate(image,kernel,iterations=1)
erode = cv2.erode(image,kernel,iterations=1)
img=np.concatenate((blur,dilate,erode),axis=1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
