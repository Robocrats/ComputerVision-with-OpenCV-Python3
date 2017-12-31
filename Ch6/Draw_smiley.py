import numpy as np
import cv2
img = np.ones((400,400,3), np.uint8)
img *= (2**16-1)
cv2.circle(img,(280,200), 100, (0,255,255), -1)
cv2.circle(img,(260,160), 10, (255,255,255), -1)
cv2.circle(img,(300,160), 10, (255,255,255), -1)
cv2.circle(img,(260,160), 5, (0,0,0), -1)
cv2.circle(img,(300,160), 5, (0,0,0), -1)
cv2.ellipse(img, (280,200), (50,50), 0, 0, 180,(0,0,0),2)
cv2.imshow("img",img)
c=cv2.waitKey()
if c==ord('q'):
    cv2.destroyAllWindows()