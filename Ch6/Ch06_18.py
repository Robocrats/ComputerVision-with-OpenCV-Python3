import cv2
cap = cv2.VideoCapture(1)
cascPath = "haarcascade_frontalface_default.xml"  
faceCascade = cv2.CascadeClassifier(cascPath)
mou = cv2.imread('moustache.png')
def draw_moustache(mou,face,x1,y1,w1,h1):
    mou_width = int(w1*0.5)+1
    mou_height = int(h1*0.2)+1
    mou = cv2.resize(mou,(mou_width,mou_height))
    for i in range(int(0.6*h1),int(0.6*h1)+mou_height):
        for j in range(int(0.3*w1),int(0.3*w1)+mou_width):
            for k in range(3):
                if mou[i-int(0.6*h1)][j-int(0.3*w1)][k] <235:
                    #face[i][j][k] = mou[i][j][k]  
                    face[y+i][x+j][k] = mou[i-int(0.6*h1)][j-int(0.3*w1)][k]    
    return face
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for (x, y, w, h) in faces:
        draw_moustache(mou,frame,x,y,w,h)
    cv2.imshow('Moustache Face!!',frame)
    c = cv2.waitKey(7) 
    if c == 27:
        break
    elif c==ord('s'):
        cv2.imwrite(str("Output")+'.jpg',frame)
        print('Successful! Your image is saved')
cap.release()
cv2.destroyAllWindows()
    
