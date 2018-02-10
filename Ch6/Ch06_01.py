import cv2
img = cv2.imread("child.jpg")
r = cv2.selectROI(img)
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("Image", imCrop)
cv2.imwrite('cropped.jpg',imCrop)
c= cv2.waitKey(0)
if c==ord('q'):
    cv2.destroyAllWindows()

