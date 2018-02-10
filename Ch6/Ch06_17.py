import cv2
facePath = "haarcascade_frontalface_default.xml"
smilePath = "haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)
cap = cv2.VideoCapture(1)
while (True):
    ret, frame = cap.read() 
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor= 1.05,minNeighbors=8,
            minSize=(55, 55),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smileCascade.detectMultiScale(roi_gray,scaleFactor= 1.7,minNeighbors=22,
                minSize=(25, 25),flags=cv2.CASCADE_SCALE_IMAGE)
        for (x1, y1, w1, h1) in smile:
            cv2.rectangle(roi_color, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 1)
            cv2.rectangle(img,(x,y-20),(x+w+30,y),(0,255,255),-1)
            cv2.putText(img,'Smile detected',(x,y-5),5,0.9,(0,0,0))
    cv2.imshow('Smile Detector', frame)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
