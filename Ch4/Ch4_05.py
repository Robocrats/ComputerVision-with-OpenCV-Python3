import cv2
img = cv2.imread('tri.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY, 115, 1)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img2 = img.copy()
index = -1
thickness = 3
color = (0, 0, 255)
cv2.drawContours(img, contours[0], -1, color, thickness)
area = cv2.contourArea(contours[0])
perimeter = cv2.arcLength(contours[0], True)
M = cv2.moments(contours[0])
cx = int( M['m10']/M['m00'])
cy = int( M['m01']/M['m00'])
cv2.circle(img, (cx,cy), 2, (0,0,255), -1)
print("Area: {}, perimeter: {}".format(area,perimeter))
cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


