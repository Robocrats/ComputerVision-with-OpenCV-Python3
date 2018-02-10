import cv2
img=cv2.imread("logo.jpg")
cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read()
    result=cv2.addWeighted(frame,0.9,img,0.1,0)
    cv2.imshow('Resultvideo', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    


