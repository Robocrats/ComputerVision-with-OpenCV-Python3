import numpy as np
import cv2
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)
print('pixel value in Black image is',black[0,0])
ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print('pixel value in ones image is',ones[0,0])
white = np.ones([150,200,3],'uint8')
white *= (2**16-1)
cv2.imshow("White",white)
print('pixel value in White image is',white[0,0])
color = np.ones([150,200,3],'uint8')
color[:,:] = (255,0,0)
cv2.imshow("Blue",color)
print('pixel value in Blue image is',color[0,0])
cv2.waitKey(0)
cv2.destroyAllWindows()

