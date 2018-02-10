import cv2
img = cv2.imread('balls.jpg',1)
(sizex,sizey,z)=img.shape;
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 100, 200)
thresh = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 0.6)
contours = cv2.findContours(edges,1,2)
cnt = contours[1]
cv2.drawContours(img,contours[1], -1, (0,255,255), 2)
cv2.rectangle(img,(sizey-150,sizex-50),(sizey,sizex),(0,255,255),-1)
peri = cv2.arcLength(cnt[0], True)
approx = cv2.approxPolyDP(cnt[0], 0.04 * peri, True)
print(len(approx))
if len(approx)==4:
    cv2.putText(img,str('Square'),(sizey-145,sizex-20),5,1,(0,0,0))
elif len(approx)==5:
    cv2.putText(img,str('Pentagon'),(sizey-145,sizex-20),5,1,(0,0,0))
elif len(approx)==6:
    cv2.putText(img,str('Hexagon'),(sizey-145,sizex-20),5,1,(0,0,0))
else:
    cv2.putText(img,str('Circle'),(sizey-145,sizex-20),5,1,(0,0,0))
print(peri)
print(approx)
cv2.imshow('frame',img)
c= cv2.waitKey(0)
if c==ord('q'):
    cv2.destroyAllWindows()

