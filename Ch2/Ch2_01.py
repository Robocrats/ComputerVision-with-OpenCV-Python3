import numpy as np
import cv2
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)
cv2.waitKey(0)
cv2.destroyAllWindows()
