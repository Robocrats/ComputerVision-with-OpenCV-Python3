import cv2
img=cv2.imread("frame.jpg",1)
cap = cv2.VideoCapture('traffic.mp4')
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_half = cv2.resize(gray, (200,100))
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
