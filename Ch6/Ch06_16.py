import cv2
import os
facePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(facePath)
cap = cv2.VideoCapture(1)
if not os.path.exists('stamp'):
    os.makedirs('stamp')
pic_num = len(os.listdir('stamp/'))
while (True):
        ret, frame = cap.read() 
        img = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor= 1.05,
                  minNeighbors=8,minSize=(55,55),flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in faces:
                resized_image= img[y-50:y+h+100, x-10:x+w+20]
        cv2.imshow('Passport snap', frame)
        c = cv2.waitKey(7) % 0x100
        if c == ord('s'): 
            pic_num +=1
            resized_image=cv2.copyMakeBorder(resized_image,10,10,10,10,
                                       cv2.BORDER_CONSTANT,value=(255,255,250))
            cv2.imwrite("stamp/"+str(pic_num)+'.jpg',resized_image )
            print('Succesfully! Saved the photo')
        elif c == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()     
