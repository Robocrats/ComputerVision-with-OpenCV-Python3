import cv2
W = 1000
img = cv2.imread('panda.jpg',1)
height, width, depth = img.shape             
imgScale = W/width
newX,newY = img.shape[1]*imgScale, img.shape[0]*imgScale
newimg = cv2.resize(img,(int(newX),int(newY)))
cv2.imshow("old Image",img)
cv2.waitKey(0)
cv2.imshow('New image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
