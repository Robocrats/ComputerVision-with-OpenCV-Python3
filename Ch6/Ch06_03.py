import cv2
import os
cap = cv2.VideoCapture(1)
if not os.path.exists('Myimages'):
    os.makedirs('Myimages')
pic_num = len(os.listdir('Myimages/'))
while (True):
    ret, frame = cap.read() 
    cv2.putText(frame,'Happy Birthday',(100,400), 7, 2,(0,0,255))
    cv2.imshow('image',frame)     
    c=cv2.waitKey(7)
    if c == 27:
        break
    elif c==ord('s'):
        cv2.imwrite("Myimages/"+str(pic_num)+'.jpg',frame)
        print('image captured &saved')
cap.release()
cv2.destroyAllWindows()
